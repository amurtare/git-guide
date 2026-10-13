# CLAUDE.md

Git 입문자를 위한 인터랙티브 도식 기반 학습 사이트. 빌드 없는 정적 HTML/CSS/JS로 만들며,
`index.html`을 브라우저로 바로 열어(`file://`) 동작해야 한다. 소개와 커리큘럼은 [README.md](README.md) 참고.

## 세션 시작 시 project-memory 참조

> **세션 시작 시 가장 먼저**: 비자명한 작업(레슨 작성, 도식 구현, 설계 논의, 릴리즈 준비, 디버깅)
> 전에 [project-memory/index.md](project-memory/index.md)를 훑고 관련 페이지로 진입할 것.
> 기록과 현재 파일이 다르면 **현재 파일이 우선**이고, project-memory 쪽을 고친다.

## 버전 업데이트

릴리즈 시 반드시 [docs/UPDATE_CHECKLIST.md](docs/UPDATE_CHECKLIST.md)의 체크리스트를 순서대로 따른다.
사용자가 "업데이트 해줘", "버전 올려줘", "릴리즈 해줘", "배포 준비해줘" 등을 요청하면 체크리스트를 실행한다.

- 버전 소스: 루트 `VERSION` 파일 하나뿐
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
- 미해결 이슈를 인지했을 때 → `project-memory/open-questions.md`
- 작업 단위를 마쳤을 때 (의도/맥락 보존 필요 시) → `project-memory/log.md`
- 미완료 작업을 남기고 세션을 끝낼 때 → `handoff.md` (로컬 전용)
