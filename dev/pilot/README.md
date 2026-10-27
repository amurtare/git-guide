# 파일럿

설계 판단을 돕기 위해 만든 화면 시안. 레슨 코드(`lessons/`)가 아니며, 내용은 확정 설계가 아니다.

| 파일 | 무엇 | 날짜 |
|---|---|---|
| [lesson-form-pilot.html](lesson-form-pilot.html) | 모든 단계가 함께 쓸 레슨 페이지 공통 폼(상자형 — 2026-10-27 슬라이드형으로 방향이 바뀜, `project-memory/decisions/lesson-layout.md`). 시각 스타일은 `project-memory/decisions/visual-style.md`. 예시 장면 5개(파일 수정 → Stage → Commit → Push)는 폼 동작을 보이기 위한 것 | 2026-10-16 |
| [lesson-slide-pilot.html](lesson-slide-pilot.html) | 슬라이드형 레슨 시안 — 화면을 타이틀 영역과 도식 카드 하나로 크게 나눔(카드 안 공간은 색 면 없이 구분선), 나레이션은 카드 위에 얹힌 말풍선 레이어(화면과 반대 시간 테마, 끌어서 옮김, 말하는 말투, 타자 효과), 툴팁(용어 정의 + 도식 요소 설명 `notes`). 장면 데이터는 설정 계약 형식이고 R8 표기와 계약 검사(콘솔 오류)를 반영. 툴팁이 있는 항목은 점선 밑줄로 표시하고 마우스를 올리면(터치는 누르면, 키보드는 포커스) 툴팁이 뜬다(2026-10-27 사용자 요청). 구석의 "설명 항상 보기 / 올렸을 때 보기" 토글과 이 툴팁 동작은 구현 Phase 1에서 정할 비교안(확정 아님). 근거: `dev/design/diagram-component-design.md` 결정 14·15, `project-memory/decisions/lesson-layout.md` | 2026-10-27 |

`index.html`처럼 브라우저로 바로 열면 된다 (`file://`). 서체는 온라인일 때만 Google Fonts로 보인다.

> `lesson-form-pilot.html`(상자형)은 용어 표기 R8("한글 표현 (원고 표기)", 2026-10-19) 이전에 만들었다. 실제 레슨의 R8 표기는 공용 스크립트가 맡는다([`dev/design/diagram-component-design.md`](../design/diagram-component-design.md) "R8 표기", 2026-10-24) — 그 파일은 시안 기록이라 고치지 않는다. `lesson-slide-pilot.html`은 R8을 반영했다.
