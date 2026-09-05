#!/usr/bin/env python3
"""Extract a flat "review model" JSON from the PCR Narrative Builder's embedded DOC.

Reads the `window.__DOC__ = {...};` line out of the builder HTML, walks the
sections/blocks/templates/dispositions, and emits a normalized structure of
containers -> lines -> sentence tokens + fields, suitable for reviewing the
whole document's content without the HTML/JS scaffolding.
"""
import argparse
import json
import re
import sys
from datetime import datetime, timezone

def fix_literal(s):
    return s.replace("35M___", "35M")


def derive_label(field_id, line_id):
    """Strip the line's domain prefix (first '_' token) from field_id, then
    turn underscores into spaces. e.g. neur_gcs_e under line neur_gcs -> 'gcs e'.
    This mirrors the worksheet's row label; the DOC hint is kept separately."""
    prefix = line_id.split("_", 1)[0] + "_"
    stripped = field_id[len(prefix):] if field_id.startswith(prefix) else field_id
    return stripped.replace("_", " ")


def dedupe_fields(fields):
    seen = {}
    out = []
    for f in fields:
        if f["id"] in seen:
            continue
        seen[f["id"]] = True
        out.append(f)
    return out


ROUGH_LEAD_WORDS = {"for", "at", "and", "with", "to", "of", "in", "on", "by", "x", "w/"}


def split_clauses(sentence):
    """Split sentence tokens into clauses at '. '-style sentence boundaries
    inside literals (commas/parens/'and' do not split)."""
    clauses = []
    current = []

    def close_current():
        if current:
            clauses.append(list(current))
            del current[:]

    n = len(sentence)
    for idx, tok in enumerate(sentence):
        if isinstance(tok, dict):
            current.append(tok)
            continue
        remaining = tok
        while True:
            pos = remaining.find(". ")
            if pos == -1:
                break
            head = remaining[:pos + 1]
            tail = remaining[pos + 2:]
            if head:
                current.append(head)
            close_current()
            remaining = tail
        if remaining:
            current.append(remaining)
        has_more_after = idx < n - 1
        stripped = remaining.rstrip()
        if stripped and stripped[-1] in ".?" and has_more_after:
            close_current()
    close_current()
    return clauses


def render_clause(tokens):
    """Join clause tokens to raw text (fields as {full field id}); also
    return the field id order and the leading literal before the first field."""
    parts = []
    field_ids = []
    leading_parts = []
    seen_field = False
    for tok in tokens:
        if isinstance(tok, dict):
            fid = tok["field"]
            parts.append("{%s}" % fid)
            field_ids.append(fid)
            seen_field = True
        else:
            parts.append(tok)
            if not seen_field:
                leading_parts.append(tok)
    raw = re.sub(r"\s+", " ", "".join(parts)).strip()
    leading = re.sub(r"\s+", " ", "".join(leading_parts)).strip()
    return raw, field_ids, leading


def is_rough(leading):
    if leading == "":
        return True
    words = leading.split()
    return len(words) <= 2 and all(w.lower() in ROUGH_LEAD_WORDS for w in words)


def finalize_text(raw):
    text = raw
    if text:
        text = text[0].upper() + text[1:]
    if text and text[-1] not in ".?!":
        text += "."
    return text


def build_fragment(tokens, field_map):
    """Build one fragment from a clause's tokens; (None, raw) if fieldless."""
    raw, field_ids, leading = render_clause(tokens)
    if not field_ids:
        return None, raw
    owner = field_ids[0]
    rough = is_rough(leading)
    if rough:
        label = field_map.get(owner, {}).get("label", owner)
        label_cap = (label[0].upper() + label[1:]) if label else owner
        frag = {
            "owner": owner,
            "fields": field_ids,
            "text": "%s: {%s}." % (label_cap, owner),
            "rough": True,
            "docExcerpt": raw,
        }
    else:
        frag = {
            "owner": owner,
            "fields": field_ids,
            "text": finalize_text(raw),
            "rough": False,
        }
    return frag, raw


