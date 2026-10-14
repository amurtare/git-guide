# 함정

항목별 **증상 / 원인 / 해법**. 근본 원인이 해결되면 `~~취소선~~` + `(해결됨: vX.Y.Z)`를 붙이고, 다음 릴리즈 점검에서 제거한다.

---

## `file://`로 열면 `fetch`·ES 모듈이 막힌다
- **증상**: 로컬에서 `index.html`을 더블클릭해 열면 JSON·텍스트 파일 로드나 `<script type="module">`의 `import`가 CORS 에러로 실패한다.
- **원인**: 브라우저는 `file://` 출처의 `fetch`와 모듈 로드를 막는다.
- **해법**: 레슨 데이터는 JS 파일 안에 넣고 일반 `<script src>`로 불러온다. "설치 없이 열기만 하면 동작"이 이 프로젝트의 약속이므로 로컬 서버를 요구하지 않는다.

## Auto 모드에서는 `.claude/` 수정이 막힌다
- **증상**: Claude Code 클라우드 세션의 Auto 모드에서 `.claude/settings.json` 작성이나 `.claude/hooks/` 수정·실행이 "Self-Modification"으로 거부된다. 대화로 "허용했어"라고 해도 통과되지 않는다.
- **원인**: Auto 모드의 자동 권한 검사가 Claude 자신의 동작 설정 변경을 차단한다.
- **해법**: 입력창 옆 모드 메뉴에서 Accept edits로 바꾼 뒤 작업하거나, 사람이 직접 파일을 수정·커밋한다.

## 클라우드 세션에서 git-scm.com이 막힌다
- **증상**: Pro Git 용어를 확인하려고 git-scm.com을 열면 이름 해석 실패(ENOTFOUND)가 난다.
- **원인**: 클라우드 세션의 네트워크 정책. GitHub는 git 프록시로 공개 저장소 읽기가 된다.
- **해법**: Pro Git 한국어판 원고를 GitHub `progit/progit2-ko`에서 스크래치 디렉터리로 클론해 대조한다. 용어집의 근거 커밋(`docs/design/glossary.md` 머리말)으로 체크아웃해야 출처가 맞는다.
