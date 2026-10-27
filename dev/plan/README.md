# git-guide 계획·설계 — 진입점 (dev/plan/)

이 저장소는 [`dev/LONG_TERM_DEV_PROCESS.md`](../LONG_TERM_DEV_PROCESS.md)(장기 단계별 개발 프로세스, git-guide 적용본)를 따른다.
**Plan → Design → Impl** 순서이고, 지금은 **Design** 단계다. 구현(`dev/impl/`)은 모든 단위의 설계가 끝난 뒤 시작한다(설계 완료 범위 A).

## 현재 위치

**다음 설계: 자동 확인 도구 결정 (플랜 모드부터).** 명세·결정할 것: [checklist.md](checklist.md) "단위별 남은 상세 설계"의 첫 미완료 항목, [open-questions.md](open-questions.md) C2(확인 대상 후보 포함). 참고 자료: [`dev/design/diagram-component-design.md`](../design/diagram-component-design.md)(실패 처리의 콘솔 오류 검사·사본 일치), [`dev/impl/README.md`](../impl/README.md) "실행 환경" 스모크 절차.

## 시작하기 — 새 세션 진입점

> ⚠️ 설계 하나도 코드처럼 **플랜 모드부터** 시작한다. 플랜에 설계 초안을 담아 검수·승인받은 뒤 설계 문서로 옮겨 쓴다.

읽는 순서:
1. 이 README — 현재 위치, 진행 방식
2. [overview.md](overview.md) — 목적·구성요소·배치 기준
3. [checklist.md](checklist.md) — 작업할 단위 고르기(위에서부터) + 역전파 체크리스트
4. [open-questions.md](open-questions.md) — 그 단위에 걸린 결정·실측
5. `project-memory/` ([index](../../project-memory/index.md)) — 결정·함정
6. [`dev/design/map.md`](../design/map.md)와 공용 참조(용어집·공용 도식 모델), 이미 있으면 그 단위의 설계 문서

> 사용자의 한 줄 지시 **"dev/plan/README.md를 읽고, 다음 설계 진행해줘."**만으로 위 순서가 성립해야 한다.

## 폴더 구성

| 폴더 | 역할 | 무엇의 단일 소스인가 |
|---|---|---|
| `dev/plan/` | 개요·확정 결정·앞단 진행 관리 (설계 문서는 두지 않는다) | 목적·확정 결정·앞단 진행 상태 |
| `dev/design/` | 설계 지도 + 단위별 상세 설계 + 공용 참조 | **설계** |
| `dev/impl/` | 구현 진행 관리 (코드는 루트 `index.html`·`lessons/`·`assets/`) | "어디까지 만들었나" |
| `dev/evidence/` | 실측 증거 | 근거 |
| `project-memory/` (루트) | 결정·함정·개발 로그 | 왜 그렇게 정했나 |

## 진행 방식 — 설계 세션 하나 (가이드 §0-3·§7)

```
 1. 맥락 잡기      이 README → overview → checklist → open-questions → map·공용 참조
 2. 플랜 모드      조사(+필요한 실측) → 사용자 결정은 텍스트로 한 번에 한 개씩(CLAUDE.md "플랜 모드 — 사용자 결정 진행 방식") → 플랜에 설계 초안 → [플랜 검수] → 승인
 3. 설계 문서      dev/design/<개념>-design.md (가이드 §8-5 골격) — 이름은 이때 정해 map.md "참조"에 적는다
 4. 문서 검수      독립 검수자 → NO-GO면 수정 → 재검수, GO까지 (재검수는 직전 지적 해소 + 회귀만)
 5. 역전파         checklist.md 맨 위 체크리스트 — map.md·overview·open-questions·README 커리큘럼 표
 6. 기록           checklist.md 항목 [x] + 한 단락 요약·링크, 비자명한 결정·함정은 project-memory/
 7. 커밋·푸시      설계 문서·역전파 문서·요약·기록을 GO 뒤 한 커밋으로
 8. 핸드오프 점검  맥락 없는 서브에이전트에 "dev/plan/README.md를 읽고, 다음 설계 진행해줘." → 결과를 아래 "점검 기록"에 남겨 추가 커밋
```

- **문서 검수 확인 항목**: 설계 문서가 R1~R8·사용자와 합의한 내용·open-questions 해소 결과와 일치하는가, 용어가 용어집과 일치하는가(용어를 추가했다면 원고 출처 대조), 역전파 누락이 없는가.
- **검수자**: 맥락 없는 서브에이전트, Opus 5.5 (`project-memory/decisions/reviewer.md`). 실제 실행 모델을 기록한다.
- **설계 수호**: 추론은 확인받고(R3), 설계는 의논 없이 바꾸지 않는다. 진행 방식(문서 배치·ID·백로그 구성)은 에이전트가 정해도 된다 — 경계는 `project-memory/decisions/dev-process.md`.
- **Design → Impl 게이트**: checklist "남은 상세 설계" 전건 `[x]`, 외부 리뷰 보강 반영, open-questions 해소 또는 preflight·구현 단계로 이관, 역전파 grep 잔존 0, 그리고 "구현 준비 상태 점검" 세션(가이드 §0-6) — 그 뒤 `dev/impl/README.md`가 진입점이 된다.