def build_fragments(sentence, field_map):
    """One fragment per fielded clause; fieldless clauses are merged into the
    previous fragment's text (space-joined), or dropped if there is none."""
    fragments = []
    for tokens in split_clauses(sentence):
        frag, raw = build_fragment(tokens, field_map)
        if frag is not None:
            fragments.append(frag)
        elif raw and fragments:
            prev = fragments[-1]
            combined = re.sub(r"\s+", " ", prev["text"].rstrip(".?!") + " " + raw).strip()
            prev["text"] = finalize_text(combined)
    return fragments


def parse_parts(parts, line_id, fields_out, depth=1):
    """Recursively flatten a parts list into sentence tokens, collecting field
    descriptors into fields_out as a side effect."""
    sentence = []
    for part in parts or []:
        if isinstance(part, str):
            sentence.append(fix_literal(part))
            continue
        if not isinstance(part, dict):
            continue

        if "g" in part:
            sentence.extend(parse_parts(part["g"], line_id, fields_out, depth))
        elif "f" in part:
            fid = part["f"]
            entry = {
                "id": fid,
                "type": "text",
                "label": derive_label(fid, line_id),
                "req": part.get("req", False),
            }
            if part.get("hint"):
                entry["hint"] = part["hint"]
            if depth > 1:
                entry["depth"] = depth
            fields_out.append(entry)
            sentence.append({"field": fid})
        elif "sum" in part:
            fid = part["id"]
            entry = {"id": fid, "type": "sum", "label": derive_label(fid, line_id)}
            if depth > 1:
                entry["depth"] = depth
            fields_out.append(entry)
            sentence.append({"field": fid})
        elif "aox" in part:
            fid = part["aox"]
            entry = {"id": fid, "type": "aox", "label": derive_label(fid, line_id)}
            if depth > 1:
                entry["depth"] = depth
            fields_out.append(entry)
            sentence.append({"field": fid})
        elif "c" in part:
            fid = part["id"]
            ftype = "chips" if part.get("multi") else "pills"
            options = []
            for opt in part["c"]:
                if isinstance(opt, str):
                    options.append(opt)
                elif isinstance(opt, dict) and "parts" in opt:
                    options.append(opt.get("label", ""))
                    parse_parts(opt["parts"], line_id, fields_out, depth=2)
                elif isinstance(opt, dict):
                    options.append(opt.get("label", str(opt)))
                else:
                    options.append(str(opt))
            entry = {
                "id": fid,
                "type": ftype,
                "label": derive_label(fid, line_id),
                "options": options,
                "req": part.get("req", False),
            }
            if part.get("hint"):
                entry["hint"] = part["hint"]
            if depth > 1:
                entry["depth"] = depth
            fields_out.append(entry)
            sentence.append({"field": fid})
            if part.get("other"):
                fields_out.append({"id": f"{fid}__other", "type": "text", "label": "other"})
        # unknown part shape: skip silently
    return sentence


def parse_line(line):
    lid = line.get("id", "")
    kind = line.get("kind")
    label = line.get("label", "")
    ref = {"id": lid, "kind": kind, "label": label}
    if line.get("note"):
        ref["note"] = line["note"]

    fields = []
    alt_keys = {"tri": ("given", "withheld"), "esc": ("normal", "fired")}
    if kind in alt_keys:
        main_key, alt_key = alt_keys[kind]
        alt_fields = []
        ref["sentence"] = parse_parts(line.get(main_key, []), lid, fields)
        ref["sentenceAlt"] = parse_parts(line.get(alt_key, []), lid, alt_fields)
        fields = dedupe_fields(fields + alt_fields)
    elif kind == "fork":
        ref["sentence"] = [label]
        fields = [{
            "id": lid,
            "type": "fork",
            "label": label,
            "options": [opt.get("label", "") for opt in line.get("options", [])],
        }]
        ref["children"] = [
            {"groupLabel": opt.get("label", ""), "lines": [parse_line(l) for l in opt.get("lines", [])]}
            for opt in line.get("options", [])
        ]
    else:
        # 'std' and any unknown kind: sentence from parts if present, else empty
        ref["sentence"] = parse_parts(line.get("parts", []), lid, fields)

    ref["fields"] = fields

    field_map = {f["id"]: f for f in fields}
    ref["fragments"] = build_fragments(ref.get("sentence", []), field_map)
    if "sentenceAlt" in ref:
        alt_frag, _ = build_fragment(ref["sentenceAlt"], field_map)
        if alt_frag is not None:
            ref["fragmentsAlt"] = [alt_frag]

    return ref


