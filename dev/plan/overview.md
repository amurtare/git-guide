# git-guide 개요

## 목적

Git 입문자가 **Git을 직접 쓰지 않고**, 도식을 보며 Git의 개념과 **정확한 용어**를 익히는 정적 학습 사이트다.
근거: [README.md](../../README.md) 소개, R5·R6 (`project-memory/decisions/learning-scope-and-terms.md`).

## 구성요소

| 구성요소 | 상태 | 근거 |
|---|---|---|
| 레슨 — 커리큘럼 단계 하나 = 단위 하나(`L0`~`L10`) | 확정 | [`dev/design/map.md`](../design/map.md), 단계별 범위는 [`curriculum-scope-design.md`](../design/curriculum-scope-design.md) |
| 공용 도식 틀 하나 — 로컬·리모트 공간, 영역, 요소, 전이 | 확정 | R1, [`dev/design/diagram-model.md`](../design/diagram-model.md) |
| 용어집 — 모든 용어의 단일 기준 | 확정 | R6, [`dev/design/glossary.md`](../design/glossary.md) |
| 파일 구조와 공용 도식 컴포넌트의 구현 계약 | 확정 | `U-diagram`, [`dev/design/diagram-component-design.md`](../design/diagram-component-design.md) |

## 배치 기준

1. 모든 레슨은 같은 공용 도식 틀을 쓰고, 레슨마다 새 화면 틀을 만들지 않는다. — R1
2. 화면과 도식 라벨의 모든 용어는 용어집 하나에서 온다. — R6
   원고 표기가 영문인 용어는 "한글 표현 (원고 표기)"로 함께 적는다. — R8
3. 학습자 조작은 장면 이동과 요소 클릭(용어 정의)뿐이고, 명령 입력·실행 UI는 두지 않는다. — R5, D1
   (2026-10-27: 용어 정의는 툴팁으로 보이고, 도식 요소에 붙는 짧은 설명 툴팁(`notes`)이 더해졌다. 그 툴팁을 띄우는 방식이 이 조작 목록에 영향을 주는지는 구현 Phase 1 시안에서 정한다 — [`diagram-component-design.md`](../design/diagram-component-design.md) 결정 14·15)
4. 빌드 없이 `file://`로 열어 동작해야 하므로, 외부 파일 `fetch`·ES 모듈에 의존하지 않는다. — R4
   (2026-10-21 Chromium으로 실측 — [`dev/evidence/2026-10-21-file-scheme.md`](../evidence/2026-10-21-file-scheme.md). Firefox·Safari는 미측정 → [open-questions.md](open-questions.md) "확보할 자료·실측")

## 운영 모델

- **학습자**: 레슨을 열고 장면을 넘기며 도식 변화를 본다. 도식 요소를 누르면 용어 정의를 본다(툴팁). 화면은 도식 중심의 슬라이드형이고 설명은 짧은 나레이션과 툴팁이다(`project-memory/decisions/lesson-layout.md`).
- **메인테이너**: 이 폴더의 Plan → Design → Impl 프로세스([`dev/LONG_TERM_DEV_PROCESS.md`](../LONG_TERM_DEV_PROCESS.md))로 개발하고,
  릴리즈는 [`docs/RELEASE_MANAGEMENT.md`](../../docs/RELEASE_MANAGEMENT.md)를 따른다.

## 확정 결정

- 절대 규칙 R1~R8: [`dev/impl/README.md`](../impl/README.md) "확정 전제"
- D1~D8, 그 밖의 결정: `project-memory/decisions/` ([index](../../project-memory/index.md))
