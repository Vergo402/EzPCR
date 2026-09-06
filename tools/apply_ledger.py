#!/usr/bin/env python3
"""Apply field-ledger review decisions to the PCR Narrative Builder's embedded DOC.

Reads .claude/preview/decisions.json and edits "PCR Narrative Builder v1.html" in
place: parses the single line `window.__DOC__ = <json>;`, mutates the JSON per the
decisions (deletions, field edits, field reordering), writes it back on the same
line, and emits a report + a DEFAULTS patch + a per-line before/after change log
for the MD editor.

Stdlib only. See CLAUDE.md for the DOC-editing contract this respects.
"""
import argparse
import json
import re
import sys
from pathlib import Path

DOC_RE = re.compile(r'^(window\.__DOC__ = )(.*)(;\s*)$', re.M)

# Invisible marker embedded in literals at the exact point a token was deleted.
# Stripped out again before the JSON is written back; used only to let the
# clause-cleanup pass (rule B) know which text was touched by a deletion.
SENTINEL = "\x02"

CONNECTOR_TAIL_RE = re.compile(
    r'(\s*)(?:at|for|by|with|to|of|on|in|per|from|x|→)\s*$',
    re.IGNORECASE)

SANDWICH_LITERALS = {"/", ",", "and"}

COMMA_SUBCLAUSE_RE = re.compile(r',\s*([^,\x02]*?)' + SENTINEL + r',\s*')


# ---------------------------------------------------------------------------
# text tidy helpers (deletion rule 1)
# ---------------------------------------------------------------------------

def collapse(s):
    while True:
        new = (s.replace("  ", " ")
                 .replace(" ,", ",")
                 .replace(" .", ".")
                 .replace(" :", ":")
                 .replace(",.", ".")
                 .replace(":.", ".")
                 .replace("( ", "(")
                 .replace(" )", ")")
                 .replace("()", "")
                 .replace(", ,", ",")
                 .replace(" / ,", ","))
        if new == s:
            return new
        s = new


def normalize_join(a, b):
    return collapse(a + b)


def strip_trailing_connector_word(s):
    """Strip ONE trailing connector word (and its surrounding spaces) per
    rule 1: `\\s*(?:at|for|by|with|to|of|on|in|per|from|x|→)\\s*$`,
    case-insensitive. Never strips units (mg, mL, mcg, g, J, min) or content
    words, and never strips a mid-word match (e.g. the "x" in "box").
    """
    m = CONNECTOR_TAIL_RE.search(s)
    if not m:
        return s
    start = m.start()
    if start > 0 and m.group(1) == "" and s[start - 1].isalpha():
        # the "connector" is actually the tail of a longer word - leave alone
        return s
    return s[:start]


def is_sandwich_connector_literal(lit):
    return lit.strip().lower() in SANDWICH_LITERALS


def has_assertive_word(text):
    """True if text contains a real assertion (an ALL-CAPS word of length>=2,
    e.g. "LOST", "CCP") rather than being pure boilerplate/label text like
    "Suspected etiology" or "Fluids".
    """
    for w in re.findall(r"[A-Za-z]+", text):
        if len(w) >= 2 and w.isupper():
            return True
    return False


def strip_dead_comma_subclauses(text):
    """Rule B, comma sub-clause case: a bare, content-free phrase sandwiched
    between two commas because its one field was deleted (e.g. ", gait ,")
    gets dropped down to a single comma.
    """
    def repl(m):
        phrase = m.group(1)
        if has_assertive_word(phrase):
            return m.group(0)
        return ", "
    return COMMA_SUBCLAUSE_RE.sub(repl, text)


# ---------------------------------------------------------------------------
# rendering (for the report / md_changes.json)
# ---------------------------------------------------------------------------

def render_token(tok):
    if isinstance(tok, str):
        return tok
    if not isinstance(tok, dict):
        return ""
    if "f" in tok:
        s = "___"
        if tok.get("hint"):
            s += " {%s}" % tok["hint"]
        return s
    if "c" in tok:
        labels = []
        for o in tok["c"]:
            if isinstance(o, dict):
                labels.append(o.get("label", ""))
            else:
                labels.append(o)
        inner = " / ".join(labels)
        if tok.get("other"):
            inner += " / other…"
        s = "[%s]" % inner
        if tok.get("multi"):
            s += "{any that apply}"
        return s
    if "sum" in tok:
        return "___" + (tok.get("suffix") or "")
    if "aox" in tok:
        return "[AOx#]"
    if "g" in tok:
        return "(" + "".join(render_token(t) for t in tok["g"]) + ")"
    return ""


def render_parts(parts):
    return "".join(render_token(t) for t in parts)


