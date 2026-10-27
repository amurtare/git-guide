# 사이트 HTML의 시각 스타일: visualize 스킬의 디자인 컨셉을 따른다

**결정 (2026-10-16, 사용자 지시)**

사이트(`index.html`·`lessons/`)와 파일럿 등 이 저장소에서 만드는 HTML은 사용자가 제공한 `visualize` 스킬의 디자인 컨셉을 참고해 만든다.
스킬은 [`.claude/skills/visualize/`](../../.claude/skills/visualize/SKILL.md)에 원본 그대로 두었다 (md → HTML 변환은 `/visualize`로 그대로 쓸 수 있고, 출력 `.viz/`는 커밋하지 않는다).

**이유 (사용자 의도)**: 첫 파일럿(공통 폼)의 구성은 괜찮지만 "딱딱하다"는 평. 따뜻한 종이 톤·세리프 제목·부드러운 카드·움직임이 있는 이 컨셉을 기본 시각 언어로 삼는다.

> **보충·일부 대체 (2026-10-27)**: 위 "구성은 괜찮지만"의 구성 평가와 아래 표의 "화면 구성은 diagram-model.md와 레슨 설계가 정한다"는 [lesson-layout.md](lesson-layout.md)로 보충·대체된다 — 레슨 화면은 파일럿의 상자형 공통 폼 대신 슬라이드형(도식 중심, 나레이션·툴팁)이고, 화면 구성은 lesson-layout과 [diagram-component-design.md](../../dev/design/diagram-component-design.md)도 함께 정한다. 이 문서의 시각 언어(토큰·서체·배경)는 그대로다.

## 무엇을 가져오나

기준 문서: [`.claude/skills/visualize/references/html-design-guide.md`](../../.claude/skills/visualize/references/html-design-guide.md)

- **Part 1 Foundation 전부**: 디자인 토큰(`--bg`·`--surface`·`--ink` 계열, 5색 팔레트 `--p1`~`--p5`와 soft/dark/muted 변형, 반경 `--r-*`, 그림자 `--e1`~`--e5`, `--ease-out`·`--ease-spring`), 타이포 역할(디스플레이 세리프 · 본문 산세리프 · mono 라벨), 프리미티브(섹션 헤더 eyebrow, 상단 컬러 바, 코너 글로우, 호버 엘리베이션, `fadeUp` 진입), 페이퍼 그레인·앰비언트 워시 배경, 최대 폭 1180px, 접근성 규칙
- **CJK 줄바꿈**: 제목·라벨에 `word-break: keep-all` (`references/patterns.md`)

## 이 사이트에 맞춘 조정

| 스킬 규칙 | 이 사이트에서 | 근거 |
|---|---|---|
| 디스플레이 서체 Newsreader | Newsreader 뒤에 **Noto Serif KR**을 이어 둔다 (Newsreader에 한글 글리프가 없다) | 한국어 사이트 |
| 본문 서체 IBM Plex Sans | **IBM Plex Sans KR** | 한국어 사이트 |
| 코드 블록·복사 버튼·프롬프트 창 | **쓰지 않는다** | R5·D8: 명령어 형태를 사이트 어디에도 쓰지 않는다 |
| md 변환용 "Design quality floor"(내비게이션 질문, 스크롤 리빌, SVG 센터피스 등)·Step 2.5 체크 | `/visualize`로 문서를 변환할 때만 적용. 레슨 페이지는 Foundation만 따르고, 화면 구성은 [`dev/design/diagram-model.md`](../../dev/design/diagram-model.md)와 레슨 설계가 정한다 | 레슨은 문서 변환물이 아니다 |
| eyebrow는 영어 키워드 | 따른다. 단 용어집 용어를 대신하지 않는 장식 라벨에만 쓴다 | R6 |
| 다크 모드 | 같은 hue로 다크 토큰을 따로 정의한다 (스킬 문서에는 라이트 토큰만 있다) | 접근성 |
| Google Fonts 필수 | 링크는 넣되 `file://` 오프라인에서는 대체 서체로 보인다. 대체 서체 스택을 반드시 둔다 | R4 |

~~도식 색 배정(공간·파일 상태)과 모양은 U-diagram 설계에서 확정한다.~~ [대체됨 2026-10-24: U-diagram 설계는 구현 계약만 정하고, 색 배정과 모양은 구현 Phase 1 시안에서 사용자 확인을 받는다 — [dev/design/diagram-component-design.md](../../dev/design/diagram-component-design.md) 결정 11] 파일럿의 배정은 시안이다. "색만으로 상태를 구분하지 않는다"는 그대로다.
