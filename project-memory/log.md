# 개발 로그

append-only. 형식: `## [YYYY-MM-DD] <kind> | <한 줄 제목>` + 본문 1~5줄 (의도·맥락 위주, diff 아님).
kind: `release`, `design`, `debug`, `content`, `handoff`

---

## [2026-10-13] design | README 작성
빈 저장소에서 시작. 프로젝트 목적(Git 입문자용 인터랙티브 도식 학습)과 0~10단계 커리큘럼 계획을 README에 정리.
레슨 파일·폴더 구조는 아직 없고 "예정"으로 표기함.

## [2026-10-13] release | v0.1.0 — 릴리즈 관리 체계 도입
amurtare/release_management_guide를 정적 HTML 프로젝트에 맞게 조정해 적용.
매니페스트가 없어 VERSION 파일을 버전 소스로 삼고, 빌드·테스트 단계는 브라우저 확인으로, 보안 점검은 XSS·CDN 고정 위주로 바꿈.
앱 내 업데이트 배너는 만들지 않기로 함 (decisions/update-delivery.md).

## [2026-10-13] design | hook 등록
release_management_guide의 hook 4개를 .claude/settings.json에 등록. 세션 시작 brief는 VERSION 파일을 읽도록 조정.
Auto 모드에서는 .claude/ 수정이 self-modification으로 차단되어, Accept edits 모드로 바꿔서 등록함.

## [2026-10-13] release | v0.1.0 태그·릴리즈 생성과 자동화
클라우드 세션에서 태그 push가 프록시에서 403으로 막혀, v0.1.0은 사용자가 GitHub 웹에서 Release로 만듦.
다음 버전부터는 .github/workflows/release.yml이 VERSION 변경을 보고 태그·릴리즈를 자동 생성 (decisions/release-automation.md).

## [2026-10-13] release | v0.1.1 — 릴리즈 자동화
학습 내용 변화 없이 메인테이너 도구만 바뀌어 PATCH로 판단. Release 워크플로가 실제로 도는 첫 릴리즈.

## [2026-10-13] design | 장기 단계별 구현 프로세스(impl/) 도입
사용자가 준 process-guide.md(perforce-ax-template)를 정적 HTML 학습 사이트에 맞게 이식. 단위 테스트 → 브라우저 스모크, 설계 문서 → docs/design/.
사용자 지시 R1(로컬·리모트 공용 틀)·R2(0단계는 로컬/서버 버전 관리부터)를 절대 규칙으로 고정. 대화 중 제안안은 확정하지 않고 impl/open-questions.md A1~A3으로 남김.
미해결 장부를 impl/open-questions.md 하나로 일원화.

## [2026-10-14] design | Phase 0 용어집·공용 도식 모델, 전제 정정
사용자 정정: 학습자는 Git을 쓰지 않고 개념만(R5), 용어는 Pro Git 한국어판 기준으로 정확하게(R6), 전체 계획 후 단계별 완성(R7).
에이전트가 "명령 실행형 실습"을 전제로 문서를 써 둔 것이 오류였고, README·impl·체크리스트에서 그 전제와 명령어 형태를 걷어냄.
git-scm.com이 막혀 GitHub의 progit2-ko 원고(커밋 고정)를 용어 근거로 삼음. "워킹 트리"/"워킹 디렉토리"처럼 원고 안 이표기가 있어 주 표기+별칭 규칙(D6)을 둠.

## [2026-10-14] design | 장기 개발 프로세스(최신 가이드) 적용, dev/로 재배치
사용자가 준 최신 LONG_TERM_DEV_PROCESS.md(Plan → Design → Impl)를 적용. plan·design·impl·evidence를 루트 dev/ 아래로 모으고(사용자 지시), 가이드 사본은 경로·폴더 구조를 반영한 적용본으로 둠.
A5는 사용자 위임으로 설계 완료 범위 A(모든 단위 설계 후 구현)로 해소 — 0단계 장면 설계는 Design 단계. 설계 대기: 커리큘럼 범위 → U-diagram → 자동 확인 도구 → L0~L10.
옛 Phase 0(설계)과 미결 장부는 dev/plan/으로 옮기고, dev/impl/에는 구현 초안만 남김. 결정: decisions/dev-process.md.

