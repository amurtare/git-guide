# Visualization Pattern Catalog

A reference for effective HTML representations by content type.

> **Relationship to SKILL.md**: the "Design quality floor" in SKILL.md is **mandatory** — the snippets in this file are the building blocks you use to satisfy it (fonts, paper grain, glass nav, scroll reveal, section headers, SVG chain, code chrome). Only the *category patterns* (kanban, deck, editor, etc.) are optional inspiration. A short source document does NOT exempt you from the floor.

Original source: <https://thariqs.github.io/html-effectiveness/>
Local copies: `references/examples/*.html` (20 examples + `_index.html`).
**For specific implementation details, read the actual file** — code is more precise than descriptions.

---

## Common design principles

Five patterns that recur across every effective visualization:

1. **Hierarchical information architecture**: Meta → TL;DR → body → appendix (actions/glossary). Scannable header depth.
2. **Color-coded semantic badges**: Compress state into small chips (Blocking/Nit/Safe, SEV-2, +/− …).
3. **Anchors + inline jump links**: Shorten long documents with TOCs and `file:line` references.
4. **Copy/export calls-to-action**: Put a "Copy markdown/diff/JSON/SVG" button on almost every editor surface.
5. **OKLCH phase palette with `--c`/`--c-soft` injection**: Five phase colors assigned per-card via inline styles; all CSS references `var(--c)`. Dark mode inverts surface/ink tokens through the same variables.

---

## Patterns by category

### Exploration & planning (PLAN.md, design docs)

