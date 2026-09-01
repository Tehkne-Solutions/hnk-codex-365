#!/usr/bin/env python3
"""Compila páginas canônicas em um manuscrito Markdown único."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"
BUILD = ROOT / "build"
OUTPUT = BUILD / "CODEX_MASTER.md"


def clean_page(text: str) -> str:
    # Remove frontmatter YAML.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]

    # Marcadores editoriais são invisíveis no manuscrito final.
    text = re.sub(r"<!--\s*HNK:COUNT START.*?-->", "", text, flags=re.IGNORECASE)
    text = text.replace("<!-- HNK:COUNT END -->", "")
    return text.strip()


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    pages = sorted(CANON.glob("**/dia-*.md")) if CANON.exists() else []

    header = "# HNK Codex Interativo 365\n\n> Manuscrito compilado automaticamente a partir de `canon/`. Não editar diretamente.\n"
    chunks = [header]

    for page in pages:
        chunks.append("\n\n---\n\n")
        chunks.append(clean_page(page.read_text(encoding="utf-8")))

    OUTPUT.write_text("".join(chunks).rstrip() + "\n", encoding="utf-8")
    print(f"Gerado: {OUTPUT.relative_to(ROOT)} ({len(pages)} páginas canônicas)")


if __name__ == "__main__":
    main()
