# git-guide 앞단(계획·설계) 미결·실측 장부

설계 중 미결 결정과 실측할 가정을 모은다. 구현 단계의 미검증 장부는 [`dev/impl/open-questions.md`](../impl/open-questions.md)다.

## 운영 규칙

- **ID**: 구획 문자 + 번호(`A2`). 지운 ID는 재사용하지 않는다 — 지금까지 지운 ID: A1(공용 도식 상세안, 2026-10-14 해소), A5(백로그 구성, 2026-10-14 해소 → `project-memory/decisions/dev-process.md`), C1(검수자 모델, 2026-10-13 해소), A3(Clone 단계)·A4(용어 "처음"·단계 이름, 2026-10-19 해소 → `dev/design/curriculum-scope-design.md`, `project-memory/decisions/term-notation.md`), B1(화면 버전 표시, 2026-10-24 해소 → `project-memory/decisions/version-display.md`, `dev/design/diagram-component-design.md`)
- **해소되면**: 항목을 지우고 결과를 `project-memory/decisions/<주제>.md`(정책) 또는 `project-memory/gotchas.md`(사실)·설계 문서로 옮긴다. 실측 항목은 지우지 않고 `[x]` + 날짜·결과·근거 링크
- **Design 종료 조건**(가이드 §0-3·§0-6): 아래 전건 해소 또는 "preflight·구현 단계로 이관"이 명시돼야 Design → Impl로 넘어간다

---

## 확보할 자료·실측

- [x] Pro Git 한국어판 원고 대조 — `progit/progit2-ko` 커밋 `f50647d`로 고정, 용어집 출처 대조 누락 0 (2026-10-14, [`dev/design/glossary.md`](../design/glossary.md) 머리말)
- [x] git-scm.com 접근 불가 — 클라우드 세션 네트워크 정책(ENOTFOUND). GitHub 원고로 대체 (2026-10-14, `project-memory/gotchas.md`)
- [x] 태그 push 403 — 세션 git 프록시가 거부(응답에 `X-Github-Request-Id` 없음). 릴리즈는 GitHub Actions로 (2026-10-13, `project-memory/decisions/release-automation.md`)
- [x] `file://`에서 `fetch`·ES 모듈이 막히는지 — Chromium 141에서 `fetch`·XHR·ES 모듈 모두 막히고 일반 `<script src>`는 된다 (2026-10-21, [`dev/evidence/2026-10-21-file-scheme.md`](../evidence/2026-10-21-file-scheme.md))
- [ ] Firefox·Safari에서도 `file://` 동작이 같은지(일반 `<script src>`로 다른 폴더 파일을 불러오는지) — 컨테이너에 Chromium만 있어 측정하지 못했다. **언제**: 구현 Phase 1 스모크 또는 릴리즈 체크리스트 6번 브라우저 확인(사람이 직접). 이 실측은 Design → Impl 게이트 조건이 아니며 구현 단계로 이관한다

## 남은 결정 논점

### A. 설계 미결 — 사용자와 정해야 하는 것

#### A2 0단계 장면 구성
- **모르는 것**: R2의 구체 장면. 제안(2026-10-13, 용어는 2026-10-14 용어집 기준으로 고침): 0-1 파일을 복사해 버전을 관리하던 방식 → 0-2 로컬 버전 관리 → 0-3 중앙집중식 버전 관리(CVCS) → 0-4 분산 버전 관리 시스템(DVCS)으로서의 Git(공용 틀 완성) → 0-5 1~10단계 지도. 공간·영역 구성은 [`dev/design/diagram-model.md`](../design/diagram-model.md)를 따른다
- **모르는 채 동작**: 구현하지 않는다
- **확인 방법**: 사용자와 의논 → L0 설계 문서(이름은 설계 세션에서 정함, `dev/design/`). 사용자가 공유하려던 Perforce 자료(`perforce-ax-template`)가 서버 방식 장면의 참고가 될 수 있음
- **언제**: Design · L0 설계
- **출처**: 프로세스 도입(2026-10-13)

