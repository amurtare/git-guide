# 구조

릴리즈 체크리스트에서 현재 구조와 맞는지 점검한다.

## 현재 (v0.1.0)

레슨·사이트 파일은 아직 없다. 문서와 릴리즈 관리 파일만 있다.

```
git-guide/
├── README.md               # 프로젝트 소개 · 커리큘럼 계획
├── CLAUDE.md               # Claude Code 작업 규칙
├── VERSION                 # 버전 단일 소스
├── docs/
│   ├── RELEASE_MANAGEMENT.md
│   ├── UPDATE_CHECKLIST.md
│   └── design/             # 설계 문서 (authoritative). Phase 0에서 채움
├── impl/                   # 구현 진행 관리 — README(진입점)·checklist·progress·open-questions
├── release-notes/          # v{버전}.md
├── .github/workflows/release.yml  # VERSION 변경 시 태그·GitHub Release 자동 생성
├── .claude/                # hook 스크립트와 등록 설정
└── project-memory/
```

## 예정 (README 기준)

- `index.html` — 커리큘럼 목차, 푸터에 버전 표시
- `lessons/NN-<slug>.html` — 단계별 레슨. 파일명의 번호 = 커리큘럼 단계 번호 (바꾸면 MAJOR)
- `assets/css/` — 공통 스타일
- `assets/js/` — 도식 렌더링·인터랙션 공통 스크립트
