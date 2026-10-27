# 공용 도식 컴포넌트 상세 설계 (단위: U-diagram)

연결: [`dev/plan/checklist.md`](../plan/checklist.md) "`U-diagram` 공용 도식 컴포넌트 구현 구분". 대상: 공용 도식 모델([diagram-model.md](diagram-model.md))을 화면으로 구현할 **파일 구조**와 **설정 계약**(레슨이 공용 스크립트에 넘기는 데이터의 모양), `file://` 제약(R4), 화면 버전 표시(B1).
확정: 2026-10-27 (사용자 결정 1~5-c-2·14·15 · 사용자 위임 · 플랜 검수 Opus 5.5 4회차 GO · 문서 검수 반영).

> 이 문서는 **구현 계약**만 정한다. 공간·영역·요소·전이의 뜻은 [diagram-model.md](diagram-model.md), 용어 정의와 한글 표현은 [glossary.md](glossary.md), 단계 범위는 [curriculum-scope-design.md](curriculum-scope-design.md)가 소스다.
> 도식의 모양과 색 배정은 구현 Phase 1 시안에서 사용자 확인을 받는다(결정 11, [diagram-model.md](diagram-model.md) 3절).

## 역할과 인터페이스

### 파일 구조 (결정 1·1-b·2·3-b)

| 파일 | 역할 | 입력/출력 |
|---|---|---|
| `index.html` | 목차 + 푸터(현재 버전, 릴리즈 노트 링크) | 뼈대는 `site.js`의 `GitGuide.index()`가 만든다 |
| `lessons/NN-<꼬리표>.html` | 레슨 하나 | `<head>`의 CSS·서체 연결, 공용 스크립트 연결, 인라인 장면 데이터(`GitGuide.lesson({...})`)만 둔다 |
| `assets/css/site.css` | 토큰·타이포·레슨 화면 배치 | [visual-style 결정](../../project-memory/decisions/visual-style.md) |
| `assets/css/diagram.css` | 공간·영역·요소의 모양 | Phase 1 시안으로 확정 |
| `assets/js/version.js` | 화면 표시용 버전 사본 | 이름 공간 준비 줄 다음에 `window.GitGuide.version = "X.Y.Z";` 한 줄. `index.html`만 불러온다. 릴리즈 워크플로가 따옴표 안 값을 `VERSION`과 비교한다 |
| `assets/js/glossary.js` | 용어집 사본 | `GitGuide.glossary`(주 표기 → 한글 표현·별칭·영문·정의·처음·출처), `GitGuide.sceneNames`(나·동료·파일 — 용어집 항목이 아닌 장면 설명용 이름) |
| `assets/js/curriculum.js` | 단계 목록 사본 | `GitGuide.curriculum = [{ stage, title, file }]` — 목차·이전/다음·레슨 머리말에 쓴다. `title`은 용어 표식 허용 |
| `assets/js/diagram.js` | 도식 그리기 | `GitGuide.diagram.render(container, scene, ctx)` — 장면 상태 하나 → 도식, 이전 상태와 비교한 움직임 |
| `assets/js/site.js` | 화면 뼈대와 진행 | `GitGuide.lesson(config)`, `GitGuide.index()` — 뼈대 생성, 장면 이동, 나레이션·툴팁, R8 표기 |