#### A6 Fork 장면의 서버 쪽 저장소 개수
- **모르는 것**: 내 계정으로 저장소 복사 (Fork)를 보여 주려면 서버 쪽에 저장소가 2개(원본, 내 계정의 복사본) 필요하다. 그런데 [`dev/design/diagram-model.md`](../design/diagram-model.md) 1절은 서버 상자를 최대 1개로 정했다
- **모르는 채 동작**: 구현하지 않는다. 에이전트가 정하지 않는다(R3) — 공용 도식 모델(D3)을 바꾸는 결정이다
- **확인 방법**: 사용자와 의논. 선택지 예: 서버 상자 안에 저장소 2개를 나란히 그림 / 서버 상자를 2개로 늘림 / 9단계는 Fork를 설명 장면으로만 다룸
- **언제**: Design · L9 설계. U-diagram 설계(2026-10-24)는 서버 상자 계약을 지금 그대로(최대 1개) 두고 Fork 복사본 저장소의 자리를 이 항목에 남겼다([`diagram-model.md`](../design/diagram-model.md) 3절, [`diagram-component-design.md`](../design/diagram-component-design.md) 확장 규칙)
- **출처**: 커리큘럼 단계별 범위 확정 플랜 검수(2026-10-19)

### B. 배포·운영

#### B2 공개 방식 (GitHub Pages 여부)
- **모르는 것**: 웹 배포 여부. 내려받기 안내 방식은 `project-memory/decisions/update-delivery-download.md`. README는 내려받은 파일의 `index.html`을 여는 방법만 안내한다
- **모르는 채 동작**: 로컬 열람만 지원
- **확인 방법**: 사용자 결정 → 릴리즈 체크리스트 8번, README 사용 방법 갱신. README 사용 방법은 2026-10-14부터 "Download ZIP 후 `index.html` 열기"로 안내한다(D8) — B2 해소 때 다시 확인
- **언제**: 첫 레슨 완성 시. Design → Impl 게이트 전에 정하지 않아도 되며, 구현 단계 장부(`dev/impl/open-questions.md`)나 preflight로 넘길 수 있다
- **출처**: v0.1.0(2026-10-13), `project-memory/open-questions.md`에서 이관

#### B3 레슨 구성이 바뀔 때의 경로 대응
- **모르는 것**: 레슨 파일 이름의 번호는 커리큘럼 단계 번호다([`diagram-component-design.md`](../design/diagram-component-design.md) 파일 구조). 레슨을 끼워 넣거나 빼거나 합치면 뒤 레슨의 경로가 바뀌어 북마크·링크가 끊긴다(MAJOR). 그때 옛 경로를 어떻게 안내할지(예: 옮긴 위치를 알리는 안내 페이지) 정하지 않았다
- **모르는 채 동작**: 레슨 구성을 바꾸지 않는 한 문제없다. 바꾸게 되면 그 변경을 설계하는 세션에서 먼저 정한다. 안내 페이지 같은 대응은 공용 틀을 바꾸지 않고 덧붙일 수 있다
- **확인 방법**: 사용자 결정
- **언제**: 처음 레슨 구성이 바뀔 때(추가·삭제·합치기). Design → Impl 게이트 조건이 아니다
- **출처**: U-diagram 설계 결정 2-b(2026-10-21, 사용자 "(가)")

### C. 검수·도구

#### C2 자동 확인 도구
- **모르는 것**: 레슨 인터랙션을 자동으로 확인할 도구. 후보: Playwright(컨테이너에 Chromium 설치됨) 스크립트를 개발 전용으로 둠. "빌드 없음" 원칙(R4)은 배포물에 대한 것이라 개발 전용 도구와 충돌하지 않는다고 보지만 확인 필요
- **모르는 채 동작**: 수동 스모크(`dev/impl/README.md` "실행 환경" 절차)만 한다
- **확인 방법**: 사용자 결정 → 도입 시 `package.json`(개발 전용) 여부와 버전 소스(`VERSION`) 관계도 함께 정리
- **확인 대상 후보**(2026-10-24 U-diagram 설계에서 추가): 사이트 쪽 사본의 일치 — `assets/js/glossary.js` ↔ `dev/design/glossary.md`, `assets/js/curriculum.js` ↔ `dev/design/curriculum-scope-design.md` 단계 이름. 정해지기 전에는 릴리즈 체크리스트 4번에서 사람이 대조한다([`diagram-component-design.md`](../design/diagram-component-design.md) 사본 일치)
- **언제**: Design · 자동 확인 도구 결정 (Design → Impl 게이트 전)
- **출처**: 프로세스 도입(2026-10-13)