def sub_block_line(sb):
    return {
        "id": sb["id"],
        "kind": "sub",
        "label": sb.get("name", ""),
        "sentence": [],
        "fields": [],
        "fragments": [],
        "children": [{
            "groupId": sb["id"],
            "groupLabel": sb.get("name", ""),
            "lines": [parse_line(l) for l in sb.get("lines", [])],
        }],
    }


def container_lines(entry):
    lines = [parse_line(l) for l in entry.get("lines", [])]
    for sb in entry.get("subBlocks") or []:
        if sb:
            lines.append(sub_block_line(sb))
    return lines


def natural_num_key(num):
    m = re.match(r"^(\d+)(.*)$", str(num))
    if m:
        return (int(m.group(1)), m.group(2))
    return (float("inf"), str(num))


def load_doc(src_path):
    with open(src_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("window.__DOC__"):
                s = line.strip()[len("window.__DOC__ = "):].rstrip(";")
                return json.loads(s)
    raise RuntimeError("window.__DOC__ line not found in source file")


def build_containers(doc):
    containers = []

    for sec in doc["shell"]["sections"]:
        containers.append({
            "id": sec["id"], "kind": "shell", "num": None,
            "name": sec.get("name", ""), "lines": container_lines(sec),
        })

    blocks = sorted(doc["blocks"].values(), key=lambda b: natural_num_key(b.get("num")))
    for b in blocks:
        containers.append({
            "id": b["id"], "kind": "block", "num": b.get("num"),
            "name": b.get("name", ""), "lines": container_lines(b),
        })

    templates = sorted(doc["templates"].values(), key=lambda t: natural_num_key(t.get("num")))
    for t in templates:
        containers.append({
            "id": t["id"], "kind": "template", "num": t.get("num"),
            "name": t.get("name", ""), "lines": container_lines(t),
        })

    for d in doc["dispositions"]:
        containers.append({
            "id": d["id"], "kind": "dispo", "num": None,
            "name": d.get("name", ""), "lines": container_lines(d),
        })

    return containers


def count_fields(lines):
    total = 0
    for l in lines:
        total += len(l.get("fields", []))
        for child in l.get("children", []):
            total += count_fields(child.get("lines", []))
    return total


def count_fragments(lines):
    """Return (total_fragments, rough_count), incl. `fragmentsAlt`, recursively."""
    total = 0
    rough = 0
    for l in lines:
        for frags in (l.get("fragments") or [], l.get("fragmentsAlt") or []):
            total += len(frags)
            rough += sum(1 for f in frags if f.get("rough"))
        for child in l.get("children", []):
            t, r = count_fragments(child.get("lines", []))
            total += t
            rough += r
    return total, rough


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", default="PCR Narrative Builder v1.html")
    ap.add_argument("--out", default="review-model.json")
    ap.add_argument("--no-timestamp", action="store_true",
                     help="write generated:null for deterministic diffs")
    args = ap.parse_args()

    doc = load_doc(args.src)
    containers = build_containers(doc)

    total_lines = sum(len(c["lines"]) for c in containers)
    total_fields = sum(count_fields(c["lines"]) for c in containers)
    frag_totals = [count_fragments(c["lines"]) for c in containers]
    total_fragments = sum(t for t, _ in frag_totals)
    total_rough = sum(r for _, r in frag_totals)
    stats = {
        "containers": len(containers), "lines": total_lines, "fields": total_fields,
        "fragments": total_fragments, "rough": total_rough,
    }

    out = {
        "generated": None if args.no_timestamp else datetime.now(timezone.utc).isoformat(),
        "source": args.src,
        "containers": containers,
        "stats": stats,
    }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)

    print(f"stats: {stats}")

    def find_line(cid, lid):
        for c in containers:
            if c["id"] == cid:
                for l in c["lines"]:
                    if l["id"] == lid:
                        return l
        return None

    print("\nneur_gcs LineRef:")
    print(json.dumps(find_line("neuro", "neur_gcs"), indent=1))

    print("\nsh_dispatch_line LineRef:")
    print(json.dumps(find_line("sh_dispatch", "sh_dispatch_line"), indent=1))


if __name__ == "__main__":
    sys.exit(main())
