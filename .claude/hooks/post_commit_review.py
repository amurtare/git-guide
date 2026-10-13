"""PostToolUse hook — 커밋 성사(HEAD 전진) 직후 project-memory 회고 유도.

Bash tool이 끝날 때마다 실행되어 HEAD sha가 직전 처리값보다 전진했는지 확인한다.
새 커밋이 얹혔으면(merge-base --is-ancestor) 회고 리마인더를 주입한다.
명령 문자열을 파싱해 "커밋인지" 추측하지 않고 실제 HEAD 변화로만 판정하므로,
문서 안 'git commit' 문자열 오탐·재실행 루프·마커 누적이 원천적으로 없다.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

for _stream_name in ("stdout", "stderr"):
    _stream = getattr(sys, _stream_name, None)
    if _stream is not None and hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MEM_DIR   = REPO_ROOT / "project-memory"

SUPPRESS_MARKER = Path.home() / ".no-commit-review"
STATE_DIR       = Path.home() / ".claude" / "commit-review-state"

# 회고 대상에서 면제할 경로 접두(회고 결과·설정 파일만 담긴 커밋은 재발동 안 함)
EXEMPT_PREFIXES = ("project-memory/", ".claude/")


def _is_repo_session() -> bool:
    return MEM_DIR.is_dir()


def _read_stdin_payload() -> dict:
    try:
        raw = sys.stdin.read()
    except Exception:
        return {}
    if not raw:
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return data if isinstance(data, dict) else {}


def _git(args: list[str]) -> str | None:
    """git 명령을 REPO_ROOT에서 실행. 실패 시 None."""
    try:
        out = subprocess.run(
            ["git", *args],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=5,
        )
    except Exception:
        return None
    if out.returncode != 0:
        return None
    return out.stdout.strip()


def _git_ok(args: list[str]) -> bool:
    """종료코드만 필요한 git 명령(예: merge-base --is-ancestor). 성공 시 True."""
    try:
        out = subprocess.run(
            ["git", *args],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=5,
        )
    except Exception:
        return False
    return out.returncode == 0


def _state_file() -> Path:
    repo_key = hashlib.sha1(str(REPO_ROOT).encode("utf-8")).hexdigest()[:8]
    return STATE_DIR / repo_key


def _read_state() -> str | None:
    try:
        val = _state_file().read_text(encoding="utf-8").strip()
    except OSError:
        return None
    return val or None


def _write_state(head: str) -> None:
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        _state_file().write_text(head, encoding="utf-8")
    except OSError:
        pass


def _range_is_exempt(last: str, current: str) -> bool:
    """last..current 에 커밋된 파일이 전부 EXEMPT_PREFIXES 이면 True."""
    out = _git(["log", "--format=", "--name-only", f"{last}..{current}"])
    if out is None:
        return False  # 판단 불가 → 회고 유도 쪽으로
    files = [ln.strip() for ln in out.splitlines() if ln.strip()]
    if not files:
        return False
    return all(f.startswith(EXEMPT_PREFIXES) for f in files)


REMINDER = (
    "[커밋 회고 — 방금 만든 커밋 단위]\n"
    "방금 커밋된 작업 단위에서 다음 세션의 에이전트에게 유용할 흔적을 project-memory/ 에 남길지 검토하세요.\n"
    "규칙은 project-memory/index.md, project-memory/insight/README.md, CLAUDE.md '메인테이너 워크플로' 섹션 참고.\n"
    "\n"
    "후보:\n"
    "- 작업 단위 한 줄 흔적(의도/시도/결과) → project-memory/log.md append\n"
    "  형식: ## [YYYY-MM-DD] <kind> | <한 줄 제목> + 본문 1~5줄.\n"
    "- 비자명한 디버깅 결론·의외의 동작 → project-memory/insight/YYYY-MM-DD-<주제>.md + index.md 등록\n"
    "- 반복적으로 부딪힐 함정 → project-memory/gotchas.md 항목 추가\n"
    "- 설계 결정의 의도 → project-memory/decisions/<topic>.md\n"
    "- 미해결 이슈/조사 중 가설 → project-memory/open-questions.md\n"
    "- 미완료 작업이 남아 있으면 → handoff.md '남은 작업' 섹션에 기록\n"
    "\n"
    "원칙: raw 코드·release-notes·git log에 이미 있는 사실은 다시 적지 않음.\n"
    "기록할 내용은 지금 작성하면 되고(다음 커밋에 함께 포함하면 됨), 남길 게 없으면 '없음' 한 줄로 답하고 진행하세요.\n"
)


def main() -> int:
    _read_stdin_payload()  # stdin 소비(명령 문자열은 감지에 쓰지 않음 — HEAD로만 판정)

    if SUPPRESS_MARKER.exists():
        return 0
    if not _is_repo_session():
        return 0

    current = _git(["rev-parse", "HEAD"])
    if current is None:  # 비-git / 커밋 없음
        return 0

    last = _read_state()
    if last is None:  # 콜드스타트 — baseline만 세우고 통과
        _write_state(current)
        return 0

    if current == last:  # HEAD 불변 — 커밋 아님
        return 0

    # HEAD 변함: last 위에 새 커밋이 얹혔을 때만 회고
    if not _git_ok(["merge-base", "--is-ancestor", last, current]):
        # sideways(checkout/reset/rebase/amend 등) — 새 작업 커밋 아님
        _write_state(current)
        return 0

    _write_state(current)

    if _range_is_exempt(last, current):  # 회고·설정 파일만 담긴 커밋 → 재발동 안 함
        return 0

    sys.stdout.write(json.dumps({"decision": "block", "reason": REMINDER}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
