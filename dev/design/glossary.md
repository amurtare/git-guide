# 용어집

이 사이트의 모든 레슨·도식 라벨·설명은 이 용어집 하나를 따른다 (R6).
용어집에 없는 용어가 필요하면 레슨 설계 단계에서 먼저 여기에 추가한다.
단계별로 어떤 용어를 다루는지는 [curriculum-scope-design.md](curriculum-scope-design.md)가 정한다.

## 근거와 표기 원칙

- **근거 원고**: Pro Git 한국어판 — <https://github.com/progit/progit2-ko> 커밋 `f50647da032bf210ef91802290d60d05da1a9416` (2025-03-05)
  - 출처 칸은 이 커밋 기준 `book/<장>/sections/<파일>.asc`와 절 제목이다
  - 원고를 갱신하려면 새 커밋으로 모든 출처를 다시 대조한 뒤 이 줄을 바꾼다
- **D5 표기**: 원고 표기를 그대로 쓴다. 맞춤법과 달라도 원고가 우선이고("디렉토리"), 원고가 영문으로 둔 용어는 영문 그대로 쓴다("Staging Area", "Push"). 처음 나올 때 영문 원어를 함께 적는다.
  원고가 영문으로 둔 용어를 화면에 어떻게 내는지는 아래 R8이 정한다. 원고가 한글·음차로 적은 용어(워킹 트리 등)는 이 D5 그대로다.
- **R8 한글 표현 병기** (2026-10-19 사용자 지시, `project-memory/decisions/term-notation.md`): 원고 표기가 영문인 용어는 화면에 **"한글 표현 (원고 표기)"**로 쓴다. 예: 다른 브랜치의 커밋 가져오기 (Cherry-Pick). 한글 표현으로 맥락을 잡고, 괄호 안 공식 용어로 원어도 익히게 한다.
  - 대상: "한글 표현" 칸에 값이 있는 용어(원고 표기가 영문인 용어)만. 원고가 한글·음차로 적은 용어는 칸을 비우고 원고 표기 그대로 쓴다
  - 빈도: 단계 이름·목차·장면 제목·도식 라벨·용어 카드는 **항상** 병기. 본문 설명문은 **장면마다 처음 한 번** 병기하고, 그 장면 안에서는 한글 표현만 쓴다
    (2026-10-27 보충: 레슨 화면에서 "용어 카드"는 용어 정의 툴팁이고, 도식 요소에 붙는 설명 툴팁(`notes`)도 "항상" 쪽이다 — [diagram-component-design.md](diagram-component-design.md) 결정 14·15)
  - 괄호 안은 원고 **주 표기**(D6)다. 한글 표현은 용어를 **대신하지 않는다** — 공식 용어는 항상 화면에 남는다(R6)
  - 한 용어의 뜻이 단계에 따라 다르면 "한글 표현" 칸에 단계 조건을 적는다(예: Checkout은 0단계만 CVCS 기준, 1단계부터 Git 기준)
- **D6 이표기**: 원고 안에 표기가 둘 이상이면 주 표기 하나를 정하고 나머지는 별칭으로 적는다. 화면에는 주 표기를 쓰고, 별칭은 처음 소개할 때 "같은 것"이라고 한 번 알려 준다.
- **D8 명령어**: 용어만 쓴다. 명령어 형태는 쓰지 않는다. 이 용어집의 정의에도 명령어를 쓰지 않는다.
- **비유**: 설명을 돕는 데만 쓰고, 용어를 대신하지 않는다.
- **처음 나오는 단계**: 그 용어가 처음 화면에 나오는 단계 번호 하나다. [curriculum-scope-design.md](curriculum-scope-design.md)(2026-10-19 확정) 기준이며, 본격 설명 단계가 다르면 그 문서의 범위 표에 적는다(예: Clone은 0단계에 처음 나오고 1단계에서 설명). 정의 문장이 뒤 단계 용어(예: DVCS 정의의 스냅샷)를 쓰는 경우가 있는데, 화면에서는 그 단계에서 아직 배우지 않은 용어를 쓰지 않도록 레슨 설계에서 문장을 조정한다(Checkout을 다른 문맥에서 쓰는 문장도 같다).

## 버전 관리 방식 (0단계)

