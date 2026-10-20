# git-guide 앞단 체크리스트 (Plan · Design)

설계 진행 관리. 단위별 설계는 이 목록의 "남은 상세 설계"를 하나씩 플랜 모드로 진행한다(진행 방식: [README.md](README.md)).

---

## 역전파 체크리스트 (설계·확정 항목을 바꿀 때마다 복사해서 체크)

- [ ] 이 변경으로 바뀐 결정이 있는가? (없으면 종료)
- [ ] **★ 식별자 grep 역전파** — 바꾼 단위·항목의 ID(`L0`~`L10`·`U-diagram`·`A2` 등)와 관련 파일명을 `dev/`·`project-memory/`·`README.md`·`CLAUDE.md` 전체에서 grep해 인용처를 빠짐없이 갱신한다. 가장 잘 빠지는 곳: 다른 설계 문서의 상호 참조, ID를 나열한 요약 표, README 커리큘럼 표(map.md의 파생물)
- [ ] 설계 지도([`dev/design/map.md`](../design/map.md))의 해당 행 한 줄 요지 갱신(또는 "변경 없음" 확인)
- [ ] [`dev/plan/overview.md`](overview.md)의 확정 사실·전제에 영향이 있는가
- [ ] [`dev/plan/open-questions.md`](open-questions.md)의 해소·신규 발생 반영(건수 포함)
- [ ] 설계 지도의 "참조" 칸이 실제 문서를 정확히 가리키는가

---

## 확정 (재논의 불필요)

| 항목 | 내용 | 근거 |
|---|---|---|
| R1~R7 | 절대 규칙 — 공용 틀, 0단계 시작점, 추론 확인, `file://`, 개념만, 정확한 용어, 전체 계획 후 단계별 완성 | [`dev/impl/README.md`](../impl/README.md) 확정 전제, `project-memory/decisions/` |
| R8 | 절대 규칙 — 원고 표기가 영문인 용어는 "한글 표현 (원고 표기)"로 함께 적는다 | 2026-10-19 사용자 지시 · `project-memory/decisions/term-notation.md` |
| D1~D8 | 조작·로컬 영역·공간 수·배치·표기·이표기·`main`·명령어 미노출 | `project-memory/decisions/learning-scope-and-terms.md`, 아래 완료 항목 명세 |
| 검수자 | 맥락 없는 서브에이전트, Opus 5.5 | `project-memory/decisions/reviewer.md` |
| 설계 완료 범위 | **A — 모든 단위(아래 남은 상세 설계 전건) 설계 후 구현** | 사용자 위임 2026-10-14 "그건 니가 결정해도 되는데?" · `project-memory/decisions/dev-process.md` |
| 폴더 위치 | 루트 `dev/` 아래 plan·design·impl·evidence | 사용자 2026-10-14 · 같은 결정 문서 |

### 완료된 설계

- [x] **용어집**(2026-10-14 완료 · 문서 검수 Opus 5.5 2회차 GO) — [`dev/design/glossary.md`](../design/glossary.md). 함께: 절대 규칙 R5·R6 기록, 잘못된 전제("명령 실행") 정정.
      **승인된 명세**(플랜 검수 4회 · Opus 5.5 GO, 사용자 승인 2026-10-14 — 플랜 파일은 세션 밖이라 여기에 고정):
      - 근거 원고: `https://github.com/progit/progit2-ko` 커밋 `f50647da032bf210ef91802290d60d05da1a9416`. 출처 형식 `book/<장>/sections/<파일>.asc` + 절 제목
      - D5 표기: Pro Git 한국어판 표기 그대로(맞춤법보다 원문 우선, 원문이 영문이면 영문 유지), 처음 나올 때 영문 병기
      - D6 이표기: 주 표기 + 별칭. 워킹 트리(주) = 워킹 디렉토리(별칭)
      - D7 기본 브랜치: `main`. `master`는 브랜치 첫 소개 때 "예전 기본 이름이자 Pro Git이 쓰는 이름"으로 한 번 언급
      - D8 명령어: 용어만. `git …` 명령어 형태는 사이트와 README 전체에 쓰지 않음
      - 항목 형식: 용어(주 표기) · 별칭 · 영문 · 정의 1~2문장 · 처음 나오는 단계(잠정) · 출처
      - 범위: VCS, 로컬 버전 관리(로컬 VCS), 로컬 데이터베이스, 중앙집중식 버전 관리(CVCS), 중앙 서버, 중앙 데이터베이스, DVCS, 저장소, 리모트 저장소, 워킹 트리, Staging Area(Index), Git 디렉토리, 커밋, 스냅샷, Committed·Modified·Staged, 브랜치, HEAD, 리모트 트래킹 브랜치, Stage·Commit·Checkout·Clone·Push·Fetch·Merge·Pull
      - 원고에서 확인 못 한 표기는 넣지 않고 open-questions에 남김
      - R5·R6를 `dev/impl/README.md`(당시 `impl/README.md`)·`CLAUDE.md`·`project-memory/decisions/learning-scope-and-terms.md`에 기록
      - 전제 정정 대상: README(소개·특징·커리큘럼 표 명령어 제거·사용 방법 Download ZIP·기여하기), `impl/README.md`·`impl/open-questions.md`·`impl/checklist.md`(당시 경로, 지금 `dev/impl/`), `docs/UPDATE_CHECKLIST.md`, `docs/RELEASE_MANAGEMENT.md`
      - 확인: 잘못된 전제·비표준 표기 grep(허용 위치 외 0건, README는 명령어 0건), 고정 커밋 재클론 후 출처 대조
