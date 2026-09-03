# EzPCR — working conventions

Single-file offline tool: `PCR Narrative Builder v1.html` assembles a PCR narrative from a
keyboard-driven worksheet for paste into emsCharts. `index.html` only redirects to it.

## Source of truth and data-first editing
- `PCR Narrative Standard DRAFT v0.10.md` is authoritative. Any wording, option, or
  structure change lands in the MD first; the builder's DOC then mirrors it exactly.
- The DOC is the one-line JSON on the line beginning `window.__DOC__ =` in the HTML. Never
  hand-edit it: parse with Python (`json.loads` between `=` and the trailing `;`), mutate,
  `json.dumps(obj, ensure_ascii=False, separators=(",", ":"))`, write back on the same
  line, and confirm it still parses. `STUB_DOC` below it is a dev fixture — ignore it.
- Never change field ids, line ids, block ids, or `carry` keys; escalation `carry` maps and
  `DEFAULTS` reference them.
- Version markers move together: MD title + filename, `#version-tag` in the HTML header,
  `DOC.meta.source`. Record every ruling in MD §28 REVISION HISTORY with a date.

## Hard runtime rules
- No `localStorage` (sessionStorage drafts only), no network calls, no PHI persistence,
  light mode only, Firefox + Chrome on the rig laptop. `grep -c localStorage` must stay 0.
- ES5-style JS matching the file; keep everything in the single HTML file.

## Engine map (names, not line numbers)
- Assembly: `assemble` (dry pass for twin suppression) → `assembleOnce` → `renderSection`
  → `renderLine` (gates: `lineEligible`, `lineHidden`, twin `ctx.suppressed`,
  `lineAccepted`) → `renderParts` / `renderFill` / `renderChoice` / `renderSum` /
  `renderAox`. `paragraphs()` buckets rows by `paraOrder(ctx)` (tokens `p1..p4` and
  `owner:<id>`). Open items: `noteMissing` / `noteLineLevel` → `buildOpenIndex` →
  `openCounts` → `paintCopyLabel` / `doCopy`.
- Worksheet: `renderWorksheet` → `shellSection` / `ownerBox` / `dispositionSection` →
  `renderUnit` → `unitWrap` + `lineRow` (+ `twinChip`) → `lineFields` / `partFields`
  (each entry carries `depth`) → `fieldNode` / `sumFieldNode`. Edits: `setValue`,
  `onFormEdit` (value edit), `structuralEdit` (full rerender).
- Draft state: `values`, `forks`, `esc`, `attested`, `naSections`, `disposition`,
  `hidden`, `showAnyway`, `topOrder`, `lineOrder`, `paraOverrides`. Indexes: `LINE_INDEX`,
  `TWIN_OF` (from `DOC.meta.twins`), `FORK_PARENT`, `PART_INDEX`.
- Part types: `{f}` fill, `{c, id}` choice (scored when options are `{label, v, emit?}`
  with `score:true`), `{sum:[ids], id, suffix}` computed read-only, `{aox}`, `{g}`.

## Verifying a change
- Preview: `.claude/launch.json` config `pcr-builder` serves the clone on :8791; agent
  worktrees are reachable at `/.claude/worktrees/<name>/PCR%20Narrative%20Builder%20v1.html`.
- Drive state from the console: mutate `state.drafts[state.activeDraft].values`, call
  `structuralEdit()`, read the preview and `lastAsm` (`.suppressed`, `.missing`).
- Syntax: extract the last `<script>` block and `node --check` it. A vm + DOM-stub harness
  loading the script with `el()` stubbed is the pattern for byte-identity assertions.

## Workflow
- Every change: branch off `main` → PR → Alex merges. Direct pushes to `main` are blocked.
- Stacked PRs are fine; after a parent merges, rebase the child onto `main` and retarget.
  A DOC/MD data change must ship with (or before, but never long before) its engine PR.
