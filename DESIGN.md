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
  rule-strong: "#CCC3B0"
  pencil-rule: "#9A8F78"
  placeholder-grey: "#756D5D"
  erase-tint: "#F2EEE3"
  given-green: "#3E6B4F"
  given-green-wash: "#E7EDE4"
  given-green-rule: "#BFD3C5"
  withheld-amber: "#8A6D2F"
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
    fontSize: "13.5px"
    fontWeight: 400
    lineHeight: 1.8
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
    fontSize: "11px"
    fontWeight: 400
    lineHeight: 1.45
  value:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.45
  pill:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.45
  keyhint:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "10.5px"
    fontWeight: 400
    lineHeight: 1.45
  counter:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: "11.5px"
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
components:
  button-secondary:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.pencil-ink}"
    typography: "{typography.value}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "30px"
  button-secondary-hover:
    backgroundColor: "{colors.cream-page}"
    textColor: "{colors.pencil-ink}"
  button-primary:
    backgroundColor: "{colors.pencil-ink}"
    textColor: "{colors.cream-page}"
    typography: "{typography.value}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "30px"
  button-primary-hover:
    backgroundColor: "{colors.ink-pressed}"
    textColor: "{colors.cream-page}"
  button-primary-confirming:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.fired-red}"
  button-danger-ghost:
    backgroundColor: "{colors.bright-leaf}"
    textColor: "{colors.fired-red}"
    typography: "{typography.value}"
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
    typography: "{typography.value}"
    rounded: "{rounded.sm}"
    padding: "0 8px"
    height: "30px"
  input-text:
    backgroundColor: "transparent"
    textColor: "{colors.pencil-ink}"
    typography: "{typography.value}"
    rounded: "{rounded.none}"
    padding: "0 8px"
    height: "30px"
  missing-badge:
    backgroundColor: "{colors.fired-red-wash}"
    textColor: "{colors.fired-red}"
    typography: "{typography.field-label}"
    rounded: "4px"
    padding: "2px 9px"
---

# Design System: PCR Narrative Builder

## Overview

**Creative North Star: "The Field Notebook"**

A pocket notebook the medic writes in after the call. The page is cream, the ink is one near-black pencil, and the proposals the builder makes are written faintly in italic until the medic overwrites or accepts them. Nothing on the page competes for attention because nothing on the page is decoration: every mark is either a label, a value, a rule, or a key hint. The narrative preview is the notebook's fair-copy page, set in serif at a reading leading, while the worksheet beside it is the working page in a small sans.

The mood is calm and clerical. Calm: one accent, used only for the two things that interrupt the writing (starting a new call, and the open-item gate on Copy). Clerical: small uppercase section heads, aligned inline labels, hairline rules between sections, a monospace strip of key hints. Density is deliberate — a 13.5px body and 13px values on a laptop put a whole shell section on one screen, and the tool is driven from the keyboard, so rows are tight and controls are short.

Selection is never a new hue. A chosen pill inverts to solid ink on cream; a focused row gains an ink border; a confirmed value turns from faint grey to full ink. Clinical meaning, when it exists, borrows the three tones the chart itself uses — given (green), withheld (amber), fired (red) — and only on settled decisions.

**Key Characteristics:**
- One ink: near-black is both the text color and the selection fill; there is no brand blue.
- Proposals are faint italic; acceptance turns them upright and full ink.
- Hairline warm-grey rules structure the page; shadows appear only on things that float.
- Serif for what the medic reads (wordmark, narrative); sans for what the medic fills; mono for hints and counts.
- Light mode only, embedded fonts, no motion beyond a 120 ms hover reveal.

## Colors

A warm paper-and-pencil palette: two off-whites, one ink, four greys, and three clinical tones that each carry a wash and a rule.

