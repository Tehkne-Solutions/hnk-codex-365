# HNK Codex Interativo 365

Repositório canônico do **HNK Codex Interativo 365**.

## Fonte da verdade

- `canon/` contém as páginas oficiais do Codex em Markdown.
- `CODEX_MANIFEST.yaml` registra o estado editorial e o próximo ponto de escrita.
- `templates/` define o formato obrigatório de cada página.
- `scripts/` contém validação e compilação.
- `.github/workflows/` automatiza validação e geração do manuscrito mestre.

## Regra editorial

Uma página só é considerada concluída quando:

1. está em `canon/`;
2. passa na validação 137/72/26 × 3;
3. possui metadados válidos;
4. está marcada como `canon`;
5. foi commitada no repositório.

## Build

Toda alteração em páginas canônicas dispara a automação editorial para gerar:

- `build/CODEX_MASTER.md`
- `build/CODEX_MASTER.docx`

O Markdown é a fonte oficial. DOCX/PDF são artefatos derivados.
