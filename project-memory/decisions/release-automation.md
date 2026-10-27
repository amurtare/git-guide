# 태그·릴리즈 생성: GitHub Actions가 만든다

**결정 (2026-10-13)**: `v{버전}` 태그와 GitHub Release는 사람이나 Claude가 직접 만들지 않고,
`.github/workflows/release.yml`이 main의 `VERSION` 변경을 보고 만든다.

**이유**
- Claude Code 클라우드 세션은 브랜치 push는 되지만 태그 push가 세션의 git 프록시에서 403으로 막힌다.
  (응답에 `X-Github-Request-Id`가 없어 GitHub이 아닌 프록시가 거부한 것으로 확인. v0.1.0 릴리즈 때 발견)
- 연결된 GitHub 도구에는 릴리즈 생성 기능이 없다.
- 워크플로는 저장소 자체 권한(`GITHUB_TOKEN`)으로 돌아 위 제약과 무관하고, 누가 릴리즈하든 같은 결과가 나온다.
- 릴리즈 본문을 `release-notes/v{버전}.md`에서 가져오므로 내용이 중복되지 않는다.

**동작 규칙**
- 트리거: main push 중 `VERSION`이 바뀐 경우, 또는 수동 실행
- 이미 릴리즈된 태그면 통과 (멱등)
- `VERSION`이 `X.Y.Z` 형식이 아니거나 릴리즈 노트 파일이 없으면 실패 → 체크리스트 8번에서 확인

> **보충 (2026-10-24)**: 구현 Phase 1에서 `assets/js/version.js`가 생기면, 그 값이 `VERSION`과 다를 때도 실패하는 비교 단계를 더한다 → [version-display.md](version-display.md).

**참고**: v0.1.0은 이 워크플로 도입 전에 사용자가 GitHub 웹에서 수동으로 만들었다.