| 용어 | 한글 표현 (R8) | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|---|
| 버전 관리 시스템(VCS) | | | Version Control System | 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템 | 0 | `01-introduction/sections/about-version-control.asc` 버전 관리란? |
| 로컬 버전 관리 | | 로컬 VCS | Local Version Control System | 내 컴퓨터 안의 간단한 데이터베이스에 파일의 변경 정보를 기록해 관리하는 방식 | 0 | 같은 파일 · 로컬 버전 관리 |
| 로컬 데이터베이스 | | | local database | 로컬 VCS에서 파일의 변경 정보를 저장하는, 내 컴퓨터 안의 데이터베이스 | 0 | 같은 파일 · 로컬 버전 관리, 중앙집중식 버전 관리(CVCS) |
| 중앙집중식 버전 관리(CVCS) | | 중앙집중식 VCS | Centralized Version Control System | 파일을 관리하는 서버를 따로 두고, 클라이언트가 그 중앙 서버에서 파일을 받아 쓰는 방식. 중앙 서버가 다운되면 그동안 아무도 협업하거나 작업을 백업할 수 없다 | 0 | 같은 파일 · 중앙집중식 버전 관리(CVCS) |
| 중앙 서버 | | | central server | CVCS에서 모든 파일과 버전 정보를 가진 서버. 클라이언트는 여기서 파일을 받아(Checkout) 쓴다 | 0 | 같은 파일 · 중앙집중식 버전 관리(CVCS) |
| 중앙 데이터베이스 | | | central database | CVCS에서 프로젝트의 모든 히스토리를 담는, 중앙 서버의 데이터베이스. 이것이 망가지면 히스토리를 모두 잃는다 | 0 | 같은 파일 · 중앙집중식 버전 관리(CVCS) |
| 분산 버전 관리 시스템(DVCS) | | | Distributed Version Control System | 클라이언트가 파일의 마지막 스냅샷만 받는 것이 아니라 저장소를 히스토리와 함께 전부 복제하는 방식. Git이 여기에 속한다 | 0 | 같은 파일 · 분산 버전 관리 시스템 |

## 공간과 영역

| 용어 | 한글 표현 (R8) | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|---|
| 저장소 | | Git 저장소 | repository | 프로젝트의 파일과 그 히스토리 전체를 담는 곳 | 0 | `01-introduction/sections/about-version-control.asc` 분산 버전 관리 시스템, `02-git-basics/sections/getting-a-repository.asc` Git 저장소 만들기 |
| 리모트 저장소 | | 원격 저장소 | remote repository | 인터넷이나 네트워크 어딘가에 있는 저장소. 다른 사람과 함께 일하려면 리모트 저장소에 데이터를 Push 하고 Pull 한다 | 0 | `02-git-basics/sections/remotes.asc` 리모트 저장소 (별칭도 같은 절, 원고 전체 8회) |
| `origin` | | | origin | Clone 할 때 원래 저장소에 자동으로 붙는 리모트 저장소 이름 | 8 | `02-git-basics/sections/remotes.asc` 리모트 저장소를 Pull 하거나 Fetch 하기 |
| 워킹 트리 | | 워킹 디렉토리 | working tree (working directory) | 프로젝트의 특정 버전을 Checkout 한 것. Git 디렉토리 안의 데이터베이스에서 파일을 꺼내 만든, 실제로 파일을 고치는 곳 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 (별칭: `02-git-basics/sections/recording-changes.asc` 수정하고 저장소에 저장하기) |
| Staging Area | 커밋 준비 영역 | Index | staging area (index) | 곧 커밋할 파일에 대한 정보를 저장하는 곳. Git 디렉토리 안에 있는 단순한 파일이다. 기술 용어로는 Index라고 한다 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 |
| Git 디렉토리 | | | Git directory | Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳. Git의 핵심이며, 저장소를 새로 만들거나 Clone 할 때 만들어진다 | 1 | `01-introduction/sections/basics.asc` 세 가지 상태, `02-git-basics/sections/getting-a-repository.asc` Git 저장소 만들기 |

## 파일 상태와 기록

| 용어 | 한글 표현 (R8) | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|---|
| Modified | 수정됨 | | modified | 워킹 트리의 파일을 수정했지만 아직 Staging Area에 올리지 않은 상태 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 |
| Staged | 커밋 준비됨 | | staged | 수정한 파일을 Staging Area에 올려, 다음에 저장할 스냅샷에 넣겠다고 표시한 상태 | 2 | 같은 절 |
| Committed | 커밋됨 | | committed | 파일이 Git 디렉토리에 안전하게 저장된 상태 | 2 | 같은 절 |
| 스냅샷 | | | snapshot | 어느 순간 프로젝트 파일 전체가 어떤 모습이었는지를 그대로 담은 것. Git은 데이터를 스냅샷의 연속으로 취급한다 | 3 | `01-introduction/sections/basics.asc` 차이가 아니라 스냅샷 |
| 커밋 히스토리 | | 히스토리 | commit history | 저장소에 쌓인 커밋들의 기록. 도식에서는 커밋 노드와 부모 방향 화살표로 그린다 | 3 | `02-git-basics/sections/viewing-history.asc` 커밋 히스토리 조회하기 |
| 커밋 | | | commit | 프로젝트의 상태를 스냅샷으로 Git 디렉토리에 영구히 저장한 것, 또는 그렇게 저장하는 일 | 3 | `01-introduction/sections/basics.asc` 세 가지 상태, 차이가 아니라 스냅샷 |