### Primary
- **Pencil Ink** (#23201A): body text, the top-bar rule, the focus ring, the selected-pill fill, the Copy button, and the preview narrative. It is the accent because inversion to ink is how selection is shown.
- **Ink Pressed** (#3A362E): the hover state of anything filled with ink (Copy, modal primary).

### Neutral
- **Cream Page** (#F7F4ED): the page background, the top bar, the key-hint strip, the status bar, and the text color on ink fills.
- **Bright Leaf** (#FCFAF4): the raised sheet — selects, buttons, pills, the preview pane, popups, the focused row, the modal card.
- **Pencil Grey** (#5F594C): every secondary text — field labels, section names, key hints, proposed values, the version tag.
- **Graphite** (#4A463D): line labels only (the slightly darker label at the head of a row).
- **Rule Faint** (#DFD8C9): the default hairline — section heads, pane borders, the left rule on grouped sub-rows, the paragraph badge outline.
- **Rule Strong** (#CCC3B0): control borders (select, button, pill) and the dotted underline on an unattested default in the preview.
- **Pencil Rule** (#9A8F78): the underline of a text input at rest; control borders on hover.
- **Placeholder Grey** (#756D5D): italic placeholder text in inputs.
- **Erase Tint** (#F2EEE3): the hover wash on rows, popup rows, preview lines, and pressed buttons; the drop slot while dragging.
- **Neutral Grey** (#6B655B) on **Neutral Grey Wash** (#EFEBE1): the N/A toggle when on, the draft switcher track, the draft chip.

### Tertiary (clinical tones)
- **Given Green** (#3E6B4F) with **Given Green Wash** (#E7EDE4) and **Given Green Rule** (#BFD3C5): a treatment given, an open-detail affordance, the handoff button, the "all" A&Ox pill.
- **Withheld Amber** (#8A6D2F) with **Withheld Amber Wash** (#F3ECD9): a treatment withheld with reason, an unconfirmed amber default (italic with a dotted underline), a paragraph moved from its home, the character counter approaching the cap, the polish banner.
- **Fired Red** (#A63A2B) with **Fired Red Wash** (#F3E3DD) and **Fired Red Rule** (#D8B0A4): an escalation that fired, the New call button, delete affordances on hover, the open-item badge, a blank in the preview, the counter over the cap, Copy in its confirming state.

### Named Rules
**The One Ink Rule.** Selection, focus, and primary action are all expressed by Pencil Ink — a fill, a border, or a full-strength text color. No hue is introduced to mean "chosen".

**The Settled Tone Rule.** Green, amber, and red appear only on a decision the medic has made (given / withheld / fired) or on a gate the medic must clear (open items, the cap). A proposal is never colored; it is faint and italic.

**The Red Interrupt Rule.** Outside the clinical tones, red is reserved for New call and the open-item gate on Copy. Nothing else on the page is red.

## Typography

**Display Font:** Source Serif 4 (with Iowan Old Style, Charter, Georgia) — embedded, 400–600 plus 400 italic
**Body Font:** Archivo (with system-ui) — embedded, 400–500 only
**Label/Mono Font:** ui-monospace, SFMono-Regular, Menlo, Consolas — system stack, not embedded

**Character:** The serif belongs to what is read — the wordmark and the finished narrative at a generous 1.8 leading. The sans belongs to what is filled — compact, two weights, no italic face of its own (italic Archivo is browser-synthesised, and that slight roughness is part of how a proposal reads as "not yet written"). Mono marks the machine's voice: key hints, the version tag, the character counter, computed sums.

### Hierarchy
- **Brand** (600, 19px, serif): the wordmark in the top bar, with the mono version tag baseline-aligned beside it.
- **Narrative** (400, 13.5px, serif, 1.8): the preview text, max 70ch, pre-wrap.
- **Body** (400, 13.5px, sans, 1.45): the default for the page.
- **Section** (500, 11px, sans, 0.11em, UPPERCASE): section names in the worksheet (DISPATCH / RESPONSE / ARRIVAL). The popup group heading is the same idea at 10px / 0.05em.
- **Line label** (400, 11.5px, 0.03em, Graphite): the name at the head of a row.
- **Field label** (400, 11px, Pencil Grey): the inline "key:" before a value; also top-bar labels and notes.
- **Value** (400, 13px): the filled text of a field; 500 when the value is a fired escalation.
- **Pill** (400 / 500 on, 12px): option pills and chips; 11px and 10.5px for the N/A toggle, hidden chip, and paragraph badge.
- **Keyhint** (400, 10.5px mono): the hint strip; 10px inside a row.
- **Counter** (400 / 500 when amber or red, 11.5px mono, tabular numerals): the character count against 4,000.

### Named Rules
**The Two-Weight Rule.** The sans has 400 and 500 and nothing heavier. Emphasis beyond 500 is done with ink (color), case, or spacing — never with bold.

**The Italic Means Proposal Rule.** Italic in the worksheet or preview always means "the builder's suggestion, not yet accepted" (proposed values, dashed proposal pills, proposal placeholders, unattested defaults). Do not use italic for emphasis or for titles.

## Layout

Two panes on a 1600px-max centered grid: the worksheet (1.06fr) and the sticky preview pane (1fr), gap 16px, padding 16px; at 1100px and up the gap and padding grow to 20px. Below 1100px the panes stack and the preview loses its stickiness. The top bar is sticky at the top (10px 16px padding, flex-wrapped controls pushed right); the status bar is sticky at the bottom. The preview pane sits at top: 66px with a max height of the viewport less 84px and scrolls internally.

The worksheet is a column of sections 20px apart. Each section has a head (name left, tools right) under a hairline, then rows. A row is a flex-wrapped line of label + fields with 5px 8px padding and a 2px/8px gap, baseline-aligned, with a transparent 1px border reserved so focus never shifts layout. Grouped sub-rows indent 14–18px with a 2px left rule; a second level indents 36px. Rows reach a scroll-margin of 78px so keyboard focus lands below the sticky bar.

The spacing scale is small and ad hoc rather than a strict grid: 2, 4, 6, 8, 10, 16, 20px. 6px is the gap inside a control cluster, 8px between controls, 16/20px between panes and sections. Control heights step down with importance: 30px for top-bar selects, buttons, and inputs; 26px for in-row inputs and sub-pills; 25px pills; 24px open-detail buttons; 22px N/A toggle; 20px hidden chip.

## Elevation & Depth

Flat by default. Depth on the page is drawn with rules, tints, and inversion: a hairline under each section head, a 2px left rule on grouped rows, an erase-tint wash on hover, an ink border and sheet background on the focused row. Shadows exist only for things that have left the page — popups, a lifted drag, the modal — and they are warm brown (rgb 60,50,30), never black, so they read as paper over paper.

### Shadow Vocabulary
- **Focused row** (`box-shadow: 0 1px 3px rgba(60,50,30,.10)`): the one in-flow shadow; paired with the ink border on the row that has keyboard focus.
- **Active tab** (`box-shadow: 0 1px 2px rgba(60,50,30,.1)`): the selected draft tab in the switcher.
- **Lifted** (`box-shadow: 0 6px 16px rgba(60,50,30,.18)`): a line or section being dragged or keyboard-grabbed.
- **Popup** (`box-shadow: 0 8px 24px rgba(60,50,30,.18)`): the add-block popup and the hidden-items popover.
- **Modal** (`box-shadow: 0 20px 60px rgba(60,50,30,.25)`): the modal card over a 35% black scrim.
- **Cursor ring** (`box-shadow: 0 0 0 1.5px #23201A inset`): the pill under the keyboard cursor; and `inset 0 -2px 0` ink as the underline bar on the preview's focused fragment.

### Named Rules
**The Paper-Over-Paper Rule.** Nothing in the document flow casts a shadow except the focused row. A shadow means the element is floating above the page, and it is always warm brown.

## Shapes

Soft, small radii that step with scale: 8px for floating surfaces (popups, the preview pane, the modal), 6px for controls and rows (buttons, selects, the row's focus border, drag handles), 3px for inline fields and preview lines, and full pills (999px) for options, chips, toggles, and the paragraph badge. Text inputs are not boxes at all — a 1.5px underline in Pencil Rule, dashed when the placeholder is a proposal, ink on hover and focus. Round delete and remove controls (50%) sit flush and only reveal on hover.

Borders carry meaning by style: solid hairline for structure, dashed for "offered but not taken" (proposal pills, the open-detail button, the hidden chip, the drop slot, a proposal input's underline), dotted for "unconfirmed" (an amber default, an unattested preview default, the all-A&Ox pill). The top bar's bottom rule is the only ink-colored line on the page.

## Components

### Buttons
Quiet until it matters: a sheet-colored outline button is the default, and the only filled button on the page is the one that finishes the job.
- **Shape:** 30px tall, softly rounded (6px), 0 12px padding, 13px sans.
- **Secondary (default):** Bright Leaf fill, Rule Strong border, ink text; hover → Cream Page fill with a Pencil Rule border; active → Erase Tint.
- **Primary (Copy):** solid Pencil Ink, cream text, weight 500, min-width 150px; hover → Ink Pressed. The label carries the open count ("Copy (1 open)").
- **Primary, confirming:** when Copy is pressed with open items it flips to Bright Leaf with Fired Red text and rule; hover → Fired Red Wash. This is the soft gate.
- **Danger ghost (New call):** outline with Fired Red text and rule; hover → Fired Red Wash. Separated from the rest of the top bar by a hairline divider.
- **Toggle (Polish):** a secondary button that inverts to ink when on.
- **Open detail:** 24px, 12px text, Given Green text on a dashed Rule Strong border; hover → green wash and rule.
- **Focus:** a 2px Pencil Ink outline, 2px offset, on every focusable control.

### Pills / Chips
- **Style:** 25px full pills, 0 11px, 12px sans, Bright Leaf on a Rule Strong border.
- **On:** inverts to Pencil Ink with cream text, weight 500.
- **Proposed:** dashed border, Pencil Grey italic — the builder's suggestion.
- **Cursor:** a 1.5px inset ink ring marks the pill the keyboard is on; Enter accepts it.
- **Structural decisions:** the given / withheld / fired / omit options keep their clinical tone when on (green, amber, red, or neutral wash with matching text and rule).
- **Small variants:** N/A toggle (22px, 11px, neutral wash when on); hidden chip (20px, 10.5px, dashed faint); paragraph badge (10.5px, faint outline pill, amber when the paragraph was moved).

### Cards / Containers
- **Preview pane:** Bright Leaf, 1px Rule Faint border, 8px corners, sticky; a head strip with the draft chip, mono counter, open badge, Polish, and Copy under a hairline.
- **Popups:** Bright Leaf, Rule Faint border, 8px corners, popup shadow, 6px padding; rows are 7px 10px with 5px corners and an Erase Tint hover; group heads are 10px uppercase.
- **Modal:** Bright Leaf card, 8px corners, 20px padding, max 440px, modal shadow; 15px/500 title, 13px Pencil Grey body, actions right-aligned.
- **Worksheet row:** transparent until hovered (Erase Tint) or focused (Bright Leaf, ink border, focused-row shadow).

### Inputs / Fields
- **Text input:** no box — transparent with a 1.5px Pencil Rule underline, 30px tall (26px inside a row), 13px sans; italic Placeholder Grey placeholder; hover and focus turn the underline ink. A proposal input has a dashed underline and an italic Pencil Grey placeholder that Enter accepts.
- **Select:** Bright Leaf box, Rule Strong border, 6px corners, 30px; hover → Cream Page with a Pencil Rule border.
- **Field value states:** idle → faint; set → ink; proposed → Pencil Grey italic; amber default → Withheld Amber italic with a dotted underline; given / withheld / fired → their tone, fired at weight 500.
- **Computed sum:** mono, ink; faint when empty; auto-filled components italic at 70% opacity.

### Navigation
- **Top bar:** Cream Page, sticky, a 1px Pencil Ink rule beneath — the single strongest line on the page. Serif wordmark with mono version tag at left; unit select, category select, add-block button, draft switcher, and New call at right. Below it a Cream Page mono strip of key hints under a hairline.
- **Draft switcher:** a Neutral Grey Wash track (6px corners, 2px padding) of 26px tabs; the active tab is Bright Leaf with weight 500 and the tab shadow.
- **Status bar:** sticky bottom, mono 11px, Pencil Grey, hairline above.

### Narrative Preview (signature)
The finished text, in serif at 1.8 leading, max 70ch, with the worksheet's state visible inline: a line is hoverable (Erase Tint, 3px corners); a blank is a Fired Red Wash chip with a red underline and 500 weight; an unattested default is faint italic with a dotted Rule Strong underline; the focused fragment is a warm highlight (#EAE3D0) with a 2px ink underline bar; a withheld sentence sits on Withheld Amber Wash. When editable, the page lightens to #FDFBF2 and takes an inset ink focus outline.

### Twin Footer (signature)
A sentence already stated earlier in the chart leaves its box entirely; what remains is a 12px Pencil Grey footer naming the winner once and offering each suppressed sentence back as an ordinary chip.

## Do's and Don'ts

### Do:
- **Do** show selection by inverting to Pencil Ink (#23201A) on Cream Page (#F7F4ED); the on-pill, the Copy button, and the Polish toggle all use this one move.
- **Do** write every proposal in Pencil Grey (#5F594C) italic with a dashed border or underline, and turn it upright and full ink the moment it is accepted.
- **Do** keep text inputs as underlines (1.5px #9A8F78), not boxes; boxes are for selects, buttons, and pills.
- **Do** reach for the warm-brown shadow (rgba(60,50,30,…)) only when something floats — popup, lifted drag, modal.
- **Do** keep the sans at 400 and 500 and the serif at 400–600; set the narrative in Source Serif 4 at 1.8 leading.
- **Do** reveal secondary controls (drag handle, delete ×) on hover with the 120 ms opacity fade, and leave them visible on touch.

### Don't:
- **Don't** introduce a second accent hue; blue, teal, or purple do not exist in this system.
- **Don't** color a value that the medic has not settled — green, amber, and red belong to given, withheld, and fired decisions and to the open-item and cap gates only.
- **Don't** use red anywhere except New call, delete-on-hover, the open-item gate, and the fired tone.
- **Don't** use italic for emphasis or titles; italic means "proposed".
- **Don't** add dark mode, motion beyond the 120 ms hover reveal, or shadows in the document flow.
- **Don't** replace the hairline Rule Faint (#DFD8C9) structure with cards; sections are rules and indents, not boxes.
