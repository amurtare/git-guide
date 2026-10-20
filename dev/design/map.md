# 설계 지도

**설계의 단일 소스**다. 모든 단위를 한 표에 둔다. 상세는 각 행의 "참조" 문서에 있다.

- **README 커리큘럼 표는 이 문서의 요약(파생물)이다.** 둘이 다르면 이 문서가 기준이고 README를 맞춘다.
- "처리" 칸은 [curriculum-scope-design.md](curriculum-scope-design.md)(2026-10-19 확정)의 단계별 범위 요약이다. 범위를 바꾸면 그 문서를 먼저 고친다. 표기는 R8("한글 표현 (원고 표기)")을 따른다.
- ID는 안정 식별자다. 단계가 추가·이동되면 새 ID를 붙이고 재번호화하지 않는다. ID와 커리큘럼 단계 번호가 달라지면 아래 표에 대응을 적는다.
- 설계 문서 이름은 `<개념>-design.md`(번호 없음, 개념 하나당 하나 — 맞물린 단계는 한 문서에 함께)로, 각 설계 세션에서 정한다.

## 공용 참조

여러 단위가 함께 인용하는 규칙. 단위가 아니다.

| 이름 | 참조 | 상태 |
|---|---|---|
| 용어집 | [glossary.md](glossary.md) | 확정 2026-10-14 |
| 공용 도식 모델 | [diagram-model.md](diagram-model.md) | 확정 2026-10-14 (노출 범위는 2026-10-19 범위 확정으로 재확인) |
| 커리큘럼 단계별 범위 | [curriculum-scope-design.md](curriculum-scope-design.md) | 확정 2026-10-19 |

## 단위

| ID | 단위 | 커리큘럼 단계 | 참조 | 처리 | 구현 구분 |
|---|---|---|---|---|---|
| `U-diagram` | 공용 도식 컴포넌트 | (모든 단계) | 미작성 | 공용 도식 모델을 화면으로 그리는 공통 부품 | U-diagram 설계 세션에서 정함 (설정 계약·파일 구조) |
| `L0` | 버전 관리란? | 0 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 로컬 버전 관리 → 중앙집중식 버전 관리(CVCS) → 분산 버전 관리 시스템(DVCS)으로서의 Git, Git과 GitHub의 차이 | 설계 시 정함 |
| `L1` | 저장소 만들기 | 1 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 저장소를 새로 만들기, 저장소 복제 (Clone) — 히스토리 전체를 로컬로 복제하는 데까지, Git 디렉토리의 역할 | 설계 시 정함 |
| `L2` | 세 가지 영역 | 2 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 워킹 트리 · 커밋 준비 영역 (Staging Area) · Git 디렉토리, 커밋 준비 영역에 올리기 (Stage), 파일 상태 수정됨 (Modified) · 커밋 준비됨 (Staged) · 커밋됨 (Committed) | 설계 시 정함 |
| `L3` | 커밋 | 3 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 커밋하기 (Commit), 커밋 = 스냅샷, 커밋 히스토리 | 설계 시 정함 |
| `L4` | 변경 확인과 되돌리기 | 4 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 변경 내용 확인(커밋 준비 전·후), 준비 취소 (Unstage), 수정됨 (Modified) 파일 되돌리기, 완료한 커밋 수정 | 설계 시 정함 |
| `L5` | 브랜치 | 5 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 브랜치와 지금 위치 표시 (HEAD), 브랜치 만들기, 브랜치 이동 (Checkout) | 설계 시 정함 |
| `L6` | 병합 (Merge) | 6 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 병합 (Merge), 빨리 감기 (Fast-forward)와 3방향 병합 (3-way Merge), 충돌 | 설계 시 정함 |
| `L7` | 커밋 다시 쌓기 (Rebase) | 7 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 커밋 다시 쌓기 (Rebase), 병합 (Merge)과의 차이, 주의할 점(이미 공유한 커밋) | 설계 시 정함 |
| `L8` | 리모트 저장소 | 8 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 리모트 저장소 등록과 `origin`, 리모트 브랜치·리모트 트래킹 브랜치, 올려 보내기 (Push), 가져오기 (Fetch), 가져와 합치기 (Pull) | 설계 시 정함 |
| `L9` | 협업 흐름 | 9 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 내 계정으로 저장소 복사 (Fork), 병합 요청 (Pull Request)과 코드 리뷰, 브랜치 워크플로, GitHub 플로우 | 설계 시 정함 |
| `L10` | 유용한 도구 | 10 | [curriculum-scope-design.md](curriculum-scope-design.md) (범위) · 레슨 설계 미작성 | 하던 작업 임시 저장 (Stash), 태그, 파일 무시하기, 다른 브랜치의 커밋 가져오기 (Cherry-Pick) | 설계 시 정함 |

"구현 구분" 열이 Design → Impl 계약이다. 구현 준비 상태 점검 때 이 열을 [`dev/impl/checklist.md`](../impl/checklist.md)의 Phase로 편성한다.
