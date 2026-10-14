# 구현 백로그

Phase별 항목. 각 항목은 플랜 모드 → 승인 → **승인된 명세를 이 파일에 고정** → 구현 순서로 진행한다.
아직 승인된 명세가 없는 항목은 한 줄 요약과 "플랜에서 정할 것"만 있다.

---

## Phase 0 — 설계 고정

코드 없이 `docs/design/`에 설계를 확정한다. 각 항목은 사용자와 의논해 결정한다(R3).

- [x] **용어집**(2026-10-14 완료 · 문서 검수 Opus 5.5 2회차 GO) — `docs/design/glossary.md`. 함께: 절대 규칙 R5·R6 기록, 잘못된 전제("명령 실행") 정정.
      **승인된 명세**(플랜 검수 4회 · Opus 5.5 GO, 사용자 승인 2026-10-14 — 플랜 파일은 세션 밖이라 여기에 고정):
      - 근거 원고: `https://github.com/progit/progit2-ko` 커밋 `f50647da032bf210ef91802290d60d05da1a9416`. 출처 형식 `book/<장>/sections/<파일>.asc` + 절 제목
      - D5 표기: Pro Git 한국어판 표기 그대로(맞춤법보다 원문 우선, 원문이 영문이면 영문 유지), 처음 나올 때 영문 병기
      - D6 이표기: 주 표기 + 별칭. 워킹 트리(주) = 워킹 디렉토리(별칭)
      - D7 기본 브랜치: `main`. `master`는 브랜치 첫 소개 때 "예전 기본 이름이자 Pro Git이 쓰는 이름"으로 한 번 언급
      - D8 명령어: 용어만. `git …` 명령어 형태는 사이트와 README 전체에 쓰지 않음
      - 항목 형식: 용어(주 표기) · 별칭 · 영문 · 정의 1~2문장 · 처음 나오는 단계(잠정) · 출처
      - 범위: VCS, 로컬 버전 관리(로컬 VCS), 로컬 데이터베이스, 중앙집중식 버전 관리(CVCS), 중앙 서버, 중앙 데이터베이스, DVCS, 저장소, 리모트 저장소, 워킹 트리, Staging Area(Index), Git 디렉토리, 커밋, 스냅샷, Committed·Modified·Staged, 브랜치, HEAD, 리모트 트래킹 브랜치, Stage·Commit·Checkout·Clone·Push·Fetch·Merge·Pull
      - 원고에서 확인 못 한 표기는 넣지 않고 open-questions에 남김
      - R5·R6를 `impl/README.md`·`CLAUDE.md`·`project-memory/decisions/learning-scope-and-terms.md`에 기록
      - 전제 정정 대상: README(소개·특징·커리큘럼 표 명령어 제거·사용 방법 Download ZIP·기여하기), `impl/README.md`, `impl/open-questions.md`, `impl/checklist.md`, `docs/UPDATE_CHECKLIST.md`, `docs/RELEASE_MANAGEMENT.md`
      - 확인: 잘못된 전제·비표준 표기 grep(허용 위치 외 0건, README는 명령어 0건), 고정 커밋 재클론 후 출처 대조
- [x] **공용 도식 모델**(2026-10-14 완료 · 같은 검수) — `docs/design/diagram-model.md`. 로컬·리모트 두 공간(R1)을 이루는 영역, 화면 요소, 전이 애니메이션, 레슨별 노출 범위.
      **승인된 명세**(같은 플랜, 2026-10-14):
      - D1 조작: 장면 이전/다음, 장면 처음으로. 도식 요소를 누르면 용어집 정의. 명령 입력·드래그 없음
      - D2 로컬 영역: 로컬 VCS 장면 "파일 | 로컬 데이터베이스", CVCS 장면 로컬에 파일만, Git 장면부터 "워킹 트리 | Staging Area | Git 디렉토리"
      - D3 공간: 도식 속 서버 상자 1개 + 로컬 상자 N개(기본 "나", CVCS 한계·DVCS 복제·협업 장면에서 "동료" 추가). 실제 서버·네트워크 없음
      - D4 배치: 데스크톱 로컬 왼쪽·서버 오른쪽, 로컬 2개면 나·서버·동료. 모바일 위아래
      - 서버 상자 라벨: 로컬 VCS 장면 없음 / CVCS "중앙 서버" / Git "리모트 저장소"
      - 문서 목차: 공간 · 영역 · 요소(파일 카드 상태, 커밋 노드, 브랜치·HEAD·리모트 트래킹 브랜치) · 전이 표(Stage, Commit, Checkout, Clone, Push, Fetch, Merge, Pull) · 표시 상태(숨김/흐리게/활성) · 레슨별 노출 범위(잠정) · 조작 · 배치
- [ ] **0단계 흐름** — `docs/design/lesson-00.md`. Git 이전의 로컬/서버 버전 관리 개념부터 시작하는 장면 구성(R2).
      **플랜에서 정할 것**: [A2](open-questions.md#a2-0단계-장면-구성), [A3](open-questions.md#a3-clone-개념을-다루는-단계)
- [ ] **커리큘럼 단계별 범위 확정** — README 커리큘럼 표의 단계별 개념·용어 범위를 다시 정한다(추가·삭제·이동).
      2026-10-14에는 범위를 유지한 채 명령어만 뺐다. 예: 4단계 되돌리기 개념 중 원고에 없는 것, 5단계 브랜치 전환 용어(원고는 Checkout).
      **플랜에서 정할 것**: [A3](open-questions.md#a3-clone-개념을-다루는-단계), [A4](open-questions.md#a4-용어집-처음-나오는-단계-잠정값과-readme의-용어-미정-항목)
- [ ] **자동 확인 도구 결정** — 결정은 `impl/README.md` 확정 전제와 `project-memory/decisions/`에 반영.
      **플랜에서 정할 것**: [C2](open-questions.md#c2-자동-확인-도구)
- [x] 검수자 지정 모델(2026-10-13) — 사용자 결정: Opus 5.5 서브에이전트. C1 해소 → `project-memory/decisions/reviewer.md`

## Phase 1 — 최소 end-to-end 슬라이스

- [ ] **공용 틀 + 첫 장면** — `assets/js/`, `assets/css/`, `index.html`, `lessons/00-*.html`.
      공용 도식 컴포넌트 최소판과 0단계 첫 장면 하나를 `file://`에서 끝까지 동작시켜, 컴포넌트 계약·스모크 절차를 조기 검증한다.
      **플랜에서 정할 것**: 컴포넌트 설정 형식(계약), 파일 구조, [B1](open-questions.md#b1-화면-버전-표시와-version-동기화)

## Phase 2 — 0단계 완성

- [ ] **0단계 나머지 장면** — Phase 0의 `lesson-00.md` 명세대로. 완성 시 MINOR 릴리즈 대상.

## Phase 3 — 1~10단계

레슨 하나 = 항목 하나. 순서는 README 커리큘럼 표를 따르며, 앞 단계가 끝나기 전에 건너뛰지 않는다.

- [ ] **1단계 · 저장소 만들기**
- [ ] **2단계 · 세 가지 영역**
- [ ] **3단계 · 커밋**
- [ ] **4단계 · 변경 확인과 되돌리기**
- [ ] **5단계 · 브랜치**
- [ ] **6단계 · 병합**
- [ ] **7단계 · 리베이스**
- [ ] **8단계 · 리모트 저장소**
- [ ] **9단계 · 협업 흐름**
- [ ] **10단계 · 유용한 도구**