레슨 파일 이름 11개(결정 2): `00-version-control`, `01-repository`, `02-three-areas`, `03-commit`, `04-undo`, `05-branch`, `06-merge`, `07-rebase`, `08-remote`, `09-collaboration`, `10-tools` (`.html`). 번호는 커리큘럼 단계 번호이고, 경로를 바꾸면 MAJOR다([docs/RELEASE_MANAGEMENT.md](../../docs/RELEASE_MANAGEMENT.md#버전-규칙)).

- 모든 스크립트는 일반 `<script src>`로 불러온다. `fetch`·XHR·ES 모듈은 `file://`에서 막힌다([실측](../evidence/2026-10-21-file-scheme.md)). 전역 이름은 `window.GitGuide` 하나다.
- 모든 `assets/js/` 파일은 첫 줄을 `window.GitGuide = window.GitGuide || {};`로 시작한다. 그래서 어느 파일이 먼저 불러와져도 이름 공간이 있다(목차는 `version.js`, 레슨은 `glossary.js`가 맨 앞).
- 불러오는 순서 — 레슨: `glossary.js` → `curriculum.js` → `diagram.js` → `site.js` → 인라인 데이터. 목차: `version.js` → `curriculum.js` → `glossary.js` → `site.js` → `GitGuide.index()`.
- 서체는 Google Fonts 링크와 대체 서체 스택을 함께 둔다(visual-style 결정). 스크립트가 꺼진 브라우저에는 `<noscript>` 안내 한 줄을 둔다.
- **레슨 화면 방향 (결정 14)**: 화면을 상자(프레임)로 나누지 않고 장면 하나를 화면 전체로 보여 주는 **슬라이드형**이다. **도식이 화면에서 가장 큰 비중**을 차지하고, 텍스트는 최소로 둔다.
  - 장면의 `title`·`body`는 짧은 **나레이션**으로 보여 준다(설명하는 사람이 있는 느낌). 텍스트 칸을 따로 더 두지 않는다(14 세부).
  - 더 필요한 설명은 **툴팁**으로 준다 — 용어 정의(요소·용어 표식을 누르면, D1)와 도식 요소에 붙는 짧은 설명(`notes`, 결정 15). 파일럿의 고정 용어 카드 칸은 두지 않는다(14 세부).
  - 전이 표시줄·장면 이동·나레이션·툴팁의 위치와 모양, 모바일 폭(약 375px) 배치는 구현 Phase 1 시안에서 사용자 확인을 받는다(14 세부, 결정 11과 같은 시점). [`dev/pilot/`](../pilot/README.md)의 상자형 공통 폼은 이 방향으로 대체된다.
  - **미결 → Phase 1 시안**: `notes` 툴팁을 띄우는 방식(처음부터 보임 / 누르면 보임 등), 같은 요소에 용어 정의와 `notes`가 함께 있을 때의 표시, 나레이션 안의 용어 표식을 눌러 정의를 보는 것이 D1("도식 요소를 누르면") 범위에 드는지, 그로 인해 D1 조작 목록이 바뀌는지. 정해지기 전까지 D1은 바뀌지 않는다([dev/impl/checklist.md](../impl/checklist.md) Phase 1).

### 설정 계약 (레슨 → 공용 스크립트)

```js
GitGuide.lesson({
  stage: 3,                 // 단계 번호 — 이전/다음, Checkout 한글 표현, 리모트 트래킹 브랜치 규칙에 쓴다
  scenes: [Scene, ...]
});

Scene = {
  title: "…[[Commit]]…",    // 용어 표식 허용 — R8 항상 병기
  body:  "…",               // 용어 표식 허용 — R8 용어마다 장면 안 처음 한 번 병기
  kind: "local" | "cvcs" | "dvcs",           // 장면 종류 → 영역 구성과 서버 라벨 (diagram-model 1·2절)
  transition: null | "Stage" | "Commit" | "Checkout" | "Clone" | "Push" | "Fetch" | "Merge" | "Pull"
            | "Unstage" | "Fast-forward" | "3-way Merge" | "Rebase"
            | "Fork" | "Pull Request" | "Stash" | "Cherry-Pick",   // 뒤 8개는 이름만 정함 (결정 9)
  from?: "me" | "peer",     // 공간을 넘는 전이의 로컬 쪽 공간. 기본 me, through에도 적용 (결정 13)
  through?: [{ transition, spaces }],        // 최종 상태 전에 차례로 재생할 중간 상태 (결정 6)
  notes?: [{ at: { space: "me" | "server" | "peer", area?: 영역 id, id?: 요소 id }, text }],
                            // 도식 자리에 붙는 짧은 설명 툴팁 (결정 15) — area만 쓰면 영역, id까지 쓰면 그 요소(커밋 id·파일 이름·라벨 이름). text는 용어 표식 허용
  spaces: { me: Space, server?: Space, peer?: Space }   // 키가 없는 공간은 숨김
}

Space = { show: "dim" | "active", areas: { [영역 id]: Area } }

Area = {
  show?: "hidden" | "dim" | "active",   // 기본 active (diagram-model 5절)
  files?:    [File],          // files · wt · sa
  versions?: [string],        // db — 로컬 데이터베이스 · 중앙 데이터베이스의 버전 목록
  history?:  History,         // gd · repo
  stash?:    [StashEntry],    // gd만 (결정 5-c-3) — 항목의 내부 필드는 L10 설계
  requests?: [PullRequest]    // repo만 (결정 5-c-5) — 항목의 내부 필드는 L9 설계
}

File = {
  name,
  state?: "Modified" | "Staged" | "Committed",
  version?: string,           // 파일의 버전 표시 — 정체성 키에 포함 (결정 10)
  conflict?: true,            // wt만 (결정 5-c-1) — 뜻·모양은 L6 설계
  ignored?:  true             // wt만 (결정 5-c-4) — 뜻·모양은 L10 설계
}

History = {
  commits:   [{ id, parents: [id, ...], lane: 0 }],   // 순서 = 가로 위치, lane = 줄 (결정 4)
  branches:  [{ name, at }],  // gd: 로컬 브랜치 / repo: 리모트 브랜치
  head?:     "main",          // gd만, 가리키는 브랜치 이름
  tracking?: [{ name, at }],  // gd만, 리모트 트래킹 브랜치
  tags?:     [{ name, at }]   // gd · repo (결정 5-c-2)
}
```

영역 id와 장면 종류의 대응 (diagram-model 2절):

| kind | 로컬 공간 (`me`·`peer`) | 서버 공간 (`server`) | 서버 라벨 |
|---|---|---|---|
| `local` | `files` 파일 · `db` 로컬 데이터베이스 | 없음 | — |
| `cvcs` | `files` 파일 (버전 정보 없음) | `db` 중앙 데이터베이스 | 중앙 서버 |
| `dvcs` | `wt` 워킹 트리 · `sa` Staging Area · `gd` Git 디렉토리 | `repo` 저장소 (커밋 히스토리) | 리모트 저장소 |

### 경계 (다른 단위와 겹치지 않는 지점)

| 파일 | 맡는 것 | 맡지 않는 것 |
|---|---|---|
| `diagram.js` | 장면 상태 → 도식, 이전 상태와 비교한 움직임(움직임 줄이기 설정이면 생략), 데스크톱/모바일 배치(D4) | 장면 이동, 설명 텍스트 |
| `site.js` | 뼈대, 장면 이동, 나레이션, 툴팁(용어 정의·`notes`), 제목·본문·라벨의 R8 표기, 목차·푸터, 데이터 검사 | 도식 그리기 |
| 레슨 HTML | 그 레슨의 장면 데이터 | 화면 구성 코드 |
| `glossary.js` · `curriculum.js` · `version.js` | 사본 값 | 로직 |

- 툴팁 연결: `diagram.js`는 그린 요소마다 용어 키(용어 정의용)와 `at` 키(공간·영역·요소 id, `notes`용)를 요소의 data 속성으로 남기고, `site.js`가 그 표식으로 툴팁을 건다. `render`의 `ctx`에는 이전 장면 상태와 `stage`를 넘긴다.
- 단계 안의 장면 구성과 문장은 각 레슨 설계(`L0`~`L10`)가 정한다. 이 문서는 그 장면을 적는 형식만 정한다.

## 정책 상세

### 요소 정체성과 움직임

- 같은 공간 안에서 같은 id(커밋 id, 라벨 이름)는 장면이 바뀌어도 같은 요소다. 위치가 바뀌면 움직이고, 새로 생기면 나타나고, 없어지면 사라진다. 전이의 움직임은 이 차이로 만들어진다.
- 파일 카드의 정체성 키는 **공간 + 파일 이름 + (있으면) 버전**이다(결정 10). 그래서 커밋 준비 영역에 올리기 (Stage)처럼 영역을 옮겨도 같은 카드가 움직인다. 같은 이름의 파일이 두 영역에 함께 있으면(Stage 뒤 다시 고친 경우) 버전으로 구분한다. 버전이 바뀌면(브랜치 이동 (Checkout)) 같은 자리에서 옛 카드가 사라지고 새 카드가 나타난다.
- 공간을 넘는 전이(Clone·Push·Fetch·Pull, CVCS 장면의 Checkout 등)에서는, 도착 공간에 새로 생긴 요소와 같은 id가 출발 공간에 있으면 그 자리에서 날아온다(결정 13). 출발·도착은 전이 이름으로 정하고([diagram-model.md](diagram-model.md) 4절 시작 → 도착), 로컬 쪽이 `me`·`peer` 중 어디인지는 장면의 `from`(기본 `me`)으로 정한다.
- `through`가 있으면 중간 상태를 차례로 그린 뒤 최종 상태를 그린다(결정 6). 예: 가져와 합치기 (Pull) = `through: [가져오기 (Fetch) 뒤 상태]` + 최종 병합 (Merge) 뒤 상태.
- `transition`은 전이 표시줄의 라벨과 경로 글자를 정한다. 경로 글자(시작 → 도착)는 diagram-model 4절 표를 공용 스크립트가 갖고 있고, Checkout은 `kind`에 따라 CVCS 경로(중앙 서버 → 로컬 파일 영역)와 Git 경로를 고른다.
- 로컬 공간은 `me`·`peer` 둘까지다(결정 12). [diagram-model.md](diagram-model.md) 1절(D3)은 "1개 이상"이지만 8절 배치(D4)가 둘까지만 정의하므로 계약도 둘이다.

### R8 표기 (결정 7)

레슨 텍스트(장면 제목·본문, `curriculum.js`의 단계 이름)에서 용어는 표식 `[[주 표기]]`로 적고, `site.js`가 용어집 사본으로 풀어 쓴다. 표식은 누르면 용어 정의 툴팁을 띄우는 버튼이 된다. `notes`의 `text`도 같은 표식을 쓴다.

| 자리 | 표기 |
|---|---|
| 장면 제목 · 도식 라벨 · 전이 표시줄 · 용어 정의 툴팁 · `notes` 툴팁 · 단계 이름 · 목차 | **항상** "한글 표현 (주 표기)" — 툴팁은 나레이션 없이 따로 읽힐 수 있으므로 라벨·용어 카드와 같이 다룬다 |
| 본문 | **용어마다** 그 장면 본문 안의 첫 표식만 "한글 표현 (주 표기)", 같은 장면의 이후 표식은 한글 표현만. 제목에 나온 것은 횟수에 넣지 않는다([glossary.md](glossary.md) 표기 원칙) |
| 한글 표현 칸이 빈 용어 | 주 표기 그대로 |
| 단계 조건이 있는 한글 표현(Checkout) | 레슨의 `stage`로 고른다 — 0단계 "중앙 서버에서 받아 오기", 1단계부터 "브랜치 이동" |

- [glossary.md](glossary.md) 표기 원칙의 "용어 카드"는 이 화면(결정 14)에서 용어 정의 툴팁을 말한다.
- D5의 "처음 나올 때 영문 병기"(예: 워킹 트리(working tree))는 자동으로 하지 않는다. 처음인지는 레슨 설계가 판단해 본문에 직접 적는다.
- 리모트 트래킹 브랜치는 1~7단계에서 숨긴다([diagram-model.md](diagram-model.md) 4절 Clone 행). 계약에서는 `stage < 8`인 레슨이 `tracking`을 쓰면 오류로 다룬다(아래 실패 처리). 0단계도 포함하는 것은 용어집에서 리모트 트래킹 브랜치의 "처음"이 8이기 때문이다.

### 확장 규칙 (결정 5·9)

- **요소**: diagram-model 3절에 없고 범위에 나오는 요소는 이번에 **이름과 자리만** 정했다(위 계약의 `conflict`·`ignored`·`stash`·`requests`·`tags`, Fork 복사본 저장소는 [A6](../plan/open-questions.md#a6-fork-장면의-서버-쪽-저장소-개수)). 뜻·모양·장면에서의 쓰임은 그 요소를 쓰는 레슨 설계가 정한다.
- **전이**: 범위에 나오고 용어집에 있는 전이 8개(Unstage·Fast-forward·3-way Merge·Rebase·Fork·Pull Request·Stash·Cherry-Pick)는 **이름만** 계약 값으로 정했다. 시작 → 도착과 바뀌는 요소는 각 레슨 설계에서 diagram-model 4절에 채운다. 병합 (Merge)·빨리 감기 (Fast-forward)·3방향 병합 (3-way Merge) 값의 구분과 Pull 마지막 단계 표시는 L6, Pull Request 전이와 요청 목록의 관계는 L9, Fork는 A6와 함께 L9.
- **더하는 순서**: 계약에 없는 요소·전이가 필요하면 그 레슨 설계에서 사용자와 의논해(R3) ① 용어집(용어가 없으면, [glossary.md](glossary.md) 머리말) ② diagram-model 3절·4절 ③ 이 문서의 계약 순서로 더한다. 장면을 계약 밖 값이나 `transition: null`로 우회하지 않는다. 용어집에 이름이 없는 동작(L4 수정됨 (Modified) 파일 되돌리기·완료한 커밋 수정, L9 서버에서 병합 요청 (Pull Request) 병합)이 이 경우다.
- 설계 완료 범위 A라서 이런 추가는 모두 구현 전에 일어난다.

### 버전 표시 (B1 — 결정 3·3-b)

- 푸터 버전은 `index.html`에만 보인다([update-delivery-download 결정](../../project-memory/decisions/update-delivery-download.md)). 값은 `assets/js/version.js` 한 곳에 둔다.
- 버전 소스는 여전히 `VERSION` 하나다. `version.js`는 화면 표시용 사본이고, 릴리즈 워크플로가 두 값을 비교해 다르면 태그·릴리즈 전에 실패한다. 비교 단계는 `version.js`를 처음 만드는 구현 커밋에서 함께 넣는다([dev/impl/checklist.md](../impl/checklist.md) Phase 1).
- 결정 문서: [`project-memory/decisions/version-display.md`](../../project-memory/decisions/version-display.md).

### 사본 일치 (결정 8)

- `glossary.js`는 [glossary.md](glossary.md)의, `curriculum.js`는 [curriculum-scope-design.md](curriculum-scope-design.md) 단계 이름의 사이트 쪽 사본이다. 소스를 고치면 사본도 고친다.
- 지금은 릴리즈 체크리스트 4번에서 사람이 대조한다. 자동 확인은 [C2](../plan/open-questions.md#c2-자동-확인-도구)의 확인 대상이다.

## 실패 처리

- `site.js`는 장면 데이터를 검사해 아래 경우를 **콘솔 오류 + 장면 번호**로 알리고, 그릴 수 있는 부분은 그린다(멈추지 않는다). 스모크 기준 "콘솔 에러 0"([dev/impl/README.md](../impl/README.md) 실행 환경)이 이를 잡는다.
  - 용어 표식이 용어집 사본에 없음
  - `kind`에 없는 영역 id, 계약 밖 키·값(요소·전이)
  - 앞에 정의되지 않은 부모 커밋
  - `stage < 8`인 레슨의 `tracking`
  - 자리 밖의 `conflict`·`ignored`·`stash`·`requests`(예: Staging Area의 `conflict`)
  - `notes`의 `at`이 그 장면에 없는 공간·영역·요소를 가리키거나, 둘 이상의 요소에 해당함(예: 같은 이름의 브랜치와 태그)
  - 같은 공간에 같은 파일 키가 둘
- 레슨 텍스트는 DOM API(`textContent`, 버튼 생성)로 넣고, 데이터를 `innerHTML`에 넣지 않는다([릴리즈 체크리스트](../../docs/UPDATE_CHECKLIST.md) 5번).

## 재시도·종료

- 해당 없음 — 네트워크·외부 호출이 없다.
- 계약을 바꾸려면 사용자와 의논한 뒤(R3) 이 문서를 고치고 역전파 체크리스트([checklist.md](../plan/checklist.md))를 따른다.

## 결정 근거

질문 번호는 이 설계 세션 안의 번호다(open-questions ID와 별개).

| # | 결정 | 사용자 원문 (2026-10-21~24) |
|---|---|---|
| 1 | 용어집 사본은 `assets/js/glossary.js` 하나, 장면 데이터는 각 레슨 HTML 안 | "(가)" |
| 1-b | 화면 뼈대는 공용 스크립트가 만든다 | "(가)" |
| 2 | 레슨 파일 이름은 번호 + 영문 꼬리표 (11개는 제시안 그대로 — 원문 확인은 "(가)"의 취지뿐) | "어자피 이후에 영문 이름만 바꾸는 경우보다는 레슨이 늘어나거나 줄어들 가능성이 높아서 연결 끊어지는 것은 어차피 대응해야 해. 그 때 혼란을 줄이기 위해서라도 (가) 가 좋겠어" |
| 2-b | 레슨 구성이 바뀌어 경로가 끊길 때의 대응은 처음 바뀔 때 정한다 → [B3](../plan/open-questions.md#b3-레슨-구성이-바뀔-때의-경로-대응) | "(가)" |
| 3 | 릴리즈 워크플로가 `VERSION`과 화면 버전 사본을 자동 비교 | "(가)" (앞서 "일치 시키면 되는 거 아니야? 왜 이 질문이 나온거야?"에 답하고 질문을 "누가 확인하나"로 줄임) |
| 3-b | 버전 사본은 별도 파일 `assets/js/version.js` | "(가)" |
| 4 | 커밋마다 부모와 줄(lane) 번호를 적고, 가로 위치는 목록 순서 | "나)" |
| 5 | 범위에 나오는 새 요소는 이름과 자리만 지금, 뜻·모양은 레슨 설계 | "(다)" (처음 "(나) -> 이거로 하지. 그런데 어차피 이후에 계속 수정할 거 같은데?" → 중간안 (다) 제시 → (나) 철회) |
| 5-b | 새 요소 후보 6개, Fork 저장소의 자리는 A6, 4단계 변경 내용 표시는 넣지 않음 | "진행해줘" |
| 5-c-1 | 충돌은 워킹 트리의 파일 카드에 붙는다. 히스토리 쪽 "병합 중단" 표시는 두지 않는다(멈춘 병합은 Merge 커밋이 없는 히스토리로 보인다 — 필요성은 L6 설계에서 확인) | "가" |
| 5-c-2 | 태그는 커밋 노드에 붙고 로컬·리모트 양쪽 히스토리에 놓일 수 있다 | "가" |
| 14 | 레슨 화면은 상자로 나누지 않는 슬라이드형, 도식이 가장 큰 비중, 텍스트는 최소, 화면 설명은 나레이션 컨셉, 필요한 설명은 툴팁 | 처음 제안 "화면 형태에서 서술형의 텍스트 설명이 필요한 케이스는 공용으로 사용할 수 있는 나레이션 패널을 추가해서 표현하는건 어떨까? 누군가 설명하는 사람이 있는 느낌이지" → 의도 설명 "현재 너무 프레임으로 나누어져 있는데, 사용자에게 화면을 전체적으로 쓰고 있는 느낌을 주고 싶은거야. PPT 같은 느낌이지. 그래서 화면 설명을 나레이션 처럼 컨셉을 잡았던 것이고", "도식이 화면 비중이 가능 크고, 텍스트는 최소한으로 줄이고 싶은 거야. 필요하다면 필요한 부분에 툴팁 형태로 제공하고" (2026-10-27) |
| 15 | 툴팁은 용어 정의에 더해 도식 요소에 붙는 짧은 설명(`notes`)도 담는다 | "(나)" (2026-10-27) |

**사용자 위임** — "이번 세션은 특별하게 다룰 결정사항은 없어서 니가 권장하는 방향으로 모두 진행해줘 질문 안해도 돼" (2026-10-24). 위임 범위는 이번 U-diagram 세션의 남은 결정이다. 아래는 이 위임 아래 에이전트가 정한 것이다.

| # | 결정 | 근거 |
|---|---|---|
| 5-c-3 | Stash는 로컬 Git 디렉토리 영역 안의 별도 목록 | Git 디렉토리는 Git이 데이터를 저장하는 곳(용어집 정의)이고, 영역 3개(D2)를 바꾸지 않는다 |
| 5-c-4 | 무시한 파일은 워킹 트리의 파일 카드에 붙는 표시 | Git이 관리하지 않는 파일은 워킹 트리에만 있다 |
| 5-c-5 | Pull Request는 리모트 저장소 영역 안의 요청 목록(보내는 브랜치 → 받는 브랜치) | 요청은 서버(GitHub) 쪽에 있다 |
| 6 | 이어지는 전이는 `through` 중간 상태로 | diagram-model 4절 "Pull = Fetch + Merge"를 그대로 표현 |
| 7 | R8 표기는 컴포넌트가 용어 표식으로 처리 | 표기 규칙을 레슨마다 손으로 지키지 않게 하고, 표식 누락은 콘솔 오류로 잡는다 |
| 8 | 사본 일치는 지금 릴리즈 체크리스트, 자동화는 C2 | 자동 확인 도구가 아직 정해지지 않았다 |
| 9 | 용어집에 있는 전이 8개는 이름만 지금 | 결정 5는 요소만 다뤘다 — 플랜 검수 1회차 지적으로 따로 정함 |
| 10 | 파일 카드에 `version`, 정체성 키에 포함 | diagram-model 4절 Checkout 행("파일 카드가 그 버전으로 바뀐다")을 그리기 위해. 플랜 검수 지적 |
| 11 | 도식 색 배정은 모양과 함께 Phase 1 시안에서 사용자 확인 | 이 항목은 구현 계약만 정한다. [visual-style](../../project-memory/decisions/visual-style.md)의 "U-diagram 설계에서 확정"을 대체 |
| 12 | 로컬 공간은 `me`·`peer` 둘 | D4 배치가 둘까지만 정의 |
| 13 | 공간을 넘는 움직임은 출발 공간의 같은 id에서, 로컬 쪽은 `from` | 같은 요소 판단이 공간 안으로만 정의돼 있었다 — 플랜 검수 지적 |
| 14 세부 | 나레이션은 `title`·`body`를 펼친 것(텍스트 칸 추가 없음), 고정 용어 카드 칸 제거(용어 정의는 툴팁), 구체 배치는 Phase 1 시안, `notes` 툴팁 표시 방식·D1 관계는 Phase 1 시안의 미결로 둠 | "텍스트 최소"와 "칸을 나누지 않는다"는 사용자 의도에 맞추고, 화면 배치는 결정 11과 같이 시안으로 확인 |
| 15 세부 | `notes`의 `at` 형식(공간 + 영역 또는 요소 id), 툴팁의 R8은 "항상 병기" | 툴팁은 나레이션 없이 따로 읽힐 수 있어 라벨·용어 카드 규칙을 따른다(glossary.md 표기 원칙의 "항상" 쪽) |
| — | 계약 세부: `curriculum.js` 신설, `kind` 값, 영역 id, 표시 기본값 active, 부분 그리기 실패 정책, 전역 이름 `GitGuide` | 위 결정을 구현 계약으로 옮기면서 정한 값 |

- 계약을 다시 판단할 때의 비교 기준: 11개 레슨이 같은 틀만으로 장면을 적을 수 있는가(R1), `file://`에서 그대로 동작하는가(R4), 장면이 바뀔 때 변한 것만 움직이는가.

## 실측 근거 / preflight

- 2026-10-21 — Chromium 141에서 `file://` 페이지의 `fetch`·XHR·ES 모듈은 막히고 일반 `<script src>`는 된다. 기록: [`dev/evidence/2026-10-21-file-scheme.md`](../evidence/2026-10-21-file-scheme.md).
- 2026-10-24 — 원고 고정 커밋 `f50647d`와 대조:
  - 충돌(`03-git-branching/sections/basic-branching-and-merging.asc` 충돌의 기초): 충돌하면 Merge가 멈추고 새 커밋이 생기지 않으며, 충돌한 파일은 unmerged로 표시된다. 개발자가 파일을 고친 뒤 Staging Area에 저장하면 해결된 것으로 표시된다 → 결정 5-c-1과 맞다.
  - 태그(`02-git-basics/sections/tagging.asc` 태그 붙이기·태그 공유하기): 태그는 브랜치와 달리 최신 커밋으로 움직이지 않고, Push가 자동으로 서버에 보내지 않아 따로 Push 해야 공유된다 → 결정 5-c-2와 맞다.
  - Stash(`07-git-tools/sections/stashing-cleaning.asc` Stashing과 Cleaning): 수정한 파일과 Staging Area의 파일을 "스택"에 보관했다가 다시 적용한다. 원고는 보관 장소를 Git 디렉토리라고 적지 않는다 → 결정 5-c-3의 근거는 원고 문장이 아니라 용어집의 Git 디렉토리 정의와 D2 유지다(위 표).
- 미검증: Firefox·Safari의 `file://` 동작 → [open-questions](../plan/open-questions.md) "확보할 자료·실측". 언제: 구현 Phase 1 스모크 또는 릴리즈 체크리스트 6번 브라우저 확인.
- 파일럿 임시 판단 처리(`project-memory/log.md` 2026-10-16): 커밋 뒤 워킹 트리의 Committed 카드 → 레슨 데이터(`files`)로 적는 문제이지 계약 문제가 아니다 / HEAD 위치 → 모양이라 Phase 1 시안. 파일럿의 R8 미반영 → 결정 7의 R8 처리로 해소(파일럿 HTML은 시안이라 고치지 않는다).
