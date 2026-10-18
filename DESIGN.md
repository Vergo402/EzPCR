---
name: PCR Narrative Builder
description: A field notebook for writing the chart after the call — cream page, one pencil ink, proposals in italic until accepted.
colors:
  cream-page: "#F7F4ED"
  bright-leaf: "#FCFAF4"
  pencil-ink: "#23201A"
  ink-pressed: "#3A362E"
  pencil-grey: "#5F594C"
  graphite: "#4A463D"
  rule-faint: "#DFD8C9"
  rule-strong: "#948870"
  pencil-rule: "#948870"
  placeholder-grey: "#756D5D"
  erase-tint: "#F2EEE3"
  focus-wash: "#EAE3D0"
  given-green: "#3E6B4F"
  given-green-wash: "#E7EDE4"
  given-green-rule: "#BFD3C5"
  withheld-amber: "#7E6326"
  withheld-amber-wash: "#F3ECD9"
  fired-red: "#A63A2B"
  fired-red-wash: "#F3E3DD"
  fired-red-rule: "#D8B0A4"
  neutral-grey: "#6B655B"
  neutral-grey-wash: "#EFEBE1"
typography:
  brand:
    fontFamily: "Source Serif 4, Iowan Old Style, Charter, Georgia, serif"
    fontSize: "19px"
    fontWeight: 600
    lineHeight: 1.45
  narrative:
    fontFamily: "Source Serif 4, Iowan Old Style, Charter, Georgia, serif"
    fontSize: "14.5px"
    fontWeight: 400
    lineHeight: 1.75
  body:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.45
  section:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "11px"
    fontWeight: 500
    letterSpacing: "0.11em"
    lineHeight: 1.45
  line-label:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "11.5px"
    fontWeight: 400
    letterSpacing: "0.03em"
    lineHeight: 1.45
  field-label:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "11.5px"
    fontWeight: 400
    lineHeight: 1.45
  value:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.45
  control:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.45
  badge:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "11px"
    fontWeight: 500
    lineHeight: 1.45
  pill:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.45
  keyhint:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "11px"
    fontWeight: 400
    lineHeight: 1.45
  keyhint-inline:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "10.5px"
    fontWeight: 400
    lineHeight: 1.45
  counter:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "12.5px"
    fontWeight: 400
    lineHeight: 1.45
rounded:
  none: "0"
  hair: "3px"
  sm: "6px"
  md: "8px"
  pill: "999px"
spacing:
  hair: "2px"
  xs: "4px"
  sm: "6px"
  md: "8px"
  lg: "10px"
  xl: "16px"
  xxl: "20px"
  xxxl: "24px"
components:
  button-secondary:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.pencil-ink}"
    typography: "{typography.control}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "30px"
  button-secondary-hover:
    backgroundColor: "{colors.cream-page}"
    textColor: "{colors.pencil-ink}"
  button-primary:
    backgroundColor: "{colors.pencil-ink}"
    textColor: "{colors.cream-page}"
    typography: "{typography.control}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "30px"
  button-primary-hover:
    backgroundColor: "{colors.ink-pressed}"
    textColor: "{colors.cream-page}"
  button-copy:
    backgroundColor: "{colors.pencil-ink}"
    textColor: "{colors.cream-page}"
    typography: "{typography.control}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "34px"
  button-primary-confirming:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.fired-red}"
  button-danger-ghost:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.fired-red}"
    typography: "{typography.control}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "30px"
  button-danger-ghost-hover:
    backgroundColor: "{colors.fired-red-wash}"
    textColor: "{colors.fired-red}"
  pill:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.pencil-ink}"
    typography: "{typography.pill}"
    rounded: "{rounded.pill}"
    padding: "0 11px"
    height: "25px"
  pill-on:
    backgroundColor: "{colors.pencil-ink}"
    textColor: "{colors.cream-page}"
  pill-proposed:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.pencil-grey}"
  select:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.pencil-ink}"
    typography: "{typography.control}"
    rounded: "{rounded.sm}"
    padding: "0 8px"
    height: "30px"
  input-text:
    backgroundColor: "transparent"
    textColor: "{colors.pencil-ink}"
    typography: "{typography.control}"
    rounded: "{rounded.none}"
    padding: "0 8px"
    height: "30px"
  missing-badge:
    backgroundColor: "{colors.fired-red-wash}"
    textColor: "{colors.fired-red}"
    typography: "{typography.badge}"
    rounded: "4px"
    padding: "2px 9px"