## 원천 자료

- 프로세스: [`dev/LONG_TERM_DEV_PROCESS.md`](../LONG_TERM_DEV_PROCESS.md) (사용자 제공, git-guide 적용본)
- 용어 근거: Pro Git 한국어판 원고 <https://github.com/progit/progit2-ko> 커밋 `f50647da032bf210ef91802290d60d05da1a9416`
- 릴리즈 관리: <https://github.com/amurtare/release_management_guide> → [`docs/RELEASE_MANAGEMENT.md`](../../docs/RELEASE_MANAGEMENT.md)

## 실측 근거

| 날짜 | 대상 | 결과 |
|---|---|---|
| 2026-10-13 | 세션에서 태그 push | 403 — 세션 git 프록시가 거부. 릴리즈는 GitHub Actions가 만든다 |
| 2026-10-14 | git-scm.com | 접근 불가(ENOTFOUND). Pro Git 원고는 GitHub에서 클론 |
| 2026-10-14 | 용어집 출처 대조 | 고정 커밋 원고와 대조, 누락 0 |
| 2026-10-21 | `file://` (Chromium 141) | `fetch`·XHR·ES 모듈 막힘, 일반 `<script src>`는 됨 — [`dev/evidence/2026-10-21-file-scheme.md`](../evidence/2026-10-21-file-scheme.md). Firefox·Safari 미측정 |

미실측 가정은 [open-questions.md](open-questions.md) "확보할 자료·실측".

## 주의 — 폐기된 초기 가설 (되살리지 말 것)

- ~~학습자가 명령을 실행하는 실습~~ → 학습자는 Git을 쓰지 않고 개념만 배운다(R5). 근거: 사용자 정정 2026-10-14, `project-memory/decisions/learning-scope-and-terms.md`
- ~~쉬운 말로 용어를 대체("기록하기", "준비 영역")~~ → 용어는 Pro Git 한국어판 그대로(R6). 근거: 같은 결정 문서
  - 주의: 2026-10-19의 R8("한글 표현 (원고 표기)" **병기**)은 이 폐기안과 다르다 — 공식 용어를 대신하지 않고 함께 적는다. 근거: `project-memory/decisions/term-notation.md`
- ~~0단계 장면 설계를 0단계 구현 때 함께 한다(A5의 a안)~~ → 모든 단위 설계 후 구현(설계 완료 범위 A). 근거: 사용자 위임 2026-10-14, `project-memory/decisions/dev-process.md`
- ~~"커밋 그래프" 표기~~ → "커밋 히스토리"(원고 표기). 근거: 커밋 `39dc587`·`c7cb0bc`

- ~~단계 이름 "병합"·"리베이스"~~ → "병합 (Merge)"·"커밋 다시 쌓기 (Rebase)"(R8). 근거: [`dev/design/curriculum-scope-design.md`](../design/curriculum-scope-design.md) 결정 근거 Q7

(구현 Phase 1/2 분할은 폐기가 아니라 [`dev/impl/checklist.md`](../impl/checklist.md)에 초안으로 보존했다.)

## 점검 기록

- 2026-10-27 U-diagram 공용 도식 컴포넌트 구현 구분(커밋 `958e1ab`) — Design 진입("dev/plan/README.md를 읽고, 다음 설계 진행해줘.") 통과: "자동 확인 도구 결정"을 플랜 모드로 짚고 C2·확인 대상 후보·실측 필요를 찾음, 지운 ID(A1·A3·A4·A5·B1·C1) 비대상, git 깨끗·원격과 같음. 고친 곳: progress 로그 제목, 진행 방식의 질문 문구(CLAUDE.md와 맞춤), checklist 자동 확인 도구 항목에 산출물 형태 메모
- 2026-10-19 커리큘럼 단계별 범위 확정(커밋 `454e91d`) — Design 진입("dev/plan/README.md를 읽고, 다음 설계 진행해줘.") 통과: `U-diagram`을 플랜 모드로 짚고 B1·`file://` 실측·A6 조건, 지운 ID(A1·A3·A4·A5·C1) 비대상, git 깨끗·원격과 같음 확인. 고친 곳: checklist U-diagram의 B1을 "이관 가능"으로 open-questions와 맞춤
- 2026-10-14 `dev/` 재배치(커밋 `fe95fde`) — Design 진입("dev/plan/README.md를 읽고, 다음 설계 진행해줘.")·Impl 진입("dev/impl/README.md를 읽고, 다음 단계 진행해줘.") 모두 통과(5/5): 둘 다 "커리큘럼 단계별 범위 확정"을 플랜 모드로 짚음. 고친 곳: `curriculum-foundations.md` 진행 상황 주석에 A4 추가