- [x] **공용 도식 모델**(2026-10-14 완료 · 같은 검수) — [`dev/design/diagram-model.md`](../design/diagram-model.md). 로컬·리모트 두 공간(R1)을 이루는 영역, 화면 요소, 전이 애니메이션, 레슨별 노출 범위.
      **승인된 명세**(같은 플랜, 2026-10-14):
      - D1 조작: 장면 이전/다음, 장면 처음으로. 도식 요소를 누르면 용어집 정의. 명령 입력·드래그 없음
      - D2 로컬 영역: 로컬 VCS 장면 "파일 | 로컬 데이터베이스", CVCS 장면 로컬에 파일만, Git 장면부터 "워킹 트리 | Staging Area | Git 디렉토리"
      - D3 공간: 도식 속 서버 상자 1개 + 로컬 상자 N개(기본 "나", CVCS 한계·DVCS 복제·협업 장면에서 "동료" 추가). 실제 서버·네트워크 없음
      - D4 배치: 데스크톱 로컬 왼쪽·서버 오른쪽, 로컬 2개면 나·서버·동료. 모바일 위아래
      - 서버 상자 라벨: 로컬 VCS 장면 없음 / CVCS "중앙 서버" / Git "리모트 저장소"
      - 문서 목차: 공간 · 영역 · 요소(파일 카드 상태, 커밋 노드, 브랜치·HEAD·리모트 트래킹 브랜치) · 전이 표(Stage, Commit, Checkout, Clone, Push, Fetch, Merge, Pull) · 표시 상태(숨김/흐리게/활성) · 레슨별 노출 범위(잠정) · 조작 · 배치

---

## 단위별 남은 상세 설계 (의존 순서 — 위에서부터)

각 항목은 플랜 모드 → 설계 문서(`dev/design/<개념>-design.md`) → 독립 검수 GO → 역전파 → `[x]` + 한 단락 요약·링크 → 커밋 순서로 끝낸다.

- [x] **커리큘럼 단계별 범위 확정**(2026-10-19 완료 · 플랜 검수 Opus 5.5 3회차 GO · 문서 검수 Opus 5.5 1회차 GO, P2 2건 반영) — [`dev/design/curriculum-scope-design.md`](../design/curriculum-scope-design.md).
      단계 0~10의 범위를 원고 장·절에 맞춰 확정했다. Clone은 1단계(히스토리 복제까지, `origin`·리모트 트래킹 브랜치는 8단계 — 1~7단계 도식에서 숨김), 4단계 되돌리기는 원고 2장 범위(Reset·revert 제외), 9·10단계는 원고 표기로.
      새 절대 규칙 **R8**: 원고가 영문인 용어는 "한글 표현 (원고 표기)"로 병기(대상·빈도·Checkout 0단계 예외는 용어집 표기 원칙). 단계 이름 `L6` "병합 (Merge)", `L7` "커밋 다시 쌓기 (Rebase)".
      용어집에 "한글 표현" 칸과 용어 13개 추가, A3·A4 해소, 새 미결 A6(Fork 장면 서버 저장소 개수). 결정: `project-memory/decisions/term-notation.md`
- [ ] **`U-diagram` 공용 도식 컴포넌트 구현 구분** — 공용 도식 모델(확정)을 구현할 설정 계약(공간·영역·커밋 히스토리 상태의 입력 형식)과 파일 구조(`index.html`·`lessons/`·`assets/`). R4·`file://` 제약 포함. 이 항목은 구현 계약만 정한다 — 도식 모양 시안은 `diagram-model.md` 3절대로 구현 Phase 1에서 확인한다(시점을 바꾸려면 사용자와 의논).
      결정할 것: [B1](open-questions.md#b1-화면-버전-표시와-version-동기화), `file://` 실측(open-questions "확보할 자료·실측")
- [ ] **자동 확인 도구 결정** — 결과는 `dev/impl/README.md` 확정 전제에 반영.
      결정할 것: [C2](open-questions.md#c2-자동-확인-도구)
- [ ] **L0 · 버전 관리란?** — 결정할 것: [A2](open-questions.md#a2-0단계-장면-구성)
- [ ] **L1 · 저장소 만들기**
- [ ] **L2 · 세 가지 영역**
- [ ] **L3 · 커밋**
- [ ] **L4 · 변경 확인과 되돌리기**
- [ ] **L5 · 브랜치**
- [ ] **L6 · 병합 (Merge)**
- [ ] **L7 · 커밋 다시 쌓기 (Rebase)**
- [ ] **L8 · 리모트 저장소**
- [ ] **L9 · 협업 흐름** — 결정할 것: [A6](open-questions.md#a6-fork-장면의-서버-쪽-저장소-개수)
- [ ] **L10 · 유용한 도구**

(단위 이름은 [curriculum-scope-design.md](../design/curriculum-scope-design.md)의 단계 이름. 단계가 추가·이동되면 새 ID를 붙이고 재번호화하지 않는다.)

---

## 외부 리뷰 보강 (필수 반영)

- [ ] Clone 정의(용어집 "처음" 0)가 `origin`(용어집 "처음" 8)을 쓴다 — 정의 문장이 뒤 단계 용어를 쓰는 경우(용어집 머리말 원칙). 해당 레슨 설계(L0·L1·L8) 때 화면 문장을 조정한다. 출처: 2026-10-14 문서 검수 참고
      처리 방향(2026-10-19): Q1에 따라 용어집 Clone 정의의 `origin` 문장을 "(8단계 보충)"으로 분리하고 1~7단계 화면에서는 쓰지 않기로 했다. L0·L1 설계에서 화면 문장을 확인하면 `[x]`
