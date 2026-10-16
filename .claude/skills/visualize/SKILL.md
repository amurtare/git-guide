---
name: visualize
description: Render input content or a markdown file into a single self-contained HTML file viewable in VS Code Live Preview. Invoked explicitly by the user via /visualize. If an argument is provided, visualize it directly. If no argument, collect candidates (recent .md files, the last assistant markdown block) and ask the user which one to visualize. Output goes to `.viz/<name>.html`. Do NOT use for CSV/JSON charts, slide decks, image generation, or modifying the source markdown.
---

# visualize

Don't merely convert markdown — produce HTML that uses what HTML can do (density, interactivity, spatial layout, navigation) so the reader grasps the work at a glance.

## Step 0: Staleness check (am I a stale cache?)

**This skill document version: `0.5.2`** — kept in sync with the plugin `VERSION` at every release.

Claude Code's skill loader may inject a **session-start snapshot** of this file: even after the plugin updates on disk, the injected copy can lag behind (this applies in ANY repo where the plugin is used). Before doing anything else, verify:

1. List installed versions of this plugin (pick the command for your shell):
   - Bash: `ls ~/.claude/plugins/cache/md-to-html-marketplace/md-to-html/`
   - PowerShell: `ls "$env:USERPROFILE\.claude\plugins\cache\md-to-html-marketplace\md-to-html"`
2. Compare the **highest** version folder there with the version stamped above.
   - **Equal (or cache dir missing** — e.g. running from a repo checkout): proceed normally.
   - **Cache has a newer version**: the copy you were given is stale. (a) Tell the user, in their language: which version you were loaded with vs. which is installed, and that `/reload-plugins` or a new session fixes it permanently. (b) Self-heal for this run: read `<highest-version>/visualize/SKILL.md` from that cache directory and follow **that** document (and its `references/`) instead of this one — stop following this copy.

---

> **Compliance contract — read this first.** This skill has a mandatory design baseline ("Design quality floor", Step 2) and a hard verification gate (Step 2.5). Your output is **not done** until every marker in the Step 2.5 table is literally present in the HTML file — verify by running grep on your own output and fix anything missing. Source length does not waive any of this: a 20-line document gets the same fonts, atmosphere, motion, and SVG centerpiece as a 300-line one. If you follow only one part of this file, follow Step 2.5.

## Core principles

- **Information density**: tables instead of lists, SVG diagrams instead of paragraphs, visual badges instead of plain text
- **Interactivity**: collapsibles, filters, sorting, copy buttons, toggles
- **Spatial layout**: grids, sidebars, cards — more content per screen
- **Navigation**: table of contents, anchors, search box for large documents

## Output language

UI text in the HTML output (labels, statuses, captions, prompts, buttons) must be translated into the **user's current language** — match whatever language the user is using in this conversation. Do not hardcode any single language; detect from the user's messages and translate accordingly. Set `<html lang="...">` to the matching BCP 47 code (e.g. `ko`, `en`, `ja`). Keep code blocks, technical terms, file names, and proper nouns in their original form.

---

## Step 1: Resolve the source

### A. Argument provided — proceed without asking

- **File path or name** (e.g. `PLAN.md`, `.planning/handoff.md`, `~/notes/spec.md`) → use that file
- **Raw markdown text** (multi-line content with headings/checkboxes passed as the argument) → save to `.viz/_input.md` then use

If the file name is ambiguous (no path, multiple matches), ask which one and proceed.

### B. No argument — always ask the user

Do NOT auto-pick. Collect 3–5 candidates and let the user choose.

Candidate sources, in priority order:

1. **`.md` files written or edited by Claude this turn** (highest priority if present)
2. **A long markdown block in the previous assistant message** (>30 lines, or containing headings/checkboxes) — label as "last assistant markdown"
3. **Recently modified `.md` files in the project** (e.g. `PLAN.md`, `handoff.md`, `.planning/**/*.md`) — use `find` or `git diff --name-only HEAD`

