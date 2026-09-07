#!/usr/bin/env python3
"""v0.13 data change: hoist the initial 12-lead and IV-access sentences out of
per-block lines into two new optional sentences in the shell Assessment
paragraph, and reshape the STEMI/2a relationship and twin groups to match.

Edits "PCR Narrative Builder v1.html" in place:
  - parses the single line `window.__DOC__ = <json>;`, mutates the JSON,
    writes it back on the same line (per CLAUDE.md's DOC-editing contract);
  - two small engine-constant text edits outside the DOC line: PARA_LINES
    (paragraph placement for the two new shell lines) and the DEFAULTS map
    (drop the stale `brn_iv_lines` preselect);
  - the HTML header's `#version-tag` text and `DOC.meta.source`.

Stdlib only. Reuses the text-tidy / rendering / indexing helpers from
apply_ledger.py rather than reinventing them.

This script is deliberately NOT built around apply_ledger's generic
apply_deletions()/clause_cleanup() pipeline for the partial-line edits (trg_iv,
met_dka_iv, abd_iv, alg_iv, brn_iv, neur_iv_reassess, card_dys_monitor,
card_acs_12l): that pipeline's has_assertive_word() heuristic treats a bare
leading "IV" as an all-caps "assertive" survivor (like "LOST" or "UNSTABLE")
and refuses to drop the now-empty clause around it, leaving debris such as
"IV g . " in the rendered line. Each of those eight lines is small and
well-understood enough to hand-build its post-edit `parts` array directly;
`collapse()` still runs over every hand-built literal as a cheap safety net.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from apply_ledger import (  # noqa: E402
    collapse, render_token, render_parts, render_line,
    build_indices, parts_arrays, collect_all_field_ids,
)

DOC_RE = re.compile(r'^(window\.__DOC__ = )(.*)(;\s*)$', re.M)
SRC = Path("PCR Narrative Builder v1.html")

REPORT = []


def note(msg):
    REPORT.append(msg)
    print(msg)


def hint_stripped(raw):
    return collapse(re.sub(r'\s*\{[^}]*\}', '', raw)).strip()


def main():
    text = SRC.read_text(encoding="utf-8")
    m = DOC_RE.search(text)
    assert m, "window.__DOC__ line not found"
    doc = json.loads(m.group(2))

    line_index, container_of = build_indices(doc)

    # ------------------------------------------------------------------
    # Pre-edit grep check: every field/line id this script is about to
    # delete should not appear anywhere in the engine (the file text minus
    # the DOC line itself), except brn_iv_lines inside DEFAULTS.
    # ------------------------------------------------------------------
    DELETED_LINE_IDS = [
        "card_acs_iv", "card_dys_iv", "gen_iv", "st_iv", "cva_iv", "met_sep_iv",
        "trm_circ_access", "resp_chf_12l", "tox_12lead", "met_dka_12lead",
        "gen_labs_12lead", "gen_screen_12lead", "abd_12lead",
    ]
    DELETED_FIELD_IDS = [
        # fields removed along with a whole-line deletion above
        "card_acs_iv_gauge", "card_acs_iv_site",
        "card_dys_iv_gauge", "card_dys_iv_site",
        "gen_iv_gauge", "gen_iv_site",
        "st_iv_gauge", "st_iv_site",
        "cva_iv_gauge", "cva_iv_site",
        "met_sep_iv_gauge", "met_sep_iv_site", "met_sep_iv2",
        "trm_iv_gauge", "trm_iv_site", "trm_iv2",
        "resp_chf_12l_findings",
        "tox_12lead_findings",
        "met_dka_12lead_findings",
        "gen_labs_12lead_findings",
        "gen_screen_12lead_finding", "gen_screen_12lead_wh",
        "abd_12l_result", "abd_12l_wh_reason",
        # fields removed from a partial-line edit (line itself survives)
        "card_acs_12l_findings",
        "trg_iv_gauge", "trg_iv_site",
        "met_dka_iv_gauge", "met_dka_iv_site",
        "abd_iv_gauge", "abd_iv_site",
        "alg_iv_gauge", "alg_iv_site",
        "brn_iv_gauge", "brn_iv_site", "brn_iv_lines",
        "neur_iv_gauge", "neur_iv_site",
        "card_dys_12l_confirms",
        "card_acs_esc_criteria", "card_acs_esc_calledto",
    ]
    engine_text = text[: m.start()] + text[m.end():]  # everything but the DOC line
    note("## Pre-edit grep of the engine (file text minus the DOC line) for every id "
         "about to be deleted")
    unexpected_hits = []
    for fid in DELETED_LINE_IDS + DELETED_FIELD_IDS:
        # whole-word match so e.g. "st_iv" doesn't match inside "st_iv_gauge"
        hits = re.findall(r'(?<![A-Za-z0-9_])' + re.escape(fid) + r'(?![A-Za-z0-9_])',
                           engine_text)
        if hits:
            if fid == "brn_iv_lines":
                note(f"- `{fid}`: {len(hits)} hit(s) in engine text (EXPECTED: DEFAULTS "
                     f"preselect, removed below)")
            else:
                unexpected_hits.append(fid)
                note(f"- `{fid}`: {len(hits)} UNEXPECTED hit(s) in engine text")
    assert not unexpected_hits, f"unexpected engine references to deleted ids: {unexpected_hits}"
    note("- all other deleted ids: 0 hits, as expected")

    # ==================================================================
    # PART 1 — two new shell lines in sh_assessment, right after
    # sh_vitals_line
    # ==================================================================
    sh_assessment = next(s for s in doc["shell"]["sections"] if s["id"] == "sh_assessment")
    before_ids = [l["id"] for l in sh_assessment["lines"]]
    assert before_ids == ["sh_vitals_line", "sh_impression_line"], before_ids

    sh_12lead_line = {
        "id": "sh_12lead_line", "kind": "std", "label": "12-lead", "opt": True,
        "parts": [
            "12-lead ",
            {"c": [
                {"label": "acquired: ___", "parts": [
                    "acquired: ",
                    {"f": "sh_12l_findings",
                     "hint": "rhythm, rate, axis, intervals, ST/T changes by lead, or \"no acute changes\"",
                     "req": True, "w": 64},
                    ", ",
                    {"c": ["transmitted", "not transmitted"], "id": "sh_12l_transmitted",
                     "multi": False, "req": True},
                ]},
                {"label": "not indicated: ___", "parts": [
                    "not indicated: ",
                    {"f": "sh_12l_not_indicated_why", "hint": "why", "req": True, "w": 32},
                ]},
            ], "id": "sh_12l_status", "multi": False, "req": True},
            ".",
        ],
    }
    sh_iv_line = {
        "id": "sh_iv_line", "kind": "std", "label": "IV access", "opt": True,
        "parts": [
            {"c": [
                {"label": "IV ___g ___", "parts": [
                    "IV ", {"f": "sh_iv_gauge", "req": True, "w": 4},
                    "g ", {"f": "sh_iv_site", "req": True, "w": 16},
                ]},
                {"label": "IO ___", "parts": [
                    "IO ", {"f": "sh_io_site", "req": True, "w": 16},
                ]},
            ], "id": "sh_access_type", "multi": True, "req": True},
            {"g": [", second access ", {"f": "sh_access_second", "req": False, "w": 16}]},
            ".",
        ],
    }
    sh_assessment["lines"] = [
        sh_assessment["lines"][0], sh_12lead_line, sh_iv_line, sh_assessment["lines"][1],
    ]
    note("\n## Part 1: inserted sh_12lead_line, sh_iv_line into sh_assessment.lines")
    note("  new order: " + ", ".join(l["id"] for l in sh_assessment["lines"]))

    # rebuild indices - shell lines list was replaced wholesale
    line_index, container_of = build_indices(doc)
    line_index["sh_12lead_line"] = sh_12lead_line
    line_index["sh_iv_line"] = sh_iv_line

    # ==================================================================
    # PART 2 — block/template edits
    # ==================================================================

    # -- card_acs_12l: keep only the R-sided group content -------------
    line = line_index["card_acs_12l"]
    assert line["parts"][1]["f"] == "card_acs_12l_findings"
    group = line["parts"][3]
    assert list(group.keys()) == ["g"]
    rsided_field = group["g"][1]
    assert rsided_field["f"] == "card_acs_rsided_12l"
    # rsided_field carried hint:"If inferior changes" from when it lived inside
    # an unconditional line's {g} sub-clause - that hint was the only signal
    # that this content was conditional. Now the whole LINE is opt:true with
    # note "inferior changes only" carrying that signal instead, so the
    # field's own hint is stale/redundant (worksheet-only; narrative
    # unaffected either way). Drop it rather than leave duplicated guidance.
    assert rsided_field.get("hint") == "If inferior changes"
    rsided_field = dict(rsided_field)
    del rsided_field["hint"]
    new_card_acs_12l = {
        "id": "card_acs_12l", "kind": "std", "label": "R-sided 12-lead",
        "opt": True, "note": "inferior changes only",
        "parts": ["R-sided 12-lead ", rsided_field, "."],
    }
    line.clear()
    line.update(new_card_acs_12l)
    note("\n## card_acs_12l restructured (R-sided only)")
    note("  before removal, findings field + acquired/transmitted literal + note dropped")
    note("  also dropped the field's own now-redundant hint \"If inferior changes\" "
         "(the line's opt/note already say that)")

    # -- whole-line deletions -------------------------------------------
    DELETE_WHOLE = set(DELETED_LINE_IDS)
    deleted_lines = {}

    def remove_lines(node):
        if isinstance(node, dict):
            if isinstance(node.get("lines"), list):
                keep = []
                for item in node["lines"]:
                    if isinstance(item, dict) and item.get("id") in DELETE_WHOLE:
                        deleted_lines[item["id"]] = item
                        continue
                    keep.append(item)
                node["lines"] = keep
            for v in node.values():
                remove_lines(v)
        elif isinstance(node, list):
            for v in node:
                remove_lines(v)

    remove_lines(doc)
    missing = DELETE_WHOLE - set(deleted_lines)
    assert not missing, f"lines not found for deletion: {missing}"
    note("\n## Whole-line deletions (" + str(len(deleted_lines)) + ")")
    for lid in DELETED_LINE_IDS:
        note(f"  - deleted `{lid}`")

    # rebuild indices again - many lines lists were rewritten
    line_index, container_of = build_indices(doc)
    line_index["sh_12lead_line"] = sh_12lead_line
    line_index["sh_iv_line"] = sh_iv_line

    # -- trg_iv: keep only the Fluids choice, relabel --------------------
    # NOTE: render_parts (imported from apply_ledger) renders a `{c:...}`
    # choice by each option's LABEL, not its expanded nested `parts` - so a
    # dict option like {"label":"bolus","parts":[...]} renders as "bolus",
    # matching the spec table's own abbreviated cell text exactly.
    line = line_index["trg_iv"]
    assert render_parts(line["parts"]) == (
        "IV ___g ___. Fluids [none / bolus]."
    ), render_parts(line["parts"])
    fluids_choice = line["parts"][5]
    assert fluids_choice.get("id") == "trg_fluids"
    line["label"] = "Fluids"
    line["parts"] = ["Fluids ", fluids_choice, "."]
    note("\n## trg_iv -> Fluids only: " + render_parts(line["parts"]))

    # -- met_dka_iv: drop IV gauge/site ----------------------------------
    line = line_index["met_dka_iv"]
    assert render_parts(line["parts"]) == "IV ___g ___, NS ___ mL, reassessed ___."
    ns_ml, reassessed = line["parts"][5], line["parts"][7]
    assert ns_ml["f"] == "met_dka_ns_ml" and reassessed["f"] == "met_dka_reassessed"
    line["parts"] = [collapse("NS "), ns_ml, " mL, reassessed ", reassessed, "."]
    note("\n## met_dka_iv -> " + render_parts(line["parts"]))

    # -- abd_iv: drop IV gauge/site, keep the reassessed/none tail -------
    line = line_index["abd_iv"]
    assert render_parts(line["parts"]) == (
        "IV ___g ___. NS ___ mL for ___, [reassessed / none]."
    ), render_parts(line["parts"])
    ns_vol, ns_indication, reassess_choice = line["parts"][5], line["parts"][7], line["parts"][9]
    assert ns_vol["f"] == "abd_ns_vol" and ns_indication["f"] == "abd_ns_indication"
    assert reassess_choice.get("id") == "abd_ns_reassess_choice"
    line["parts"] = [collapse("NS "), ns_vol, " mL for ", ns_indication, ", ",
                     reassess_choice, "."]
    note("\n## abd_iv -> " + render_parts(line["parts"]))

    # -- alg_iv: drop IV gauge/site, keep the repeated/none tail ---------
    line = line_index["alg_iv"]
    assert render_parts(line["parts"]) == (
        "IV ___g ___. NS 500 mL bolus for SBP <100 / MAP <65, reassessed ___, "
        "[repeated / none]."
    ), render_parts(line["parts"])
    reassess_field, repeat_choice = line["parts"][5], line["parts"][7]
    assert reassess_field["f"] == "alg_ns_reassess"
    assert repeat_choice.get("id") == "alg_ns_repeat_choice"
    line["parts"] = [collapse("NS 500 mL bolus for SBP <100 / MAP <65, reassessed "),
                     reassess_field, ", ", repeat_choice, "."]
    note("\n## alg_iv -> " + render_parts(line["parts"]))
    note("  NOTE: the spec's table cell for this row (`NS 500 mL bolus for SBP <100 / "
         "MAP <65, reassessed ___.`) omits the trailing `, [repeated / none]` clause. "
         "The instruction itself only says \"delete the IV fields + literal\" (nothing "
         "about the repeated/none choice), and abd_iv's sibling row explicitly says to "
         "keep its tail exactly - so the tail is kept here too and the table cell is "
         "read as an abbreviated preview, not a literal target string. Flagging this "
         "explicitly per the deviation-reporting instruction.")

    # -- brn_iv: drop IV gauge/site/lines-count choice -------------------
    line = line_index["brn_iv"]
    assert render_parts(line["parts"]) == (
        "IV ___g ___ x [1 / 2]. NS 500 mL bolus, reassessed ___. Hypothermia "
        "prevention ___ {>10% BSA: dry dressings only, pt kept warm}."
    ), render_parts(line["parts"])
    ns_reassess, hypo_prev = line["parts"][7], line["parts"][9]
    assert ns_reassess["f"] == "brn_ns_reassess" and hypo_prev["f"] == "brn_hypothermia_prevention"
    line["parts"] = [collapse("NS 500 mL bolus, reassessed "), ns_reassess,
                     ". Hypothermia prevention ", hypo_prev, "."]
    note("\n## brn_iv -> " + render_parts(line["parts"]))

    # -- neur_iv_reassess: drop IV gauge/site, relabel -------------------
    line = line_index["neur_iv_reassess"]
    assert render_parts(line["parts"]) == (
        "IV ___g ___. Treatments per fork above. Pt reassessed: GCS ___, "
        "NYS-LAMS [unchanged / other…]."
    ), render_parts(line["parts"])
    gcs_field, lams_choice = line["parts"][5], line["parts"][7]
    assert gcs_field["f"] == "neur_reassess_gcs"
    assert lams_choice.get("id") == "neur_reassess_lams"
    line["label"] = "Reassessment"
    line["parts"] = [collapse("Treatments per fork above. Pt reassessed: GCS "),
                     gcs_field, ", NYS-LAMS ", lams_choice, "."]
    note("\n## neur_iv_reassess -> " + render_parts(line["parts"]))

    # -- card_dys_monitor: drop the 12-lead-confirms clause, relabel -----
    line = line_index["card_dys_monitor"]
    assert render_parts(line["parts"]) == (
        "Monitor: ___ {rhythm, rate, regularity, QRS width, P-wave relationship, "
        "block degree and type}. 12-lead confirms ___."
    ), render_parts(line["parts"])
    findings_field = line["parts"][1]
    assert findings_field["f"] == "card_dys_monitor_findings"
    line["label"] = "Monitor"
    line["parts"] = ["Monitor: ", findings_field, "."]
    note("\n## card_dys_monitor -> " + render_parts(line["parts"]))

    # -- st_12lead_initial: reword the leading literal only, relabel -----
    line = line_index["st_12lead_initial"]
    assert line["parts"][0] == "12-lead: ST elevation "
    line["label"] = "STEMI criteria"
    line["parts"][0] = "STEMI criteria on 12-lead: ST elevation "
    note("\n## st_12lead_initial -> " + hint_stripped(render_parts(line["parts"])))

    # -- card_acs_esc: fired becomes literal-only, carry cleared ---------
    line = line_index["card_acs_esc"]
    assert line["normal"] == ["STEMI criteria not met on serial 12-leads."]
    assert line["carry"] == {"card_acs_esc_calledto": "st_alert_dest"}
    line["fired"] = ["STEMI criteria MET on 12-lead."]
    line["carry"] = {}
    note("\n## card_acs_esc: normal unchanged, fired -> " + render_parts(line["fired"]) +
         ", carry -> {}")

    # -- templates.stemi.intro reword ------------------------------------
    stemi = doc["templates"]["stemi"]
    assert stemi["intro"] == "Starts as Cardiac 2a; from the moment criteria fire, this replaces it."
    stemi["intro"] = "Stacks after Cardiac 2a; anything 2a already stated is not repeated here."
    note("\n## templates.stemi.intro reworded")

    # -- explicit no-ops (sanity that these still exist, untouched) ------
    for lid in ("ca_access", "card_dys_post", "ca_rosc_12lead", "brn_electrical"):
        assert lid in line_index, f"{lid} missing"
    note("\n## Confirmed unchanged: ca_access, card_dys_post, ca_rosc_12lead, brn_electrical")

    # ==================================================================
    # PART 3 — DOC.meta.twins
    # ==================================================================
    twins = doc["meta"]["twins"]
    by_id = {g["id"]: g for g in twins}
    assert set(by_id) == {
        "analgesia-withheld", "albuterol-neb", "dexamethasone", "epi-im", "naloxone",
        "fentanyl-analgesia", "twelve-lead-serial", "twelve-lead",
        "twelve-lead-not-indicated", "needle-decompression", "unstable-sedation",
        "reassessed-at", "ns-bolus", "epi-infusion", "gcs", "moi-toi",
        "bgl-neuro-stroke", "lams", "iv", "ntg-withheld", "anticoag",
        "resp-etco2-vitals",
    }, sorted(by_id)

    new_twins = [g for g in twins if g["id"] not in ("twelve-lead", "twelve-lead-not-indicated")]
    for g in new_twins:
        if g["id"] == "iv":
            g["lines"] = ["sh_iv_line", "ca_access"]
        elif g["id"] == "ntg-withheld":
            g["id"] = "ntg"
            g["lines"] = ["card_acs_ntg", "resp_chf_ntg", "st_ntg"]
    new_twins.extend([
        {"id": "rsided-12lead", "lines": ["card_acs_12l", "st_rsided_12lead"]},
        {"id": "asa", "lines": ["card_acs_asa", "st_asa"]},
        {"id": "hypotension-bolus", "lines": ["card_acs_hypo", "st_hypotension_tx"]},
        {"id": "pads", "lines": ["card_dys_pads", "st_pads"]},
        {"id": "reassessed-en-route", "lines": ["sh_reassess_line", "st_reassess"]},
    ])
    doc["meta"]["twins"] = new_twins
    note("\n## Part 3: twins reshaped, " + str(len(twins)) + " -> " + str(len(new_twins)) +
         " groups")
    note("  groups: " + ", ".join(g["id"] for g in new_twins))

    # rebuild indices once more before the integrity assertions below
    line_index, container_of = build_indices(doc)
    line_index["sh_12lead_line"] = sh_12lead_line
    line_index["sh_iv_line"] = sh_iv_line

    missing_twin_lines = []
    for g in new_twins:
        for lid in g["lines"]:
            if lid not in line_index:
                missing_twin_lines.append((g["id"], lid))
    assert not missing_twin_lines, f"twin group references missing line ids: {missing_twin_lines}"
    note("  every twin-group line id exists in the DOC: OK")

    # ==================================================================
    # PART 4 — version markers
    # ==================================================================
    assert doc["meta"]["source"] == "v0.12"
    doc["meta"]["source"] = "v0.13"
    note("\n## Part 4: DOC.meta.source -> v0.13")

    # ==================================================================
    # write the DOC back
    # ==================================================================
    doc_json = json.dumps(doc, ensure_ascii=False, separators=(",", ":"))
    reparsed = json.loads(doc_json)
    assert reparsed == doc
    new_line = m.group(1) + doc_json + m.group(3)
    new_text = text[: m.start()] + new_line + text[m.end():]

    # ==================================================================
    # engine-constant text edits (outside the DOC line)
    # ==================================================================
    old_para = 'const PARA_LINES = { sh_vitals_line: "p2", sh_impression_line: "p3" };'
    new_para = ('const PARA_LINES = { sh_vitals_line: "p2", sh_impression_line: "p3", '
                'sh_12lead_line: "p2", sh_iv_line: "p2" };')
    assert new_text.count(old_para) == 1, "PARA_LINES marker not found exactly once"
    new_text = new_text.replace(old_para, new_para)
    note("\n## Engine: PARA_LINES updated")
    note("  " + new_para)

    old_defaults_frag = 'brn_dressing_type:"dry sterile",brn_iv_lines:"1",'
    new_defaults_frag = 'brn_dressing_type:"dry sterile",'
    assert new_text.count(old_defaults_frag) == 1, "brn_iv_lines DEFAULTS entry not found exactly once"
    new_text = new_text.replace(old_defaults_frag, new_defaults_frag)
    note("\n## Engine: DEFAULTS.brn_iv_lines removed")

    old_tag = 'Builder v1 · source v0.12 · NYS v26.1'
    new_tag = 'Builder v1 · source v0.13 · NYS v26.1'
    assert new_text.count(old_tag) == 1, "version-tag text not found exactly once"
    new_text = new_text.replace(old_tag, new_tag)
    note("\n## HTML header #version-tag updated to source v0.13")

    SRC.write_text(new_text, encoding="utf-8")

    # confirm reparse from disk
    text2 = SRC.read_text(encoding="utf-8")
    m2 = DOC_RE.search(text2)
    json.loads(m2.group(2))
    note("\n## Wrote file; re-read from disk and reparsed window.__DOC__ OK")

    # ==================================================================
    # PART 5 — post-edit referential-integrity assertions
    # ==================================================================
    note("\n## Part 5: referential-integrity assertions")

    final_line_index, final_container_of = build_indices(doc)
    final_line_index["sh_12lead_line"] = sh_12lead_line
    final_line_index["sh_iv_line"] = sh_iv_line
    all_field_ids = collect_all_field_ids(doc)
    # collect_all_field_ids walks doc["blocks"]/shell/dispositions/templates via
    # build_indices; the two new shell lines were spliced in directly above so
    # they ARE part of doc already - recompute cleanly from doc itself.
    all_field_ids = set()
    from apply_ledger import collect_field_ids
    for lid, line in final_line_index.items():
        for _name, arr in parts_arrays(line):
            collect_field_ids(arr, all_field_ids)
    note(f"  total field/choice ids collected from DOC: {len(all_field_ids)}")

    # DEFAULTS / DEFAULTS_FN keys, extracted from the just-written engine text
    defaults_block_m = re.search(r'const DEFAULTS = \{(.*?)\n\};', new_text, re.S)
    assert defaults_block_m, "DEFAULTS block not found post-edit"
    defaults_keys = re.findall(r'(?:^|,)\s*([A-Za-z_][A-Za-z0-9_]*)\s*:', defaults_block_m.group(1))
    bad_defaults = [k for k in defaults_keys if k not in all_field_ids]
    note(f"  DEFAULTS keys: {len(defaults_keys)}, missing from DOC: {bad_defaults}")
    assert not bad_defaults, bad_defaults
    assert "brn_iv_lines" not in defaults_keys, "brn_iv_lines still in DEFAULTS"

    defaults_fn_block_m = re.search(r'const DEFAULTS_FN = \{(.*?)\n\};', new_text, re.S)
    assert defaults_fn_block_m
    defaults_fn_keys = re.findall(r'(?:^|,)\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*function',
                                   defaults_fn_block_m.group(1))
    bad_defaults_fn = [k for k in defaults_fn_keys if k not in all_field_ids]
    note(f"  DEFAULTS_FN keys: {defaults_fn_keys}, missing from DOC: {bad_defaults_fn}")
    assert not bad_defaults_fn, bad_defaults_fn

    # every carry map: both keys and values must exist as field ids
    bad_carry = []
    for lid, line in final_line_index.items():
        carry = line.get("carry")
        if carry:
            for k, v in carry.items():
                if k not in all_field_ids:
                    bad_carry.append((lid, "key", k))
                if v not in all_field_ids:
                    bad_carry.append((lid, "val", v))
    for bid, block in doc["blocks"].items():
        carry = (block.get("handoff") or {}).get("carry")
        if carry:
            for k, v in carry.items():
                if k not in all_field_ids:
                    bad_carry.append((f"{bid}.handoff", "key", k))
                if v not in all_field_ids:
                    bad_carry.append((f"{bid}.handoff", "val", v))
    note(f"  carry maps checked (line-level esc carries + blocks.ob.handoff): "
         f"bad references: {bad_carry}")
    assert not bad_carry, bad_carry

    SRC_TXT_FOR_GREP = new_text  # engine + DOC, post-edit
    still_present = [fid for fid in DELETED_LINE_IDS + DELETED_FIELD_IDS
                      if fid in SRC_TXT_FOR_GREP]
    note(f"  deleted ids still present anywhere in the file post-edit: {still_present}")
    assert not still_present, still_present

    note("\nAll assertions passed.")

    # ==================================================================
    # flattened-sentence report (raw render_token output, and a
    # hint-stripped version for easier comparison against the MD)
    # ==================================================================
    note("\n## Flattened sentences (render_token: choices show option LABELS, "
         "not expanded nested parts - see note above on trg_iv/abd_iv/alg_iv)")
    to_print = ["sh_12lead_line", "sh_iv_line", "card_acs_12l", "card_dys_monitor",
                "trg_iv", "met_dka_iv", "abd_iv", "alg_iv", "brn_iv",
                "neur_iv_reassess", "st_12lead_initial"]
    for lid in to_print:
        line = final_line_index[lid]
        raw = render_line(line)
        note(f"- `{lid}`:")
        note(f"    raw:           {raw}")
        note(f"    hint-stripped: {hint_stripped(raw)}")
    esc = final_line_index["card_acs_esc"]
    note("- `card_acs_esc`:")
    note(f"    normal: {render_parts(esc['normal'])}")
    note(f"    fired:  {render_parts(esc['fired'])}")


if __name__ == "__main__":
    main()
