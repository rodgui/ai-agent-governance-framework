---
title: ADR-0011 — Adoção da release 1.1.0 do framework
status: approved
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - 0006-framework-release-1-0-adoption.md
  - 0008-manual-documentation-site-publication.md
  - 0009-risk-tier-and-admissibility.md
  - 0010-structured-governance-contracts-2.0.md
  - ../../../CHANGELOG.md
  - ../../../specs/002-governance-contract-alignment/validation.md
---

# ADR-0011 — Adoção da release 1.1.0 do framework

## Contexto

A release 1.0 consolidou o framework modular e absorveu o guia v3.4, mas uma revisão independente encontrou divergências entre documentação e contratos estruturados: T4 tinha duas semânticas, lifecycle não cabia no Registry, model/source/tool governance estava majoritariamente em prose e a mudança incompatível do Control Catalog foi rotulada como minor.

O owner aprovou as correções com duas decisões explícitas: publicação em GitHub Pages permanece opcional/manual; roadmaps de 90 dias/24 semanas e piloto são guidance para quem precisa saber por onde começar, não obrigações normativas.

## Decisão proposta

1. Adotar a release **1.1.0** quando os quality gates e a revisão do PR estiverem verdes.
2. Tratar a release como evolução minor do framework de conhecimento, embora componentes estruturados recebam major version própria:
   - Agent Registry schema 2.0;
   - Agent Blueprint schema 2.0;
   - Control Catalog schema 2.0;
   - Control Catalog conteúdo 1.2.0;
   - cinco contratos de referência novos em 1.0.
3. Tornar `v1.0.0` recuperável no commit de adoção histórico e `v1.1.0` recuperável no merge desta correção.
4. Publicar GitHub Releases para as duas tags, com limites e notas de migração; não configurar GitHub Pages.
5. A adoção da release continua sendo versionamento deste repositório, não adoção organizacional, certificação ou assurance externa.

## Conteúdo da release

- risk tier separado de admissibilidade;
- lifecycle stage separado de operational state;
- discovery status separado de confidence;
- bindings de model/version/evaluation e catálogos de source/tool;
- release evidence manifest e audit event envelope;
- 15 capabilities com crosswalk para maturity e controls;
- toolkit humano ampliado;
- programas de implantação explicitamente sugestivos;
- build documental preservado com publicação manual.

## Lacunas conhecidas

- controls ainda não foram calibrados contra estate real;
- thresholds e cadências são pontos de partida, não benchmarks;
- ISO permanece sem mapping control a control;
- o owner também atua como authority editorial; revisão técnica no PR reduz, mas não elimina, essa concentração;
- catálogos estruturados são referência e exigem adaptação aos systems of record da organização.

## Critérios para mudar `approved` para `accepted`

- validator, unit tests, Ruff, `py_compile`, Markdown, build strict e diff check verdes;
- revisão de segurança e qualidade sem finding crítico aberto;
- CI do PR verde;
- merge commit identificado;
- tags e GitHub Releases criadas e recuperáveis.

## Evidência da decisão

Direção aprovada por Rodrigo Garcia Guimarães em 2026-08-10. O status permanece `approved` até os critérios técnicos e de release serem concluídos; depois deve mudar para `accepted` sem reescrever esta condição.
