---
title: Alinhamento dos contratos de governança e expansão do toolkit
status: approved
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - ../../docs/architecture/decisions/0003-single-canonical-source-and-guide-absorption.md
  - ../../docs/architecture/decisions/0004-risk-tier-taxonomy-and-fast-path.md
  - ../../docs/architecture/decisions/0005-control-catalog-scope-verification-and-mappings.md
  - ../../docs/architecture/decisions/0007-documentation-site-build.md
  - plan.md
  - tasks.md
  - validation.md
---

# Especificação: alinhamento dos contratos de governança

## Problema

A absorção do guia v3.4 enriqueceu o conteúdo operacional, mas alguns conceitos novos não foram propagados para os contratos estruturados. T4 passou a representar simultaneamente criticidade e restrição, a state machine de lifecycle divergiu do Agent Registry, model/source/tool governance não possui catálogos estruturados completos e o schema do Control Catalog recebeu mudança incompatível como versão minor.

## Objetivo

Consolidar o repositório como guia, bíblia e framework vendor-neutral para implantação de governança de agentes de IA, com documentação rica e contratos estruturados suficientes para tornar exemplos e controles verificáveis sem transformar o projeto em produto de software.

## Decisões aprovadas pelo owner

1. GitHub Pages permanece opcional e manual; criar/publicar o site não é requisito.
2. Programas de 90 dias, 24 semanas e piloto são guias sugestivos para organizações que precisam de um ponto de partida; não criam prazos ou gates universais.
3. T1–T4 continuam representando criticidade/risco. Admissibilidade é dimensão separada.
4. Registry, Blueprint e Control Catalog podem receber major version de schema para eliminar incompatibilidades.
5. O toolkit deve privilegiar templates, exemplos, schemas e crosswalks úteis à adoção organizacional.

## Requisitos funcionais

### RF-01 — Risco e admissibilidade

Separar `riskTier` de `admissibility`, com valores `permitted`, `conditional`, `restricted` e `prohibited`. T4 continua sendo critical; não significa automaticamente default deny.

### RF-02 — Lifecycle estruturado

O Registry deve separar etapa de lifecycle de estado operacional e registrar histórico de transições com authority, reason, timestamp e evidence.

### RF-03 — Discovery estruturado

O Registry deve representar `confirmed`, `probable` e `suspected` separadamente de confidence e permitir múltiplos sinais de discovery.

### RF-04 — Model, source e tool bindings

O Blueprint deve referenciar entradas canônicas de catálogos de modelos/provedores, fontes certificadas e tools, incluindo versão de modelo e evaluation vinculada.

### RF-05 — Catálogos e evidência

Fornecer schemas e exemplos vendor-neutral para model/provider catalog, certified source catalog, enterprise tool registry, release evidence manifest e audit event.

### RF-06 — Control Catalog

Publicar o contrato incompatível como schema 2.0, manter `catalogVersion` independente, exigir automation e mappings, e fornecer migração 1.0/1.1→2.0.

### RF-07 — Guias sugestivos

Declarar explicitamente que 90 dias, 24 semanas e piloto são patterns de implementação adaptáveis; G0–G7 permanecem os decision gates canônicos.

### RF-08 — Capability map

Usar as 15 capabilities do guia e fornecer crosswalk para as dez dimensões de maturity e os domínios de controls.

### RF-09 — Toolkit humano

Adicionar templates reutilizáveis para capability assessment, agent risk record, behavioral analytics use case, governance RACI, attestation/sunset e release evidence manifest.

### RF-10 — ADR e release

Superseder ADRs alteradas em vez de reescrevê-las silenciosamente. Tornar releases recuperáveis por tags e GitHub Releases, sem exigir GitHub Pages.

## Requisitos de qualidade

- documentação e nomes canônicos em português, preservando termos técnicos consolidados;
- núcleo vendor-neutral;
- schemas Draft 2020-12 com `additionalProperties: false`;
- exemplos fictícios e sanitizados;
- links relativos válidos;
- sem claims de compliance, certificação ou eficácia operacional;
- foco em governança/documentação, com automação apenas para verificar contratos.

## Não objetivos

- criar produto SaaS, dashboard executável ou motor de workflow;
- configurar GitHub Pages;
- impor cronograma, piloto ou estrutura organizacional universal;
- mapear ISO control a control sem acesso ao texto normativo;
- provar adoção ou efetividade em estate real.

## Critérios de aceite

1. T4 tem uma única semântica canônica e admissibility é separada em docs, schemas e exemplos.
2. Registry 2.0 valida stage, operational state, discovery signals e transition history.
3. Blueprint 2.0 exige model version/catalog/evaluation e catalog refs de source/tool.
4. Cinco novos schemas possuem exemplos válidos e cross-record refs verificadas.
5. Control Catalog usa schema 2.0; catálogo 1.0 anterior falha por migração declarada, não por versionamento minor enganoso.
6. ADR-0004, ADR-0005 e ADR-0007 são preservadas como superseded e substituídas por novas decisões.
7. Guias de 24 semanas e piloto declaram caráter sugestivo e caminhos equivalentes.
8. Capability map apresenta 15 capabilities e crosswalk explícito.
9. Toolkit humano inclui os seis templates priorizados.
10. Validador, unit tests, lint, compile, Markdown e build documental passam.
11. Changelog, README, ROADMAP, handbook e índices refletem a nova release.
12. Mudança passa por PR e revisão antes do merge.

## Autorização

A especificação foi aprovada pela instrução explícita do owner em 2026-08-10 para corrigir os gaps, preservar Pages como opcional/manual e tratar cronogramas e piloto como orientação sugestiva para organizações que precisam saber como começar.
