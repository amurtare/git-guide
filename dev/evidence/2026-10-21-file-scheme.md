# `file://`에서 막히는 것과 되는 것 (Chromium)

- **날짜**: 2026-10-21
- **대상**: Chromium 141.0.7390.37 (headless, Playwright 1.56.1, 클라우드 세션 컨테이너의 `/opt/pw-browsers`)
- **목적**: [`dev/plan/open-questions.md`](../plan/open-questions.md) "확보할 자료·실측"의 `file://` 항목 — `project-memory/gotchas.md`에 적혀 있던 "`fetch`·ES 모듈이 막힌다"를 이 저장소에서 직접 확인
- **쓰는 곳**: [`dev/design/diagram-component-design.md`](../design/diagram-component-design.md) 파일 구조(모든 데이터는 일반 `<script src>`로)

## 방법

1. `dev/pilot/lesson-form-pilot.html`을 `file:///home/user/git-guide/dev/pilot/lesson-form-pilot.html`로 연다 (저장소 파일을 고치지 않는 읽기 전용 측정).
2. 페이지 안에서(`page.evaluate`) 다음을 차례로 시도하고 결과와 콘솔 메시지를 모은다.
   - `fetch("../../VERSION")` — 저장소 루트의 `VERSION`
   - 같은 파일을 XHR로 읽기
   - 다른 폴더의 JS 파일을 `import()`로 불러오기
   - 같은 JS 파일을 `<script type="module" src>`로 붙이기
   - 같은 JS 파일을 일반 `<script src>`로 붙이기
   - JS 파일은 컨테이너에 있는 `file:///opt/node-tools/node_modules/playwright/index.js`(저장소 밖, 다른 폴더)를 썼다

## 결과

| 시도 | 결과 | 콘솔 메시지 |
|---|---|---|
| `fetch` | 실패 (`TypeError: Failed to fetch`) | `Fetch API cannot load file:///home/user/git-guide/VERSION. URL scheme "file" is not supported.` |
| XHR | 실패 (`onerror`) | `… from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: chrome, chrome-untrusted, data, http, https.` |
| `import()` | 실패 (`TypeError: Failed to fetch dynamically imported module`) | — |
| `<script type="module" src>` | 실패 (`onerror`) | `Access to script at '…index.js' from origin 'null' has been blocked by CORS policy …` |
| 일반 `<script src>` | **성공** (`onload`) | — |

페이지 출처(`location.origin`)는 `file://`, 스크립트 쪽 출처는 `null`로 취급된다.

## 결론

- `file://`로 연 페이지는 데이터 파일을 읽을 수 없고(`fetch`·XHR), ES 모듈도 쓸 수 없다. 일반 `<script src>`는 다른 폴더의 파일까지 불러온다.
- 따라서 용어집·버전·레슨 데이터는 일반 스크립트 안의 JS 값으로 둔다.

## 미검증

- Firefox·Safari — 컨테이너에 없어 측정하지 못했다. [`dev/plan/open-questions.md`](../plan/open-questions.md) "확보할 자료·실측"에 남김.
