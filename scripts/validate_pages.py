#!/usr/bin/env python3
"""Validador editorial do HNK Codex Interativo 365."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"

START_RE = re.compile(
    r"<!--\s*HNK:COUNT START\s+([a-z0-9-]+)\s+target=(\d+)\s*-->",
    re.IGNORECASE,
)
END = "<!-- HNK:COUNT END -->"
WORD_RE = re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-’'][0-9A-Za-zÀ-ÖØ-öø-ÿ]+)*", re.UNICODE)

EXPECTED = {
    "jachin-doctrine": 137,
    "jachin-kavanah": 72,
    "jachin-ordalia": 26,
    "boaz-doctrine": 137,
    "boaz-kavanah": 72,
    "boaz-ordalia": 26,
    "middle-doctrine": 137,
    "middle-kavanah": 72,
    "middle-ordalia": 26,
}


def count_words(text: str) -> int:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"[`*_#>]", " ", text)
    return len(WORD_RE.findall(text))


def frontmatter_value(text: str, key: str):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    frontmatter = text[3:end]
    match = re.search(rf"^\s*{re.escape(key)}\s*:\s*[\"']?([^\n\"']+)", frontmatter, re.MULTILINE)
    return match.group(1).strip() if match else None


def validate_file(path: Path):
    text = path.read_text(encoding="utf-8")
    errors = []

    status = frontmatter_value(text, "status")
    if status != "canon":
        errors.append(f"status deve ser 'canon' (atual: {status!r})")

    day = frontmatter_value(text, "day")
    match_day = re.search(r"dia-(\d{3})\.md$", path.name)
    if match_day and day and int(match_day.group(1)) != int(day):
        errors.append(f"day={day} não corresponde ao arquivo {path.name}")

    found = {}
    pos = 0
    while True:
        match = START_RE.search(text, pos)
        if not match:
            break
        block_id, declared_target = match.group(1).lower(), int(match.group(2))
        end_pos = text.find(END, match.end())
        if end_pos == -1:
            errors.append(f"bloco {block_id}: marcador END ausente")
            break
        body = text[match.end():end_pos]
        found[block_id] = (declared_target, count_words(body))
        pos = end_pos + len(END)

    missing = sorted(set(EXPECTED) - set(found))
    extra = sorted(set(found) - set(EXPECTED))
    if missing:
        errors.append("blocos ausentes: " + ", ".join(missing))
    if extra:
        errors.append("blocos desconhecidos: " + ", ".join(extra))

    total = 0
    for block_id, expected in EXPECTED.items():
        if block_id not in found:
            continue
        declared, actual = found[block_id]
        total += actual
        if declared != expected:
            errors.append(f"{block_id}: target declarado {declared}, esperado {expected}")
        if actual != expected:
            errors.append(f"{block_id}: {actual} palavras, esperado {expected}")

    if len(found) == 9 and total != 705:
        errors.append(f"total nuclear: {total} palavras, esperado 705")

    return errors, total


def main():
    pages = sorted(CANON.glob("**/dia-*.md")) if CANON.exists() else []
    if not pages:
        print("Nenhuma página canônica encontrada. Estrutura pronta para migração.")
        return 0

    failed = False
    for page in pages:
        errors, total = validate_file(page)
        rel = page.relative_to(ROOT)
        if errors:
            failed = True
            print(f"FAIL {rel}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {rel} — {total} palavras nucleares")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
