# Protocolo Editorial Canônico

## Fluxo obrigatório

GERAR → VALIDAR → REVISAR → SALVAR → COMMITAR → ATUALIZAR MANIFESTO.

## Fonte da verdade

O diretório `canon/` é a única fonte oficial das páginas concluídas. Arquivos DOCX, PDF e outros formatos são derivados e nunca substituem o Markdown canônico.

## Estados

- `draft`: texto em produção.
- `reviewed`: estrutura e conteúdo revisados, ainda não canônicos.
- `canon`: aprovado e integrado à sequência oficial.

## Padrão 705

Cada página contém 3 pilares. Cada pilar contém:

- Doutrina: 137 palavras.
- Kavanah: 72 palavras.
- Ordália: 26 palavras.

Total: `(137 + 72 + 26) × 3 = 705` palavras nucleares.

Os blocos contáveis devem ser delimitados pelos marcadores HTML `HNK:COUNT START` e `HNK:COUNT END`. Cabeçalhos, metadados, QR Code, Espelho da Alma e comentários editoriais não entram na contagem.

## Nome dos arquivos

Formato: `canon/capitulo-NN-nome/dia-NNN.md`.

Exemplo: `canon/capitulo-01-kether/dia-008.md`.

## Commits

Padrão recomendado para página nova:

`codex: add day 008 — Kether / Jeliel`

Correções editoriais:

`codex: revise day 008 — word count`

## Regra de conclusão

Nenhuma página é considerada concluída até passar no validador, estar marcada como `canon` e existir na branch principal do repositório.
