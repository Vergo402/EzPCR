# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

One user: Alex Vergo, paramedic at Cortlandt-Peekskill Regional Paramedic Services
(CPRPS, 35M units). He writes the narrative after the call, at the hospital or back in
quarters, on the rig laptop (Firefox and Chrome), with patient handoff already done. No
second user is planned; wording and defaults are his own rulings.

## Product Purpose

`PCR Narrative Builder v1.html` assembles the HPI narrative of a patient care report from a
keyboard-driven worksheet, for paste into Zoll emsCharts. It exists because emsCharts'
free-text HPI field gives no structure, truncates silently at 4,000 characters, and
tempts restating values that already live in the activity log.

Success per narrative: the copied text fits the 4,000-character HPI cap with zero open
items, and reads chronologically with nothing restated from the activity log. Only values
that justify a decision appear.

## Positioning

Chronological append with accept-to-emit. Call-type blocks and templates stack in the
order things happened and each prints as its own paragraph between assessment and
disposition; nothing is replaced. Nothing prints until the medic accepts it (defaults are
faint proposals, not emissions). A sentence two stacked blocks both carry is stated once,
at the earliest place in the chart. The result reads as a record of the call, not a form
dump — which a stock emsCharts template or dictation cannot truthfully produce.

## Operating Context

- Workflow: open the builder, fill the shell (dispatch, primary, mental status/CC/history,
  assessment), stack blocks and templates for the call type, pick one of four
  dispositions, resolve open items, copy, paste into the emsCharts HPI field.
- emsCharts limits: `PRMAIN.hpi` max 4,000 characters with silent truncation on paste;
  a hard return counts 2 characters; CC / Secondary CC 255; Stretcher Purpose 200.
- Clinical frame: NYS ALS Collaborative Protocols v26.1 (effective 2026-09-01) and the
  National Field Triage Red/Yellow criteria. Protocol names stay out of the narrative;
  only medical-control contact and deviations are cited.
- Service reality: very short transports (receiving hospitals are close). Time-consuming
  en-route interventions (e.g. serial 12-leads on ACS) are exceptions, not defaults.
- Governing document: the newest `PCR Narrative Standard DRAFT v*.md` (v0.13 today). Every
  wording, option, or structure change lands there first; the builder's `window.__DOC__`
  mirrors it exactly. Rulings are recorded in the standard's REVISION HISTORY with a date.

## Capabilities and Constraints

- Shell (every call), four dispositions, 18 call-type blocks, 6 dedicated templates with
  escalation lines that switch a block to its template.
- Scored fields (GCS, NYS-LAMS, burn % BSA) are entered as components; the builder computes
  the total.
- Twin sentences across stacked blocks are suppressed to one copy, with the losers listed
  at the foot of their box until the medic shows one.
- Open-item tracking gates Copy; the disposition is the only standing open item.
- Drafts persist in `sessionStorage` only. No `localStorage`, no network calls, no PHI
  persistence, light mode only, single HTML file, ES5-style JavaScript.
- Terminology: block, template, shell, disposition, twin, open item, escalation, stack.
  Canonical abbreviations: NYS-LAMS, Hx, A&Ox, DNR/MOLST, NYP-HVHC; 26 others are spelled
  out per the 2026-09-03 ruling.
- Undecided: whether the Field Ledger decisions (per-field order, free-standing fields,
  label style) are applied to the DOC and engine. The ledger exists; the apply pass is
  partial (reviewed containers only; respiratory held).

## Brand Commitments

No brand beyond the name EzPCR. Voice of the product's output is the narrative standard's
own: terse clinical prose, third person, "Pt", unit "35M___". The worksheet's own copy
(labels, hints, open-item notes) follows the same register.

## Evidence on Hand

- `PCR Narrative Standard DRAFT v0.13.md` — the full standard, 76 KB.
- `PCR Narrative Builder v1.html` — the shipping tool, 523 KB, DOC embedded.
- `review-model.json` and `tools/extract_review_model.py` — the per-field review model
  behind the Field Ledger artifact.
- No testimonials, adoption numbers, or external users. Do not fabricate any.

## Product Principles

1. The chart is a chronological record: append, never replace.
2. Nothing emits until the medic accepts it.
3. The standard is the source of truth; the builder mirrors it, never leads it.
4. Restate only what justifies a decision; the activity log holds the rest.
5. Fit the paste target: 4,000 characters, zero open items, every time.

## Accessibility & Inclusion

Keyboard-first operation is a product requirement (the worksheet is driven without the
mouse). No other product-specific requirement was established; the user is one person
with no stated assistive needs.
