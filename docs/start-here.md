---
title: Comece aqui — trilhas de leitura para implantação
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - index.md
  - handbook/README.md
  - guides/framework-implementation-playbook.md
---

# Comece aqui — trilhas de leitura para implantação

Esta página existe porque o repositório tem muitos caminhos e uma organização que vai implantar precisa de **um**.

Se o objetivo é estudar, o [handbook](handbook/README.md) é a ordem certa e esta página não é necessária. Se o objetivo é implantar, comece aqui e ignore o resto da navegação até terminar a sua trilha.

## Antes de tudo: sua organização já tem policy de IA?

Se tem, **ela prevalece** e este framework entra como a camada de execução para agentes, não como substituta. Como fazer essa subordinação está em [policy de governança de agentes](governance/policy.md#se-a-organização-já-tem-uma-policy-corporativa-de-ia).

Ignorar isso é o erro de posicionamento mais caro possível: o framework parece competir com um instrumento corporativo já aprovado e é rejeitado por jurisdição, não por mérito.

## A regra que economiza mais tempo

**Leia o [implementation playbook](guides/framework-implementation-playbook.md) antes de qualquer outra coisa.**

É o único documento que dá **ordem**. Todos os outros dão **conteúdo**. Ler os domínios antes dele produz a sensação de muita informação e nenhum caminho — que é exatamente o erro que faz programas de governança começarem pela ferramenta.

## Quatro trilhas

Cada trilha termina numa decisão, não numa leitura concluída.

### Trilha 0 — Sponsor e comitê executivo · ~1 hora

1. [Brief executivo](executive/governing-agents-at-scale.md)
2. [Fundamentos](fundamentals/README.md) — apenas as distinções de vocabulário
3. [Operating model](governance/operating-model.md) — a tabela de decision rights
4. [Caso T3](explanations/cases/benefits-eligibility-triage.md) — o que "governança funcionando" significa num caso concreto

**Decisão:** patrocinar, nomear o governance owner e aprovar o mandato.

### Trilha 1 — Quem monta o programa · ~1 semana

1. [Implementation playbook](guides/framework-implementation-playbook.md) — o contrato dos gates e a dependência real entre eles
2. [Programa de 24 semanas](guides/implementation-program-24-weeks.md) — como pattern adaptável, não cronograma
3. [Catálogo de artefatos](reference/artifact-catalog.md) — o que precisa existir, por owner e fase
4. [Capability map](guides/capability-map.md) e [maturity model](guides/maturity-model.md) — medir a base antes de desenhar o alvo
5. [Checklist de autossuficiência](reference/self-sufficiency-checklist.md) — aplicado à sua organização

**Decisão:** escopo, fases, workstreams, gargalos e alvo de maturidade.

### Trilha 2 — Risco, Responsible AI, jurídico e compliance · ~1 semana

1. [Policy de governança de agentes](governance/policy.md)
2. [Gestão de riscos](risk-management/README.md) — a tabela dos dez escaladores e a separação entre criticidade e admissibilidade
3. [Minimum Production Bar](risk-management/minimum-production-bar.md)
4. [Responsible AI](responsible-ai/README.md) e [human oversight](human-oversight/README.md)
5. [Evidence pack por tier](auditability/evidence-pack-by-tier.md)
6. [Control catalog](../controls/README.md) — comece pelos `blocking`
7. [Cláusulas de contrato com fornecedor](../templates/ai-vendor-contract-clauses.md) — o que compras e jurídico precisam exigir

**Decisão:** tiers calibrados, escaladores adaptados ao setor, triggers de RAI e o que bloqueia release.

### Trilha 3 — Arquitetura e plataforma · ~2 semanas

1. [Arquitetura de referência](architecture/overview.md)
2. [Mapeamento de capability para tecnologia](architecture/capability-to-technology.md) — conecta o framework ao estate que já existe
3. [Registry](registry/README.md), [identidade](identity/README.md), [dados](data-access/README.md), [tools e MCP](tool-governance/README.md), [modelos e provedores](model-governance/README.md)
4. [Schemas](../schemas/README.md) e os [casos de referência](explanations/cases/README.md), lendo os JSON junto
5. [Design patterns](patterns/README.md)

**Decisão:** source of truth por atributo, pontos de enforcement e o que é comprado versus construído.

## Depois de ler: a ordem de execução

```text
baseline → desenho → fundações → um caso real → escala
```

1. **Baseline** — capability map e maturity assessment com evidência, separando o observado da hipótese.
2. **Desenho** — tiers calibrados com casos reais, operating model e decision rights.
3. **Fundações** — registry, identidade, catálogos de dados e tools, telemetria e Minimum Production Bar.
4. **Um caso real ponta a ponta** — de preferência um T2, que é onde a governança começa a custar.
5. **Escala** — automação de discovery, policy-as-code, attestation e dashboards.

Os gates G0–G7 autorizam avançar entre essas etapas. **A numeração deles não é cronograma** — a dependência real está no [playbook](guides/framework-implementation-playbook.md#a-numeração-não-é-um-cronograma).

## O que esperar e o que não esperar

O framework é vendor-neutral e verificável: 44 controls com evidência declarada, contratos estruturados e validação automatizada. Nenhum control, porém, foi exercitado contra um estate real — os [casos de referência](explanations/cases/README.md) são fictícios e provam coerência do método, não eficácia.

Consequência prática para o programa: **thresholds, tiers e prazos precisam ser recalibrados com os seus dados**, e a primeira implantação é também a primeira validação. Reserve orçamento para isso.

## O resto da navegação

As demais superfícies — [índice por persona e objetivo](index.md), [handbook](handbook/README.md) e o toolkit do [README](../README.md) — são **referência**. Servem para localizar um assunto específico depois, não para decidir por onde começar.
