#!/usr/bin/env python3
"""Prepare an HNK Codex day for branch/PR publication.

This script does NOT write to GitHub. It creates a deterministic publish bundle
that another authenticated layer can use to create a branch, files, and PR.
"""
from pathlib import Path
import argparse, json, re, unicodedata

CHAPTERS = {
  1: ("Kether",1,36), 2:("Chokmah",37,73), 3:("Binah",74,109),
  4:("Chesed",110,146), 5:("Geburah",147,182), 6:("Tiphereth",183,219),
  7:("Netzach",220,255), 8:("Hod",256,292), 9:("Yesod",293,328), 10:("Malkuth",329,365),
}
WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-’'][0-9A-Za-zÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)
START_RE = re.compile(r"<!--\s*HNK:COUNT START\s+([a-z0-9-]+)\s+target=(\d+)\s*-->", re.I)
END = "<!-- HNK:COUNT END -->"
EXPECTED={"jachin-doctrine":137,"jachin-kavanah":72,"jachin-ordalia":26,"boaz-doctrine":137,"boaz-kavanah":72,"boaz-ordalia":26,"middle-doctrine":137,"middle-kavanah":72,"middle-ordalia":26}

def slugify(s):
    s=unicodedata.normalize("NFKD",s).encode("ascii","ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+","-",s).strip("-")

def chapter_for_day(day):
    for cid,(name,a,b) in CHAPTERS.items():
        if a<=day<=b:return cid,name
    raise ValueError("day outside 1..365")

def frontmatter_value(text,key):
    if not text.startswith("---"): return None
    end=text.find("\n---",3)
    if end<0:return None
    fm=text[3:end]
    m=re.search(rf"^\s*{re.escape(key)}\s*:\s*[\"']?([^\n\"']+)",fm,re.M)
    return m.group(1).strip() if m else None

def count_words(text):
    text=re.sub(r"<!--.*?-->"," ",text,flags=re.S)
    text=re.sub(r"\[(?:\d+\s*(?:,\s*\d+\s*)*)\]"," ",text)
    text=re.sub(r"[`*_#>]"," ",text)
    return len(WORD_RE.findall(text))

def validate(text):
    errors=[];found={};pos=0
    while True:
        m=START_RE.search(text,pos)
        if not m:break
        end=text.find(END,m.end())
        if end<0:errors.append(f"{m.group(1)} END missing");break
        found[m.group(1).lower()] = (int(m.group(2)),count_words(text[m.end():end]))
        pos=end+len(END)
    for k,t in EXPECTED.items():
        if k not in found:errors.append(f"{k}: missing");continue
        declared,actual=found[k]
        if declared!=t:errors.append(f"{k}: target {declared}, expected {t}")
        if actual!=t:errors.append(f"{k}: {actual} words, expected {t}")
    total=sum(v[1] for k,v in found.items() if k in EXPECTED)
    if total!=705:errors.append(f"total {total}, expected 705")
    status=frontmatter_value(text,"status")
    if status not in ("reviewed","canon"): errors.append(f"status must be reviewed/canon, got {status!r}")
    return errors,total,status

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("markdown")
    ap.add_argument("--review",required=True)
    ap.add_argument("--out",default="publish-bundle.json")
    args=ap.parse_args()
    md=Path(args.markdown).read_text(encoding="utf-8")
    review=json.loads(Path(args.review).read_text(encoding="utf-8"))
    day=int(frontmatter_value(md,"day") or 0)
    sephira=frontmatter_value(md,"sephira") or ""
    title_line=next((x.lstrip("# ").strip() for x in md.splitlines() if x.startswith("# DIA ")),f"Dia {day}")
    errors,total,status=validate(md)
    if errors:
        print("PUBLISH BLOCKED")
        for e in errors: print(" -",e)
        raise SystemExit(1)
    chapter,chapter_name=chapter_for_day(day)
    if chapter_name.lower()!=sephira.lower():
        print(f"PUBLISH BLOCKED\n - sephira {sephira!r} does not match chapter {chapter_name!r}")
        raise SystemExit(1)
    slug=slugify(title_line.replace(f"DIA {day:03d}","").strip(" |"))
    branch=f"codex/day-{day:03d}-{slug[:40] or slugify(sephira)}"
    canon_path=f"canon/capitulo-{chapter:02d}-{slugify(sephira)}/dia-{day:03d}.md"
    review_path=f"reviews/dia-{day:03d}.review.json"
    bundle={
      "day":day,"state":status,"word_total":total,"branch":branch,
      "canon_path":canon_path,"review_path":review_path,"markdown":md,
      "review_record":review,
      "pull_request":{
        "title":f"canon: Dia {day:03d} — {sephira}",
        "base":"main","head":branch,
        "body":f"Publicação controlada do Dia {day:03d}.\n\n- matriz: 705/705\n- estado: {status}\n- review record: `{review_path}`\n- canon target: `{canon_path}`\n\nNenhuma escrita direta no `main`."
      }
    }
    Path(args.out).write_text(json.dumps(bundle,ensure_ascii=False,indent=2),encoding="utf-8")
    print("PUBLISH BUNDLE READY")
    print(branch)
    print(canon_path)
    print(review_path)

if __name__=="__main__": main()
