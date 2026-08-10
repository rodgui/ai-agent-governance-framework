---
title: Matriz de validação do handbook e produto de consultoria
status: in-progress
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: major-change
supersedes: null
related:
  - spec.md
  - plan.md
  - tasks.md
---

# Matriz de validação

| Critério | Verificação | Evidência esperada |
|---|---|---|
| Policy v1 intacta | `git diff origin/main -- <policy>` | diff vazio e blob idêntico |
| Markdown válido | markdownlint | exit 0 no diff |
| Links locais válidos | `validate-repository.py` | zero links ausentes |
| Schemas válidos | JSON parse + Draft 2020-12 | exit 0 |
| Exemplos válidos | jsonschema contra schemas | quatro exemplos aprovados |
| Visual neutro | renderer + inspeção | PNG 1800 × 2400, sem vendor principal |
| Caso Microsoft separado | links e títulos | asset restrito ao estudo de caso |
| Determinismo visual | duas renderizações | SHA-256 idêntico |
| Ordem editorial | links e sequência | handbook linear sem conteúdo duplicado |
| Segurança | scan de padrões sensíveis | zero secrets e paths pessoais |
| Fontes | ledger + verificação | ids conhecidos e claims limitados |
| Oferta comercial | executive-doc judge | sem claims indevidos ou ambiguidades |
| PR | GitHub | aberto, sincronizado e mergeable |

## Gate de publicação

A publicação somente pode ser marcada como pronta quando todos os critérios acima estiverem verdes e o owner tiver revisado os documentos decisórios.
