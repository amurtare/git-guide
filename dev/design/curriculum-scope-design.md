# 커리큘럼 단계별 범위 상세 설계 (단위: L0~L10)

연결: [`dev/plan/checklist.md`](../plan/checklist.md) "커리큘럼 단계별 범위 확정". 대상: 단계마다 다루는 개념·용어의 범위와 단계 이름, 화면 용어 표기 형식(R8).
확정: 2026-10-19 (사용자 확정 Q1~Q8 · 플랜 검수 3회차 GO · 문서 검수 반영).

## 역할과 인터페이스

| 단위 | 단계 | 단계 이름 | 다루는 내용 | 원고 근거 (progit2-ko `f50647d`, `book/` 아래) |
|---|---|---|---|---|
| `L0` | 0 | 버전 관리란? | 로컬 버전 관리 → 중앙집중식 버전 관리(CVCS) → 분산 버전 관리 시스템(DVCS)으로서의 Git, Git과 GitHub의 차이 | `01-introduction/sections/about-version-control.asc` 버전 관리란? |
| `L1` | 1 | 저장소 만들기 | 저장소를 새로 만들기, 저장소 복제 (Clone) — 리모트 저장소의 히스토리 전체를 로컬로 복제하는 데까지, Git 디렉토리의 역할 | `02-git-basics/sections/getting-a-repository.asc` Git 저장소 만들기 |
| `L2` | 2 | 세 가지 영역 | 워킹 트리 · 커밋 준비 영역 (Staging Area) · Git 디렉토리, 커밋 준비 영역에 올리기 (Stage), 파일 상태 수정됨 (Modified) · 커밋 준비됨 (Staged) · 커밋됨 (Committed) | `01-introduction/sections/basics.asc` 세 가지 상태, `02-git-basics/sections/recording-changes.asc` 수정하고 저장소에 저장하기 |
| `L3` | 3 | 커밋 | 커밋하기 (Commit), 커밋 = 스냅샷, 커밋 히스토리 | `01-introduction/sections/basics.asc` 차이가 아니라 스냅샷, `02-git-basics/sections/recording-changes.asc` 변경사항 커밋하기, `02-git-basics/sections/viewing-history.asc` 커밋 히스토리 조회하기 |
| `L4` | 4 | 변경 확인과 되돌리기 | 변경 내용 확인 — 커밋 준비 전·후의 변경, 준비 취소 (Unstage), 수정됨 (Modified) 파일 되돌리기, 완료한 커밋 수정 | `02-git-basics/sections/recording-changes.asc` Staged와 Unstaged 상태의 변경 내용을 보기, `02-git-basics/sections/undoing.asc` 되돌리기 |
| `L5` | 5 | 브랜치 | 브랜치와 지금 위치 표시 (HEAD), 브랜치 만들기, 브랜치 이동 (Checkout) | `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가, 새 브랜치 생성하기, 브랜치 이동하기 |
| `L6` | 6 | 병합 (Merge) | 병합 (Merge), 빨리 감기 (Fast-forward)와 3방향 병합 (3-way Merge), 충돌 | `03-git-branching/sections/basic-branching-and-merging.asc` 브랜치의 기초(Fast forward 첫 정의), Merge 의 기초, 충돌의 기초 |
| `L7` | 7 | 커밋 다시 쌓기 (Rebase) | 커밋 다시 쌓기 (Rebase), 병합 (Merge)과의 차이, 주의할 점(이미 공유한 커밋) | `03-git-branching/sections/rebasing.asc` Rebase 하기, Rebase 의 위험성, Rebase vs. Merge |
| `L8` | 8 | 리모트 저장소 | 리모트 저장소 등록과 `origin`, 리모트 브랜치·리모트 트래킹 브랜치, 올려 보내기 (Push), 가져오기 (Fetch), 가져와 합치기 (Pull) | `02-git-basics/sections/remotes.asc` 리모트 저장소, `03-git-branching/sections/remote-branches.asc` 리모트 브랜치 |
| `L9` | 9 | 협업 흐름 | 내 계정으로 저장소 복사 (Fork), 병합 요청 (Pull Request)과 그 안의 코드 리뷰, 브랜치 워크플로, GitHub 플로우 | `06-github/sections/2-contributing.asc` 프로젝트 Fork 하기, GitHub 플로우, `03-git-branching/sections/workflows.asc` 브랜치 워크플로 |
| `L10` | 10 | 유용한 도구 | 하던 작업 임시 저장 (Stash), 태그, 파일 무시하기, 다른 브랜치의 커밋 가져오기 (Cherry-Pick) | `07-git-tools/sections/stashing-cleaning.asc` 하던 일을 Stash 하기, `02-git-basics/sections/tagging.asc` 태그, `02-git-basics/sections/recording-changes.asc` 파일 무시하기, `05-distributed-git/sections/maintaining.asc` Rebase와 Cherry-Pick 워크플로 |

- 단계 수·순서·ID는 바뀌지 않았다(0~10, `L0`~`L10`). 단계 이름이 바뀐 것은 `L6`·`L7`뿐이다.
- "다루는 내용" 칸은 R8 표기를 따른다. "원고 근거" 칸은 원고 절 제목을 원문 그대로 인용한다.
- **본격 설명 단계**(용어집 "처음" 칸은 처음 화면에 나오는 단계 하나만 적는다):
  - 저장소 복제 (Clone): 0단계 DVCS 설명에 처음 나오고, 1단계에서 설명한다
  - Checkout: 0단계는 CVCS 뜻(중앙 서버에서 받아 오기), Git 뜻(브랜치 이동)은 5단계에서 설명한다
  - L7 주의할 점(이미 공유한 커밋)은 0·1단계에서 본 리모트 개념으로 설명하고, 올려 보내기 (Push)는 8단계에서 설명한다 — 문장은 L7 설계에서 확인한다
  - `origin`·리모트 트래킹 브랜치: 8단계에서 처음 설명한다. 1~7단계 도식에서는 리모트 트래킹 브랜치를 숨긴다([diagram-model.md](diagram-model.md) 4절 Clone 행)
- "Unstaged"는 원고 절 제목 속 상태 표현이라 용어로 추가하지 않는다. 화면에서는 "커밋 준비 전 변경"으로 풀어 쓰는 것을 기본으로 하고, 문장은 L4 설계에서 다시 확인한다.
- "완료한 커밋 수정"은 원고 본문의 동작 설명(`undoing.asc` 되돌리기)이며 이름 붙은 용어가 아니라 용어집에 넣지 않는다.

### 경계 (다른 문서와 겹치지 않는 지점)

- 이 문서가 **단계별 범위와 단계 이름**의 유일한 소스다. [map.md](map.md) "처리" 칸과 [README](../../README.md) 커리큘럼 표는 이 표의 요약이다.
- 용어 정의, 한글 표현 값, "처음" 단계 값은 [glossary.md](glossary.md)가 유일한 소스다. 아래 표기 표는 이 설계에서 정한 값을 기록한 것이며, 바뀌면 용어집을 먼저 고친다.
- 단계 안의 장면 구성·화면 문장은 각 레슨 설계(`L0`~`L10`)가 정한다. 도식의 공간·영역·노출은 [diagram-model.md](diagram-model.md)가 정한다.

## 정책 상세

### 범위 밖 (다루지 않는 것)

- Reset, revert(원고 7장) — 4단계 되돌리기는 원고 2장 "되돌리기" 범위만 다룬다
- 대화형 Rebase, 서브모듈 등 원고 7장의 나머지 고급 도구
- Git 서버 설치·운영(원고 4장), GitHub 계정 설정·관리(원고 6장의 Fork·Pull Request·GitHub 플로우 외 부분)

### 용어 표기 (R8)

원고 표기가 영문인 용어는 화면에 **"한글 표현 (원고 표기)"**로 쓴다. 대상·빈도 규칙은 [glossary.md](glossary.md) 표기 원칙, 결정은 [`project-memory/decisions/term-notation.md`](../../project-memory/decisions/term-notation.md).

| 원고 표기 | 화면 표기 | 처음 | 용어집 |
|---|---|---|---|
| Staging Area | 커밋 준비 영역 (Staging Area) | 2 | 기존 |
| Modified / Staged / Committed | 수정됨 (Modified) / 커밋 준비됨 (Staged) / 커밋됨 (Committed) | 2 | 기존 |
| Stage | 커밋 준비 영역에 올리기 (Stage) | 2 | 기존 |
| Commit | 커밋하기 (Commit) — 명사 "커밋"은 원고 한글 표기 그대로 | 3 | 기존 |
| HEAD | 지금 위치 표시 (HEAD) | 5 | 기존 |
| Checkout | 0단계: 중앙 서버에서 받아 오기 (Checkout) · 1단계부터: 브랜치 이동 (Checkout) | 0 | 기존 |
| Clone | 저장소 복제 (Clone) | 0 | 기존 |
| Merge | 병합 (Merge) | 6 | 기존 |
| Push / Fetch / Pull | 올려 보내기 (Push) / 가져오기 (Fetch) / 가져와 합치기 (Pull) | 8 | 기존 |
| Unstage | 준비 취소 (Unstage) | 4 | 추가 |
| Fast-forward | 빨리 감기 (Fast-forward) | 6 | 추가 (별칭 Fast forward) |
| 3-way Merge | 3방향 병합 (3-way Merge) | 6 | 추가 |
| Rebase | 커밋 다시 쌓기 (Rebase) | 7 | 추가 |
| Fork | 내 계정으로 저장소 복사 (Fork) | 9 | 추가 |
| Pull Request | 병합 요청 (Pull Request) | 9 | 추가 |
| Stash | 하던 작업 임시 저장 (Stash) | 10 | 추가 |
| Cherry-Pick | 다른 브랜치의 커밋 가져오기 (Cherry-Pick) | 10 | 추가 (별칭 Cherry-pick) |
| 충돌 · 브랜치 워크플로 · GitHub 플로우 · 태그 · 파일 무시하기 | 원고 표기 그대로 (원고가 한글·음차로 적은 용어라 R8 대상 아님) | 6 · 9 · 9 · 10 · 10 | 추가 |

- 기존 용어의 "처음" 값은 이 범위로 다시 확인했고 바뀐 것이 없다.
- 원고가 한글로 적은 용어는 D5대로 처음 나올 때 영문을 함께 적는다(예: 워킹 트리(working tree)).

## 실패 처리

해당 없음 — 실행되는 코드가 아니라 범위·표기 설계다.

## 재시도·종료

해당 없음. 범위를 바꾸려면 사용자와 의논한 뒤(R3) 이 문서를 고치고 역전파 체크리스트([checklist.md](../plan/checklist.md))를 따른다.

## 결정 근거

모두 사용자 결정이다(2026-10-19, 대화 원문). 질문 번호는 이 설계 세션 안의 번호다(open-questions의 ID와 별개).

| # | 결정 | 사용자 원문 |
|---|---|---|
| Q1 (A3) | Clone은 1단계에 둔다. 1단계는 "리모트 저장소의 히스토리 전체를 로컬로 복제"까지, `origin`과 리모트 트래킹 브랜치는 8단계에서 처음 설명한다. 근거: 원고에서 Clone은 새로 만들기와 같은 절("Git 저장소 만들기")에 있다 | "그렇게 해줘" (추천안: "A안. 1단계에서는 '리모트 저장소의 히스토리 전체를 로컬로 복제한다'는 데까지만 보여 주고, `origin`이라는 이름과 리모트 트래킹 브랜치는 8단계에서 처음 설명합니다") |
| Q3 | 4단계 되돌리기는 원고 2장 "되돌리기" 범위(완료한 커밋 수정, Unstage, Modified 파일 되돌리기). Reset·revert는 원고 7장 내용이라 다루지 않는다 | "Q3 : (a)" |
| Q5 → R8 | 원고 표기가 영문인 용어는 "한글 표현 (원고 표기)"로 쓴다 | "전체적으로 지금과 같은 한글 표기 옆에 원고 표기를 다른 브랜치의 커밋 가져오기 (cherry-pick) 형태로 해줘. … 이거 지침으로도 해줘" (전문은 결정 문서) |
| Q6 | R8 대상은 원고가 영문인 용어만, 빈도는 제목·라벨·용어 카드 항상, 본문은 장면마다 처음 한 번 | "모두 추천 안으로 해줘" |
| Q7 | 6단계 "병합 (Merge)", 7단계 "커밋 다시 쌓기 (Rebase)" (앞선 답 Q2 "Merge/Rebase로 변경"을 R8 형식으로 대체) | 같은 답 |
| Q4 | 위 표기 표의 한글 표현과 "처음" 값. Checkout만 단계별 예외 | "Checkout 은 0단계 만 예외로 CVCS 기준으로 표기하고, 그 이후부터는 Git 기준으로 해줘", "나머지는 동의" |
| Q8 | 1~7단계 도식에서 리모트 트래킹 브랜치를 숨기고 8단계부터 표시한다 | "(a) 로 해줘" |

- 단계 범위는 원고(Pro Git 한국어판) 장·절에 근거를 둔다. 원고에 없는 개념은 넣지 않는다 — 이 기준으로 4단계 "커밋 되돌리기"를 원고 2장 범위로 바꾸었다.
- 범위를 다시 판단할 때의 비교 기준: 입문자가 원고 2·3장(기초·브랜치)을 따라갈 수 있는가, 앞 단계에서 배우지 않은 개념에 기대지 않는가.

## 실측 근거 / preflight

- 2026-10-19 — 위 "원고 근거" 칸의 파일과 절 제목, 추가 용어 13개의 표기를 원고 고정 커밋 `f50647d`의 한국어 본문에서 확인했다. 원고 안 다른 표기: "Fast forward"(`basic-branching-and-merging.asc` 브랜치의 기초), "Cherry-pick"(`maintaining.asc` 같은 절 본문·그림 설명) → 용어집 별칭.
- 미검증으로 남긴 것: 없음. 이 설계는 외부 시스템 동작에 기대지 않는다.
- 남은 미결: Fork 장면의 서버 쪽 저장소 개수 → [open-questions A6](../plan/open-questions.md#a6-fork-장면의-서버-쪽-저장소-개수) (L9 설계).