Ask using this shape (translated to the user's language):

> Choose what to visualize:
> 1. `PLAN.md` — written this turn
> 2. `handoff.md` — modified 5 minutes ago
> 3. Last assistant markdown block (52 lines)
> 4. Specify a different file or content

If there are zero candidates, ask: "What file or content should I visualize? (e.g. `PLAN.md`, or pass raw markdown)"

---

## Step 2: Write the HTML

### Navigation — ask the user first

If the document will have **3+ sections**, ask the user before writing (in their language, ideally as a single choice prompt):

1. **Include navigation?** — yes / no
2. **If yes, placement**: **top horizontal** (sticky glass bar with section links — patterns.md "Glassmorphism sticky bar") or **left vertical** (sticky sidebar TOC — patterns.md "Sidebar + content layout")

Recommend a default based on content shape: top bar for guide/landing-style pages with few sections, left sidebar for prose-heavy long documents with many sections. Skip the question entirely for documents under 3 sections (no nav). Whichever is chosen, wire up IntersectionObserver active-link tracking.

### Authoring rules

- **Single file**: inline CSS and JS. Exceptions: the Google Fonts `<link>` below (always include) and CDN libraries such as Mermaid or D3 (only when a diagram genuinely needs them)
- **Fonts (always)**: add the Google Fonts link for Newsreader + IBM Plex Sans + JetBrains Mono in `<head>` — the design system's serif display type does not exist in the fallback stacks, and without it output quality visibly collapses. Keep the fallback stacks in the `font-family` declarations for offline viewing.
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  ```
- **Dark mode**: include a `prefers-color-scheme: dark` media query
- **Localized UI**: set `<html lang>` to the user's language and translate all UI text accordingly
- **CJK line breaking**: for Korean (and CJK) pages, apply `word-break: keep-all` to headings, card titles, and short labels (`h1/h2/h3`, `.hero-title`, `.sec-title`, nav links) so words never split mid-word (e.g. "설치" breaking into "설/치" is a defect); keep `overflow-wrap: break-word` on long body/code text
- **Responsive**: must not break on mobile widths

### Design quality floor (mandatory)

The following are **not optional decorations** — they are the baseline for **every** source of ~10 lines or more. A short document is NOT an exemption: a 25-line guide gets the same hero, atmosphere, motion, and centerpiece treatment as a 300-line spec — only the number of sections shrinks, never the design investment per section. "The content is simple, so I kept the page simple" is precisely the failure mode this floor exists to prevent. A page that renders as "clean but flat document" instead of "designed editorial page" is a failure, and you must fix it before finishing.

1. **Page shell + atmosphere**: `.shell`/`.wrap` (max-width **1180px**, not 900px) + paper-grain noise `body::after` + ambient radial-gradient color washes `body::before` (patterns.md "Paper grain background"). In dark mode switch `mix-blend-mode` to `screen` and lower opacity.
2. **Hero**: eyebrow (mono, uppercase, leading rule line) + display serif title with italic `<em>` accent + lede paragraph, each entering with a staggered `fadeUp` animation.
3. **Navigation** (3+ sections): follow the user's choice from "Navigation — ask the user first" above — top horizontal sticky glass bar or left vertical sidebar TOC, both with IntersectionObserver active-link tracking. Omit only if the user declined nav or the document has fewer than 3 sections.
4. **Section headers**: every section uses `.sec-head` (eyebrow + serif `.sec-title` with `em` accent, optional `.sec-sub`), and each section rotates its own accent hue (`--accent`/`--c`: p1 → p3 → p2 → p5 → p4). Eyebrow rules — all three are cognitively load-bearing:
   - **Accent color on the whole label**: the eyebrow text is colored with the section's accent (`color: var(--accent)`), not muted ink.
   - **English keyword label**: even on Korean/CJK pages the eyebrow is a short English keyword (`QUICK START`, `FLOW`, `COMPARE`, `PROMPT`) — mono, uppercase, letter-spaced. Body text stays in the user's language; the eyebrow is a typographic device where Latin reads better.
   - **Trailing rule line**: the eyebrow row ends with a hairline extending to the right (`.sec-eyebrow::after { flex:1; height:1px; background: var(--ink-line) }`) — never omit it.
   - **Numbers**: prefix a number **only** when the sections form a genuinely ordered sequence the reader walks through in order (installation steps, phases). Anything else — including a 2-section doc, summary/overview/comparison sections — gets no number. **Default is no number; when in doubt, no number.**
5. **Motion**: scroll-reveal (IntersectionObserver + `.reveal`/`.visible`, staggered delays) on section heads and card grids; spring-easing hover lift + shadow tier bump on all cards.
6. **Card-grid transformation**: any enumerable content (3+ parallel items — components, options, steps, file lists) becomes a multi-column card grid (`info-card`, `qs-card`) with per-card `--c` injection — never a plain `<ul>`.
7. **Code block chrome**: every code block gets a header bar (language label left, copy button right) on a dark `pre` — not a bare `<pre>` with a floating button.
8. **One bespoke centerpiece**: if the document contains a flow, pipeline, sequence, or architecture, render it as a **custom SVG diagram** (colored nodes, arrow connectors with draw-in animation, clickable nodes driving a detail panel) — not merely a text timeline. This is usually the single element that most separates goal-quality output from a flat page.
9. **Section vertical rhythm**: generous padding (`4.5rem 0 3.5rem` scale), footer with mono metadata. Do NOT add `section + section` border/hairline separators — the eyebrow's trailing rule line already marks each section boundary; a second line between sections is redundant.
10. **Top-level design frame — no exceptions**: every top-level block inside a section — prompt, code block, table, diagram, timeline — sits inside a **surface card frame** (`.qs-card` style: surface background, hairline border, top accent bar `border-top: 4px solid var(--accent)`, `--r-lg` radius, `--e2` shadow, header row with label + action button). A bare block placed directly on the page background is a defect. **The content's shape *inside* the frame is decided by what the markdown content *is***: text the reader pastes into Claude → **prompt window** (`.prompt-window`, patterns.md: one dark rounded unit — dark title bar with mono `PROMPT · <TYPE>` label + Copy button, dark mono body with syntax tints); shell commands / code → dark `.code-block` with `.code-header` chrome (fence-language tag + copy); comparison data → `.tbl-wrap` table; flow → SVG chain. Never strip the outer card because the content already has its own shape, and **the frame must stay visible**: the surface card keeps its own padding on all four sides, so the dark window sits inside a visible surface border — collapsing the card to zero padding (dark window filling the frame edge-to-edge, accent bar sitting directly on the window) is a defect. **Copy buttons live inside the window's own header** (prompt window / code header) — so the design frame around these blocks has no header row of its own. Frame/header rules: **(a)** the frame's own header row is rare — prompt windows and code blocks carry their label + Copy in their own dark headers, and diagrams/tables usually need no header at all. Add a frame-level label **only when it carries information neither the section title nor the inner window gives** (a scope note, a card title in a multi-card grid). Never invent a label to fill the pattern, and never use the raw code-fence language (`TEXT`, `MD`) alone as a label; **(b)** a copy button exists **only for content that is genuinely copy-pasteable as-is** (a prompt, shell commands, config text) and sits **inside the content window's header**, standard `.copy-btn` styling — putting a copy button on a diagram/table/timeline card, or duplicating one on the frame, is a defect.

### Technique table (mix freely)

| Content shape | Treatment |
| --- | --- |
| Many comparable attributes | Sortable / filterable table |
| Ordered steps or phases | Interactive SVG node chain + detail panel (floor item 9); vertical timeline only as a secondary element |
| Items grouped by state | Kanban-style columns (visual grouping; no drag needed) |
| Dependencies or connections | SVG diagram or Mermaid |
| Prose-heavy long document | Sidebar TOC + body + search box |
| Checklists | Progress bar + done/todo badges |
| Code or JSON snippets | Syntax highlight + copy button |
| Parameters or options | Sliders / toggles for live tweaking |
| Categorized items | Tabs or accordion |
| Code review | Annotated diff, severity tags, file-by-file tour |

### References

- `references/patterns.md` — curated catalog: common principles, category patterns, reusable snippets. **Read this first.**
- `references/html-design-guide.md` — full design system rules + component catalog (`.qs-card`, `.fh-card`, `.phase-tab`, `.playbook`, `.role-bar`, etc.). Consult when a specific component is needed.
- `references/index.html` — design reference implementation (172 KB). **Do not load in full.** When you need the exact markup or JS for a specific component, use grep or partial read to extract only that section.
- `references/examples/*.html` — 20 working examples. **If a specific implementation detail is unclear, read the actual file.**

These are not mandatory templates — if a better representation comes to mind, use it.

### Anti-patterns

- HTML that's just a literal markdown rendering (only headings, lists, paragraphs)
- Static pages with no interactivity (single read-only view)
- Presenting key data as prose when a table would convey it better
- Skipping the Google Fonts link — Georgia/system fallbacks destroy the editorial look
- A flat single-column page mirroring the markdown's section order 1:1 when the content could be spatially regrouped (grids, diagram + detail panel)
- No motion at all (no entrance animation, no scroll reveal, no hover response)
- **Inventing blocks the source doesn't have** — e.g. extracting commands out of a prompt into a duplicate "quick reference" card. The markdown's content inventory decides what cards exist; re-shaping content is the job, duplicating it is not (and doing it to satisfy a Step 2.5 marker is doubly wrong — the markers describe treatments for content that exists)

---

## Step 2.5: Self-check after saving (hard gate)

After writing the file, **run grep against your own output file** for each marker below (e.g. `grep -c "fonts.googleapis" <output>.html`). Any required marker at 0 hits means the page fails the gate — edit the file to add it, then re-verify. Do not report completion while any required marker is missing.

| # | Floor item | Marker that must exist in the HTML |
| --- | --- | --- |
| 1 | Google Fonts loaded | `fonts.googleapis.com/css2?family=Newsreader` `<link>` in `<head>` |
| 2 | Paper grain + ambient washes | `feTurbulence` data-URI on `body::after` + `radial-gradient` washes on `body::before` |
| 3 | Wide shell | `max-width: 1180px` (not 720/800/900) |
| 4 | Hero treatment | `.hero-title` in `--f-display` serif with italic `<em>` + eyebrow + `@keyframes fadeUp` staggered entrance |
| 5 | Navigation | per user's choice (top glass bar `backdrop-filter` / left sidebar) — only omissible if <3 sections or user declined |
| 6 | Scroll reveal + hover lift | `IntersectionObserver` + `.reveal`/`.visible` classes; `:hover { transform: translateY(` on cards |
| 7 | Section accent rotation | each `<section>` carries its own `--accent`/`--c` inline style |
| 8 | Code block chrome | `.code-header` bar (lang label + copy button) on every code block — **0 hits is correct when the document has no plain code blocks** (e.g. its only fenced content is a Claude prompt rendered as `.prompt-window`). NEVER fabricate an extra code card, or duplicate content already shown elsewhere, just to satisfy this marker |
| 9 | SVG centerpiece | `<svg` node-chain diagram whenever the source contains a flow / ordered steps / pipeline (a numbered "진행 흐름"-style list **is** a flow — render it as the SVG chain with clickable nodes + detail panel, not as a text timeline) |
| 10 | Top-level frame | every top-level block (prompt/code/table/diagram) wrapped in a surface card frame — `border-top: 4px solid` accent card with header row; inside it, content keeps its md-determined shape (Claude prompt → `.prompt-window` dark terminal-style window, code → `.code-block`); no bare block as a direct child of a section |

Items 2, 4, 6, 9, 10 are the ones most often rationalized away on short documents — they are exactly what separates goal-quality output from a flat page.

---

## Step 3: Save the file

Write to the **same directory as the source file**, using the same basename with `.html` extension.

- `docs/PLAN.md` → `docs/PLAN.html`
- `README.md` → `README.html`
- Inline input (no source file) → `.viz/_input.html` (create `.viz/` if needed)

---

## Step 4: Report

1–2 lines, in the user's language. Include the output path and the chosen treatment (e.g. "table + timeline", "searchable card grid").
Append one line telling the user to right-click the HTML and choose "Show Preview" in VS Code for auto-refresh.

---

## Exceptions

- **Source file missing**: stop and ask.
- **Source under 5 lines with no headings**: warn that there isn't much to visualize and confirm before proceeding.
- **Re-render request**: keep the same source, apply a different treatment without re-resolving.
