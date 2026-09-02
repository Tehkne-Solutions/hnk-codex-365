#!/usr/bin/env python3
"""Gate de revisão/aprovação para páginas HNK antes de promoção a reviewed/canon."""
from pathlib import Path
import argparse, json, re, sys

START_RE = re.compile(r"<!--\s*HNK:COUNT START\s+([a-z0-9-]+)\s+target=(\d+)\s*-->", re.I)
END = "<!-- HNK:COUNT END -->"
WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-’'][0-9A-Za-zÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)
EXPECTED = {
    "jachin-doctrine":137,"jachin-kavanah":72,"jachin-ordalia":26,
    "boaz-doctrine":137,"boaz-kavanah":72,"boaz-ordalia":26,
    "middle-doctrine":137,"middle-kavanah":72,"middle-ordalia":26,
}

def count_words(text):
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\[(?:\d+\s*(?:,\s*\d+\s*)*)\]", " ", text)
    text = re.sub(r"[`*_#>]", " ", text)
    return len(WORD_RE.findall(text))

def fm(text, key):
    if not text.startswith("---"): return None
    end = text.find("\n---", 3)
    if end < 0: return None
    m = re.search(rf"^\s*{re.escape(key)}\s*:\s*[\"']?([^\n\"']+)", text[3:end], re.M)
    return m.group(1).strip() if m else None

def validate_page(text):
    errors, found, pos = [], {}, 0
    while True:
        m = START_RE.search(text, pos)
        if not m: break
        end = text.find(END, m.end())
        if end < 0:
            errors.append(f"{m.group(1)}: END ausente"); break
        found[m.group(1).lower()] = (int(m.group(2)), count_words(text[m.end():end]))
        pos = end + len(END)
    for block, target in EXPECTED.items():
        if block not in found:
            errors.append(f"{block}: ausente"); continue
        declared, actual = found[block]
        if declared != target: errors.append(f"{block}: target {declared}, esperado {target}")
        if actual != target: errors.append(f"{block}: {actual} palavras, esperado {target}")
    total = sum(v[1] for k,v in found.items() if k in EXPECTED)
    if len(found) == 9 and total != 705: errors.append(f"total {total}, esperado 705")
    for key in ("day","chapter","sephira","world","level","xp","status","target_words","epistemic_protocol"):
        if fm(text,key) is None: errors.append(f"frontmatter ausente: {key}")
    if fm(text,"target_words") != "705": errors.append("target_words deve ser 705")
    if fm(text,"epistemic_protocol") != "HNK-EP-1.1": errors.append("epistemic_protocol deve ser HNK-EP-1.1")
    return errors, total

def validate_review(data, target_state):
    errors=[]
    state=data.get("state")
    reviewers=data.get("reviewers") or {}
    if target_state == "reviewed":
        if not reviewers.get("editorial","").strip(): errors.append("revisor editorial ausente")
        if not data.get("epistemic_ack"): errors.append("HNK-EP-1.1 não confirmado")
        if state not in ("reviewed","canon"): errors.append(f"review state deve ser reviewed/canon, atual={state!r}")
    elif target_state == "canon":
        if state != "canon": errors.append(f"review state deve ser canon, atual={state!r}")
        if not reviewers.get("editorial","").strip(): errors.append("revisor editorial ausente")
        if not reviewers.get("canonical","").strip(): errors.append("aprovador canônico ausente")
        if not data.get("epistemic_ack"): errors.append("HNK-EP-1.1 não confirmado")
    return errors

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("page", type=Path)
    ap.add_argument("review", type=Path)
    ap.add_argument("--target-state", choices=("reviewed","canon"), default="reviewed")
    args=ap.parse_args()
    text=args.page.read_text(encoding="utf-8")
    review=json.loads(args.review.read_text(encoding="utf-8"))
    errors,total=validate_page(text)
    errors += validate_review(review,args.target_state)
    if errors:
        print(f"FAIL {args.page} -> {args.target_state}")
        for e in errors: print(" -",e)
        return 1
    print(f"OK {args.page} -> {args.target_state} — {total} palavras nucleares")
    return 0

if __name__ == "__main__": sys.exit(main())