def render_line(line):
    kind = line["kind"]
    if kind == "std":
        return render_parts(line["parts"])
    if kind == "tri":
        return "given: %s | withheld: %s" % (
            render_parts(line["given"]), render_parts(line["withheld"]))
    if kind == "esc":
        return "normal: %s | fired: %s" % (
            render_parts(line["normal"]), render_parts(line["fired"]))
    return ""


# ---------------------------------------------------------------------------
# DOC indexing
# ---------------------------------------------------------------------------

def parts_arrays(line):
    kind = line["kind"]
    if kind == "std":
        return [("parts", line["parts"])]
    if kind == "tri":
        return [("given", line["given"]), ("withheld", line["withheld"])]
    if kind == "esc":
        return [("normal", line["normal"]), ("fired", line["fired"])]
    return []


def index_lines(lines, container, line_index, container_of):
    for line in lines:
        line_index[line["id"]] = line
        container_of[line["id"]] = container
        if line["kind"] == "fork":
            for opt in line.get("options", []):
                index_lines(opt.get("lines", []), container, line_index, container_of)


def build_indices(doc):
    line_index = {}
    container_of = {}
    for bid, block in doc["blocks"].items():
        index_lines(block["lines"], bid, line_index, container_of)
        for sb in (block.get("subBlocks") or []):
            if sb:
                index_lines(sb["lines"], bid, line_index, container_of)
    for sec in doc["shell"]["sections"]:
        index_lines(sec["lines"], sec["id"], line_index, container_of)
    for dispo in doc["dispositions"]:
        index_lines(dispo["lines"], dispo["id"], line_index, container_of)
    for tid, tmpl in doc["templates"].items():
        index_lines(tmpl["lines"], tid, line_index, container_of)
    return line_index, container_of


# ---------------------------------------------------------------------------
# recursive token search (for label/hint/other/options/control edits)
# ---------------------------------------------------------------------------

def find_tokens(tokens, field_id, results):
    for i, tok in enumerate(tokens):
        if not isinstance(tok, dict):
            continue
        matched = False
        if "f" in tok and tok["f"] == field_id:
            matched = True
        elif "c" in tok and tok.get("id") == field_id:
            matched = True
        elif "sum" in tok and tok.get("id") == field_id:
            matched = True
        elif tok.get("aox") == field_id:
            matched = True
        if matched:
            results.append((tokens, i))
        if "c" in tok:
            for opt in tok["c"]:
                if isinstance(opt, dict) and "parts" in opt:
                    find_tokens(opt["parts"], field_id, results)
        if "g" in tok:
            find_tokens(tok["g"], field_id, results)


def find_field_locations(line, field_id):
    """Return list of (parent_list, index) across every parts array of line."""
    results = []
    for _name, arr in parts_arrays(line):
        find_tokens(arr, field_id, results)
    return results


def collect_field_ids(tokens, out):
    for tok in tokens:
        if not isinstance(tok, dict):
            continue
        if "f" in tok:
            out.add(tok["f"])
        if "c" in tok:
            if tok.get("id"):
                out.add(tok["id"])
            for opt in tok["c"]:
                if isinstance(opt, dict) and "parts" in opt:
                    collect_field_ids(opt["parts"], out)
        if "sum" in tok and tok.get("id"):
            out.add(tok["id"])
        if tok.get("aox"):
            out.add(tok["aox"])
        if "g" in tok:
            collect_field_ids(tok["g"], out)


def collect_all_field_ids(doc):
    out = set()
    line_index, _ = build_indices(doc)
    for line in line_index.values():
        for _name, arr in parts_arrays(line):
            collect_field_ids(arr, out)
    return out


# ---------------------------------------------------------------------------
# top-level field-id helper (rule D: aox/sum tokens count as fields too)
# ---------------------------------------------------------------------------

def is_field_like_toplevel(tok):
    if not isinstance(tok, dict):
        return False
    return ("f" in tok) or ("c" in tok and "id" in tok) or ("sum" in tok) or ("aox" in tok)


def toplevel_field_id(tok):
    """The id a top-level field-like token is addressed by in fieldOrder /
    decisions. `{f: id}` and `{c:..., id: id}` and `{sum:..., id: id}` all use
    `id`/`f`; `{aox: id}` stores its id under the "aox" key instead - missing
    that case was rule-D's bug (it dropped the aox token from every reorder).
    """
    return tok.get("f") or tok.get("id") or tok.get("aox")


# ---------------------------------------------------------------------------
# deletion pass (rule 1: connector tidy + sandwich-literal drop)
# ---------------------------------------------------------------------------

