"""PreToolUse hook — ExitPlanMode 호출 시 플랜 리뷰 게이트.

설치된 외부 리뷰어(Codex 또는 Copilot)를 런타임에 감지해 리뷰를 요청한다.
둘 다 없으면 게이트를 통과시킨다(사용 가능한 외부 리뷰어가 있을 때만 강제).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
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

SUPPRESS_MARKER = Path.home() / ".no-plan-exit-review"
MARKER_DIR      = Path.home() / ".claude" / "plan-review-markers"
PLANS_DIR       = Path.home() / ".claude" / "plans"

# 플러그인 매니페스트 경로 (계정마다 codex는 .claude, copilot은 .claude-enterprise에 분리)
_PLUGIN_MANIFESTS = [
    Path.home() / ".claude" / "plugins" / "installed_plugins.json",
    Path.home() / ".claude-enterprise" / "plugins" / "installed_plugins.json",
]

# 리뷰어별 subagent_type
_REVIEWER_SUBAGENT = {
    "codex":   "codex:codex-rescue",
    "copilot": "copilot:copilot-rescue",
}

SAFE_KEY = re.compile(r"[^A-Za-z0-9_.-]")


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


def _marker_for(plan_path: Path) -> Path:
    key = SAFE_KEY.sub("_", plan_path.stem)
    if not key:  # ".md" 등 빈 stem → 경로 해시 폴백 (충돌/공통키 방지)
        key = hashlib.sha1(str(plan_path).encode("utf-8")).hexdigest()[:16]
    return MARKER_DIR / f".plan-reviewed-{key}"


def _find_latest_plan() -> Path | None:
    if not PLANS_DIR.is_dir():
        return None
    plans = sorted(
        (p for p in PLANS_DIR.glob("*.md") if p.is_file()),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return plans[0] if plans else None


def _detect_reviewer() -> str | None:
    """설치된 리뷰어를 감지한다. Codex 우선, 없으면 Copilot, 둘 다 없으면 None.

    두 매니페스트 경로를 모두 스캔하며, 파일/JSON 파싱 오류는 조용히 무시한다.
    키 형식 'name@marketplace' 에서 '@' 앞 이름만으로 판정해 marketplace 변동에 강하다.
    """
    found: set[str] = set()

    for manifest_path in _PLUGIN_MANIFESTS:
        try:
            raw = manifest_path.read_text(encoding="utf-8")
            data = json.loads(raw)
        except Exception:
            continue

        plugins = data.get("plugins") if isinstance(data, dict) else None
        if not isinstance(plugins, dict):
            continue

        for key in plugins:
            if not isinstance(key, str):
                continue
            name = key.split("@", 1)[0].lower()
            if name in _REVIEWER_SUBAGENT:
                found.add(name)

    # Codex 우선 (Copilot은 Codex 미사용 환경의 대체제)
    if "codex" in found:
        return "codex"
    if "copilot" in found:
        return "copilot"
    return None


REVIEW_INSTRUCTION = (
    "[플랜 리뷰 게이트 — 플랜마다 1회 발동]\n"
    "ExitPlanMode가 차단되었습니다. 플랜을 외부 리뷰어에 보내 검수를 받아야 합니다.\n"
    "\n"
    "1. Agent 도구를 subagent_type \"{subagent_type}\"으로 호출하세요.\n"
    "2. prompt에 플랜 파일({plan_path})의 내용을 포함하여 리뷰를 요청하세요.\n"
    "   리뷰 관점: 실현 가능성, 완전성, 잠재적 문제, 놓친 엣지 케이스\n"
    "3. 리뷰 결과를 확인하고 필요하면 플랜을 수정하세요.\n"
    "4. ExitPlanMode를 다시 호출하세요 (같은 플랜 2회차는 자동 통과).\n"
)


def main() -> int:
    payload = _read_stdin_payload()  # stdin 소비 목적 유지 (session_id는 더는 안 씀)

    if SUPPRESS_MARKER.exists():
        return 0
    if not _is_repo_session():
        return 0

    reviewer = _detect_reviewer()  # 리뷰어 없으면 통과
    if reviewer is None:
        return 0

    plan_path = _find_latest_plan()  # 플랜 없으면 통과
    if plan_path is None:
        return 0

    marker = _marker_for(plan_path)  # 플랜(파일) 기준 마커

    # 원자적 생성: 이미 있으면(이 플랜은 리뷰됨) FileExistsError → 통과
    try:
        MARKER_DIR.mkdir(parents=True, exist_ok=True)
        os.close(os.open(str(marker), os.O_CREAT | os.O_EXCL | os.O_WRONLY))
    except FileExistsError:
        return 0
    except OSError:
        return 0

    subagent_type = _REVIEWER_SUBAGENT[reviewer]
    reason = REVIEW_INSTRUCTION.format(plan_path=plan_path, subagent_type=subagent_type)
    sys.stdout.write(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
