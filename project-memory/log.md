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
