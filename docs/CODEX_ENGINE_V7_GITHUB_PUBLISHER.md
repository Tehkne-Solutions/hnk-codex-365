# HNK CODEX ENGINE v7 — GITHUB PUBLISHER

## Princípio

Nenhum Dia é escrito diretamente em `main`.

Fluxo:

`reviewed` → publish bundle → branch isolada → Markdown + review record → PR → CI → aprovação canônica → merge.

## Integração oficial

O Publisher respeita:

- `canon/` como source of truth;
- `scripts/validate_pages.py`;
- `scripts/validate_review_gate.py`;
- `HNK-EP-1.1`;
- estados `draft`, `reviewed`, `canon`.

## Bundle

O bundle determina de forma reproduzível:

- branch;
- path canônico;
- path do review record;
- conteúdo Markdown;
- review JSON;
- título e corpo do PR.

## Segurança editorial

O script `prepare_publish_bundle.py` é deliberadamente sem credenciais GitHub. Ele apenas prepara e valida. Uma camada autenticada separada executa branch/file/PR.

Isso mantém o ato de publicar auditável e impede que um editor local escreva diretamente no cânone.