def collect_removed_by_parent(tok, out):
    if "c" in tok:
        for opt in tok["c"]:
            if isinstance(opt, dict) and "parts" in opt:
                for t in opt["parts"]:
                    if isinstance(t, dict):
                        if "f" in t:
                            out.add(t["f"])
                        elif t.get("id"):
                            out.add(t["id"])
                        collect_removed_by_parent(t, out)


def apply_deletions(tokens, deleted_fields, deleted_choices, removed_by_parent, removed_groups):
    n = len(tokens)
    removed = [False] * n
    for i, tok in enumerate(tokens):
        if isinstance(tok, dict):
            if "f" in tok and tok["f"] in deleted_fields:
                removed[i] = True
            elif "c" in tok and tok.get("id") in deleted_choices:
                removed[i] = True
                collect_removed_by_parent(tok, removed_by_parent)

    # a literal made up entirely of punctuation/connectors (" / ", ", ", " and ")
    # sandwiched between two removed tokens is dropped outright, not tidied
    drop_literal = [False] * n
    for i, tok in enumerate(tokens):
        if isinstance(tok, str) and is_sandwich_connector_literal(tok):
            prev_removed = i > 0 and removed[i - 1]
            next_removed = i + 1 < n and removed[i + 1]
            if prev_removed and next_removed:
                drop_literal[i] = True

    output = []
    pending_merge = False
    for i, tok in enumerate(tokens):
        if removed[i]:
            if output and isinstance(output[-1], str):
                output[-1] = strip_trailing_connector_word(output[-1]) + SENTINEL
            else:
                output.append(SENTINEL)
            pending_merge = True
            continue

        if isinstance(tok, str):
            if drop_literal[i]:
                pending_merge = True
                continue
            if pending_merge:
                if output and isinstance(output[-1], str):
                    output[-1] = normalize_join(output[-1], tok)
                else:
                    output.append(tok)
                pending_merge = False
            else:
                output.append(tok)
            continue

        if not isinstance(tok, dict):
            output.append(tok)
            pending_merge = False
            continue

        pending_merge = False

        if "c" in tok:
            new_opts = []
            for opt in tok["c"]:
                if isinstance(opt, dict) and "parts" in opt:
                    opt2 = dict(opt)
                    opt2["parts"] = apply_deletions(
                        opt["parts"], deleted_fields, deleted_choices,
                        removed_by_parent, removed_groups)
                    new_opts.append(opt2)
                else:
                    new_opts.append(opt)
            tok2 = dict(tok)
            tok2["c"] = new_opts
            output.append(tok2)
            continue

        if "g" in tok:
            inner = apply_deletions(tok["g"], deleted_fields, deleted_choices,
                                     removed_by_parent, removed_groups)
            has_nonliteral = any(isinstance(t, dict) for t in inner)
            if not has_nonliteral:
                removed_groups.append(tok)
                if output and isinstance(output[-1], str):
                    output[-1] = strip_trailing_connector_word(output[-1]) + SENTINEL
                else:
                    output.append(SENTINEL)
                pending_merge = True
                continue
            tok2 = dict(tok)
            tok2["g"] = inner
            output.append(tok2)
            continue

        output.append(tok)

    return output


# ---------------------------------------------------------------------------
# clause cleanup pass (rule B)
# ---------------------------------------------------------------------------

def split_into_sentences(arr):
    """Split a top-level parts array into sentence segments at '. '
    boundaries. Each segment is a list of the original elements (literal
    fragments and/or tokens) that make it up, and (except the last) ends
    with its own trailing ". " separator literal.
    """
    sentences = [[]]
    for el in arr:
        if isinstance(el, str):
            pieces = el.split(". ")
            for k, piece in enumerate(pieces):
                if k > 0:
                    sentences[-1].append(". ")
                    sentences.append([])
                if piece:
                    sentences[-1].append(piece)
        else:
            sentences[-1].append(el)
    return sentences


