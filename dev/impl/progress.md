# 진행 로그 (핸드오프)

최신이 위. 각 항목: 날짜 · 완료분 · 다음 착수 지점. 상세 백로그는 [checklist.md](checklist.md).

## 다음 착수 지점

**구현 단계 아님 — 지금은 Design 단계.** [`dev/plan/README.md`](../plan/README.md)의 "현재 위치"(다음 설계: 자동 확인 도구 결정)를 따른다.
구현은 Design → Impl 게이트(모든 단위 설계 완료 + 구현 준비 상태 점검) 뒤 [checklist.md](checklist.md)를 다시 편성해 시작한다.

## 2026-10-27 — U-diagram 공용 도식 컴포넌트 구현 구분 (커밋 `958e1ab`, Design 단계 · 코드 없음, 2026-10-21~27)

- 설계: `dev/design/diagram-component-design.md`. 실측 `dev/evidence/2026-10-21-file-scheme.md`. 결정 1~5-c-2는 사용자, 이후는 사용자 위임(2026-10-24). 문서 검수 중 사용자 제안으로 레슨 화면 방향(슬라이드형·나레이션·툴팁, 결정 14·15, 2026-10-27) 추가
- 플랜 검수: Opus 5.5 서브에이전트 — 1회차 NO-GO(P1 3) → 2회차 NO-GO(P1 1) → 3회차 NO-GO(P1 1, 회귀) → 4회차 GO
- 문서 검수: Opus 5.5 서브에이전트(맥락 없음, model opus 지정) — 1회차 NO-GO(P1 1: `window.GitGuide` 생성 주체) → 2회차 NO-GO(P1 2: 결정 14 세부를 사용자 결정으로 적음, D1·overview 역전파·`notes` 표시 방식) → 3회차 GO(P2 2건 반영, 참고 1건은 Phase 1 미결에 추가)
- 미검증: 해소 B1, 추가 B3·Firefox/Safari `file://` 실측(`dev/plan/open-questions.md`)
- 핸드오프 점검: 통과 — 다음 단위(자동 확인 도구 결정)·플랜 모드·C2를 짚음, 지운 ID 비대상, git 깨끗·원격과 같음. 고친 곳: 이 로그 제목(해시·날짜), plan README 질문 방식 문구, checklist C2 항목 산출물 형태 메모
- 다음: 자동 확인 도구 결정(C2)

## 2026-10-19 — 커리큘럼 단계별 범위 확정, 용어 표기 R8 (커밋 `454e91d`, Design 단계 · 코드 없음)

- 설계: `dev/design/curriculum-scope-design.md`. 플랜 검수 Opus 5.5 3회차 GO, 문서 검수 1회차 GO(P2 2건 반영). 핸드오프 점검 통과
- 다음: `U-diagram` 설계(`dev/plan/README.md` 현재 위치)

## 2026-10-14 — 장기 개발 프로세스(최신 가이드) 적용, `dev/`로 재배치 (커밋 `fe95fde`, 코드 없음)

- **사용자 결정**: 최신 `LONG_TERM_DEV_PROCESS.md` 적용, plan·design·impl을 상위 폴더 하나로 → 루트 `dev/`("구현은 실제 코드잖아? 그러면 최상위 폴더를 docs 가 아닌 dev 가 좋겠는데?"), 가이드 사본도 폴더 구조에 맞게 고칠 것. A5는 위임("그건 니가 결정해도 되는데?") → 설계 완료 범위 A
- **구현**: `impl/` → `dev/impl/`, `docs/design/{glossary,diagram-model}.md` → `dev/design/`(git mv), `dev/plan/` 4문서·`dev/design/map.md`·`dev/evidence/` 신설, 가이드 적용본, Phase 0 항목·미결 장부를 `dev/plan/`으로 이관, 경로 갱신(CLAUDE.md·README·docs·project-memory·hook), 결정 `decisions/dev-process.md`
- **플랜 검수**: Opus 5.5 — NO-GO(P1 4, P2 8; P1-1은 사용자 위임 원문으로 반박) → 반영 → GO(P2 2) → 사용자 요청으로 가이드 적용본 절 추가 → GO(P2 4) — 모두 반영
- **문서 검수**: Opus 5.5(실행 모델 claude-opus-5-5 확인) — **GO**, P2 3건 중 2건 반영(U-diagram 시안 시점 문구, 범위 확정 예시 복원). `curriculum-foundations.md`의 "A1~A3"은 결정 본문 불변 규칙상 두고 바로 아래 진행 상황 주석으로 정정됨
- **확인**: 옛 경로 grep 허용 위치 외 0, 상대 링크·앵커 깨짐 0, 설계 문서 rename+링크 1줄, 가이드 적용본 diff는 규칙 1·3·4·상자 정렬뿐, hook 실행 확인
- **미검증**: A5 해소(→ 결정 문서), A2·A3·A4·B1·B2·C2는 `dev/plan/open-questions.md`로 이관(ID 유지). 구현 장부 0건
- **핸드오프 점검**: Design 진입·Impl 진입 모두 통과(5/5) — 둘 다 plan의 "커리큘럼 단계별 범위 확정"을 플랜 모드로 짚음. 고친 곳: `curriculum-foundations.md` 진행 상황 주석에 A4 추가

> 아래 로그는 재배치 전 기록이라 당시 경로(`impl/`, `docs/design/`)를 그대로 둔다.

## 2026-10-14 — Phase 0 · 용어집 + 공용 도식 모델 (코드 없음)

- **사용자 결정**(플랜 중): R5 학습자는 Git을 쓰지 않고 개념만, R6 용어는 정확하게(Pro Git 한국어판), R7 전체 계획 → 단계별 완성. D1~D4 승인, D5 원고 표기 우선, D6 워킹 트리(주)=워킹 디렉토리(별칭), D7 기본 브랜치 `main`(`master`는 첫 소개 때 언급), D8 명령어 형태는 사이트·README 전체에서 금지
- **플랜 검수**: Opus 5.5 — NO-GO(P1 7) → 반영 → 회귀 P1 → 반영(D8 범위는 사용자 결정) → 회귀 P1 → 반영 → **GO**(P2 1 반영)
- **구현**: `docs/design/glossary.md`(원고 고정 커밋 `f50647d`, 출처 대조 누락 0), `docs/design/diagram-model.md`, R5~R7 기록(`impl/README.md`, `CLAUDE.md`, `decisions/learning-scope-and-terms.md`), 잘못된 전제 정정(README 명령어 0건, impl·UPDATE_CHECKLIST·RELEASE_MANAGEMENT), `decisions/update-delivery-download.md`가 옛 결정 대체. 손대지 않음: README 단계 이름 "병합"·"리베이스"(A4)
- **문서 검수**: Opus 5.5(실행 모델 claude-opus-5-5 확인) — NO-GO(P1 4: 옛 `git pull` 전제, 로컬 데이터베이스 정의 충돌, 해소된 A1 참조, "리베이스" 비원고 표기) → 반영 → **GO**
- **자동 확인**: 해당 없음(Phase 0). 대신 전제·명령어·비표준 표기 grep 허용 위치 외 0건
- **미검증**: 해소 A1, 추가 A4 A5, 갱신 A2 A3 B2
- **핸드오프 점검**: 통과(5/5). 고친 곳: RELEASE_MANAGEMENT의 웹 배포 전제를 B2와 맞춤, 다음 착수 지점에 A5 링크·"플랜 모드 안에서 A5 먼저" 명시. `curriculum-foundations.md` 12행의 "A1~A3"은 결정 본문 불변 규칙상 그대로 두고 아래 진행 상황 주석으로 정정함

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
