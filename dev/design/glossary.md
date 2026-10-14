# 용어집

이 사이트의 모든 레슨·도식 라벨·설명은 이 용어집 하나를 따른다 (R6).
용어집에 없는 용어가 필요하면 레슨 플랜 단계에서 먼저 여기에 추가한다.

## 근거와 표기 원칙

- **근거 원고**: Pro Git 한국어판 — <https://github.com/progit/progit2-ko> 커밋 `f50647da032bf210ef91802290d60d05da1a9416` (2025-03-05)
  - 출처 칸은 이 커밋 기준 `book/<장>/sections/<파일>.asc`와 절 제목이다
  - 원고를 갱신하려면 새 커밋으로 모든 출처를 다시 대조한 뒤 이 줄을 바꾼다
- **D5 표기**: 원고 표기를 그대로 쓴다. 맞춤법과 달라도 원고가 우선이고("디렉토리"), 원고가 영문으로 둔 용어는 영문 그대로 쓴다("Staging Area", "Push"). 처음 나올 때 영문 원어를 함께 적는다.
- **D6 이표기**: 원고 안에 표기가 둘 이상이면 주 표기 하나를 정하고 나머지는 별칭으로 적는다. 화면에는 주 표기를 쓰고, 별칭은 처음 소개할 때 "같은 것"이라고 한 번 알려 준다.
- **D8 명령어**: 용어만 쓴다. 명령어 형태는 쓰지 않는다. 이 용어집의 정의에도 명령어를 쓰지 않는다.
- **비유**: 설명을 돕는 데만 쓰고, 용어를 대신하지 않는다.
- **처음 나오는 단계**: 현재 README 커리큘럼 표 기준 **잠정값**이다. 정의 문장이 뒤 단계 용어(예: DVCS 정의의 스냅샷)를 쓰는 경우가 있는데, 화면에서는 그 단계에서 아직 배우지 않은 용어를 쓰지 않도록 레슨 플랜에서 문장을 조정한다. "커리큘럼 단계별 범위 확정" 항목과 open-questions A3·A4가 해소되면 다시 확인한다.

## 버전 관리 방식 (0단계)

| 용어 | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|
| 버전 관리 시스템(VCS) | | Version Control System | 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템 | 0 | `01-introduction/sections/about-version-control.asc` 버전 관리란? |
| 로컬 버전 관리 | 로컬 VCS | Local Version Control System | 내 컴퓨터 안의 간단한 데이터베이스에 파일의 변경 정보를 기록해 관리하는 방식 | 0 | 같은 파일 · 로컬 버전 관리 |
| 로컬 데이터베이스 | | local database | 로컬 VCS에서 파일의 변경 정보를 저장하는, 내 컴퓨터 안의 데이터베이스 | 0 | 같은 파일 · 로컬 버전 관리, 중앙집중식 버전 관리(CVCS) |
| 중앙집중식 버전 관리(CVCS) | 중앙집중식 VCS | Centralized Version Control System | 파일을 관리하는 서버를 따로 두고, 클라이언트가 그 중앙 서버에서 파일을 받아 쓰는 방식. 중앙 서버가 다운되면 그동안 아무도 협업하거나 작업을 백업할 수 없다 | 0 | 같은 파일 · 중앙집중식 버전 관리(CVCS) |
| 중앙 서버 | | central server | CVCS에서 모든 파일과 버전 정보를 가진 서버. 클라이언트는 여기서 파일을 받아(Checkout) 쓴다 | 0 | 같은 파일 · 중앙집중식 버전 관리(CVCS) |
| 중앙 데이터베이스 | | central database | CVCS에서 프로젝트의 모든 히스토리를 담는, 중앙 서버의 데이터베이스. 이것이 망가지면 히스토리를 모두 잃는다 | 0 | 같은 파일 · 중앙집중식 버전 관리(CVCS) |
| 분산 버전 관리 시스템(DVCS) | | Distributed Version Control System | 클라이언트가 파일의 마지막 스냅샷만 받는 것이 아니라 저장소를 히스토리와 함께 전부 복제하는 방식. Git이 여기에 속한다 | 0 | 같은 파일 · 분산 버전 관리 시스템 |