---

# Design System: PCR Narrative Builder

## Overview

**Creative North Star: "The Field Notebook"**

A pocket notebook the medic writes in after the call. The page is cream, the ink is one near-black pencil, and the proposals the builder makes are written faintly in italic until the medic overwrites or accepts them. Nothing on the page competes for attention because nothing on the page is decoration: every mark is either a label, a value, a rule, or a key hint. The narrative preview is the notebook's fair-copy page, set in serif at a reading leading, while the worksheet beside it is the working page in a small sans.

The mood is calm and clerical. Calm: one accent, used only for the two things that interrupt the writing (starting a new call, and the open items that gate Copy — a red chip wherever a field is still missing). Clerical: small uppercase section heads, labels right-aligned in one ledger column with their values beside them, hairline rules between sections, a monospace strip of key hints. Density is deliberate — a 13.5px body and 13.5px values on a laptop put a whole shell section on one screen, and the tool is driven from the keyboard, so rows are tight and controls are short.

Selection is never a new hue. A chosen pill inverts to solid ink on cream; a focused row gains an ink border; a confirmed value turns from faint grey to full ink at weight 500. Clinical meaning, when it exists, borrows the three tones the chart itself uses — given (green), withheld (amber), fired (red) — and only on settled decisions.

**Key Characteristics:**
- One ink: near-black is both the text color and the selection fill; there is no brand blue.
- Proposals are faint italic; acceptance turns them upright, full ink, weight 500.
- Hairline warm-grey rules structure the page; shadows appear only on things that float.
- Serif for what the medic reads (wordmark, narrative); sans for what the medic fills; mono for hints and counts.
- Light mode only, embedded fonts, no motion beyond a 120 ms hover reveal.

## Colors

A warm paper-and-pencil palette: two off-whites, one ink, four greys, and three clinical tones that each carry a wash and a rule.

