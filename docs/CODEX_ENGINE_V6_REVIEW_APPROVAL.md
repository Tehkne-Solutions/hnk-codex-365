# HNK CODEX ENGINE v6 — REVIEW & APPROVAL

O v6 é a camada de governança editorial entre Workbench e `canon/`.

## Alinhamento com o repositório

- fonte de verdade: `canon/`;
- template: `templates/day-template.md`;
- validador: `scripts/validate_pages.py`;
- protocolo epistêmico: `canon/HNK_PROTOCOLO_EPISTEMICO.md`;
- estados oficiais: `draft`, `reviewed`, `canon`;
- matriz: `137/72/26 × 3 = 705`.

## Fluxo

1. carregar fonte canônica;
2. criar/editar draft;
3. comparar fonte × draft;
4. registrar comentários;
5. criar snapshots;
6. validar matriz;
7. confirmar HNK-EP-1.1;
8. registrar revisor;
9. promover para `reviewed`;
10. registrar aprovador canônico;
11. promover para `canon`;
12. exportar Markdown;
13. validar com `scripts/validate_pages.py`;
14. somente então escrever em `canon/`.

Nenhuma página canônica é sobrescrita automaticamente pela ferramenta.