def clause_cleanup(arr):
    """Rule B: after rule-1 deletions, drop (or flag) any clause that
    contained a removed field and is now left with no field tokens at all.
    Returns (new_arr, flags).
    """
    sentences = split_into_sentences(arr)
    flags = []
    keep_mask = [True] * len(sentences)
    only_clause = len(sentences) == 1

    for idx, seg in enumerate(sentences):
        has_token = any(isinstance(e, dict) for e in seg)
        text = "".join(e for e in seg if isinstance(e, str))
        if has_token or SENTINEL not in text:
            continue
        clean = text.replace(SENTINEL, "")
        stripped = clean.strip().rstrip(".:,; ")
        if only_clause:
            flags.append("needs-review")
            flags.append("no-blanks-left")
            continue
        if stripped and has_assertive_word(stripped):
            continue  # real content survives (e.g. "Pulses LOST") - keep
        keep_mask[idx] = False
        flags.append("clause-dropped")

    new_arr = []
    for idx, seg in enumerate(sentences):
        if keep_mask[idx]:
            new_arr.extend(seg)

    # comma sub-clause cleanup within sentences that were kept (still have
    # other tokens) but contain a now-bare, content-free comma sub-clause
    cleaned = []
    for el in new_arr:
        if isinstance(el, str) and SENTINEL in el:
            el = strip_dead_comma_subclauses(el)
        cleaned.append(el)

    # strip remaining sentinels and re-collapse each literal
    final_arr = []
    for el in cleaned:
        if isinstance(el, str):
            final_arr.append(collapse(el.replace(SENTINEL, "")))
        else:
            final_arr.append(el)

    # merge any literals left adjacent by a dropped clause
    merged = []
    for el in final_arr:
        if isinstance(el, str) and merged and isinstance(merged[-1], str):
            merged[-1] = collapse(merged[-1] + el)
        else:
            merged.append(el)

    # trim a dangling trailing space left by a dropped final clause
    if merged and isinstance(merged[-1], str):
        merged[-1] = merged[-1].rstrip(" ")

    merged = [e for e in merged if not (isinstance(e, str) and e == "")]

    return merged, flags


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--decisions", default=".claude/preview/decisions.json")
    ap.add_argument("--src", default="PCR Narrative Builder v1.html")
    args = ap.parse_args()

    decisions = json.loads(Path(args.decisions).read_text(encoding="utf-8"))
    src_path = Path(args.src)
    text = src_path.read_text(encoding="utf-8")
    m = DOC_RE.search(text)
    if not m:
        print("ERROR: could not find window.__DOC__ line", file=sys.stderr)
        sys.exit(1)
    doc = json.loads(m.group(2))

    line_index, container_of = build_indices(doc)

    report = []          # list of markdown lines
    defaults_patch = {}
    md_changes = []
    changed_line_ids = set()
    counts = {
        "deleted_fields": 0, "deleted_choices": 0, "skipped_deletes": 0,
        "labels": 0, "controls": 0, "options": 0, "other": 0, "hint": 0,
        "preselect": 0, "field_order": 0, "carry_removed": 0, "skipped": 0,
    }

    def note(msg):
        report.append(msg)

    # -- group deletions by line ---------------------------------------
    per_line_deleted_fields = {}
    per_line_deleted_choices = {}
    other_flag_clears = []  # (line_id, parent_choice_id)

    for rec in decisions.get("deleted", []):
        field = rec["field"]
        line_id = rec["line"]
        meta = rec.get("meta", {})
        line = line_index.get(line_id)
        if line is None:
            note(f"- SKIP delete `{field}` on `{line_id}`: line not found")
            counts["skipped_deletes"] += 1
            continue
        if field.endswith("__other"):
            parent_id = field[: -len("__other")]
            other_flag_clears.append((line_id, parent_id, field))
            continue
        if meta.get("type") in ("pills", "chips"):
            per_line_deleted_choices.setdefault(line_id, set()).add(field)
        else:
            per_line_deleted_fields.setdefault(line_id, set()).add(field)

    removed_by_parent_all = set()
    removed_groups_all = []

    for line_id in set(list(per_line_deleted_fields) + list(per_line_deleted_choices)):
        line = line_index[line_id]
        dfields = per_line_deleted_fields.get(line_id, set())
        dchoices = per_line_deleted_choices.get(line_id, set())
        before = render_line(line)
        removed_by_parent = set()
        removed_groups = []
        line_flags = []
        for name, arr in parts_arrays(line):
            new_arr = apply_deletions(arr, dfields, dchoices, removed_by_parent, removed_groups)
            new_arr, arr_flags = clause_cleanup(new_arr)
            for f in arr_flags:
                if f not in line_flags:
                    line_flags.append(f)
            arr[:] = new_arr
        after = render_line(line)
        changed_line_ids.add(line_id)
        counts["deleted_fields"] += len(dfields)
        counts["deleted_choices"] += len(dchoices)
        removed_by_parent_all |= removed_by_parent
        removed_groups_all.extend(removed_groups)

        notes = []
        if dfields:
            notes.append("deleted fields: " + ", ".join(sorted(dfields)))
        if dchoices:
            notes.append("deleted choices: " + ", ".join(sorted(dchoices)))
        if removed_by_parent:
            notes.append("removed-by-parent: " + ", ".join(sorted(removed_by_parent)))
        if removed_groups:
            notes.append(f"{len(removed_groups)} empty group(s) removed")

        has_field = False
        for _n, arr in parts_arrays(line):
            has_field = has_field or any(is_field_like_toplevel(t) or
                                          (isinstance(t, dict) and "g" in t and
                                           any(is_field_like_toplevel(x) for x in t["g"]))
                                          for t in arr)
        if not has_field:
            notes.append("line now has no blanks — Alex to decide keep/drop")
            if "no-blanks-left" not in line_flags:
                line_flags.append("no-blanks-left")

        md_changes.append({
            "lineId": line_id, "container": container_of.get(line_id),
            "label": line.get("label"), "before": before, "after": after,
            "notes": notes, "flags": line_flags,
        })
        note(f"- delete on `{line_id}` ({container_of.get(line_id)}): {', '.join(notes) if notes else ''}")
        note(f"  before: {before}")
        note(f"  after:  {after}")
        if line_flags:
            note(f"  flags:  {', '.join(line_flags)}")

    # -- rule 3: __other clears -----------------------------------------
    for line_id, parent_id, field in other_flag_clears:
        line = line_index.get(line_id)
        if line is None:
            note(f"- SKIP `{field}`: line `{line_id}` not found")
            counts["skipped"] += 1
            continue
        locs = find_field_locations(line, parent_id)
        if not locs:
            note(f"- SKIP `{field}`: parent choice `{parent_id}` not found")
            counts["skipped"] += 1
            continue
        for parent_list, idx in locs:
            tok = parent_list[idx]
            if "other" in tok:
                del tok["other"]
        changed_line_ids.add(line_id)
        note(f"- cleared other:true on `{parent_id}` (via `{field}`) on line `{line_id}`")

    # -- reusable helper to fetch decision records ----------------------
    field_recs = decisions.get("fields", [])

    def get_options_now(tok):
        if "c" in tok:
            return tok["c"]
        return None

    def has_scored_options(opts):
        """Scored options (`{label, v}`, optionally with score:true on the
        token) are a different mechanism than plain/nested-parts options and
        are never touched by the merge logic below - still skipped outright."""
        for o in opts:
            if isinstance(o, dict) and "v" in o:
                return True
        return False

    def opt_label(o):
        return o if isinstance(o, str) else (o.get("label") or "")

    def opt_has_parts(o):
        return isinstance(o, dict) and "parts" in o

    def norm_label(s):
        return re.sub(r"\s+", " ", s.strip()).lower()

    def merge_options(existing, requested):
        """Merge a requested option-label list into the existing options
        list. Scored entries must never reach here (callers filter those out
        via has_scored_options). Returns (new_list, events) where events is
        a list of dicts describing what happened to each entry, for the
        merge report.
        """
        n = len(existing)
        consumed = [False] * n
        matched_idx = [None] * len(requested)

        def find_unconsumed(pred):
            for i, o in enumerate(existing):
                if not consumed[i] and pred(o):
                    return i
            return None

        # phase 1: exact match, case-insensitive / whitespace-trimmed
        for ri, r in enumerate(requested):
            rn = norm_label(r)
            idx = find_unconsumed(lambda o: norm_label(opt_label(o)) == rn)
            if idx is not None:
                matched_idx[ri] = idx
                consumed[idx] = True

        # phase 2: containment match (one label a substring of the other) -
        # catches "casualty collection point" <-> "...at ___", "focused" <->
        # "focused exam", "secured" <-> "secured at ___"
        for ri, r in enumerate(requested):
            if matched_idx[ri] is not None:
                continue
            rn = norm_label(r)

            def pred(o, rn=rn):
                en = norm_label(opt_label(o))
                return en != "" and (en in rn or rn in en)

            idx = find_unconsumed(pred)
            if idx is not None:
                matched_idx[ri] = idx
                consumed[idx] = True

        # phase 3: exactly-one-unmatched-each-side fallback (arbitrary pairing)
        remaining_req = [ri for ri in range(len(requested)) if matched_idx[ri] is None]
        remaining_exist = [i for i in range(n) if not consumed[i]]
        if len(remaining_req) == 1 and len(remaining_exist) == 1:
            ri, idx = remaining_req[0], remaining_exist[0]
            matched_idx[ri] = idx
            consumed[idx] = True

        events = []
        new_list = []
        for ri, r in enumerate(requested):
            idx = matched_idx[ri]
            if idx is None:
                new_list.append(r)
                events.append({"type": "added", "new": r})
                continue
            o = existing[idx]
            old_label = opt_label(o)
            if isinstance(o, dict):
                entry = dict(o)
                if entry.get("label") != r:
                    entry["label"] = r
                    events.append({"type": "renamed", "old": old_label, "new": r,
                                    "parts": opt_has_parts(o)})
                else:
                    events.append({"type": "kept", "old": old_label, "new": r,
                                    "parts": opt_has_parts(o)})
                new_list.append(entry)
            else:
                if old_label != r:
                    events.append({"type": "renamed", "old": old_label, "new": r, "parts": False})
                else:
                    events.append({"type": "kept", "old": old_label, "new": r, "parts": False})
                new_list.append(r)

        for i in range(n):
            if not consumed[i]:
                o = existing[i]
                events.append({"type": "removed", "old": opt_label(o), "parts": opt_has_parts(o)})

        return new_list, events

    options_merge_reports = []  # (field, old_labels, new_labels, events) for the printed report

    # order matters: label(4) control(5) options(6) other(7) hint(8) preselect(9)
    for rec in field_recs:
        field = rec["field"]
        line_id = rec["line"]
        meta = rec.get("meta", {})
        dec = rec.get("decision", {})
        line = line_index.get(line_id)
        if line is None:
            note(f"- SKIP `{field}`: line `{line_id}` not found")
            counts["skipped"] += 1
            continue
        if field.endswith("__other"):
            note(f"- SKIP `{field}`: synthetic __other id, not directly editable")
            counts["skipped"] += 1
            continue

        locs = find_field_locations(line, field)
        if not locs:
            note(f"- SKIP `{field}` on `{line_id}`: field token not found (deleted or renamed?)")
            counts["skipped"] += 1
            continue

        touched = False

        # 4. label
        if "label" in dec:
            for parent_list, idx in locs:
                parent_list[idx]["q"] = dec["label"]
            counts["labels"] += 1
            touched = True

        # 5. control
        if "control" in dec:
            new_control = dec["control"]
            old_type = meta.get("type")
            new_locs = []
            for parent_list, idx in locs:
                tok = parent_list[idx]
                if new_control in ("pills", "chips") and "f" in tok:
                    opts = dec.get("options") or meta.get("options")
                    if not opts:
                        note(f"- SKIP control change on `{field}`: no options available")
                        counts["skipped"] += 1
                        new_locs.append((parent_list, idx))
                        continue
                    new_tok = {"c": opts, "id": field}
                    if new_control == "chips":
                        new_tok["multi"] = True
                    if "req" in tok:
                        new_tok["req"] = tok["req"]
                    if "hint" in tok:
                        new_tok["hint"] = tok["hint"]
                    if "q" in tok:
                        new_tok["q"] = tok["q"]
                    parent_list[idx] = new_tok
                    new_locs.append((parent_list, idx))
                elif new_control in ("pills", "chips") and "c" in tok:
                    tok["multi"] = (new_control == "chips")
                    new_locs.append((parent_list, idx))
                elif new_control == "text" and "c" in tok:
                    new_tok = {"f": field}
                    if "req" in tok:
                        new_tok["req"] = tok["req"]
                    if "hint" in tok:
                        new_tok["hint"] = tok["hint"]
                    if "q" in tok:
                        new_tok["q"] = tok["q"]
                    parent_list[idx] = new_tok
                    new_locs.append((parent_list, idx))
                else:
                    new_locs.append((parent_list, idx))
            locs = new_locs
            counts["controls"] += 1
            touched = True

        # 6. options
        if "options" in dec:
            applied_options = False
            skipped_options = False
            for parent_list, idx in locs:
                tok = parent_list[idx]
                if "c" not in tok:
                    continue
                cur = get_options_now(tok)
                if cur is not None and has_scored_options(cur):
                    skipped_options = True
                    continue
                old_labels = [opt_label(o) for o in cur] if cur else []
                new_list, events = merge_options(cur or [], dec["options"])
                tok["c"] = new_list
                new_labels = [opt_label(o) for o in new_list]
                options_merge_reports.append({
                    "field": field, "line": line_id,
                    "old": old_labels, "new": new_labels, "events": events,
                })
                applied_options = True
            if skipped_options and not applied_options:
                note(f"- SKIP options change on `{field}`: existing options contain "
                     f"scored entries")
                counts["skipped"] += 1
            if applied_options:
                counts["options"] += 1
                touched = True
                ev_bits = []
                for ev in events:
                    if ev["type"] == "kept":
                        ev_bits.append(f"kept \"{ev['new']}\"" + (" (nested parts)" if ev["parts"] else ""))
                    elif ev["type"] == "renamed":
                        ev_bits.append(f"renamed \"{ev['old']}\" -> \"{ev['new']}\"" +
                                        (" (kept nested parts)" if ev["parts"] else ""))
                    elif ev["type"] == "removed":
                        ev_bits.append(f"removed \"{ev['old']}\"" + (" (had nested blanks)" if ev["parts"] else ""))
                    elif ev["type"] == "added":
                        ev_bits.append(f"added \"{ev['new']}\" (new plain option)")
                note(f"- MERGED options on `{field}` ({line_id}): {old_labels} -> {new_labels}")
                note(f"  {'; '.join(ev_bits)}")

        # 7. other
        if "other" in dec:
            for parent_list, idx in locs:
                tok = parent_list[idx]
                if "c" not in tok:
                    continue
                if dec["other"]:
                    tok["other"] = True
                else:
                    tok.pop("other", None)
            counts["other"] += 1
            touched = True

        # 8. hint
        if "hint" in dec:
            for parent_list, idx in locs:
                parent_list[idx]["hint"] = dec["hint"]
            counts["hint"] += 1
            touched = True

        # 9. preselect -> defaults_patch only
        if "preselect" in dec:
            values = dec["preselect"]
            plist0, idx0 = locs[0]
            tok = plist0[idx0]
            multi = bool(tok.get("multi")) if isinstance(tok, dict) else False
            opts_now = get_options_now(tok) if isinstance(tok, dict) else None
            opt_labels = set()
            if opts_now:
                for o in opts_now:
                    if isinstance(o, dict):
                        opt_labels.add(o.get("label"))
                    else:
                        opt_labels.add(o)
            bad = [v for v in values if v not in opt_labels]
            if bad:
                note(f"- SKIP preselect on `{field}`: value(s) {bad} not in current options")
                counts["skipped"] += 1
            else:
                defaults_patch[field] = values if multi else values[0]
                counts["preselect"] += 1
                touched = True

        if touched:
            changed_line_ids.add(line_id)
            note(f"- updated `{field}` on `{line_id}`: {sorted(dec.keys())}")

    # -- 10. fieldOrder ---------------------------------------------------
    for rec in decisions.get("fieldOrder", []):
        line_id = rec["line"]
        requested = rec["order"]
        line = line_index.get(line_id)
        if line is None:
            note(f"- SKIP fieldOrder on `{line_id}`: line not found")
            counts["skipped"] += 1
            continue
        any_change = False
        before = render_line(line)
        for _name, arr in parts_arrays(line):
            # compute the DOC's own top-level order first; a requested order
            # that, once filtered down to top-level ids, matches it is a
            # no-op - the request only moved nested (choice-option) fields.
            current_ids = [toplevel_field_id(t) for t in arr if is_field_like_toplevel(t)]
            filtered_request = [f for f in requested if f in current_ids]
            if not filtered_request or filtered_request == current_ids:
                continue
            # build (literal-before, token) chunks
            chunks = {}
            pending_lit = ""
            trailing = ""
            order_seen = []
            for tok in arr:
                if is_field_like_toplevel(tok):
                    fid = toplevel_field_id(tok)
                    chunks[fid] = (pending_lit, tok)
                    order_seen.append(fid)
                    pending_lit = ""
                elif isinstance(tok, str):
                    pending_lit += tok
                else:
                    # unexpected non-field dict at top level; leave whole reorder alone
                    chunks = None
                    break
            if chunks is None:
                note(f"- SKIP fieldOrder on `{line_id}`/{_name}: non-field token present, "
                     f"reorder not attempted")
                counts["skipped"] += 1
                continue
            trailing = pending_lit
            new_arr = []
            for fid in filtered_request:
                lit, tok = chunks[fid]
                if lit:
                    if new_arr and isinstance(new_arr[-1], str):
                        new_arr[-1] = collapse(new_arr[-1] + lit)
                    else:
                        new_arr.append(lit)
                new_arr.append(tok)
            if trailing:
                if new_arr and isinstance(new_arr[-1], str):
                    new_arr[-1] = collapse(new_arr[-1] + trailing)
                else:
                    new_arr.append(trailing)
            arr[:] = new_arr
            any_change = True
        after = render_line(line)
        if any_change:
            changed_line_ids.add(line_id)
            counts["field_order"] += 1
            md_changes.append({
                "lineId": line_id, "container": container_of.get(line_id),
                "label": line.get("label"), "before": before, "after": after,
                "notes": ["needs-review: field order changed, connectors may read oddly"],
                "flags": ["needs-review"],
            })
            note(f"- REORDERED fields on `{line_id}` (needs-review)")
            note(f"  before: {before}")
            note(f"  after:  {after}")
        else:
            note(f"- fieldOrder on `{line_id}`: no change "
                 f"(requested order only touched nested/non-top-level ids, or already matched)")

    # -- 11. carry / targets cleanup --------------------------------------
    all_field_ids_now = collect_all_field_ids(doc)
    for line in line_index.values():
        if line.get("kind") != "esc":
            continue
        carry = line.get("carry")
        if not carry:
            continue
        for key in list(carry.keys()):
            val = carry[key]
            if key not in all_field_ids_now or val not in all_field_ids_now:
                del carry[key]
                counts["carry_removed"] += 1
                note(f"- removed stale carry entry on `{line['id']}`: `{key}` -> `{val}`")

    # -- 12. version marker -------------------------------------------------
    doc["meta"]["source"] = "v0.11"

    # -- held/unreviewed --------------------------------------------------
    for rec in decisions.get("heldUnreviewed", []):
        note(f"- HELD (unreviewed, no change applied): `{rec['field']}` on `{rec['line']}`")

    # -- assertions ---------------------------------------------------------
    doc_json = json.dumps(doc, ensure_ascii=False, separators=(",", ":"))
    reparsed = json.loads(doc_json)
    assert reparsed == doc
    assert SENTINEL not in doc_json, "sentinel leaked into DOC JSON"

    all_deleted_ids = set()
    for s in per_line_deleted_fields.values():
        all_deleted_ids |= s
    for s in per_line_deleted_choices.values():
        all_deleted_ids |= s
    all_deleted_ids |= removed_by_parent_all
    all_deleted_ids.add("card_acs_fluid_amt")

    leaked = [fid for fid in all_deleted_ids if fid in doc_json]
    if leaked:
        print("ERROR: deleted field ids still present in DOC:", leaked, file=sys.stderr)
        sys.exit(1)

    # -- write file back ------------------------------------------------
    new_line = m.group(1) + doc_json + m.group(3)
    new_text = text[: m.start()] + new_line + text[m.end():]
    src_path.write_text(new_text, encoding="utf-8")

    # confirm reparse from disk
    text2 = src_path.read_text(encoding="utf-8")
    m2 = DOC_RE.search(text2)
    json.loads(m2.group(2))

    # -- write outputs ----------------------------------------------------
    preview_dir = Path(args.decisions).parent
    report_path = preview_dir / "apply-report.md"
    defaults_path = preview_dir / "defaults_patch.json"
    md_changes_path = preview_dir / "md_changes.json"

    flagged_lines = [c["lineId"] for c in md_changes if c.get("flags")]

    report_header = [
        "# Ledger apply report (v0.11)",
        "",
        f"Deleted fields: {counts['deleted_fields']}  ",
        f"Deleted choices: {counts['deleted_choices']}  ",
        f"Removed-by-parent fields: {len(removed_by_parent_all)}  ",
        f"Empty groups removed: {len(removed_groups_all)}  ",
        f"Labels changed: {counts['labels']}  ",
        f"Controls changed: {counts['controls']}  ",
        f"Options changed: {counts['options']}  ",
        f"Other flag changed: {counts['other']}  ",
        f"Hints changed: {counts['hint']}  ",
        f"Preselect defaults written: {counts['preselect']}  ",
        f"Field orders changed: {counts['field_order']}  ",
        f"Carry entries removed: {counts['carry_removed']}  ",
        f"Skipped/held items: {counts['skipped'] + counts['skipped_deletes']}  ",
        f"Lines changed: {len(changed_line_ids)}  ",
        f"Flagged lines: {', '.join(flagged_lines) if flagged_lines else '(none)'}",
        "",
        "## Options merges",
        "",
    ]
    for rep in options_merge_reports:
        report_header.append(f"- `{rep['field']}` ({rep['line']}): {rep['old']} -> {rep['new']}")
        for ev in rep["events"]:
            if ev["type"] == "kept":
                report_header.append(f"  - kept \"{ev['new']}\"" + (" (nested parts preserved)" if ev["parts"] else ""))
            elif ev["type"] == "renamed":
                report_header.append(f"  - renamed \"{ev['old']}\" -> \"{ev['new']}\"" +
                                      (" (kept nested parts)" if ev["parts"] else ""))
            elif ev["type"] == "removed":
                report_header.append(f"  - removed \"{ev['old']}\"" + (" (had nested blanks)" if ev["parts"] else ""))
            elif ev["type"] == "added":
                report_header.append(f"  - added \"{ev['new']}\" (new plain option)")
    report_header += ["", "## Details", ""]
    full_report = report_header + report

    report_path.write_text("\n".join(full_report) + "\n", encoding="utf-8")
    defaults_path.write_text(json.dumps(defaults_patch, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                              encoding="utf-8")
    md_changes_path.write_text(json.dumps(md_changes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Counts:", json.dumps(counts, indent=2))
    print()
    print("\n".join(full_report[:40]))


if __name__ == "__main__":
    main()
