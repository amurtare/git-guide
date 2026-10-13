# project-memory

세션 시작 진입점. 관련 페이지만 골라 읽는다.
기록은 "기록 당시의 맥락"이다. **현재 파일·설정과 다르면 현재 파일이 우선**이며, 이쪽을 고치거나 superseded 표시한다.

## 개발 로그
- [log.md](log.md) — 작업 단위별 의도·맥락 (append-only)

## 설계 결정
- [decisions/version-source.md](decisions/version-source.md) — 버전 소스를 `VERSION` 파일로 둔 이유
- [decisions/update-delivery.md](decisions/update-delivery.md) — 앱 내 업데이트 확인 기능을 만들지 않는 이유
- [decisions/release-automation.md](decisions/release-automation.md) — 태그·릴리즈를 GitHub Actions가 만드는 이유
- [decisions/reviewer.md](decisions/reviewer.md) — 독립 검수자 = Opus 5.5 서브에이전트 (사용자 결정)
- [decisions/curriculum-foundations.md](decisions/curriculum-foundations.md) — 로컬·리모트 공용 틀, 0단계는 버전 관리 개념부터 (사용자 지시)

## 함정
- [gotchas.md](gotchas.md) — 반복해서 부딪힐 문제와 해법

## 구조
- [components.md](components.md) — 파일 구조와 레슨·공통 스크립트 관계

## 미해결 이슈
- [../impl/open-questions.md](../impl/open-questions.md) — 장부는 여기 하나 (구현 진행 상황은 [../impl/progress.md](../impl/progress.md))

## insight
- [insight/README.md](insight/README.md) — raw 메모 규칙
