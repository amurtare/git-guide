# 구조

릴리즈 체크리스트에서 현재 구조와 맞는지 점검한다.

## 현재

레슨·사이트 파일은 아직 없다. 문서와 릴리즈 관리 파일만 있다.

```
git-guide/
├── README.md               # 프로젝트 소개 · 커리큘럼 계획
├── CLAUDE.md               # Claude Code 작업 규칙
├── VERSION                 # 버전 단일 소스
├── docs/
│   ├── RELEASE_MANAGEMENT.md
│   └── UPDATE_CHECKLIST.md
├── dev/                    # 개발 프로세스(Plan → Design → Impl) — LONG_TERM_DEV_PROCESS.md(적용본)
│   ├── plan/               # 진입점(README)·overview·checklist·open-questions
│   ├── design/             # 설계 단일 소스 — map.md, glossary.md, diagram-model.md, curriculum-scope-design.md, diagram-component-design.md
│   ├── pilot/              # 화면 시안(설계 참고용, 레슨 코드 아님)
│   ├── impl/               # 구현 진행 관리 — README·checklist(초안)·progress·open-questions
│   └── evidence/           # 실측 증거
├── release-notes/          # v{버전}.md
├── .github/workflows/release.yml  # VERSION 변경 시 태그·GitHub Release 자동 생성
├── .claude/                # hook 스크립트와 등록 설정, skills/visualize(디자인 컨셉 원본)
└── project-memory/
```

## 예정 (설계 확정: [dev/design/diagram-component-design.md](../dev/design/diagram-component-design.md), 2026-10-24)

- `index.html` — 커리큘럼 목차, 푸터에 버전·릴리즈 노트 링크. 뼈대는 `site.js`가 만든다
- `lessons/NN-<꼬리표>.html` — 단계별 레슨(`00-version-control` … `10-tools`). 파일명의 번호 = 커리큘럼 단계 번호 (바꾸면 MAJOR). 내용은 공용 스크립트 연결 + 인라인 장면 데이터만
- `assets/css/` — `site.css`(토큰·타이포·레슨 화면 배치), `diagram.css`(도식)
- `assets/js/` — `glossary.js`·`curriculum.js`·`version.js`(사본 값), `diagram.js`(도식 그리기), `site.js`(뼈대·장면 이동·나레이션·툴팁·R8 표기). 모두 일반 `<script src>`, 전역 `window.GitGuide`
