---
title: ADR-0001 — Núcleo canônico modular e mappings por fornecedor
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: major-change
supersedes: null
related:
  - ../../../specs/001-handbook-consulting-product/spec.md
  - ../../index.md
  - ../../explanations/microsoft-agent-governance-case-study.md
---

# ADR-0001 — Núcleo canônico modular e mappings por fornecedor

## Contexto

O framework precisa funcionar como policy, guia, handbook, catálogo de patterns e base de consultoria. A primeira consolidação usou cinco artigos Microsoft Customer Zero como evidência útil, mas um visual e uma narrativa centrados em Agent 365 podem ser interpretados como arquitetura universal ou dependência de fornecedor.

Manter uma segunda versão monolítica para ebook criaria divergência editorial. Manter todos os detalhes no README prejudicaria navegação e revisão.

## Decisão

1. O núcleo do framework será **vendor-neutral** e organizado em documentos modulares por domínio.
2. A Policy v1 continuará como baseline adotada até mudança explícita e versionada.
3. Estudos de caso e mappings por fornecedor serão separados do núcleo normativo e arquitetural.
4. O README funcionará como landing page e mapa; não como handbook completo.
5. Uma futura publicação, quando priorizada, será derivada dos documentos canônicos e da ordem linear do handbook.
6. A oferta de consultoria será derivada do mesmo método, control catalog, assessments, templates e critérios de aceite.
7. O visual principal será neutro; visuais de fornecedores serão rotulados como estudos de caso.

## Opções consideradas

### Opção A — README monolítico

Rejeitada. Facilita leitura inicial, mas dificulta manutenção, ownership, revisão e reuso por persona.

### Opção B — Framework centrado em Agent 365

Rejeitada. Produz uma boa implementação específica, mas reduz portabilidade e confunde control plane de fornecedor com governança completa.

### Opção C — Livro independente copiado dos documentos

Rejeitada. Cria duas fontes e exige sincronização manual.

### Opção D — Núcleo modular + publicação gerada

Aceita. Preserva rastreabilidade, permite jornadas diferentes e sustenta múltiplos formatos sem duplicação.

## Consequências positivas

- maior portabilidade entre fornecedores e arquiteturas;
- separação clara entre normativo, explicativo, operacional e comercial;
- documentação revisável por domínio;
- ebook e assets reproduzíveis;
- patterns, schemas e controles reutilizáveis em engagements de consultoria;
- estudos de caso podem evoluir sem redefinir o framework.

## Consequências negativas

- mais arquivos e links para manter;
- necessidade futura de pipeline de publicação quando o conteúdo estiver maduro;
- leitores precisam de jornadas e índices bem cuidados;
- mappings por fornecedor exigem revisão periódica.

## Critérios de reversão

A decisão deve ser revista se a modularidade causar duplicação sistemática, se as jornadas de leitura se tornarem incoerentes ou se a manutenção dos mappings superar o valor de portabilidade.