## [2026-10-16] design | 레슨 공통 폼 파일럿, visualize 스킬을 시각 스타일 기준으로
- 레슨 페이지 공통 폼(히어로·전이 표시·공용 도식·장면 설명·용어 카드·장면 이동)을 파일럿으로 만들어 사용자에게 보임. `dev/pilot/`에 보관(레슨 코드 아님, U-diagram 설계 근거 자료)
- 사용자 평: 구성은 괜찮고 "딱딱하다" → 사용자 제공 visualize 스킬의 디자인 컨셉을 기준으로 삼음 (`decisions/visual-style.md`)
- 파일럿에서 설계 문서에 없던 임시 판단: 커밋 뒤 파일 카드는 워킹 트리에 Committed로 다시 그림, HEAD는 브랜치 이름표 아래 — U-diagram 설계에서 확인할 것

## [2026-10-16] process | 브랜치 규칙: 항상 main에서 작업
사용자 지시로 이 저장소는 main에서 직접 작업·푸시한다. 브랜치는 사용자가 요청할 때만 만든다. 클라우드 세션이 `claude/...` 작업 브랜치를 지정해도 CLAUDE.md "브랜치" 규칙이 우선한다.

## [2026-10-19] design | 커리큘럼 단계별 범위 확정, 용어 표기 R8
단계 0~10 범위를 Pro Git 원고 장·절에 맞춰 확정(dev/design/curriculum-scope-design.md). Clone은 1단계(히스토리 복제까지), `origin`·리모트 트래킹 브랜치는 8단계, 4단계 되돌리기는 원고 2장 범위로 좁힘.
사용자 지시로 새 절대 규칙 R8: 원고가 영문인 용어는 "한글 표현 (원고 표기)" 병기. 2026-10-14에 폐기한 "쉬운 말로 대체"와 달리 공식 용어를 남기는 병기라는 점을 결정 문서에 분명히 적음.
플랜 검수에서 D5(처음 영문 병기)를 에이전트가 사용자 확인 없이 줄인 것이 지적돼 되돌림 — 새 규칙이 기존 규칙과 겹칠 때는 기존 규칙을 유지한 채 범위만 나누는 쪽이 안전.

## [2026-10-24] design | U-diagram 공용 도식 컴포넌트 구현 구분
`file://` 제약을 Chromium으로 실측(evidence 2026-10-21)하고, 파일 구조·설정 계약을 dev/design/diagram-component-design.md에 확정. 용어집·단계 목록·버전은 assets/js 사본 스크립트, 장면 데이터는 레슨 HTML 안, 뼈대·도식·R8 표기는 공용 스크립트. B1 해소(decisions/version-display.md).
사용자 결정은 CLAUDE.md에 새로 들어온 "한 번에 한 개씩, 텍스트로" 방식으로 진행. 처음에 선택지 UI·두 질문 동시로 물었다가 지적받아 고침. 후반은 사용자 위임.
플랜 검수 4회: 결정 5(요소)를 전이에도 넓혀 쓰려던 것이 "답의 범위를 넓히지 않는다"에 걸려 결정 9로 분리 — 사용자 답이 다룬 대상(요소)과 비슷한 대상(전이)은 따로 결정으로 드러낼 것.
파일럿 임시 판단(2026-10-16 항목) 처리: 커밋 뒤 Committed 카드 → 레슨 데이터로 적는 문제, HEAD 위치 → Phase 1 시안.
- (2026-10-27 추가) 문서 검수 대기 중 사용자 제안 "나레이션 패널" → 의도는 상자형 파일럿 대신 PPT 같은 슬라이드형, 도식 중심, 텍스트 최소, 툴팁. 결정 14·15, decisions/lesson-layout.md. 제안을 "칸 하나 추가"로 좁혀 묻기 전에 의도(화면 전체 구성)를 먼저 확인했어야 했다.
