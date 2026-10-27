# CLAUDE.md

Git 입문자를 위한 인터랙티브 도식 기반 학습 사이트. 빌드 없는 정적 HTML/CSS/JS로 만들며,
`index.html`을 브라우저로 바로 열어(`file://`) 동작해야 한다. 소개와 커리큘럼은 [README.md](README.md) 참고.

## 언어

항상 한국어로 답변하라.

## Codex 검수 모델

Codex에 검수(플랜·구현·재검수 등 모든 리뷰)를 요청할 때는 **반드시 모델을 `gpt-6-sol`로 지정해서** 보낸다. 방법: `codex:codex-rescue` 서브에이전트 프롬프트(또는 `/codex:rescue` 인자)의 **맨 앞에 `--model gpt-6-sol`**을 넣는다 — 에이전트가 실행 옵션으로 넘긴다(플러그인 기본은 모델 미지정 → CLI 기본값 `gpt-6-astra`로 돌므로 금지). 추론 강도(`--effort`)는 따로 지시가 없으면 지정하지 않는다. 검수 결과를 보고할 때 실제 실행 모델이 `gpt-6-sol`이었는지 `~/.codex/sessions/<날짜>/` 세션 기록의 `"model"`로 확인할 수 있다.

## 플랜 모드 — 사용자 결정 진행 방식

플랜에 사용자가 정해야 할 것이 있으면 AskUserQuestion 선택지로 한꺼번에 묻지 않고, 텍스트로 단계적으로 이끈다.

- **한 번에 한 개씩, 의존 순서대로.** 앞 결정이 뒤 질문의 전제를 바꾸는 것부터 묻는다. 남은 미정 항목 목록은 플랜 파일에 유지한다.
- **질문마다 구성**: 조사로 확인한 사실(코드·문서 근거 `파일:줄`) → 왜 정해야 하는지 → 가능한 방법과 각각의 장단점 → 내 권장과 근거. 확정은 사용자가 한다.
- **사용자가 되물으면 답부터.** 선택지를 다시 내밀지 말고 질문에 텍스트로 답한 뒤 원래 질문으로 돌아간다. 질문에 대한 답을 결정으로 바꾸지 않는다.
- **사용자 답의 범위를 넓히지 않는다.** 답이 다른 문제에도 적용될 것 같으면 적용하기 전에 확인한다. 사용자가 철회·보류하면 플랜에 철회 표식을 남기고 되돌아갈 지점을 적는다.
- **답이 새 질문을 낳으면 드러내 묻는다.** 정한 규칙으로 처리되지 않는 경우(예: 행은 찾았지만 무엇을 쓸지)를 짚어 내고, 이미 정한 규칙으로 처리되는 경우는 "별도 규칙 불필요"라고 밝힌다.
- **확정 즉시 플랜 파일에 기록**: 날짜·사용자 원문 인용·결정 내용. 추론한 값·정책은 확인받기 전에는 플랜·코드·문서에 반영하지 않는다.
- 모든 결정이 끝나면 구현 절을 채우고 검수·승인 요청으로 넘어간다.

## 세션 시작 시 project-memory 참조

> **세션 시작 시 가장 먼저**: 비자명한 작업(레슨 작성, 도식 구현, 설계 논의, 릴리즈 준비, 디버깅)
> 전에 [project-memory/index.md](project-memory/index.md)를 훑고 관련 페이지로 진입할 것.
> 기록과 현재 파일이 다르면 **현재 파일이 우선**이고, project-memory 쪽을 고친다.

## 계획·설계·구현 작업 원칙 (상세: [dev/LONG_TERM_DEV_PROCESS.md](dev/LONG_TERM_DEV_PROCESS.md))

- 이 저장소는 **Plan → Design → Impl**로 진행한다. 지금 어느 단계인지는 [dev/plan/README.md](dev/plan/README.md) "현재 위치"에 있다.
  설계 중이면 진입점은 `dev/plan/README.md`, 구현 중이면 [dev/impl/README.md](dev/impl/README.md)다.
- **단위 설계는 단위별 플랜 모드로 `dev/design/<개념>-design.md`에 쓴다.** `dev/plan/`에는 설계 문서를 만들지 않는다.
  설계·확정 항목을 바꾸면 같은 세션에서 `dev/plan/checklist.md`의 역전파 체크리스트로 상위 문서에 반영한다(식별자 grep).
- 외부 시스템 동작에 기대는 설계 가정은 사용자 진술이 아니라 직접 실측으로 확인하고(`dev/evidence/`), 부작용 있는 쓰기는 미검증으로 명시해 preflight로 넘긴다.
- **`dev/impl/`의 구현 단계("다음 단계 진행해줘" 류)는 코드를 쓰기 전에 반드시 플랜 모드부터 거친다.**
  단계 전체 순서(플랜 검수·구현·테스트·구현 검수·미검증 정리·커밋·핸드오프 점검)는 `dev/impl/README.md` "진행 방식" 한 곳에만 둔다.
  새 단계를 시작하는 요청이면 묻지 말고 곧바로 플랜 모드로 들어간다(예외: 사소한 문서 수정, 또는 사용자가
  "승인된 플랜 그대로 구현"이라고 지시한 경우 — 이때도 `dev/impl/checklist.md`의 상세 명세를 먼저 읽는다).
