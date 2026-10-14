# git-guide 개요

## 목적

Git 입문자가 **Git을 직접 쓰지 않고**, 도식을 보며 Git의 개념과 **정확한 용어**를 익히는 정적 학습 사이트다.
근거: [README.md](../../README.md) 소개, R5·R6 (`project-memory/decisions/learning-scope-and-terms.md`).

## 구성요소

| 구성요소 | 상태 | 근거 |
|---|---|---|
| 레슨 — 커리큘럼 단계 하나 = 단위 하나(`L0`~`L10`) | 확정 | [`dev/design/map.md`](../design/map.md) |
| 공용 도식 틀 하나 — 로컬·리모트 공간, 영역, 요소, 전이 | 확정 | R1, [`dev/design/diagram-model.md`](../design/diagram-model.md) |
| 용어집 — 모든 용어의 단일 기준 | 확정 | R6, [`dev/design/glossary.md`](../design/glossary.md) |
| 파일 구조와 공용 도식 컴포넌트의 구현 계약 | **미정** | `U-diagram` 설계 세션 ([checklist.md](checklist.md)) |

## 배치 기준

1. 모든 레슨은 같은 공용 도식 틀을 쓰고, 레슨마다 새 화면 틀을 만들지 않는다. — R1
2. 화면과 도식 라벨의 모든 용어는 용어집 하나에서 온다. — R6
3. 학습자 조작은 장면 이동과 요소 클릭(용어 정의)뿐이고, 명령 입력·실행 UI는 두지 않는다. — R5, D1
4. 빌드 없이 `file://`로 열어 동작해야 하므로, 외부 파일 `fetch`·ES 모듈에 의존하지 않는다. — R4
   ("막힌다"는 사실은 이 저장소에서 아직 실측하지 않았다 → [open-questions.md](open-questions.md) "확보할 자료·실측")

## 운영 모델

- **학습자**: 레슨을 열고 장면을 넘기며 도식 변화를 본다. 도식 요소를 누르면 용어 정의를 본다.
- **메인테이너**: 이 폴더의 Plan → Design → Impl 프로세스([`dev/LONG_TERM_DEV_PROCESS.md`](../LONG_TERM_DEV_PROCESS.md))로 개발하고,
  릴리즈는 [`docs/RELEASE_MANAGEMENT.md`](../../docs/RELEASE_MANAGEMENT.md)를 따른다.

## 확정 결정

- 절대 규칙 R1~R7: [`dev/impl/README.md`](../impl/README.md) "확정 전제"
- D1~D8, 그 밖의 결정: `project-memory/decisions/` ([index](../../project-memory/index.md))
