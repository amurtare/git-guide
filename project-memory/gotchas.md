# 함정

항목별 **증상 / 원인 / 해법**. 근본 원인이 해결되면 `~~취소선~~` + `(해결됨: vX.Y.Z)`를 붙이고, 다음 릴리즈 점검에서 제거한다.

---

## `file://`로 열면 `fetch`·ES 모듈이 막힌다
- **증상**: 로컬에서 `index.html`을 더블클릭해 열면 JSON·텍스트 파일 로드나 `<script type="module">`의 `import`가 CORS 에러로 실패한다.
- **원인**: 브라우저는 `file://` 출처의 `fetch`와 모듈 로드를 막는다. 2026-10-21 Chromium 141 실측: `fetch`·XHR·`import()`·`<script type="module">` 모두 실패, 일반 `<script src>`는 다른 폴더 파일도 성공([`dev/evidence/2026-10-21-file-scheme.md`](../dev/evidence/2026-10-21-file-scheme.md)). Firefox·Safari는 미측정.
- **해법**: 레슨 데이터는 JS 파일 안에 넣고 일반 `<script src>`로 불러온다. "설치 없이 열기만 하면 동작"이 이 프로젝트의 약속이므로 로컬 서버를 요구하지 않는다.

## Auto 모드에서는 `.claude/` 수정이 막힌다
- **증상**: Claude Code 클라우드 세션의 Auto 모드에서 `.claude/settings.json` 작성이나 `.claude/hooks/` 수정·실행이 "Self-Modification"으로 거부된다. 대화로 "허용했어"라고 해도 통과되지 않는다.
- **원인**: Auto 모드의 자동 권한 검사가 Claude 자신의 동작 설정 변경을 차단한다.
- **해법**: 입력창 옆 모드 메뉴에서 Accept edits로 바꾼 뒤 작업하거나, 사람이 직접 파일을 수정·커밋한다.

## 클라우드 세션에서 git-scm.com이 막힌다
- **증상**: Pro Git 용어를 확인하려고 git-scm.com을 열면 이름 해석 실패(ENOTFOUND)가 난다.
- **원인**: 클라우드 세션의 네트워크 정책. GitHub는 git 프록시로 공개 저장소 읽기가 된다.
- **해법**: Pro Git 한국어판 원고를 GitHub `progit/progit2-ko`에서 스크래치 디렉터리로 클론해 대조한다. 용어집의 근거 커밋(`dev/design/glossary.md` 머리말)으로 체크아웃해야 출처가 맞는다.

## 클라우드 세션에서 원격 브랜치 삭제가 막힌다
- **증상**: 원격 브랜치를 지우는 push가 "unexpected disconnect while reading sideband packet / the remote end hung up unexpectedly"로 실패한다. 일반 커밋 push는 된다 (2026-10-16 실측).
- **원인**: 세션 git 프록시가 ref 삭제를 거부한다 (태그 push 403과 같은 계열, `decisions/release-automation.md`).
- **해법**: 사용자가 GitHub 웹(저장소 → Branches)에서 지운다. 브랜치 규칙상 main에서만 작업하므로 새로 생길 일은 드물다.

## 앱 패널에 문서를 띄우려면 작업 디렉토리 안 HTML로
- **증상**: 플랜 파일(`/root/.claude/plans/…`)이나 스크래치패드의 `.md`를 파일 보내기로 띄우면 사용자 앱 패널에 뜨지 않는다 (2026-10-16 실측).
- **원인**: 앱은 작업 디렉토리(와 허용된 경로) 안 파일만 열고, 마크다운은 렌더가 불안정하다.
- **해법**: 저장소 안 `.viz/<이름>.html`(gitignore 대상)로 HTML을 만들어 render로 보낸다. 커밋되지 않는다.

## 클라우드 세션의 커밋 독촉 Stop 훅은 지워도 이번 세션에는 계속 뜬다
- **증상**: 설계 결정을 기다리며 미커밋 변경을 둔 채 답변을 마칠 때마다 "There are uncommitted changes … commit and push" 메시지가 뜬다. 저장소 규칙(검수 GO 전 커밋 금지)과 부딪힌다.
- **원인**: 환경이 `/root/.claude/launcher-settings.json`에 넣은 `~/.claude/stop-hook-git-check.sh`다(저장소 `.claude/` 아님). 설정은 세션 시작 때 읽혀서 항목을 지워도 그 세션에는 적용되지 않고, 스크립트를 `exit 0`으로 바꿔도 환경이 원래 내용으로 되돌렸다(2026-10-27 실측). 새 컨테이너에서는 다시 생긴다.
- **해법**: 메시지가 나와도 저장소 규칙을 따른다(GO 전에는 커밋하지 않음). 사용자에게 이유를 한 줄로 알리고, 결정 대기가 끝나면 바로 검수·커밋한다.