### Primary
- **Pencil Ink** (#23201A): body text, the top-bar rule, the focus ring, the selected-pill fill, the Copy button, and the preview narrative. It is the accent because inversion to ink is how selection is shown.
- **Ink Pressed** (#3A362E): the hover state of anything filled with ink (Copy, modal primary).

### Neutral
- **Cream Page** (#F7F4ED): the page background, the top bar, the key-hint strip, the status bar, the preview pane's foot strip, and the text color on ink fills and on the modal's red danger button.
- **Bright Leaf** (#FCFAF4): the raised sheet — selects, buttons, pills, the preview pane, popups, the focused row, the modal card.
- **Pencil Grey** (#5F594C): every secondary text — top-bar labels and notes, key hints (strip and in-row), proposed values, auto-filled components in a computed sum, the twin footer, the hidden, twin, and paragraph chips, the version tag.
- **Graphite** (#4A463D): line labels only (the slightly darker label at the head of a row).
- **Rule Faint** (#DFD8C9): the default hairline — section heads, pane borders, the hairline above the preview's foot strip, the left rule on second-level sub-rows and a fork's chosen arm.
- **Rule Strong** (#948870): the control-border floor, at 3:1 or better on both Cream Page and Bright Leaf — select, button, and pill borders, the paragraph badge outline, the dashed border of the hidden and twin chips and the open-detail button, the dotted underline on an unattested default in the preview, and the scrollbar thumb.
- **Pencil Rule** (#948870): the underline of a text input at rest. It now has the same value as Rule Strong, so a control's hover border no longer changes; the two names stay so the input rule and the control border can part ways again.
- **Placeholder Grey** (#756D5D): italic placeholder text in inputs, field labels, idle hint text, the rows of an N/A section, an unattested default in the preview, and the empty preview's placeholder line.
- **Erase Tint** (#F2EEE3): the hover wash on rows, popup rows, preview lines, and pressed buttons; the drop slot while dragging.
- **Focus Wash** (#EAE3D0): the warm highlight behind the preview's focused fragment, and the selection colour for text anywhere on the page (ink text on it).
- **Neutral Grey** (#6B655B) on **Neutral Grey Wash** (#EFEBE1): the N/A toggle when on, the draft switcher track, the draft chip.

### Tertiary (clinical tones)
- **Given Green** (#3E6B4F) with **Given Green Wash** (#E7EDE4) and **Given Green Rule** (#BFD3C5): a treatment given, an open-detail affordance, the handoff button, the "all" A&Ox pill.
- **Withheld Amber** (#7E6326) with **Withheld Amber Wash** (#F3ECD9): a treatment withheld with reason, a paragraph moved from its home, the character counter approaching the cap, the polish banner. Nothing else is amber.
- **Fired Red** (#A63A2B) with **Fired Red Wash** (#F3E3DD) and **Fired Red Rule** (#D8B0A4): an escalation that fired, the New call button, delete affordances on hover, the open-item badge, an open item on the worksheet and its blank in the preview, the counter over the cap, Copy in its confirming state.

### Named Rules
**The One Ink Rule.** Selection, focus, and primary action are all expressed by Pencil Ink — a fill, a border, or a full-strength text color. No hue is introduced to mean "chosen".

**The Settled Tone Rule.** Green, amber, and red appear only on a decision the medic has made (given / withheld / fired) or on a gate the medic must clear (open items, the cap). A proposal is never colored; it is faint and italic.

**The Red Interrupt Rule.** Outside the clinical tones, red is reserved for New call and the open items that gate Copy. An open item is one red chip wherever it appears: a missing field on the worksheet wears the same red-wash chip as its blank in the preview — red text, red wash, a 1.5px red underline, weight 500 (the worksheet's `.ws-amber` state class keeps its old name). Nothing else on the page is red.

## Typography

**Display Font:** Source Serif 4 (with Iowan Old Style, Charter, Georgia) — embedded, 400–600 plus 400 italic
**Body Font:** Archivo (with system-ui) — embedded, 400–500 only
**Label/Mono Font:** ui-monospace, SFMono-Regular, Menlo, Consolas — system stack, not embedded

**Character:** The serif belongs to what is read — the wordmark and the finished narrative at a generous 1.75 leading. The sans belongs to what is filled — compact, two weights, no italic face of its own (italic Archivo is browser-synthesised, and that slight roughness is part of how a proposal reads as "not yet written"). Mono marks the machine's voice: key hints, the version tag, the character counter, computed sums.

### Hierarchy
- **Brand** (600, 19px, serif): the wordmark in the top bar, with the mono version tag baseline-aligned beside it.
- **Narrative** (400, 14.5px, serif, 1.75): the preview text, max 75ch, pre-wrap.
- **Body** (400, 13.5px, sans, 1.45): the default for the page.
- **Section** (500, 11px, sans, 0.11em, UPPERCASE, ink): section names in the worksheet (DISPATCH / RESPONSE / ARRIVAL). The popup group heading is the same idea at 10px / 0.05em.
- **Line label** (400, 11.5px, 0.03em, Graphite): the name at the head of a row, right-aligned in the fixed 8.75rem label column.
- **Field label** (400, 11.5px, Placeholder Grey): the inline "key:" before a value, right-aligned in that same 8.75rem column so every value starts on one edge. Top-bar labels and row notes stay 11px Pencil Grey.
- **Value** (400, 13.5px): the filled text of a field. A settled (accepted) value is ink at 500; a fired escalation is red at 500.
- **Idle hint** (400, 12px, Placeholder Grey): the quiet text of a field nothing has been entered in.
- **Control** (400, 13px): the text inside buttons, selects, and text inputs.
- **Badge** (500, 11px, Fired Red on Fired Red Wash): the open-item count beside Copy.
- **Pill** (400 / 500 on, 12px): option pills and chips; 11px for the N/A toggle and the paragraph badge, 11.5px for the hidden and twin chips.
- **Keyhint** (400, 11px mono, Pencil Grey): the hint strip; 10.5px inside a row.
- **Counter** (400 / 500 when amber or red, 12.5px mono, tabular numerals): the character count against 4,000.

### Named Rules
**The Two-Weight Rule.** The sans has 400 and 500 and nothing heavier. Emphasis beyond 500 is done with ink (color), case, or spacing — never with bold.

**The Italic Means Proposal Rule.** Italic in the worksheet or preview always means "the builder's suggestion, not yet accepted" (proposed values, dashed proposal pills, proposal placeholders, unattested defaults) — or, for the empty preview's one placeholder line, "nothing is written yet". Do not use italic for emphasis or for titles.

## Layout

Two panes on a 1600px-max centered grid: the worksheet (1.06fr) and the sticky preview pane (1fr), gap 16px, padding 16px; at 1100px and up the gap and padding grow to 20px. Below 1100px the panes stack and the preview loses its stickiness. The top bar is sticky at the top (10px 16px padding, flex-wrapped controls pushed right); the status bar is sticky at the bottom. The preview pane sits at top: 66px with a max height of the viewport less 84px; the narrative scrolls inside it while the foot strip stays put.

The worksheet is a column of sections 24px apart. Each section has a head (name left, tools right; 6px padding above the hairline, 6px margin below it), then rows. A row is a flex-wrapped line of label + fields with 3px 8px padding, a 28px minimum height, and a 2px/8px gap, baseline-aligned — focused or not — with a transparent 1px border reserved so focus never shifts layout. Every row's label sits right-aligned in one fixed 8.75rem column with its value beside it, so values share a left edge down the sheet. Continuation rows (a line's later fields, `ws-sub-1`) sit flush, with no indent and no left rule; a second level (`ws-sub-2`) still indents 36px under the 2px rule, and a fork's chosen arm keeps its 14px indent and rule. The twin footer, a row's note, and the in-row key hint all align to the value column. Rows reach a scroll-margin of 78px so keyboard focus lands below the sticky bar.

The spacing scale is small and ad hoc rather than a strict grid: 2, 3, 4, 6, 8, 10, 16, 20, 24px. 6px is the gap inside a control cluster, 8px between controls, 16/20px between panes, 24px between worksheet sections. Control heights step down with importance: 34px for Copy and Polish at the preview's foot; 30px for top-bar selects, buttons, and inputs; 26px for in-row inputs and sub-pills; 25px pills; 24px open-detail buttons; 22px N/A toggle and hidden or twin chips.

## Elevation & Depth

Flat by default. Depth on the page is drawn with rules, tints, and inversion: a hairline under each section head, a 2px left rule on nested groups, an erase-tint wash on hover, an ink border and sheet background on the focused row. Shadows exist only for things that have left the page — popups, a lifted drag, the modal — and they are warm brown (rgb 60,50,30), never black, so they read as paper over paper.

### Shadow Vocabulary
- **Focused row** (`box-shadow: 0 1px 3px rgba(60,50,30,.10)`): the one in-flow shadow; paired with the ink border on the row that has keyboard focus.
- **Active tab** (`box-shadow: 0 1px 2px rgba(60,50,30,.1)`): the selected draft tab in the switcher.
- **Lifted** (`box-shadow: 0 6px 16px rgba(60,50,30,.18)`): a line or section being dragged or keyboard-grabbed.
- **Popup** (`box-shadow: 0 8px 24px rgba(60,50,30,.18)`): the add-block popup and the hidden-items popover.
- **Modal** (`box-shadow: 0 20px 60px rgba(60,50,30,.25)`): the modal card over a warm scrim, `rgba(35,32,26,.38)` — Pencil Ink at 38%, not black.
- **Cursor ring** (`box-shadow: 0 0 0 1.5px #23201A inset`): the pill under the keyboard cursor; and `inset 0 -2px 0` ink as the underline bar on the preview's focused fragment.

### Named Rules
**The Paper-Over-Paper Rule.** Nothing in the document flow casts a shadow except the focused row. A shadow means the element is floating above the page, and it is always warm brown.

## Shapes

Soft, small radii that step with scale: 8px for floating surfaces (popups, the preview pane, the modal), 6px for controls and rows (buttons, selects, the row's focus border, drag handles), 3px for inline fields and preview lines, and full pills (999px) for options, chips, toggles, and the paragraph badge. Text inputs are not boxes at all — a 1.5px underline in Pencil Rule, dashed when the placeholder is a proposal, ink on hover and focus. Round delete and remove controls (50%) sit flush and only reveal on hover.

Borders carry meaning by style: solid hairline for structure, dashed for "offered but not taken" (proposal pills, the open-detail button, the hidden chip, the drop slot, a proposal input's underline), dotted for "unconfirmed" (an unattested preview default, the all-A&Ox pill). The top bar's bottom rule is the only ink-colored line on the page.

## Components

### Buttons
Quiet until it matters: a sheet-colored outline button is the default, and the only filled button on the page is the one that finishes the job.
- **Shape:** 30px tall, softly rounded (6px), 0 12px padding, 13px sans.
- **Secondary (default):** Bright Leaf fill, Rule Strong border, ink text; hover → Cream Page fill (the Pencil Rule border it gains is now the same value as Rule Strong, so only the fill changes); active → Erase Tint.
- **Primary (Copy):** solid Pencil Ink, cream text, weight 500, min-width 176px, 34px tall; hover → Ink Pressed. The label carries the open count ("Copy (1 open)").
- **Primary, confirming:** when Copy is pressed with open items it flips to Bright Leaf with Fired Red text and rule; hover → Fired Red Wash. This is the soft gate.
- **Danger ghost (New call):** outline with Fired Red text and rule; hover → Fired Red Wash. Separated from the rest of the top bar by a hairline divider.
- **Toggle (Polish):** a secondary button, 34px tall beside Copy, that inverts to ink when on.
- **Danger (modal confirm):** Fired Red fill with Cream Page text, not white.
- **Open detail:** 24px, 12px text, Given Green text on a dashed Rule Strong border; hover → green wash and rule.
- **Focus:** a 2px Pencil Ink outline, 2px offset, on every focusable control.

### Pills / Chips
- **Style:** 25px full pills, 0 11px, 12px sans, Bright Leaf on a Rule Strong border.
- **On:** inverts to Pencil Ink with cream text, weight 500.
- **Proposed:** dashed border, Pencil Grey italic — the builder's suggestion.
- **Cursor:** a 1.5px inset ink ring marks the pill the keyboard is on; Enter accepts it.
- **Structural decisions:** the given / withheld / fired / omit options keep their clinical tone when on (green, amber, red, or neutral wash with matching text and rule).
- **Small variants:** N/A toggle (22px, 11px, neutral wash when on); hidden and twin chips (22px, 11.5px, Pencil Grey text on a dashed Rule Strong border); paragraph badge (11px, Pencil Grey on a Rule Strong outline pill — hidden at rest, shown on hover, always shown, in amber, once the paragraph has been moved).

### Cards / Containers
- **Preview pane:** Bright Leaf, 1px Rule Faint border, 8px corners, sticky; the narrative first, then the head strip — draft chip, mono counter, open badge, Polish, and Copy — at the pane's foot on Cream Page under a hairline: read, then copy. The character warning and the Polish banner sit between the text and the foot. Until something is accepted the narrative area holds one italic Placeholder Grey line, "The narrative builds here as you accept fields."
- **Popups:** Bright Leaf, Rule Faint border, 8px corners, popup shadow, 6px padding; rows are 7px 10px with 5px corners and an Erase Tint hover; group heads are 10px uppercase.
- **Modal:** Bright Leaf card on the warm scrim, 8px corners, 20px padding, max 440px, modal shadow; 15px/500 title, 13px Pencil Grey body, actions right-aligned.
- **Worksheet row:** transparent until hovered (Erase Tint) or focused (Bright Leaf, ink border, focused-row shadow); an N/A section's rows turn Placeholder Grey rather than fading.

### Inputs / Fields
- **Text input:** no box — transparent with a 1.5px Pencil Rule (#948870) underline, 30px tall (26px inside a row), 13px sans; italic Placeholder Grey placeholder; hover and focus turn the underline ink. A proposal input has a dashed underline and an italic Pencil Grey placeholder that Enter accepts.
- **Select:** Bright Leaf box, Rule Strong border, 6px corners, 30px; hover → Cream Page fill.
- **Field value states:** idle → 12px Placeholder Grey hint; set → ink at 500; proposed → Pencil Grey italic; open item → the red-wash chip (red text, red wash, 1.5px red underline, 500), the same one a blank wears in the preview; given / withheld / fired → their tone, fired at weight 500.
- **Computed sum:** mono, ink, tabular numerals; faint when empty; auto-filled components Pencil Grey italic.

### Navigation
- **Top bar:** Cream Page, sticky, a 1px Pencil Ink rule beneath — the single strongest line on the page. Serif wordmark with mono version tag at left; unit select, category select, add-block button, draft switcher, and New call at right. Below it a Cream Page mono strip of key hints (11px, Pencil Grey) under a hairline.
- **Draft switcher:** a Neutral Grey Wash track (6px corners, 2px padding) of 26px tabs; the active tab is Bright Leaf with weight 500 and the tab shadow.
- **Status bar:** sticky bottom, mono 11px, Pencil Grey, hairline above.

### Browser Surfaces
- **Selection:** Focus Wash (#EAE3D0) behind ink text, the page's own highlight rather than the system's.
- **Caret:** ink, in every input, select, and editable region.
- **Scrollbars:** thin, with a Rule Strong thumb on a transparent track — on the page, the preview, and the add-block popup.

### Narrative Preview (signature)
The finished text, in serif at 14.5px on a 1.75 leading, max 75ch, padded 24px 28px, with the worksheet's state visible inline: a line is hoverable (Erase Tint, 3px corners); a blank is a Fired Red Wash chip with a red underline and 500 weight; an unattested default is Placeholder Grey italic with a dotted Rule Strong underline; the focused fragment is Focus Wash (#EAE3D0) with a 2px ink underline bar; a withheld sentence sits on Withheld Amber Wash. When editable, the page lightens to #FDFBF2 and takes an inset ink focus outline.

### Twin Footer (signature)
A sentence already stated earlier in the chart leaves its box entirely; what remains is a 12px Pencil Grey footer naming the winner once and offering each suppressed sentence back as an ordinary chip.

## Do's and Don'ts

### Do:
- **Do** show selection by inverting to Pencil Ink (#23201A) on Cream Page (#F7F4ED); the on-pill, the Copy button, and the Polish toggle all use this one move.
- **Do** write every proposal in Pencil Grey (#5F594C) italic with a dashed border or underline, and turn it upright and full ink (weight 500) the moment it is accepted.
- **Do** keep text inputs as underlines (1.5px #948870), not boxes; boxes are for selects, buttons, and pills.
- **Do** keep every control border and input rule at Rule Strong (#948870) or darker, so it holds 3:1 against the page.
- **Do** reach for the warm-brown shadow (rgba(60,50,30,…)) only when something floats — popup, lifted drag, modal.
- **Do** keep the sans at 400 and 500 and the serif at 400–600; set the narrative in Source Serif 4 at 1.75 leading.
- **Do** reveal secondary controls (drag handle, delete ×) on hover with the 120 ms opacity fade, and leave them visible on touch.

### Don't:
- **Don't** introduce a second accent hue; blue, teal, or purple do not exist in this system.
- **Don't** color a value that the medic has not settled — green, amber, and red belong to given, withheld, and fired decisions and to the open-item and cap gates only.
- **Don't** use red anywhere except New call, delete-on-hover, the open-item gate (including the worksheet's missing-field chip), and the fired tone.
- **Don't** use italic for emphasis or titles; italic means "proposed".
- **Don't** add dark mode, motion beyond the 120 ms hover reveal, or shadows in the document flow.
- **Don't** replace the hairline Rule Faint (#DFD8C9) structure with cards; sections are rules and indents, not boxes.
