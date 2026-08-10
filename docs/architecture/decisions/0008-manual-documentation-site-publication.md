---
title: ADR-0008 — Build verificável e publicação manual do site
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: 0007-documentation-site-build.md
related:
  - 0003-single-canonical-source-and-guide-absorption.md
  - 0007-documentation-site-build.md
  - ../../handbook/README.md
  - ../../../tools/scripts/build-docs-site.py
---

# ADR-0008 — Build verificável e publicação manual do site

## Contexto

A [ADR-0007](0007-documentation-site-build.md) decidiu corretamente gerar uma superfície de leitura a partir do corpus canônico, mas acoplou duas decisões diferentes: **construir e validar** o site e **publicá-lo automaticamente** em GitHub Pages.

O owner confirmou que, nesta fase, não deseja assumir a criação ou operação de GitHub Pages. O repositório é a superfície canônica e já pode ser usado diretamente; o site gerado é conveniência de leitura e teste de integridade, não requisito de adoção.

## Decisão

1. Preservar MkDocs, staging e build strict como derivados verificáveis do corpus.
2. Preservar o build nos quality gates para detectar links, navegação ou Mermaid quebrados.
3. Manter `.github/workflows/pages.yml` somente com `workflow_dispatch`, sem publicação automática por push.
4. Não exigir configuração externa de GitHub Pages nem tratar ausência de publicação como falha do framework.
5. Permitir que um mantenedor publique manualmente o site quando houver destino e necessidade explícitos.
6. O handbook e o repositório continuam sendo as fontes canônicas; qualquer site é artefato descartável e reproduzível.

## Consequências

### Positivas

- zero dependência operacional de GitHub Pages;
- leitura derivada permanece disponível sem impor publicação;
- qualidade de links e navegação continua verificada em CI;
- a decisão do owner fica alinhada ao workflow real.

### Negativas

- não existe URL pública garantida para leitores não familiarizados com GitHub;
- publicação manual pode ficar defasada se alguém a executar sem usar o commit correto;
- README e handbook precisam continuar suficientemente navegáveis por si próprios.

## Riscos e mitigação

| Risco | Mitigação |
| --- | --- |
| site manual divergir do corpus | sempre construir de commit/tag explícito; nunca editar output |
| ausência de site ser interpretada como framework incompleto | declarar que publicação é canal opcional, não acceptance criterion |
| qualidade do build deteriorar | manter build strict no quality gate |

## Critérios de validação

- build local e em CI passa em modo strict;
- workflow de Pages possui apenas disparo manual;
- nenhuma configuração de Pages é prerequisite do framework;
- corpus e handbook continuam navegáveis sem o site.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10: não priorizar a criação de GitHub Pages, mantendo somente a capacidade de build e publicação manual.
