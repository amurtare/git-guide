# 화면 버전 표시: `assets/js/version.js` 사본 + 릴리즈 워크플로 비교

**결정 (2026-10-21, 사용자 결정 — U-diagram 설계 세션)**: [version-source.md](version-source.md)를 보충하고, [dev/plan/open-questions.md](../../dev/plan/open-questions.md)의 B1을 해소한다.

**배경**
- 버전 소스는 루트 `VERSION` 하나다(version-source.md). `index.html` 푸터에 현재 버전과 릴리즈 노트 링크를 두기로 했다([update-delivery-download.md](update-delivery-download.md)).
- `file://`로 연 페이지는 `VERSION`을 읽을 수 없다(2026-10-21 실측, [`dev/evidence/2026-10-21-file-scheme.md`](../../dev/evidence/2026-10-21-file-scheme.md)). 그래서 화면용 사본이 하나 필요하다.

**결정 내용**
- 화면 표시용 사본은 `assets/js/version.js` 한 파일에 값 한 줄로 둔다(예: 이름 공간 준비 줄 `window.GitGuide = window.GitGuide || {};` 다음에 `window.GitGuide.version = "X.Y.Z";`). 일반 `<script src>`로 불러와 실행하는 방식이다. 형식의 기준은 [설계 문서](../../dev/design/diagram-component-design.md) 파일 구조다.
- `index.html`만 이 파일을 불러오고, 공용 스크립트가 푸터에 넣는다. 레슨 페이지에는 버전을 보이지 않는다.
- 릴리즈 워크플로(`.github/workflows/release.yml`)가 `version.js`의 값과 `VERSION`을 비교해, 다르면 태그·릴리즈를 만들기 전에 실패한다. 이 비교 단계는 `version.js`를 처음 만드는 구현 커밋(구현 Phase 1)에서 함께 넣는다.

**사용자 원문**
| 결정 | 원문 |
|---|---|
| 자동 비교 | 질문 "릴리즈 때 `VERSION`과 푸터 버전 사본이 같은지 누가 확인할까요"에 "(가)" — 앞서 "일치 시키면 되는 거 아니야? 왜 이 질문이 나온거야?"에 답하고 질문을 줄임 |
| 별도 파일 | 질문 "버전 사본을 어느 파일에 둘까요"에 "(가)" — 앞서 "html 에 표시는 assets/js/version.js 이 파일을 읽어서 하는 것인가?"에 불러와 실행하는 방식으로 답함 |

관련 설계: [dev/design/diagram-component-design.md](../../dev/design/diagram-component-design.md) "버전 표시"