## 브랜치와 포인터

| 용어 | 한글 표현 (R8) | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|---|
| 브랜치 | | | branch | 커밋 사이를 가볍게 이동할 수 있는 포인터. 새 커밋을 만들면 지금 브랜치가 그 커밋을 가리키도록 자동으로 움직인다 | 5 | `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가 |
| `main` | | (`master`) | main | 이 사이트가 예시로 쓰는 기본 브랜치 이름. **D7**: Pro Git 원고는 기본 브랜치를 `master`로 쓴다. 브랜치를 처음 소개할 때 "`master`는 예전 기본 이름이자 Pro Git이 쓰는 이름이며 의미는 같다"고 한 번만 언급한다 | 5 | 원고 표기는 `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가 (`master`) |
| HEAD | 지금 위치 표시 | | HEAD | 지금 작업하는 로컬 브랜치를 가리키는 특수한 포인터 | 5 | `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가 |
| 리모트 브랜치 | | | remote branch | 리모트 저장소에 있는 브랜치 | 8 | `03-git-branching/sections/remote-branches.asc` 리모트 브랜치 |
| 리모트 트래킹 브랜치 | | | remote-tracking branch | 리모트 브랜치를 추적하는 레퍼런스이자 브랜치. 로컬에 있지만 마음대로 움직일 수 없고, 리모트 저장소에 마지막으로 연결했던 순간에 그 브랜치가 어느 커밋을 가리켰는지를 나타낸다. 예: `origin/main` | 8 | `03-git-branching/sections/remote-branches.asc` 리모트 브랜치 |

## 작업 이름 (도식의 전이 — 화면에서는 나레이션 제목에 쓴다, 2026-10-27)

학습자가 실행하는 명령이 아니라, 도식에서 무엇이 어디로 움직이는지를 가리키는 **용어**다 (R5·D8).

| 용어 | 한글 표현 (R8) | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|---|
| Stage | 커밋 준비 영역에 올리기 | | stage | 워킹 트리에서 수정한 파일을 Staging Area에 올려 커밋할 스냅샷을 만드는 일 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 |
| Commit | 커밋하기 | | commit | Staging Area에 있는 파일을 Git 디렉토리에 영구적인 스냅샷으로 저장하는 일 | 3 | 같은 절 |
| Checkout | 0단계: 중앙 서버에서 받아 오기 · 1단계부터: 브랜치 이동 | | checkout | 저장소에서 특정 버전을 꺼내 워킹 트리에 펼치는 일. CVCS에서는 중앙 서버에서 파일을 받아 쓰는 일을, Git에서는 브랜치를 옮겨 HEAD가 그 브랜치를 가리키게 하는 일을 말한다 | 0 | `01-introduction/sections/about-version-control.asc` 중앙집중식 버전 관리(CVCS), `03-git-branching/sections/nutshell.asc` 브랜치 이동하기 |
| Clone | 저장소 복제 | | clone | 다른 곳의 Git 저장소를 히스토리째 통째로 복사해 오는 일. (8단계 보충) Clone 하면 원래 저장소가 `origin`이라는 이름의 리모트 저장소로 등록된다 — 1~7단계 화면에서는 이 문장을 쓰지 않는다 | 0 | `02-git-basics/sections/getting-a-repository.asc` 기존 저장소를 Clone 하기, `02-git-basics/sections/remotes.asc` 리모트 저장소 |
| Push | 올려 보내기 | | push | 로컬의 브랜치 내용을 리모트 저장소에 올려 공유하는 일. 다른 사람이 먼저 Push 했다면 그대로는 Push 할 수 없다 | 8 | `02-git-basics/sections/remotes.asc` 리모트 저장소에 Push 하기 |
| Fetch | 가져오기 | | fetch | 리모트 저장소에는 있지만 로컬에는 없는 데이터를 모두 가져오는 일. 가져오기만 하고 자동으로 Merge 하지 않는다 | 8 | `02-git-basics/sections/remotes.asc` 리모트 저장소를 Pull 하거나 Fetch 하기 |
| Merge | 병합 | | merge | 두 브랜치의 작업을 하나로 합치는 일 | 6 | `03-git-branching/sections/basic-branching-and-merging.asc` 브랜치와 Merge 의 기초 |
| Pull | 가져와 합치기 | | pull | 리모트 저장소에서 데이터를 내려받아(Fetch) 연결된 리모트 브랜치와 자동으로 Merge 하는 일. 즉 Pull = Fetch + Merge | 8 | `03-git-branching/sections/remote-branches.asc` 브랜치 추적, Pull 하기 |
| Unstage | 준비 취소 | | unstage | Staging Area에 올린 파일을 다시 꺼내 Stage 하기 전 상태로 되돌리는 일 | 4 | `02-git-basics/sections/undoing.asc` 파일 상태를 Unstage로 변경하기 |
| Fast-forward | 빨리 감기 | Fast forward | fast-forward | Merge 할 브랜치가 지금 브랜치 이후의 커밋을 가리키고 있어, 새 커밋을 만들지 않고 지금 브랜치 포인터를 그 커밋으로 옮기기만 하는 Merge 방식 | 6 | `03-git-branching/sections/basic-branching-and-merging.asc` 브랜치의 기초(별칭 "Fast forward"), Merge 의 기초 |
| 3-way Merge | 3방향 병합 | | three-way merge | 두 브랜치가 가리키는 커밋 두 개와 공통 조상 하나를 사용해 합치고, 그 결과를 부모가 여러 개인 새 커밋(Merge 커밋)으로 만드는 Merge 방식 | 6 | 같은 파일 · Merge 의 기초 |
| Rebase | 커밋 다시 쌓기 | | rebase | 한 브랜치에서 변경된 사항을 다른 브랜치 위에 다시 적용해, 히스토리를 한 줄로 만드는 방식. 이미 공개 저장소에 Push 한 커밋은 Rebase 하지 않는다 | 7 | `03-git-branching/sections/rebasing.asc` Rebase 하기, Rebase 의 위험성 |
| Fork | 내 계정으로 저장소 복사 | | fork | Push 할 권한이 없는 프로젝트를 GitHub이 통째로 복사해 내 계정(네임스페이스)에 만들어 주는 일. 복사본에는 Push 할 수 있다 | 9 | `06-github/sections/2-contributing.asc` 프로젝트 Fork 하기 |
| Pull Request | 병합 요청 | | pull request | 내 브랜치의 변경을 원래 프로젝트에 Merge 해 달라고 요청하고, 그 위에서 코드 리뷰와 토론을 하는 GitHub의 기능 | 9 | 같은 파일 · GitHub 플로우 |
| Stash | 하던 작업 임시 저장 | | stash | 아직 커밋하지 않은 수정 사항(워킹 트리에서 수정한 파일과 Staging Area의 파일)을 잠시 보관했다가 나중에 다시 적용하는 일 | 10 | `07-git-tools/sections/stashing-cleaning.asc` 하던 일을 Stash 하기 |
| Cherry-Pick | 다른 브랜치의 커밋 가져오기 | Cherry-pick | cherry-pick | 다른 브랜치에 있는 커밋 하나만 골라 그 변경을 지금 브랜치에 적용하는 일. 커밋 하나만 Rebase 하는 것과 같다 | 10 | `05-distributed-git/sections/maintaining.asc` Rebase와 Cherry-Pick 워크플로(별칭 "Cherry-pick"은 같은 절 본문·그림 설명) |

## 협업과 도구

| 용어 | 한글 표현 (R8) | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|---|
| 충돌 | | | conflict | 두 브랜치에서 같은 파일의 같은 부분을 수정해, Git이 자동으로 합치지 못하는 상태. 사람이 직접 고쳐야 한다 | 6 | `03-git-branching/sections/basic-branching-and-merging.asc` 충돌의 기초 |
| 브랜치 워크플로 | | | branching workflows | 브랜치를 만들고 Merge 하는 일을 개발 과정에 어떻게 쓰는지에 대한 방식들 | 9 | `03-git-branching/sections/workflows.asc` 브랜치 워크플로 |
| GitHub 플로우 | | | GitHub flow | GitHub에서 Fork 하고 토픽 브랜치에서 작업한 뒤 Pull Request로 기여하는, Pull Request 중심의 협업 방식 | 9 | `06-github/sections/2-contributing.asc` GitHub 플로우 |
| 태그 | | | tag | 히스토리의 특정 커밋에 붙이는 이름. 보통 릴리즈할 때 쓴다(예: v1.0) | 10 | `02-git-basics/sections/tagging.asc` 태그 |
| 파일 무시하기 | | | ignoring files | Git이 관리할 필요가 없는 파일(로그 파일, 자동 생성 파일 등)을 무시할 파일로 지정하는 일 | 10 | `02-git-basics/sections/recording-changes.asc` 파일 무시하기 |
