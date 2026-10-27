# 릴리즈 관리

이 프로젝트의 버전·릴리즈·개발 맥락 관리 규칙이다.
[release_management_guide](https://github.com/amurtare/release_management_guide/blob/main/RELEASE_MANAGEMENT_GUIDE.md)를
**빌드 단계가 없는 정적 HTML 학습 사이트**라는 이 프로젝트의 성격에 맞게 조정했다.

## 구성 요소

| 파일/도구 | 역할 |
|-----------|------|
| `VERSION` | 버전 번호 단일 소스 (매니페스트 파일이 없으므로 plain-text 파일 사용) |
| `docs/UPDATE_CHECKLIST.md` | 릴리즈 시 순서대로 따르는 체크리스트 |
| `release-notes/v{버전}.md` | 버전별 변경 내역 (학습자·기여자용) |
| Git 태그 `vX.Y.Z` + GitHub Release | 버전 지점 고정. `.github/workflows/release.yml`이 자동 생성 |
| `CLAUDE.md` | Claude Code가 릴리즈 요청 시 체크리스트를 따르도록 하는 트리거 |
| `project-memory/` | 개발 맥락 누적 — 설계 결정·함정·구조·미해결 이슈 |
| `handoff.md` | 세션 이월용 (로컬 전용, `.gitignore`) |
| `.claude/hooks/` + `.claude/settings.json` | 세션 시작 brief · 커밋 후 회고 · 압축 전 회고 · 플랜 리뷰 게이트 |

### hook

| 파일 | 시점 | 하는 일 |
|------|------|---------|
| `session_start_brief.py` | 세션 시작 | `VERSION`, 최근 log·insight, `dev/impl/progress.md` 다음 착수 지점, `dev/plan/README.md` 현재 위치, `handoff.md` 남은 작업을 요약 출력 |
| `post_commit_review.py` | Bash 실행 후 HEAD가 전진했을 때 | project-memory 회고 리마인더 (설치 후 첫 커밋은 기준점만 기록, `project-memory/`·`.claude/`만 바꾼 커밋은 제외) |
| `pre_compact_review.py` | 수동 `/compact` 직전 | 편집이 있었으면 회고 리마인더 |
| `pre_plan_exit_review.py` | 플랜 모드 종료 시 | Codex/Copilot 플러그인이 있으면 플랜 리뷰 요청, 없으면 통과 |

끄려면 홈 디렉터리에 빈 파일을 만든다: `.no-git-guide-session-brief`, `.no-commit-review`, `.no-pre-compact-review`, `.no-plan-exit-review`.
Windows에서 `python` 명령이 없고 `py`만 있으면 `settings.json`의 `python`을 `py`로 바꾼다.

## 버전 규칙

`MAJOR.MINOR.PATCH` ([semver.org](https://semver.org)). 이 프로젝트에서 "사용자"는 **학습자**이고,
"호환성"은 **학습자가 저장한 링크·진도·학습 순서가 그대로 유효한가**로 판단한다.

| 세그먼트 | 올리는 조건 | 예시 |
|----------|------------|------|
| **MAJOR** | 기존 링크·학습 순서가 깨지는 변경 | 커리큘럼 단계 재편·번호 변경, 레슨 파일 경로 변경, 페이지 구조 전면 개편 |
| **MINOR** | 기존을 유지하며 학습 내용 추가 | 새 레슨(단계) 추가, 새 인터랙티브 도식, 기존 레슨에 새 장면 추가 |
| **PATCH** | 내용 추가 없는 수정 | 오탈자·설명 다듬기, 도식 동작 버그 수정, 스타일·접근성 개선 |

**판단이 애매할 때:**
- "북마크해 둔 레슨 URL이 그대로 열리고, 같은 단계 번호를 가리키는가?" → NO면 MAJOR
- "학습자가 새로 배울 수 있는 것이 생겼는가?" → YES면 MINOR
- 여러 오류를 한꺼번에 고쳤어도 새 학습 내용이 없으면 PATCH

상위 세그먼트를 올리면 하위는 0으로 초기화한다 (`0.3.2` → MINOR → `0.4.0`).

**`1.0.0`의 기준:** README의 커리큘럼 0~10단계가 모두 레슨으로 완성된 시점. 그 전까지는 `0.x`로 운영하며,
`0.x` 기간에는 레슨 하나를 완성할 때마다 MINOR를 올린다.

프리릴리즈 식별자(`-alpha`, `-beta`, `-rc`)는 사용하지 않는다. 정적 사이트라 바로 정식 버전을 올려도 되고,
미완성 레슨은 브랜치에서 작업한다.

## Git 태그와 GitHub Release

태그와 GitHub Release는 [`.github/workflows/release.yml`](../.github/workflows/release.yml)이 자동으로 만든다.

- `VERSION`이 바뀐 커밋이 main에 push되면 실행된다
- `v{VERSION}` 태그가 아직 릴리즈되지 않았으면, 그 커밋에 태그를 붙이고 GitHub Release를 만든다
- 제목은 `release-notes/v{VERSION}.md`의 첫 줄(`## ` 제외), 본문은 나머지 내용
- 이미 릴리즈된 버전이면 아무것도 하지 않는다. Actions 탭에서 수동으로 다시 실행할 수도 있다

태그를 손으로 만들지 않는 이유는
[project-memory/decisions/release-automation.md](../project-memory/decisions/release-automation.md) 참고.

```bash
git fetch --tags
git tag --sort=-version:refname   # 최신순 목록
git switch --detach v0.1.0        # 특정 버전으로 이동
```

## 릴리즈 노트 형식

`release-notes/v{버전}.md`. 변경이 없는 섹션은 생략한다.

```markdown
## v0.2.0 — 한 줄 요약

### 새 레슨
- **N단계 · 주제** — 무엇을 배우는지

### 새 도식·인터랙션
- **도식 이름** — 무엇을 보여주는지

### 개선
- **항목** — 설명

### 버그 수정
- **증상** — 수정 내용

### 구조 변경
- 경로·파일 이동, 링크 변경 등 (MAJOR라면 필수)

### 신규 파일
- `lessons/03-commit.html` — 역할 설명
```

## 업데이트 전달 방식

앱 내 업데이트 확인 기능은 만들지 않는다. 근거는
[project-memory/decisions/update-delivery-download.md](../project-memory/decisions/update-delivery-download.md).

- **웹으로 보는 학습자** — (웹 배포 여부는 미정, [dev/plan/open-questions.md B2](../dev/plan/open-questions.md#b2-공개-방식-github-pages-여부)) 배포하게 되면 사이트가 push 시점에 바로 갱신된다.
- **내려받아 보는 학습자** — 새 버전을 다시 내려받는다. 무엇이 바뀌었는지는 `release-notes/`에서 확인한다.
- **버전 표시** — 페이지가 생기면 `index.html` 푸터에 현재 버전과 릴리즈 노트 링크를 둔다. 값은 `assets/js/version.js`의 사본이고, 릴리즈 워크플로가 `VERSION`과 비교한다([version-display 결정](../project-memory/decisions/version-display.md)).

## 워크플로 요약

```
레슨/도식 작업 완료
    ↓
버전 결정 (MAJOR / MINOR / PATCH)
    ↓
docs/UPDATE_CHECKLIST.md 순서대로 실행
    ├── VERSION 갱신
    ├── release-notes/v{버전}.md 작성
    ├── README.md 커리큘럼·구조 갱신
    ├── 콘텐츠 정확성 · 안전성 · 브라우저 확인
    └── project-memory 갱신 점검
    ↓
커밋 "vX.Y.Z: 변경 요약" → git push origin main
    ↓
GitHub Actions가 태그 vX.Y.Z + GitHub Release 생성
```

## 체크리스트 항목 추가 기준

| 상황 | 추가할 항목 |
|------|-------------|
| GitHub Pages 배포를 시작한 경우 | 8번에 배포 페이지 확인을 필수로 승격 |
| CI(링크 검사, HTML 검증 등)를 도입한 경우 | 6번에 CI 통과 확인 추가 |
| 다국어(영어 등) 버전을 추가한 경우 | 4번에 번역본 동기화 확인 추가 |
| 빌드 도구를 도입한 경우 | 6번에 빌드 명령 추가, 버전 소스를 매니페스트로 옮길지 검토 |
