# 진행 로그 (핸드오프)

최신이 위. 각 항목: 날짜 · 완료분 · 다음 착수 지점. 상세 백로그는 [checklist.md](checklist.md).

## 다음 착수 지점

**A5 사용자 결정 먼저 (코드 없음).** R7(전체 계획 → 단계별 완성)에 맞춰 백로그를 어떻게 둘지 정한다: `open-questions.md` A5.
- 결정에 따라 다음 단계는 (a) **Phase 0 · 커리큘럼 단계별 범위 확정** 또는 (b) **Phase 0 · 0단계 흐름** 이다. 어느 쪽이든 플랜 모드부터.
- 관련: `checklist.md` Phase 0, `open-questions.md` A2·A3·A4·A5. 용어는 `docs/design/glossary.md`, 도식은 `docs/design/diagram-model.md`를 따른다.

**미검증**: `open-questions.md` — 2026-10-14 Phase 0 용어집·공용 도식 모델: 해소 **A1**, 추가 **A4 A5**, 갱신 **A2 A3 B2**.

## 2026-10-14 — Phase 0 · 용어집 + 공용 도식 모델 (코드 없음)

- **사용자 결정**(플랜 중): R5 학습자는 Git을 쓰지 않고 개념만, R6 용어는 정확하게(Pro Git 한국어판), R7 전체 계획 → 단계별 완성. D1~D4 승인, D5 원고 표기 우선, D6 워킹 트리(주)=워킹 디렉토리(별칭), D7 기본 브랜치 `main`(`master`는 첫 소개 때 언급), D8 명령어 형태는 사이트·README 전체에서 금지
- **플랜 검수**: Opus 5.5 — NO-GO(P1 7) → 반영 → 회귀 P1 → 반영(D8 범위는 사용자 결정) → 회귀 P1 → 반영 → **GO**(P2 1 반영)
- **구현**: `docs/design/glossary.md`(원고 고정 커밋 `f50647d`, 출처 대조 누락 0), `docs/design/diagram-model.md`, R5~R7 기록(`impl/README.md`, `CLAUDE.md`, `decisions/learning-scope-and-terms.md`), 잘못된 전제 정정(README 명령어 0건, impl·UPDATE_CHECKLIST·RELEASE_MANAGEMENT), `decisions/update-delivery-download.md`가 옛 결정 대체. 손대지 않음: README 단계 이름 "병합"·"리베이스"(A4)
- **문서 검수**: Opus 5.5(실행 모델 claude-opus-5-5 확인) — NO-GO(P1 4: 옛 `git pull` 전제, 로컬 데이터베이스 정의 충돌, 해소된 A1 참조, "리베이스" 비원고 표기) → 반영 → **GO**
- **자동 확인**: 해당 없음(Phase 0). 대신 전제·명령어·비표준 표기 grep 허용 위치 외 0건
- **미검증**: 해소 A1, 추가 A4 A5, 갱신 A2 A3 B2
- **핸드오프 점검**: 아래 커밋 뒤 수행

**다음**: A5 결정 → 커리큘럼 단계별 범위 확정 또는 0단계 흐름 (플랜 모드부터).

## 2026-10-13 — C1 해소 (사용자 결정)

- **사용자 결정**: 독립 검수자 = 맥락 없는 서브에이전트, 모델 Opus 5.5. `impl/README.md` 확정 전제·`decisions/reviewer.md`에 반영
- **미검증**: 해소 C1

## 2026-10-13 — 구현 프로세스 도입 (코드 없음)

- **사용자 결정**: 도식은 로컬·리모트 공용 틀(R1), 0단계는 로컬/서버 버전 관리 개념부터(R2). 상세 장면·도식 안은 아직 제안 단계
- **구현**: `impl/` 4개 문서, `docs/design/` 위치 지정, `CLAUDE.md` 구현 원칙, 미해결 장부를 `impl/open-questions.md`로 일원화. README 0단계 설명 갱신
- **미검증**: 추가 A1 A2 A3 B1 B2 C1 C2 (B1·B2는 `project-memory/open-questions.md`에서 이관)
- **핸드오프 점검**: 통과(5/5). 고친 곳: 이 로그의 빈 참조, Phase 0의 스모크·검수 적용 방식(README), components.md의 낡은 버전 표기

**다음**: Phase 0 · 공용 도식 모델 (플랜 모드부터).