- **Side-by-side comparison** ([code-approaches](https://thariqs.github.io/html-effectiveness/01-exploration-code-approaches.html)): 2–3 approaches stacked vertically + Pro/Con table + inline metric badges (`Bundle impact`).
- **Light/dark design compare** ([visual-designs](https://thariqs.github.io/html-effectiveness/02-exploration-visual-designs.html)): 4 directions × Light/Dark toggles, subtle animations.
- **Milestones → data flow → mockups → code** ([implementation-plan](https://thariqs.github.io/html-effectiveness/16-implementation-plan.html)): Progress badges, risk/mitigation 2-column table, threaded comments.

### Code review (REVIEW.md, PR notes)

- **Annotated PR** ([annotated-pr](https://thariqs.github.io/html-effectiveness/03-code-review-pr.html)): Overview → risk map → file list. Inline line annotations + Blocking/Nit/Safe badges.
- **PR writeup** ([pr-writeup](https://thariqs.github.io/html-effectiveness/17-pr-writeup.html)): TL;DR → Why → File-by-file → Test plan → Rollout. `file:line` references, ±line-count badges, Before/After tables.
- **Module map** ([module-map](https://thariqs.github.io/html-effectiveness/04-code-understanding.html)): Diagram → 5-step call-stack walkthrough. `<details>` toggles fold source.

### Design system

- **Living design system** ([design-system](https://thariqs.github.io/html-effectiveness/05-design-system.html)): Color/type/spacing/shadow/component hierarchy + live buttons, inputs, badges.
- **Component variants sheet** ([component-variants](https://thariqs.github.io/html-effectiveness/06-component-variants.html)): 6-variant grid + padding/border/shadow sliders for live tuning + hover-reveal Props code.

### Prototyping

- **Micro-interaction sandbox** ([animation](https://thariqs.github.io/html-effectiveness/07-prototype-animation.html)): Click checkbox → fill → draw check → strike-through → shrink. Spring easing.
- **Drag-and-drop flow** ([interaction](https://thariqs.github.io/html-effectiveness/08-prototype-interaction.html)): Reorder sidebar list, snap when crossing the midline. ~40 lines of vanilla JS.

### Diagrams

- **SVG sheet** ([svg-illustrations](https://thariqs.github.io/html-effectiveness/10-svg-illustrations.html)): Three 720×320 SVGs + individual Download buttons. 5-color palette, consistent corner radius.
- **Clickable flowchart** ([flowchart](https://thariqs.github.io/html-effectiveness/13-flowchart-diagram.html)): Click a node → panel with runtime/duration/failure modes. Rect = process, diamond = decision.

### Decks, research & reports

- **Arrow-key slide deck** ([deck](https://thariqs.github.io/html-effectiveness/09-slide-deck.html)): Left/right arrow nav, 1/6 counter, big-number metrics.
- **Feature explainer** ([feature-explainer](https://thariqs.github.io/html-effectiveness/14-research-feature-explainer.html)): TOC + 4-stage expand + 3-column code compare + FAQ.
- **Concept simulator** ([concept-explainer](https://thariqs.github.io/html-effectiveness/15-research-concept-explainer.html)): Linear learning flow + interactive simulator (hash-ring add/remove/reset) + comparison table + glossary.
- **Weekly status report** ([status](https://thariqs.github.io/html-effectiveness/11-status-report.html)): Big-number KPI header + Shipped table + daily heatmap.
- **Incident report** ([incident](https://thariqs.github.io/html-effectiveness/12-incident-report.html)): Meta chip row (SEV-2/state/owner) → TL;DR → timeline → root cause → impact → actions.

### Custom editors

- **Triage board** ([triage-board](https://thariqs.github.io/html-effectiveness/18-editor-triage-board.html)): Now/Next/Later/Cut kanban + DnD + tag filter + "Copy as markdown" export.
- **Feature flag editor** ([feature-flags](https://thariqs.github.io/html-effectiveness/19-editor-feature-flags.html)): Toggles + auto-updating dependency warnings + Copy diff / Copy full JSON + "Pending changes (n)" counter.
- **Prompt tuner** ([prompt-tuner](https://thariqs.github.io/html-effectiveness/20-editor-prompt-tuner.html)): Left edit / right live preview + `{{slot}}` syntax + token count + Copy prompt.

---

## Reusable snippets

> **Note on example labels**: Text like "Step 1", "Todo item", "PRs merged" in the snippets below are structural placeholders. Translate all UI-facing text to the user's conversation language per SKILL.md.

> **Note on example files**: The 20 files in `examples/` use a legacy palette (`--ivory`, `--clay`, `--olive`). Use them for structural patterns only; the snippets below define the authoritative design tokens.

### Foundation: color & type tokens

```css
/* ── FONTS — ALWAYS include the Google Fonts <link> in <head> (see SKILL.md) ──
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
   <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&family=IBM+Plex+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
   The fallback stacks below (ui-serif, system-ui, ui-monospace) stay in the
   font-family declarations so the page degrades gracefully offline. */

:root {
  /* ── Surfaces ── */
  --bg:           oklch(0.95 0.02 85);
  --bg-deep:      oklch(0.91 0.025 80);
  --surface:      oklch(0.985 0.012 88);
  --surface-alt:  oklch(0.97 0.018 85);
  --surface-glass:oklch(0.99 0.008 90 / 0.62);

  /* ── Ink ── */
  --ink:          oklch(0.18 0.03 245);
  --ink-soft:     oklch(0.36 0.025 245);
  --ink-muted:    oklch(0.55 0.02 245);
  --ink-line:     oklch(0.85 0.02 80);

  /* ── Phase palette (5 hues) ── */
  --p1: oklch(0.62 0.14 48);   /* terracotta */
  --p2: oklch(0.56 0.13 148);  /* moss       */
  --p3: oklch(0.66 0.16 85);   /* saffron    */
  --p4: oklch(0.48 0.14 320);  /* mulberry   */
  --p5: oklch(0.50 0.09 200);  /* verdigris  */

  --p1-soft: oklch(0.93 0.05 50);   --p1-dark: oklch(0.44 0.10 48);   --p1-muted: oklch(0.70 0.07 48);
  --p2-soft: oklch(0.93 0.04 148);  --p2-dark: oklch(0.38 0.09 148);  --p2-muted: oklch(0.64 0.07 148);
  --p3-soft: oklch(0.94 0.06 85);   --p3-dark: oklch(0.48 0.11 85);   --p3-muted: oklch(0.74 0.08 85);
  --p4-soft: oklch(0.92 0.04 320);  --p4-dark: oklch(0.30 0.10 320);  --p4-muted: oklch(0.56 0.07 320);
  --p5-soft: oklch(0.93 0.03 200);  --p5-dark: oklch(0.32 0.06 200);  --p5-muted: oklch(0.58 0.05 200);

  /* ── Geometry ── */
  --r-lg:   18px;
  --r-md:   12px;
  --r-sm:   6px;
  --r-pill: 999px;

  /* ── Elevation (5 tiers) ── */
  --e1: 0 1px 2px oklch(0.20 0.03 245 / 0.05), 0 1px 3px oklch(0.20 0.03 245 / 0.04);
  --e2: 0 2px 4px oklch(0.20 0.03 245 / 0.05), 0 4px 12px oklch(0.20 0.03 245 / 0.06);
  --e3: 0 4px 8px oklch(0.20 0.03 245 / 0.06), 0 12px 28px oklch(0.20 0.03 245 / 0.08);
  --e4: 0 6px 14px oklch(0.20 0.03 245 / 0.08), 0 24px 48px oklch(0.20 0.03 245 / 0.10);
  --e5: 0 12px 24px oklch(0.20 0.03 245 / 0.12), 0 40px 80px oklch(0.20 0.03 245 / 0.14);

  /* ── Typography ── */
  --f-display: "Newsreader", ui-serif, Georgia, serif;
  --f-body:    "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif;
  --f-mono:    "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;

  /* ── Motion ── */
  --ease-out:    cubic-bezier(0.22, 1, 0.36, 1);
  --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* ── Dark mode (L−0.18 / C×0.7 derived, hand-tuned) ── */
@media (prefers-color-scheme: dark) {
  :root {
    --bg:           oklch(0.13 0.015 250);
    --bg-deep:      oklch(0.09 0.02 250);
    --surface:      oklch(0.17 0.012 250);
    --surface-alt:  oklch(0.15 0.015 250);
    --surface-glass:oklch(0.17 0.01 250 / 0.62);

    --ink:          oklch(0.92 0.01 90);
    --ink-soft:     oklch(0.75 0.015 90);
    --ink-muted:    oklch(0.55 0.015 90);
    --ink-line:     oklch(0.25 0.015 250);

    --p1: oklch(0.72 0.12 48);   --p2: oklch(0.66 0.11 148);
    --p3: oklch(0.76 0.13 85);   --p4: oklch(0.58 0.12 320);
    --p5: oklch(0.60 0.08 200);

    --p1-soft: oklch(0.22 0.04 50);   --p1-dark: oklch(0.80 0.10 48);   --p1-muted: oklch(0.78 0.06 48);
    --p2-soft: oklch(0.22 0.03 148);  --p2-dark: oklch(0.74 0.09 148);  --p2-muted: oklch(0.72 0.06 148);
    --p3-soft: oklch(0.22 0.04 85);   --p3-dark: oklch(0.84 0.11 85);   --p3-muted: oklch(0.82 0.07 85);
    --p4-soft: oklch(0.22 0.03 320);  --p4-dark: oklch(0.66 0.10 320);  --p4-muted: oklch(0.64 0.06 320);
    --p5-soft: oklch(0.22 0.02 200);  --p5-dark: oklch(0.68 0.06 200);  --p5-muted: oklch(0.66 0.04 200);

    --e1: 0 1px 2px oklch(0 0 0 / 0.15), 0 1px 3px oklch(0 0 0 / 0.12);
    --e2: 0 2px 4px oklch(0 0 0 / 0.18), 0 4px 12px oklch(0 0 0 / 0.15);
    --e3: 0 4px 8px oklch(0 0 0 / 0.20), 0 12px 28px oklch(0 0 0 / 0.18);
    --e4: 0 6px 14px oklch(0 0 0 / 0.22), 0 24px 48px oklch(0 0 0 / 0.20);
    --e5: 0 12px 24px oklch(0 0 0 / 0.25), 0 40px 80px oklch(0 0 0 / 0.22);
  }
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg); color: var(--ink);
  font-family: var(--f-body);
  font-feature-settings: "ss01", "cv11";
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}
::selection { background: oklch(0.56 0.13 148 / 0.25); color: var(--ink); }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
:focus-visible { outline: 2px solid var(--p2); outline-offset: 2px; }
:focus:not(:focus-visible) { outline: none; }
```

### Typography rules

| Family | Variable | Usage | Rules |
|--------|----------|-------|-------|
| Newsreader | `--f-display` | Headings, card titles, numbers, quotes, `<em>` | `font-weight: 500`, decorative use: `font-style: italic` |
| IBM Plex Sans | `--f-body` | Body default | `font-feature-settings: "ss01","cv11"` on body |
| JetBrains Mono | `--f-mono` | Eyebrows, labels, code, tags, stats | Always `0.68–0.78rem`, `text-transform: uppercase`, `letter-spacing: 0.08–0.12em` |

```css
/* Heading scale */
.h-display  { font-size: clamp(1.85rem, 4.2vw, 3.4rem); font-weight: 600; letter-spacing: -0.022em; }
.sec-title  { font-size: clamp(1.75rem, 3.5vw, 2.6rem); font-weight: 500; letter-spacing: -0.02em; }

/* CJK: words must never split mid-word in headings/labels ("설치" → "설/치" is a defect) */
h1, h2, h3, h4, .h-display, .sec-title, .hero-title { word-break: keep-all; }
```

### Card equal-width rule

**Never use** `repeat(auto-fit, minmax(Npx, 1fr))` — the last row stretches when item count isn't a multiple of columns. Always use `repeat(N, minmax(0, 1fr))` + media queries for explicit column switching. `minmax(0, 1fr)` forces true equal width by preventing intrinsic-minimum expansion from `<pre>` etc.

**Breakpoint reference by card count:**

| Cards | Default columns | Breakpoints |
|-------|----------------|-------------|
| 2 | `repeat(2, minmax(0,1fr))` | @600px → `1fr` |
| 3 | `repeat(3, minmax(0,1fr))` | @900px → `1fr` |
| 4 | `repeat(2, minmax(0,1fr))` | @600px → `1fr` |
| 5 | `repeat(3, minmax(0,1fr))` | @800px → `repeat(2,1fr)` · @560px → `1fr` |
| 5 (rail) | `repeat(5, minmax(0,1fr))` | @720px → `repeat(2,1fr)` |
| 7–8 | `repeat(4, minmax(0,1fr))` | @900px → `repeat(2,1fr)` · @560px → `1fr` |

### Color bar accents

Top bar (default — applied via `::before` on cards with `overflow: hidden`):

```css
.card::before { content: ""; position: absolute; top: 0; left: 0; right: 0;
                height: 4px; background: var(--c); }
```

Bottom bar variant (active tab indicator — scales in on activation):

```css
.tab-bar::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0;
                  height: 3px; background: var(--c);
                  transform: scaleX(0); transform-origin: left;
                  transition: transform 0.4s var(--ease-out); }
.tab-bar[aria-pressed="true"]::after { transform: scaleX(1); }
```

Left rail variant (callout/playbook sidebar accent):

```css
.rail-accent::before { content: ""; position: absolute; top: 0; left: 0;
                       width: 4px; height: 100%; background: var(--c); }
```

### Color injection pattern (`--c` / `--c-soft`)

Each card receives its color via inline `style`, and all CSS references `var(--c)`:

```html
<article class="card" style="--c: var(--p1); --c-soft: var(--p1-soft)">
  <!-- card content -->
</article>
```

```css
.card::before { background: var(--c); }      /* top bar */
.card-num     { color: var(--c); }            /* accent number */
.card strong  { color: var(--c); }            /* emphasis */
.card-tag     { background: var(--c-soft); }  /* tinted bg */
```

**Color assignment strategy:**

| Situation | Strategy |
|-----------|----------|
| Ordered cards (steps, phases) | Hue rotation: p1 → p3 → p2 → p5 → p4 |
| Parallel choices (roles, options) | Single section accent or 2-color alternation |
| Condition → result | Unified single accent |
| 6+ items | Cycle dark variants: p1-dark → p2-dark → … (see below) |

**Palette extension rule — never add a 6th hue.** Use the three variant tiers of the existing 5 colors:

| Variant | Formula | Variable | Use |
|---------|---------|----------|-----|
| soft | L+0.31, C×0.34 | `--pN-soft` | Card backgrounds, highlight areas |
| dark | L−0.18, C×0.7 | `--pN-dark` | Completed/final states, strong emphasis |
| muted | L+0.08, C×0.5 | `--pN-muted` | Inactive/secondary states |

**Hue selection**: pick the `--pN` whose hue angle is closest to the desired color. For ink-like tones (hue ~245°), use `--p5` (200°) dark variant.

```css
/* 6+ items — restart cycle with dark tier */
.node-6 { --c: var(--p1-dark); --c-soft: var(--p1-soft); }
.node-7 { --c: var(--p2-dark); --c-soft: var(--p2-soft); }
/* ... */
```

### Semantic badge system

```html
<span class="badge badge--blocking">Blocking</span>
<span class="badge badge--nit">Nit</span>
<span class="badge badge--safe">Safe</span>
<style>
.badge { font: 600 11px/1 var(--f-mono); padding: 3px 8px;
         border-radius: var(--r-pill); letter-spacing: .03em; }
.badge--blocking { background: var(--p1-soft); color: var(--p1-dark); }
.badge--nit      { background: var(--p3-soft); color: var(--p3-dark); }
.badge--safe     { background: var(--p2-soft); color: var(--p2-dark); }
</style>
```

### KPI header (status reports, postmortems)

Card style with top color bar + shadow. Each item gets its accent via `--c` injection.

```html
<div class="kpi-row">
  <div class="kpi-item" style="--c: var(--p2)">
    <b>14</b><span>PRs merged</span>
  </div>
  <div class="kpi-item" style="--c: var(--p3)">
    <b>92%</b><span>green builds</span>
  </div>
</div>
<style>
.kpi-row { display: flex; gap: 1rem; flex-wrap: wrap; }
.kpi-item {
  background: var(--surface); border-radius: var(--r-md);
  padding: 1rem 1.4rem; box-shadow: var(--e1);
  position: relative; overflow: hidden; min-width: 130px;
}
.kpi-item::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0;
  height: 3px; background: var(--c, var(--p2));
}
.kpi-item b { font: 600 1.8rem/1 var(--f-display); display: block; color: var(--c, var(--p2)); }
.kpi-item span { font: 500 0.65rem/1 var(--f-mono); color: var(--ink-muted);
                 text-transform: uppercase; letter-spacing: .08em; display: block; margin-top: 6px; }
</style>
```

### "Show source" toggle (via `<details>`)

```html
<details class="source">
  <summary>show source · auth/session.ts</summary>
  <pre><code>export function createSession(...) { ... }</code></pre>
</details>
<style>
.source { background: var(--surface); border-radius: var(--r-md); margin: 8px 0; }
.source summary { cursor: pointer; font: 500 12px var(--f-mono);
                  color: var(--ink-muted); padding: 8px 12px; }
.source pre { margin: 0; padding: 0 12px 12px; }
</style>
```

### Arrow-key slide deck

```html
<div id="deck">
  <section>Slide 1</section>
  <section hidden>Slide 2</section>
  <section hidden>Slide 3</section>
</div>
<aside id="counter">1 / 3</aside>
<script>
const s = [...document.querySelectorAll('#deck section')]; let i = 0;
const show = n => {
  s.forEach((e, k) => e.hidden = k !== n);
  counter.textContent = `${n+1} / ${s.length}`;
};
addEventListener('keydown', e => {
  if (e.key === 'ArrowRight') show(i = Math.min(i+1, s.length-1));
  if (e.key === 'ArrowLeft')  show(i = Math.max(i-1, 0));
});
</script>
<style>
#deck section { padding: 40px; min-height: 60vh; }
#counter { position: fixed; top: 16px; right: 20px; color: var(--ink-muted);
           font: 500 12px var(--f-mono); }
</style>
```

### Sidebar + content layout (searchable)

Sidebar contains **only** a small context label (e.g. "이 페이지", "On this page") + nav TOC. Do NOT add logo, brand name, project title, or version text — the sidebar is a navigation aid, not a branding area. Do NOT set a background color on the sidebar; let it inherit the page background. Do NOT use `border-right` or `gap` to separate sidebar from content — sidebar and content sit flush (gap: 0). Page margin lives on the outer `.layout` container, not between sidebar and content.

```html
<div class="layout">
  <aside class="sidebar">
    <div class="sidebar-label">On this page</div>
    <nav id="toc"><!-- TOC --></nav>
  </aside>
  <main><!-- Body --></main>
</div>
<style>
.layout { display: grid; grid-template-columns: 240px 1fr; gap: 0;
          max-width: 1200px; margin: 0 auto; padding: 0 2rem; }
.sidebar { position: sticky; top: 16px; align-self: start; padding-right: 1rem; }
.sidebar-label { font: 500 0.68rem/1 var(--f-mono); text-transform: uppercase;
                 letter-spacing: 0.08em; color: var(--ink-muted); margin-bottom: 1rem; }
.sidebar nav a {
  display: block; padding: 6px 10px; margin-bottom: 2px;
  font-size: 0.82rem; color: var(--ink-soft); text-decoration: none;
  border-left: 3px solid transparent; border-radius: 0;
  transition: all 0.2s var(--ease-out);
}
.sidebar nav a:hover { color: var(--ink); border-left-color: var(--ink-line); }
.sidebar nav a.active { color: var(--accent, var(--p1)); border-left-color: var(--accent, var(--p1)); font-weight: 600; }
@media (max-width: 800px) { .layout { grid-template-columns: 1fr; }
  .sidebar { padding-bottom: 16px; } }
</style>
```

### Card grid (color by `--c` injection)

```html
<div class="grid">
  <article class="card" style="--c: var(--p2); --c-soft: var(--p2-soft)">
    <header><h3>Title</h3><span class="badge badge--safe">Done</span></header>
    <p>Body</p>
  </article>
</div>
<style>
.grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
@media (max-width: 900px) { .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 560px) { .grid { grid-template-columns: 1fr; } }
.card { background: var(--surface); padding: 16px; border-radius: var(--r-lg);
        position: relative; overflow: hidden; box-shadow: var(--e1);
        transition: transform 0.3s var(--ease-out), box-shadow 0.3s var(--ease-out); }
.card::before { content: ""; position: absolute; top: 0; left: 0; right: 0;
                height: 4px; background: var(--c, var(--p2)); }
.card:hover { transform: translateY(-2px); box-shadow: var(--e2); }
</style>
```

### Sortable table

```html
<table id="t">
  <thead><tr><th onclick="sort(0)">Name</th><th onclick="sort(1)">Status</th></tr></thead>
  <tbody><!-- ... --></tbody>
</table>
<script>
function sort(col) {
  const tb = document.querySelector('#t tbody');
  const rows = [...tb.rows];
  const asc = tb.dataset.col === String(col) && tb.dataset.dir !== 'asc';
  rows.sort((a, b) => a.cells[col].textContent.localeCompare(b.cells[col].textContent) * (asc ? 1 : -1));
  tb.dataset.col = col; tb.dataset.dir = asc ? 'asc' : 'desc';
  rows.forEach(r => tb.appendChild(r));
}
</script>
<style>
table { width: 100%; border-collapse: collapse; }
th { font: 600 0.72rem/1 var(--f-mono); text-transform: uppercase; letter-spacing: .06em;
     color: var(--ink-muted); text-align: left; padding: 10px 12px; cursor: pointer;
     border-bottom: 2px solid var(--ink-line); }
td { padding: 10px 12px; border-bottom: 1px solid var(--ink-line); }
tbody tr:hover { background: var(--surface-alt); }
</style>
```

### Copy button

```html
<pre><code>code content</code></pre>
<button class="copy-btn" onclick="navigator.clipboard.writeText(this.previousElementSibling.textContent).then(()=>{this.textContent='Copied';setTimeout(()=>this.textContent='Copy',1500)})">Copy</button>
<style>
.copy-btn { font: 500 0.72rem/1 var(--f-mono); padding: 4px 10px;
            background: var(--surface-alt); border: 1px solid var(--ink-line);
            border-radius: var(--r-sm); cursor: pointer; color: var(--ink-muted);
            transition: all 0.2s var(--ease-out); }
.copy-btn:hover { color: var(--ink); border-color: var(--ink-muted); }
</style>
```

### Collapsible (native `<details>`)

```html
<details open>
  <summary>Section title</summary>
  <div>Content</div>
</details>
<style>
details { background: var(--surface); border-radius: var(--r-md);
          padding: 8px 14px; margin-bottom: 8px;
          border: 1px solid var(--ink-line); }
summary { cursor: pointer; font: 500 1rem/1.4 var(--f-display); color: var(--ink); }
</style>
```

### Vertical timeline

```html
<div class="timeline">
  <div class="stop done"><div class="dot"></div><div class="content"><h4>Step 1</h4></div></div>
  <div class="stop active"><div class="dot"></div><div class="content"><h4>Step 2</h4></div></div>
</div>
<style>
.timeline { position: relative; padding-left: 24px; }
.timeline::before { content: ""; position: absolute; left: 7px; top: 0; bottom: 0;
                    width: 2px; background: var(--ink-line); }
.stop { position: relative; margin-bottom: 16px; }
.stop .dot { position: absolute; left: -22px; top: 6px; width: 14px; height: 14px;
             border-radius: 50%; background: var(--bg); border: 3px solid var(--ink-muted); }
.stop.done   .dot { background: var(--p2); border-color: var(--p2); }
.stop.active .dot { border-color: var(--p3); }
</style>
```

### Tabs

```html
<div class="tabs">
  <button class="tab active" onclick="showTab(this,0)">Overview</button>
  <button class="tab" onclick="showTab(this,1)">Details</button>
</div>
<div class="panel active">Overview content</div>
<div class="panel">Details content</div>
<script>
function showTab(btn, i) {
  document.querySelectorAll('.tab').forEach((t, idx) => t.classList.toggle('active', idx === i));
  document.querySelectorAll('.panel').forEach((p, idx) => p.classList.toggle('active', idx === i));
}
</script>
<style>
.tabs { display: flex; gap: 4px; border-bottom: 1px solid var(--ink-line); }
.tab { background: none; border: none; padding: 8px 16px; cursor: pointer;
       font: 500 0.85rem/1 var(--f-mono); color: var(--ink-muted);
       transition: color 0.2s var(--ease-out); }
.tab.active { color: var(--ink); border-bottom: 2px solid var(--c, var(--p2)); }
.panel { display: none; padding: 16px 0; }
.panel.active { display: block; }
</style>
```

### Spring-easing check animation

```html
<label class="check" data-done="false" onclick="this.dataset.done = this.dataset.done==='true' ? 'false' : 'true'">
  <svg viewBox="0 0 24 24" width="20" height="20">
    <path d="M5 12l5 5L20 7" fill="none" stroke="currentColor" stroke-width="2.5"
          stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  <span>Todo item</span>
</label>
<style>
.check { display: inline-flex; align-items: center; gap: 8px; cursor: pointer;
         padding: 6px 12px; border-radius: var(--r-md);
         transition: background .25s var(--ease-spring), color .25s var(--ease-spring); }
.check svg path { stroke-dasharray: 24; stroke-dashoffset: 24;
                  transition: stroke-dashoffset .35s var(--ease-spring) .1s; }
.check[data-done="true"] { background: var(--p2); color: oklch(0.99 0.005 90); }
.check[data-done="true"] svg path { stroke-dashoffset: 0; }
.check[data-done="true"] span { text-decoration: line-through; opacity: .7; }
</style>
```

### Section header (eyebrow + title)

Eyebrow rules (all cognitively load-bearing — never drop any of them):

- **Accent-colored label**: the whole eyebrow text uses the section accent (`color: var(--c)`), not muted ink.
- **English keyword**: even on Korean/CJK pages the eyebrow is a short English keyword (`QUICK START`, `FLOW`, `COMPARE`, `PROMPT`) — mono, uppercase, letter-spaced. It's a typographic device; body text stays in the user's language.
- **Trailing rule line**: `.sec-eyebrow::after` hairline stretches to the right of the label — required.
- **Numbers only for true sequences** (steps/phases the reader follows in order). A 2-section doc, summary, overview, comparison → no number. Default is no number.

```html
<section id="example" style="--c: var(--p2)">
  <div class="wrap">
    <div class="sec-head">
      <div class="sec-eyebrow">Quick start</div>
      <h2 class="sec-title">Heading <em>emphasis</em></h2>
      <p class="sec-sub">Subtitle text.</p>
    </div>
    <!-- section content -->
  </div>
</section>
<style>
section { padding: 5rem 0 4rem; position: relative; }
.sec-head { margin-bottom: 2.5rem; max-width: 44rem; }
.sec-eyebrow { font: 600 0.72rem/1 var(--f-mono); text-transform: uppercase;
               letter-spacing: 0.12em; color: var(--c, var(--p2));
               display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.85rem; }
.sec-eyebrow::after { content: ""; flex: 1; height: 1px; background: var(--ink-line); }
/* sequence variant only: <div class="sec-eyebrow"><span class="num">01</span> Step label</div> */
.sec-eyebrow .num { font-weight: 600; }
.sec-title { font: 500 clamp(1.75rem, 3.5vw, 2.6rem)/1.1 var(--f-display);
             letter-spacing: -0.02em; margin-bottom: 0.85rem; color: var(--ink); }
.sec-title em { font-style: italic; font-weight: 400; color: var(--c, var(--p2)); }
.sec-sub { font-size: 1rem; color: var(--ink-soft); line-height: 1.6; max-width: 38rem; }
</style>
```

### Hover elevation tiers

Three levels of hover lift. Apply via class or inline to any card element:

```css
/* Light lift — subtle cards */
.lift-light {
  transition: transform 0.3s var(--ease-out), box-shadow 0.3s var(--ease-out);
}
.lift-light:hover { transform: translateY(-2px); box-shadow: var(--e2); }

/* Medium lift — prominent cards */
.lift-medium {
  transition: transform 0.3s var(--ease-out), box-shadow 0.3s var(--ease-out);
}
.lift-medium:hover { transform: translateY(-3px); box-shadow: var(--e3); }

/* Full lift — hero/feature cards */
.lift-full {
  transition: transform 0.4s var(--ease-out), box-shadow 0.4s var(--ease-out);
}
.lift-full:hover { transform: translateY(-4px); box-shadow: var(--e3); }
```

### Scroll-reveal animation

```html
<div class="reveal">Content fades in on scroll</div>
<style>
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to   { opacity: 1; transform: translateY(0); }
}
.reveal { opacity: 0; }
.reveal.visible { animation: fadeUp 0.6s var(--ease-out) both; }
.reveal.visible:nth-child(2) { animation-delay: 80ms; }
.reveal.visible:nth-child(3) { animation-delay: 160ms; }
.reveal.visible:nth-child(4) { animation-delay: 240ms; }
.reveal.visible:nth-child(5) { animation-delay: 320ms; }
</style>
<script>
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
</script>
```

### Page shell

```css
body { overflow-x: hidden; position: relative; }
.shell { position: relative; z-index: 2; }
.wrap  { max-width: 1180px; margin: 0 auto; padding: 0 1.5rem; }
@media (min-width: 1280px) { .wrap { padding: 0 2rem; } }
```

### Blockquote / prompt

Left color bar + curly-quote pattern for natural-language prompts and callouts:

```html
<blockquote class="prompt" style="--c: var(--p2)">Prompt or quote text here.</blockquote>
<style>
.prompt {
  padding: 0.85rem 1rem;
  background: oklch(0.97 0.02 85);
  border-left: 3px solid var(--c, var(--p2));
  border-radius: 0 var(--r-sm) var(--r-sm) 0;
  font-family: var(--f-display);
  font-size: 1rem; font-style: italic;
  color: var(--ink); line-height: 1.5;
}
.prompt::before { content: '\201C'; font-size: 1.6rem; color: var(--c, var(--p2));
                  margin-right: 0.15rem; vertical-align: -0.18em; }
.prompt::after  { content: '\201D'; font-size: 1.6rem; color: var(--c, var(--p2));
                  margin-left: 0.15rem; vertical-align: -0.18em; }
@media (prefers-color-scheme: dark) {
  .prompt { background: oklch(0.17 0.015 250); }
}
</style>
```

### Top-level design frame (`.qs-card`) — content shape decided inside

**Rule 1 — the frame is universal**: every top-level block in a section (prompt, code, table, diagram, timeline) is wrapped in a **surface card frame**: surface bg, hairline border, `border-top: 4px solid var(--c)` accent bar, `--r-lg` radius, `--e2` shadow, header row (label + action button). Never place a block bare on the page background, and never drop the card because the content "already has its own shape".

**Rule 2 — the shape inside the frame follows the markdown content**:

| Content in the md | Shape inside the card |
|---|---|
| Text the reader pastes into Claude | `.prompt-window` — dark prompt window (see below): dark title bar with mono `PROMPT · <TYPE>` label + Copy button, dark mono body with syntax tints |
| Shell commands / code | `.code-block` (dark pre + `.code-header` with fence-language tag + ghost Copy) |
| Comparison data | `.tbl-wrap` table |
| Flow / ordered steps | SVG node chain (`.wf-chain` content) |

**The copy button lives inside the window's own header** (prompt window and code block alike). Because of this, the surrounding design frame does NOT get a header row of its own for these blocks — the card is just the frame; label and action belong to the window inside it.

**The frame must stay visible.** The `.qs-card` keeps its surface background and padding on all four sides, so the dark window sits clearly *inside* a light card. Collapsing the card to zero padding — the dark window filling the frame edge-to-edge with the accent bar sitting directly on the window (frame visually gone) — is a defect.

Header rules:

- **Header row only when it earns its place.** A card whose purpose is already obvious from the section header gets **no header row at all** — diagrams and tables usually need none. Add a label only when it carries information the section title doesn't (an instruction like "복사해서 붙여넣기", a scope note). Never invent a label just to fill the pattern.
- **When a label exists, it must mean something — in the user's language.** "복사해서 붙여넣기", "Claude Code 프롬프트", "설치 명령 2줄" are good; the raw code-fence language alone (`TEXT`, `MD`, `BASH`) is a defect — it tells the reader nothing. (Fence-language tags belong only on the inner `.code-header` bars of code blocks.)
- **Action button only when there is something to copy.** The header button exists only for content that is genuinely copy-pasteable as-is (prompt, shell commands, config). Adding a copy button to a diagram / table / timeline card is a defect (what would it copy?). Use the standard `.copy-btn` styling (see "Copy button" snippet) — no special emphasis treatment.

```html
<!-- Claude-directed prompt: card frame (no header row) with the prompt window inside.
     Label + Copy live in the window's own dark header. -->
<div class="qs-card" style="--c: var(--p1)">
  <div class="prompt-window">
    <div class="prompt-window-head">
      <span class="pw-label">PROMPT · TEXT</span>
      <button class="copy-btn" onclick="copyFrom(this,'payload')">Copy</button>
    </div>
    <pre class="prompt-window-body" id="payload">Claude에게 전달할 프롬프트 원문…</pre>
  </div>
</div>

<!-- Shell commands: same card frame (no header row), dark code shape inside -->
<div class="qs-card" style="--c: var(--p3)">
  <div class="code-block">
    <div class="code-header"><span class="code-lang">bash</span><button class="copy-btn">copy</button></div>
    <pre id="cmds">claude plugin marketplace add … --scope user
claude plugin install … -s user</pre>
  </div>
</div>

<style>
.qs-card { background: var(--surface); border: 1px solid var(--ink-line);
           border-top: 4px solid var(--c, var(--p2)); border-radius: var(--r-lg);
           padding: 1.6rem 1.7rem; box-shadow: var(--e2);
           transition: transform 0.45s var(--ease-spring), box-shadow 0.3s var(--ease-out); }
.qs-card:hover { transform: translateY(-4px); box-shadow: var(--e3); }
/* Prompt window — one dark rounded unit: dark header bar + dark body */
.prompt-window { border-radius: var(--r-md); overflow: hidden;
                 border: 1px solid oklch(0.28 0.025 245); }
.prompt-window-head { display: flex; align-items: center; justify-content: space-between;
                      gap: 0.75rem; background: oklch(0.22 0.022 245);
                      padding: 0.55rem 1rem;
                      border-bottom: 1px solid oklch(0.28 0.025 245); }
.pw-label { font: 600 0.7rem/1 var(--f-mono); letter-spacing: 0.12em;
            text-transform: uppercase; color: oklch(0.72 0.02 85); }
.prompt-window-body { background: var(--code-bg); color: var(--code-ink);
                      font-family: var(--f-mono); font-size: 0.82rem; line-height: 1.8;
                      padding: 1.25rem 1.4rem; white-space: pre-wrap; word-break: break-word;
                      margin: 0; }
/* inline emphasis inside the prompt body: step numbers / commands / slash-commands */
.prompt-window-body b    { color: oklch(0.78 0.14 145); font-weight: 600; }  /* step numbers, commands */
.prompt-window-body .hi  { color: oklch(0.80 0.16 75); }                     /* slash-commands, key values */
</style>
```

The window header's `Copy` uses the standard ghost `.copy-btn` styling (see "Copy button" snippet) — dark-context variant: transparent bg, subtle border, light text.

### Dark code block

Terminal/code snapshots on a dark background with syntax highlight tokens. **Never place this bare in a section** — when it is a section's primary block, nest it inside a framed card (see "Framed prompt card" above); standalone use is fine only as a sub-element of an existing card/column layout.

```html
<pre class="code-dark">code content here</pre>
<style>
.code-dark {
  background: oklch(0.16 0.02 245);
  color: oklch(0.86 0.012 90);
  border-radius: var(--r-md);
  padding: 1.2rem 1.35rem;
  font-family: var(--f-mono);
  font-size: 0.78rem; line-height: 1.7;
  white-space: pre-wrap; overflow-x: auto;
}
.code-dark .dim  { color: oklch(0.55 0.012 90); }
.code-dark .key  { color: oklch(0.78 0.14 145); }
.code-dark .hi   { color: oklch(0.80 0.16 75); }
.code-dark .link { color: oklch(0.72 0.14 200); }
</style>
```

### Glassmorphism sticky bar

For sticky navigation or filter bars. Uses `backdrop-filter` for frosted-glass effect:

```css
.sticky-bar {
  position: sticky; top: 0; z-index: 50;
  background: oklch(0.95 0.02 85 / 0.78);
  backdrop-filter: blur(20px) saturate(1.4);
  -webkit-backdrop-filter: blur(20px) saturate(1.4);
  border-bottom: 1px solid oklch(0.85 0.02 80 / 0.5);
}
@media (prefers-color-scheme: dark) {
  .sticky-bar {
    background: oklch(0.13 0.015 250 / 0.78);
    border-bottom-color: oklch(0.25 0.015 250 / 0.5);
  }
}
```

### Corner glow

Radial glow at the card's top-right corner using `var(--c-soft)`. Intensifies on hover. Requires `position: relative; overflow: hidden` on the card (already present in the card grid snippet above). Uses `::after` — coordinate with `::before` (top bar) so they don't conflict.

```css
.card::after {
  content: "";
  position: absolute;
  top: -60px; right: -60px;     /* adjust: -50px to -100px */
  width: 200px; height: 200px;  /* adjust: 160px to 300px */
  background: radial-gradient(circle, var(--c-soft) 0%, transparent 70%);
  filter: blur(20px);
  opacity: 0.5;
  pointer-events: none;
  transition: opacity 0.4s;
}
.card:hover::after { opacity: 1; }
```

| Card size | Glow size | Offset |
|-----------|-----------|--------|
| Small | 160×160 | -50px |
| Medium (default) | 200×200 | -60px |
| Large | 300×300 | -100px |

### Paper grain background

Two `body` pseudo-elements layered under all content. `.shell` must have `position: relative; z-index: 2` (already in page shell snippet). This is part of the SKILL.md quality floor — include it by default; omit only on purely functional dashboards.

Dark-mode handling: `multiply` blackens on dark surfaces, so route blend mode and opacity through tokens and flip them in the dark block (`--grain-blend: screen; --grain-opacity: 0.28`).

```css
:root { --grain-blend: multiply; --grain-opacity: 0.55; }
@media (prefers-color-scheme: dark) {
  :root { --grain-blend: screen; --grain-opacity: 0.28; }
}

/* Ambient gradient */
body::before {
  content: "";
  position: fixed; inset: 0;
  pointer-events: none; z-index: 0;
  background:
    radial-gradient(ellipse 80% 60% at 20% 0%,  oklch(0.66 0.16 85 / 0.10) 0%, transparent 60%),
    radial-gradient(ellipse 70% 50% at 100% 30%, oklch(0.50 0.09 200 / 0.07) 0%, transparent 60%),
    radial-gradient(ellipse 80% 70% at 0% 100%,  oklch(0.48 0.14 320 / 0.06) 0%, transparent 60%);
  mix-blend-mode: var(--grain-blend);
}

/* SVG noise texture */
body::after {
  content: "";
  position: fixed; inset: 0;
  pointer-events: none; z-index: 1;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0.2 0 0 0 0 0.18 0 0 0 0 0.18 0 0 0 0.05 0'/></filter><rect width='100%25' height='100%25' filter='url(%23n)'/></svg>");
  opacity: var(--grain-opacity);
  mix-blend-mode: var(--grain-blend);
}
```

### Interactive SVG node chain (flow centerpiece)

The single highest-impact upgrade for any document containing a flow/pipeline: a horizontal chain of colored SVG nodes with arrow connectors (draw-in animated) and clickable nodes driving a detail panel below. See `ref` usage in SKILL.md quality floor item 8.

Key rules:
- **Use `var(--token)` for every fill/stroke** (works in SVG presentation attributes in modern browsers) so the diagram adapts to dark mode — never hard-code light-theme oklch values.
- Node anatomy: glow halo (`r=36`, `opacity=0.12`, gaussian blur filter) → surface ring (`r=30`, `fill: var(--surface)`, colored stroke) → solid dot (`r=18`, colored fill, `class="wf-node-dot"`) → white number → serif name below → mono EN caption.
- Backbone: full-width dashed `var(--ink-line)` line behind colored arrow connectors (`marker-end` arrowhead, `.wf-line` with `stroke-dasharray`/`dashoffset` draw-in on IntersectionObserver).
- Detail panel: `grid-template-columns: 190px 1fr` — left column = mono stage label + serif name + keyed chip; right = body with `--c`-colored `<strong>`. Clicking a node re-renders the panel and highlights the active dot (`stroke: var(--ink)`).
- Wrap the SVG in an `overflow-x: auto` container with `min-width: 640px` on the SVG so mobile scrolls instead of squashing.

Do NOT simplify the node anatomy (e.g. a single pastel circle with the label crammed inside) — the layered halo/ring/dot with the serif name **below** the circle is what makes the diagram read as designed. Copy this structure verbatim and adjust coordinates/colors:

```html
<div class="wf-chain" id="wfChain">
  <div class="wf-chain-wrap">
    <svg class="wf-chain-svg" viewBox="0 0 1060 200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="wfArrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
          <path d="M 0 0 L 10 5 L 0 10 z" fill="oklch(0.55 0.02 245)"/>
        </marker>
        <filter id="wfGlow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>
      </defs>
      <!-- dashed backbone behind everything -->
      <line x1="110" y1="100" x2="950" y2="100" stroke="var(--ink-line)" stroke-width="2" stroke-dasharray="4 4"/>
      <!-- colored arrow connectors (draw-in via .wf-line) -->
      <line class="wf-line" x1="148" x2="350" y1="100" y2="100" stroke="var(--p1)" stroke-width="2" marker-end="url(#wfArrow)" opacity="0.7"/>
      <!-- one node: key label above, halo+ring+dot, number inside, serif name + mono caption below -->
      <g class="wf-node" data-i="0">
        <text x="110" y="38" text-anchor="middle" class="wf-node-key" fill="var(--p1)">key label</text>
        <circle cx="110" cy="100" r="36" fill="var(--p1)" opacity="0.12" filter="url(#wfGlow)"/>
        <circle cx="110" cy="100" r="30" fill="var(--surface)" stroke="var(--p1)" stroke-width="2"/>
        <circle cx="110" cy="100" r="18" fill="var(--p1)" class="wf-node-dot"/>
        <text x="110" y="105" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="14" font-weight="600" fill="var(--surface)" style="pointer-events:none">1</text>
        <text x="110" y="155" text-anchor="middle" class="wf-node-name">단계 이름</text>
        <text x="110" y="172" text-anchor="middle" class="wf-node-en">STAGE</text>
      </g>
      <!-- ...repeat per node, cx spaced ~280px apart, hue rotation p1→p3→p2→p5 -->
    </svg>
  </div>
  <div class="wf-chain-detail" id="wfChainDetail"></div>
</div>
```

```css
.wf-chain { background: var(--surface); border: 1px solid var(--ink-line); border-radius: var(--r-lg);
            padding: 1.75rem 1.75rem 1.25rem; box-shadow: var(--e2); }
.wf-chain-wrap { overflow-x: auto; }
.wf-chain-svg { width: 100%; min-width: 640px; height: 200px; display: block; }
.wf-node-dot { cursor: pointer; transition: r 0.25s var(--ease-spring); }
.wf-node-dot:hover { r: 22; }
.wf-node-name { font-family: var(--f-display); font-size: 17px; font-weight: 500; fill: var(--ink); }
.wf-node-en   { font-family: var(--f-mono); font-size: 9px; fill: var(--ink-muted); letter-spacing: 0.08em; }
.wf-node-key  { font-family: var(--f-mono); font-size: 10px; letter-spacing: 0.04em; }
.wf-line { stroke-dasharray: 150; stroke-dashoffset: 150; transition: stroke-dashoffset 0.35s var(--ease-out); }
.wf-line.drawn { stroke-dashoffset: 0; }
.wf-chain-detail { margin-top: 1.5rem; padding: 1.4rem 1.6rem; background: var(--surface-alt);
                   border-radius: var(--r-md); border-left: 4px solid var(--c, var(--p2));
                   display: grid; grid-template-columns: 190px 1fr; gap: 1.75rem; min-height: 110px; }
@media (max-width: 700px) { .wf-chain-detail { grid-template-columns: 1fr; } }
.wd-stage { font-family: var(--f-mono); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.08em;
            color: var(--c, var(--p2)); font-weight: 600; margin-bottom: 0.4rem; }
.wd-name  { font-family: var(--f-display); font-size: 1.35rem; font-weight: 500; color: var(--ink); margin-bottom: 0.5rem; }
.wd-key   { font-family: var(--f-mono); font-size: 0.76rem; color: var(--ink-muted); background: var(--surface);
            padding: 0.25rem 0.5rem; border-radius: 4px; border: 1px solid var(--ink-line); display: inline-block; }
.wd-body  { font-size: 0.92rem; line-height: 1.65; color: var(--ink); align-self: center; }
```

```js
// stage data: [{label, en, key, color:'var(--pN)', body}, ...]
const wfChainDetail = document.getElementById('wfChainDetail');
function renderWfStage(i) {
  const s = wfStages[i];
  wfChainDetail.style.setProperty('--c', s.color);
  wfChainDetail.innerHTML = `
    <div>
      <div class="wd-stage">STEP ${String(i+1).padStart(2,'0')} · ${s.en}</div>
      <div class="wd-name">${s.label}</div>
      <div class="wd-key">${s.key}</div>
    </div>
    <div class="wd-body">${s.body}</div>`;
  document.querySelectorAll('.wf-node-dot').forEach((n, k) => {
    n.setAttribute('stroke', k === i ? 'var(--ink)' : 'none');
    n.setAttribute('stroke-width', k === i ? '2.5' : '0');
  });
}
document.querySelectorAll('.wf-node').forEach(g =>
  g.addEventListener('click', () => renderWfStage(Number(g.dataset.i))));
renderWfStage(0);
// draw-in when scrolled into view
const wfLines = document.querySelectorAll('.wf-line');
new IntersectionObserver((es, o) => es.forEach(e => { if (e.isIntersecting) {
  wfLines.forEach((l, i) => setTimeout(() => l.classList.add('drawn'), i * 140)); o.disconnect();
}}), { threshold: 0.3 }).observe(document.getElementById('wfChain'));
```

### HTML skeleton

Boilerplate for new pages. Adapt the `<style>` sections to include only the tokens and components used:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page title</title>
<style>
/* 1. Foundation tokens (:root + dark mode) */
/* 2. Body reset, selection, reduced-motion, focus */
/* 3. Page shell (.wrap) */
/* 4. Section headers (sec-eyebrow, sec-title) */
/* 5. Primitives used (cards, badges, etc.) */
/* 6. Responsive media queries */
</style>
</head>
<body>
<div class="wrap">

  <!-- Hero / header -->

  <section id="section-id" style="--c: var(--p2)">
    <div class="sec-head">
      <div class="sec-eyebrow"><span class="num">01</span> Label</div>
      <h2 class="sec-title">Title <em>emphasis</em></h2>
      <p class="sec-sub">Subtitle.</p>
    </div>
    <!-- content -->
  </section>

  <footer><!-- footer --></footer>

</div>
<script>
// Interactive elements JS
</script>
</body>
</html>
```

### Mermaid diagram (CDN, only when needed)

```html
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<div class="mermaid">
flowchart LR
  A[Start] --> B{Decision}
  B -->|yes| C[Run]
  B -->|no|  D[Stop]
</div>
<script>mermaid.initialize({ startOnLoad: true, theme: 'default' });</script>
```
