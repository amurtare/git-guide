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