## 공간과 영역

| 용어 | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|
| 저장소 | Git 저장소 | repository | 프로젝트의 파일과 그 히스토리 전체를 담는 곳 | 0 | `01-introduction/sections/about-version-control.asc` 분산 버전 관리 시스템, `02-git-basics/sections/getting-a-repository.asc` Git 저장소 만들기 |
| 리모트 저장소 | 원격 저장소 | remote repository | 인터넷이나 네트워크 어딘가에 있는 저장소. 다른 사람과 함께 일하려면 리모트 저장소에 데이터를 Push 하고 Pull 한다 | 0 | `02-git-basics/sections/remotes.asc` 리모트 저장소 (별칭도 같은 절, 원고 전체 8회) |
| `origin` | | origin | Clone 할 때 원래 저장소에 자동으로 붙는 리모트 저장소 이름 | 8 | `02-git-basics/sections/remotes.asc` 리모트 저장소를 Pull 하거나 Fetch 하기 |
| 워킹 트리 | 워킹 디렉토리 | working tree (working directory) | 프로젝트의 특정 버전을 Checkout 한 것. Git 디렉토리 안의 데이터베이스에서 파일을 꺼내 만든, 실제로 파일을 고치는 곳 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 (별칭: `02-git-basics/sections/recording-changes.asc` 수정하고 저장소에 저장하기) |
| Staging Area | Index | staging area (index) | 곧 커밋할 파일에 대한 정보를 저장하는 곳. Git 디렉토리 안에 있는 단순한 파일이다. 기술 용어로는 Index라고 한다 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 |
| Git 디렉토리 | | Git directory | Git이 프로젝트의 메타데이터와 객체 데이터베이스를 저장하는 곳. Git의 핵심이며, 저장소를 새로 만들거나 Clone 할 때 만들어진다 | 1 | `01-introduction/sections/basics.asc` 세 가지 상태, `02-git-basics/sections/getting-a-repository.asc` Git 저장소 만들기 |

## 파일 상태와 기록

| 용어 | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|
| Modified | | modified | 워킹 트리의 파일을 수정했지만 아직 Staging Area에 올리지 않은 상태 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 |
| Staged | | staged | 수정한 파일을 Staging Area에 올려, 다음에 저장할 스냅샷에 넣겠다고 표시한 상태 | 2 | 같은 절 |
| Committed | | committed | 파일이 Git 디렉토리에 안전하게 저장된 상태 | 2 | 같은 절 |
| 스냅샷 | | snapshot | 어느 순간 프로젝트 파일 전체가 어떤 모습이었는지를 그대로 담은 것. Git은 데이터를 스냅샷의 연속으로 취급한다 | 3 | `01-introduction/sections/basics.asc` 차이가 아니라 스냅샷 |
| 커밋 히스토리 | 히스토리 | commit history | 저장소에 쌓인 커밋들의 기록. 도식에서는 커밋 노드와 부모 방향 화살표로 그린다 | 3 | `02-git-basics/sections/viewing-history.asc` 커밋 히스토리 조회하기 |
| 커밋 | | commit | 프로젝트의 상태를 스냅샷으로 Git 디렉토리에 영구히 저장한 것, 또는 그렇게 저장하는 일 | 3 | `01-introduction/sections/basics.asc` 세 가지 상태, 차이가 아니라 스냅샷 |

## 브랜치와 포인터