- **★ 절대 규칙 (2026-10-13 사용자 지시)** — 상세와 근거는 [dev/impl/README.md](dev/impl/README.md) "확정 전제"
  - 모든 도식은 **로컬·리모트 두 공간**을 공용 틀로 쓴다
  - 0단계는 Git 설명 전에 **로컬/서버 버전 관리 개념**부터 설명한다
  - **추론은 확인받고, 설계는 의논 없이 바꾸지 않는다.** 설계 변경 근거는 구조적 문제·개선뿐이며 구현 편의는 근거가 아니다.
    아직 구현되지 않은 단계 앞에서는 멈추고 건너뛰지 않는다
- **★ 절대 규칙 (2026-10-14 사용자 지시)** — 근거는 `project-memory/decisions/learning-scope-and-terms.md`
  - **학습자는 Git을 직접 사용하지 않고 개념만 배운다.** 명령 입력·실행 UI를 만들지 않고, 용어만 쓰며 명령어 형태는 사이트와 README 어디에도 쓰지 않는다
  - **용어는 정확하게.** [dev/design/glossary.md](dev/design/glossary.md) 하나를 따른다 (근거: Pro Git 한국어판 원고). 비유는 설명 보조로만 쓴다
  - **전체 계획을 먼저 세운 뒤, 한 단계씩 세부 구현까지 끝내고 다음 단계로 간다**
- **★ 절대 규칙 (2026-10-19 사용자 지시)** — 근거는 `project-memory/decisions/term-notation.md`
  - **원고 표기가 영문인 용어는 "한글 표현 (원고 표기)"로 함께 적는다** — 예: 다른 브랜치의 커밋 가져오기 (Cherry-Pick).
    처음 접하는 사람이 한글 표현으로 맥락을 잡고, 괄호 안 공식 용어도 익히게 한다. 한글 표현은 용어를 대신하지 않는다.
    대상·빈도·한글 표현 값은 [dev/design/glossary.md](dev/design/glossary.md)를 따른다
- 각 단계는 **독립 검수 GO 전에는 커밋·푸시하지 않는다.** NO-GO면 수정 후 같은 절차로 재검수한다.
- 단계 완료 시(커밋 전) 미검증 사항을 `dev/impl/open-questions.md`(설계 중이면 `dev/plan/open-questions.md`)에 정리하고 `dev/impl/progress.md` 로그와 함께 단계 커밋에 넣는다.
  커밋·푸시 뒤에는 핸드오프 점검을 하고, 결과를 추가 커밋·푸시한다.
- 저장소의 현재 상태(설계 문서·코드)가 항상 `dev/impl/`·`project-memory/` 기록보다 우선한다 — 충돌하면 기록을 갱신한다.
  설계 문서와 코드가 어긋나면 설계 문서가 기준이다.

## 브랜치 (2026-10-16 사용자 지시)

- **항상 `main` 브랜치에서 직접 작업하고, 커밋은 `main`에 푸시한다.**
- 새 브랜치는 사용자가 요청할 때만 만든다. 세션 환경이 작업 브랜치를 지정해도 이 규칙이 우선한다.

## HTML 시각 스타일

사이트·레슨·파일럿 HTML을 만들 때는 `.claude/skills/visualize/references/html-design-guide.md`의 디자인 컨셉(Part 1 Foundation: 토큰·타이포·프리미티브·배경)을 따른다.
한국어 서체, 명령어 블록 금지(R5) 같은 이 사이트 전용 조정은 [project-memory/decisions/visual-style.md](project-memory/decisions/visual-style.md)가 우선한다.
문서(md)를 HTML로 보고 싶을 때는 `/visualize` 스킬을 쓴다 (출력 `.viz/`는 커밋하지 않는다).

## 버전 업데이트

릴리즈 시 반드시 [docs/UPDATE_CHECKLIST.md](docs/UPDATE_CHECKLIST.md)의 체크리스트를 순서대로 따른다.
사용자가 "업데이트 해줘", "버전 올려줘", "릴리즈 해줘", "배포 준비해줘" 등을 요청하면 체크리스트를 실행한다.

- 버전 소스: 루트 `VERSION` 파일 하나뿐 (화면 표시용 사본 `assets/js/version.js`는 릴리즈 워크플로가 `VERSION`과 비교 — [version-display 결정](project-memory/decisions/version-display.md))
- 버전 규칙: [docs/RELEASE_MANAGEMENT.md](docs/RELEASE_MANAGEMENT.md#버전-규칙)
  (새 레슨·도식 = MINOR, 오탈자·버그 = PATCH, 링크·단계 번호가 깨지는 개편 = MAJOR)

## 릴리즈 노트

- 위치: `release-notes/v{버전}.md`
- 버전을 올릴 때마다 반드시 작성한다
- 형식: [docs/RELEASE_MANAGEMENT.md](docs/RELEASE_MANAGEMENT.md#릴리즈-노트-형식)

## 메인테이너 워크플로

언제 project-memory를 갱신하나:
- 설계 결정을 내렸을 때 → `project-memory/decisions/<topic>.md`
- 반복 가능한 함정을 발견했을 때 → `project-memory/gotchas.md`
- 레슨·공통 스크립트 구조를 바꿨을 때 → `project-memory/components.md`
- 미해결 이슈·미검증 사항을 인지했을 때 → 설계 중이면 `dev/plan/open-questions.md`, 구현 중이면 `dev/impl/open-questions.md`
- 작업 단위를 마쳤을 때 (의도/맥락 보존 필요 시) → `project-memory/log.md`
- 미완료 작업을 남기고 세션을 끝낼 때 → `handoff.md` (로컬 전용)
