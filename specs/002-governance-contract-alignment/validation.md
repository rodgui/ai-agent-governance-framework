---
title: Validação do alinhamento dos contratos de governança
status: draft
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - spec.md
  - plan.md
  - tasks.md
---

# Validação

## Matriz de aceite

| Critério | Evidência esperada | Estado |
| --- | --- | --- |
| T4 separado de admissibility | ADR, docs, schemas e probes | pending |
| lifecycle e discovery estruturados | Registry 2.0 + example + tests | pending |
| model/source/tool bindings | Blueprint 2.0 + catalogs + invariants | pending |
| Control Catalog versionado corretamente | schema 2.0 + migration + tests | pending |
| Pages manual documentado | ADR de supersession; workflow preservado | pending |
| programas sugestivos | callouts nos guias e índices | pending |
| capability crosswalk | 15 capabilities → maturity → controls | pending |
| toolkit humano ampliado | seis templates e index | pending |
| release reproduzível | tags e GitHub Releases | pending |
| quality gates | comandos e resultados reais | pending |

## Comandos planejados

```bash
uv run --with-requirements requirements-ci.txt python -m unittest tools/scripts/test_validate_repository.py
uv run --with-requirements requirements-ci.txt python tools/scripts/validate-repository.py
uv run --with-requirements requirements-ci.txt ruff check tools/scripts
uv run --with-requirements requirements-ci.txt python -m py_compile tools/scripts/*.py
uv run --with-requirements requirements-docs.txt python tools/scripts/build-docs-site.py
npx --yes markdownlint-cli2@0.20.0 '**/*.md' '#site/**' '#site_src/**'
git diff --check
```

Resultados serão registrados após execução; nenhum status será antecipado.
