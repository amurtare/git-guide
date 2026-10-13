# Git Guide 🌱

> Git을 처음 접하는 사람을 위한 **인터랙티브 도식 기반 Git 학습 가이드**
>
> v0.1.1 기준 · [변경 내역](release-notes/)

명령어를 외우기 전에, Git 안에서 **무슨 일이 일어나는지 눈으로 보면서** 이해하는 것을 목표로 합니다.
각 단계는 브라우저에서 바로 열 수 있는 HTML 페이지로 제공되며, 버튼을 누르거나 명령을 실행하면
커밋·브랜치·HEAD 등의 변화가 도식(다이어그램)으로 실시간 표현됩니다.

---

## ✨ 특징

- **시각화 중심** — 작업 디렉터리, 스테이징 영역, 저장소, 커밋 그래프를 도식으로 보여줍니다.
- **인터랙티브** — 직접 클릭하고 명령을 실행하며 결과가 어떻게 바뀌는지 확인합니다.
- **커리큘럼 단계별 구성** — 기초 개념부터 협업까지 순서대로 따라가며 학습합니다.
- **설치 불필요** — 별도 빌드나 서버 없이 HTML 파일을 브라우저로 열기만 하면 됩니다.
- **초보자 친화적** — 전문 용어는 쉬운 비유와 함께 설명합니다.

---

## 📚 커리큘럼 (계획)

| 단계 | 주제 | 다루는 내용 |
|:---:|---|---|
| 0 | 버전 관리란? | Git 이전의 로컬·서버 버전 관리 방식, 분산 버전 관리로서의 Git, Git과 GitHub의 차이 |
| 1 | 저장소 만들기 | `git init`, `git clone`, `.git` 폴더의 역할 |
| 2 | 세 가지 영역 | 작업 디렉터리 · 스테이징 영역 · 저장소, `git add`, `git status` |
| 3 | 커밋 | `git commit`, 커밋 = 스냅샷, `git log` |
| 4 | 변경 확인과 되돌리기 | `git diff`, `git restore`, `git reset`, `git revert` |
| 5 | 브랜치 | 브랜치와 HEAD의 정체, `git branch`, `git switch` |
| 6 | 병합 | `git merge`, Fast-forward vs 3-way merge, 충돌 해결 |
| 7 | 리베이스 | `git rebase`, merge와의 차이, 주의할 점 |
| 8 | 원격 저장소 | `git remote`, `git push`, `git fetch`, `git pull` |
| 9 | 협업 흐름 | Fork, Pull Request, 코드 리뷰, 브랜치 전략 |
| 10 | 유용한 도구 | `git stash`, `git tag`, `.gitignore`, `git cherry-pick` |

> 커리큘럼은 진행 상황에 따라 변경될 수 있습니다.

---

## 🚀 사용 방법

1. 저장소를 클론합니다.
   ```bash
   git clone https://github.com/amurtare/git-guide.git
   cd git-guide
   ```
2. `index.html`을 브라우저로 엽니다.
3. 0단계부터 순서대로 진행하며 도식을 직접 조작해 봅니다.

---

## 🗂️ 프로젝트 구조 (예정)

```
git-guide/
├── index.html          # 메인 페이지 (커리큘럼 목차)
├── lessons/            # 단계별 학습 페이지
│   ├── 00-what-is-git.html
│   ├── 01-repository.html
│   └── ...
├── assets/
│   ├── css/            # 공통 스타일
│   └── js/             # 도식 렌더링 · 인터랙션 스크립트
├── .github/workflows/  # 릴리즈 자동화 (태그 · GitHub Release)
├── docs/               # 릴리즈 관리 규칙 · 체크리스트
├── release-notes/      # 버전별 변경 내역
├── project-memory/     # 설계 결정 · 함정 · 개발 로그
├── VERSION             # 현재 버전
└── README.md
```

---

## 🏷️ 버전과 릴리즈

[Semver](https://semver.org)(`MAJOR.MINOR.PATCH`)를 따르며, 버전은 `VERSION` 파일 하나로 관리합니다.

| 구분 | 언제 올리나 |
|---|---|
| MAJOR | 커리큘럼 단계 재편, 레슨 경로 변경처럼 기존 링크가 깨질 때 |
| MINOR | 새 레슨이나 새 인터랙티브 도식이 추가될 때 |
| PATCH | 오탈자, 설명 수정, 도식 버그 수정 |

- 커리큘럼 0~10단계가 모두 완성되면 `1.0.0`이 됩니다.
- 버전별 변경 내역은 [`release-notes/`](release-notes/)에서 볼 수 있습니다.
- 릴리즈 절차는 [`docs/RELEASE_MANAGEMENT.md`](docs/RELEASE_MANAGEMENT.md)와 [`docs/UPDATE_CHECKLIST.md`](docs/UPDATE_CHECKLIST.md)를 따릅니다.

---

## 🤝 기여하기

오타 수정, 설명 개선, 새로운 단계 제안 모두 환영합니다.

1. 이 저장소를 Fork 합니다.
2. 새 브랜치를 만듭니다. (`git switch -c feature/my-lesson`)
3. 변경 사항을 커밋합니다. (`git commit -m "Add lesson: ..."`)
4. 브랜치에 Push 합니다. (`git push origin feature/my-lesson`)
5. Pull Request를 생성합니다.

> 이 과정 자체가 이 가이드의 8~9단계에서 배우는 내용입니다 😉
