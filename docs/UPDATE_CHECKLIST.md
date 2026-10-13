# 버전 업데이트 체크리스트

릴리즈(MAJOR/MINOR/PATCH) 시 아래 항목을 순서대로 확인한다.
규칙의 근거는 [RELEASE_MANAGEMENT.md](RELEASE_MANAGEMENT.md) 참고.

## 1. 버전 번호 갱신

- [ ] 루트 `VERSION` 파일 갱신 — 버전의 **유일한 소스**
- [ ] 버전 규칙: `MAJOR.MINOR.PATCH` — [RELEASE_MANAGEMENT.md](RELEASE_MANAGEMENT.md#버전-규칙) 참고
  - MAJOR: 커리큘럼 단계 번호·순서 재편, 레슨 파일 경로(URL) 변경 등 북마크·링크가 깨지는 변경
  - MINOR: 새 레슨(단계) 추가, 새 인터랙티브 도식 추가, 기존 레슨에 새 실습 추가
  - PATCH: 오탈자·설명 수정, 도식 동작 버그 수정, 스타일 조정
- [ ] 화면에 버전을 표시하는 곳이 생겼다면(예: `index.html` 푸터) 같은 값으로 맞춰졌는지 확인

## 2. 릴리즈 노트 작성

- [ ] `release-notes/v{버전}.md` 신규 생성 — [형식](RELEASE_MANAGEMENT.md#릴리즈-노트-형식)
- [ ] 포함 항목: 새 레슨, 새 도식, 개선, 버그 수정, 구조 변경
- [ ] 기존 릴리즈 노트와 동일한 포맷 유지

## 3. README.md 갱신 여부 확인

- [ ] 커리큘럼 표 — 새 레슨 추가·순서 변경을 반영, 완성된 단계 표시 갱신
- [ ] 프로젝트 구조 — 파일/폴더 구조가 바뀌었으면 갱신
- [ ] 사용 방법 — 진입 파일·열람 방법(로컬/GitHub Pages)이 바뀌었으면 갱신
- [ ] 버전 표기 — `vX.Y.Z 기준` 문구를 현재 버전으로 갱신

## 4. 콘텐츠 정확성 점검 (레슨이 추가·수정된 경우)

- [ ] 레슨에 나오는 Git 명령어를 실제 Git(최신 안정 버전)으로 실행해 결과가 설명·도식과 일치하는지 확인
- [ ] 구식 명령을 권장하지 않는지 확인 (예: `checkout` 대신 `switch`/`restore` 우선 소개, 기본 브랜치명 `main`)
- [ ] 레슨 간 용어가 일관적인지 확인 (작업 디렉터리 / 스테이징 영역 / 저장소 등)
- [ ] 이전·다음 레슨 링크가 올바른지 확인

## 5. 안전성 점검 (스크립트·외부 리소스가 바뀐 경우)

- [ ] 사용자가 입력한 텍스트(예: 실습용 명령 입력창)를 `innerHTML`로 그대로 넣지 않는가? → `textContent` 사용 (XSS 방지)
- [ ] 외부 스크립트는 정확한 버전이 고정된 CDN URL만 사용하는가? (`lib@x.y.z`, `@latest` 금지)
- [ ] 새로 추가된 외부 요청(분석 도구, 폰트 등)이 꼭 필요한가?

## 6. 브라우저 동작 확인

빌드 단계가 없으므로 "빌드 & 테스트"는 브라우저 확인으로 대신한다.

- [ ] `index.html`을 브라우저에서 직접 열어(`file://`) 모든 레슨이 동작하는지 확인
- [ ] 개발자 도구 콘솔에 에러·404가 없는지 확인
- [ ] Chrome · Firefox · Safari(가능하면) 중 최소 2종에서 확인
- [ ] 모바일 폭(약 375px)에서 가로 스크롤 없이 도식이 보이는지 확인
- [ ] 라이트/다크 모드 모두에서 도식이 읽히는지 확인
- [ ] 새 인터랙션을 처음부터 끝까지 직접 조작해 보고, "초기화" 동작도 확인

## 7. project-memory 갱신 점검

이번 릴리즈에서 다음 중 하나라도 변경됐으면 `project-memory/`도 같이 갱신한다.
**stale한 project-memory는 거짓말 소스가 되므로** 빠뜨리지 말 것.
순수 오탈자·문구 수정 PATCH라면 생략 가능.

- [ ] 설계 의도/정책 변경 → `project-memory/decisions/<topic>.md` 추가 (기존 결정을 뒤집으면 superseded 표시)
- [ ] 반복 가능한 함정 발견 → `project-memory/gotchas.md` 항목 추가
- [ ] 레슨·공통 스크립트 구조 변경 → `project-memory/components.md` 갱신
- [ ] 미해결 이슈 진척/해결 → `project-memory/open-questions.md` 갱신
- [ ] `project-memory/log.md`에 이번 릴리즈 항목 append (1~3줄, 의도 위주)
- [ ] `project-memory/insight/` 정리 — 6개월 이상 참조 0회 항목 삭제
- [ ] staleness 점검: decisions에 superseded 누락 없는지, gotchas에 해결된 항목 없는지,
  components가 현재 구조와 맞는지 확인

## 8. 커밋 & 배포

- [ ] 관련 파일 모두 `git add` (VERSION, release-notes, README.md, 레슨·assets 파일, project-memory)
- [ ] 커밋 메시지에 버전 포함: `v0.2.0: 3단계 커밋 레슨 추가`
- [ ] `git push origin main` — 태그는 직접 만들지 않는다
- [ ] GitHub Actions의 **Release** 워크플로가 성공했는지 확인
  - `VERSION`이 바뀐 push에서 자동 실행되어 `v{버전}` 태그와 GitHub Release를 만든다 (본문 = `release-notes/v{버전}.md`)
  - 실패했으면 로그 확인: `VERSION` 형식 오류이거나 릴리즈 노트 파일 누락이 대부분
  - 다시 돌리려면 Actions 탭에서 Release → Run workflow (이미 릴리즈된 버전이면 아무것도 하지 않음)
- [ ] (GitHub Pages 사용 시) 배포된 페이지에서 새 버전이 보이는지 확인