| 용어 | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|
| 브랜치 | | branch | 커밋 사이를 가볍게 이동할 수 있는 포인터. 새 커밋을 만들면 지금 브랜치가 그 커밋을 가리키도록 자동으로 움직인다 | 5 | `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가 |
| `main` | (`master`) | main | 이 사이트가 예시로 쓰는 기본 브랜치 이름. **D7**: Pro Git 원고는 기본 브랜치를 `master`로 쓴다. 브랜치를 처음 소개할 때 "`master`는 예전 기본 이름이자 Pro Git이 쓰는 이름이며 의미는 같다"고 한 번만 언급한다 | 5 | 원고 표기는 `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가 (`master`) |
| HEAD | | HEAD | 지금 작업하는 로컬 브랜치를 가리키는 특수한 포인터 | 5 | `03-git-branching/sections/nutshell.asc` 브랜치란 무엇인가 |
| 리모트 브랜치 | | remote branch | 리모트 저장소에 있는 브랜치 | 8 | `03-git-branching/sections/remote-branches.asc` 리모트 브랜치 |
| 리모트 트래킹 브랜치 | | remote-tracking branch | 리모트 브랜치를 추적하는 레퍼런스이자 브랜치. 로컬에 있지만 마음대로 움직일 수 없고, 리모트 저장소에 마지막으로 연결했던 순간에 그 브랜치가 어느 커밋을 가리켰는지를 나타낸다. 예: `origin/main` | 8 | `03-git-branching/sections/remote-branches.asc` 리모트 브랜치 |

## 작업 이름 (도식의 전이 라벨)

학습자가 실행하는 명령이 아니라, 도식에서 무엇이 어디로 움직이는지를 가리키는 **용어**다 (R5·D8).

| 용어 | 별칭 | 영문 | 정의 | 처음 | 출처 |
|---|---|---|---|---|---|
| Stage | | stage | 워킹 트리에서 수정한 파일을 Staging Area에 올려 커밋할 스냅샷을 만드는 일 | 2 | `01-introduction/sections/basics.asc` 세 가지 상태 |
| Commit | | commit | Staging Area에 있는 파일을 Git 디렉토리에 영구적인 스냅샷으로 저장하는 일 | 3 | 같은 절 |
| Checkout | | checkout | 저장소에서 특정 버전을 꺼내 워킹 트리에 펼치는 일. CVCS에서는 중앙 서버에서 파일을 받아 쓰는 일을, Git에서는 브랜치를 옮겨 HEAD가 그 브랜치를 가리키게 하는 일을 말한다 | 0 | `01-introduction/sections/about-version-control.asc` 중앙집중식 버전 관리(CVCS), `03-git-branching/sections/nutshell.asc` 브랜치 이동하기 |
| Clone | | clone | 다른 곳의 Git 저장소를 히스토리째 통째로 복사해 오는 일. Clone 하면 원래 저장소가 `origin`이라는 이름의 리모트 저장소로 등록된다 | 0 | `02-git-basics/sections/getting-a-repository.asc` 기존 저장소를 Clone 하기, `02-git-basics/sections/remotes.asc` 리모트 저장소 |
| Push | | push | 로컬의 브랜치 내용을 리모트 저장소에 올려 공유하는 일. 다른 사람이 먼저 Push 했다면 그대로는 Push 할 수 없다 | 8 | `02-git-basics/sections/remotes.asc` 리모트 저장소에 Push 하기 |
| Fetch | | fetch | 리모트 저장소에는 있지만 로컬에는 없는 데이터를 모두 가져오는 일. 가져오기만 하고 자동으로 Merge 하지 않는다 | 8 | `02-git-basics/sections/remotes.asc` 리모트 저장소를 Pull 하거나 Fetch 하기 |
| Merge | | merge | 두 브랜치의 작업을 하나로 합치는 일 | 6 | `03-git-branching/sections/basic-branching-and-merging.asc` 브랜치와 Merge 의 기초 |
| Pull | | pull | 리모트 저장소에서 데이터를 내려받아(Fetch) 연결된 리모트 브랜치와 자동으로 Merge 하는 일. 즉 Pull = Fetch + Merge | 8 | `03-git-branching/sections/remote-branches.asc` 브랜치 추적, Pull 하기 |
