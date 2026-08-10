---
title: Índice e jornadas de leitura
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - handbook/README.md
  - ../README.md
---

# Índice e jornadas de leitura

O repositório usa documentos modulares como fonte canônica. Escolha uma jornada; não é necessário ler tudo em sequência.

## Jornada por persona

### Conselho, executivo ou sponsor

**Objetivo:** decidir mandato, apetite a risco, funding e accountability.

1. [Brief executivo](executive/governing-agents-at-scale.md)
2. [Fundamentos](fundamentals/README.md)
3. [Estratégia e valor](value/README.md)
4. [Operating model](governance/operating-model.md)
5. [Maturity model](guides/maturity-model.md)

**Decisões esperadas:** sponsor, escopo, risk appetite, autoridade de contenção e critérios de valor.

### CISO, DPO, jurídico, compliance ou Responsible AI

**Objetivo:** definir controles, assurance, exceções e evidências.

1. [Policy modular](governance/policy.md)
2. [Gestão de riscos](risk-management/README.md)
3. [Segurança](security/README.md)
4. [Responsible AI](responsible-ai/README.md)
5. [Human oversight](human-oversight/README.md)
6. [Auditabilidade](auditability/README.md)
7. [Control catalog](../controls/README.md)

**Decisões esperadas:** triggers de assessment, risk acceptance, human approval, retenção, monitoramento e waiver.

### Arquitetura e plataforma

**Objetivo:** construir o control plane e integrar os sistemas especializados.

1. [Arquitetura de referência](architecture/overview.md)
2. [Design patterns](patterns/README.md)
3. [Estate, registry e taxonomia](registry/README.md)
4. [Identidade](identity/README.md)
5. [Dados](data-access/README.md)
6. [Tools e MCP](tool-governance/README.md)
7. [Modelos e provedores](model-governance/README.md)
8. [Schemas](../schemas/README.md)

**Decisões esperadas:** source of truth, blueprint, workload identity, gateways, enforcement points e adapters por plataforma.

### Product owner, maker ou engenharia

**Objetivo:** levar um agente da hipótese à operação com evidência suficiente.

1. [Implementation playbook](guides/framework-implementation-playbook.md)
2. [Roadmap de 90 dias](guides/implementation-plan-90-days.md)
3. [Risk pre-screen](../templates/risk-pre-screen.md)
4. [Evaluations](evaluations/README.md)
5. [Adoção e suporte](adoption/README.md)
6. [Templates](../templates/README.md)
7. [Examples](../examples/README.md)
8. [Publication checklist](../templates/publication-checklist.md)

**Decisões esperadas:** escopo, risco, dados, tools, evals, release, rollback e sunset.

### Operações, SOC, suporte ou SRE

**Objetivo:** observar comportamento e executar resposta proporcional.

1. [Operações](operations/README.md)
2. [Auditabilidade](auditability/README.md)
3. [Lifecycle, mudança material e retirement](lifecycle/README.md)
4. [Runtime observability and quarantine pattern](patterns/runtime-observability-and-quarantine.md)
5. [Lifecycle attestation and sunset pattern](patterns/lifecycle-attestation-and-sunset.md)
6. [Sunset plan](../templates/sunset-plan.md)

**Decisões esperadas:** SLOs, alertas, incident severity, quarantine, reactivation, attestation e retirement.

### Auditoria, assurance e challenge

**Objetivo:** verificar design, operação e evidência sem assumir o papel do owner nem presumir independência não demonstrada.

1. [Control catalog](../controls/README.md)
2. [Maturity model](guides/maturity-model.md)
3. [Auditabilidade](auditability/README.md)
4. [Assessment templates](../templates/README.md)
5. [Fontes e limitações](../references/sources.md)

**Decisões esperadas:** suficiência de evidência, grau de segregação/independência quando aplicável, findings, prazo de remediação e attestation.

### Consultor ou líder de transformação

**Objetivo:** conduzir diagnóstico, target state, roadmap e transferência de capacidade.

1. [Handbook](handbook/README.md)
2. [Implementation playbook](guides/framework-implementation-playbook.md)
3. [Programa de 24 semanas](guides/implementation-program-24-weeks.md)
4. [Plano de piloto](guides/pilot-plan.md)
5. [Maturity model](guides/maturity-model.md)
6. [Design patterns](patterns/README.md)
7. [Toolkit](../templates/README.md)

**Decisões esperadas:** baseline, gaps, target operating model, backlog priorizado, entregáveis e critérios de aceite.

## Jornada por objetivo

| Objetivo | Documentos principais |
|---|---|
| definir policy e accountability | [Policy modular](governance/policy.md) + [operating model](governance/operating-model.md) |
| inventariar agentes | [Estate e registry](registry/README.md) + [descoberta e forecast](registry/discovery-and-forecast.md) + [schemas](../schemas/README.md) |
| classificar risco | [Risk-tiered governance](patterns/risk-tiered-governance.md) + [risk management](risk-management/README.md) |
| governar identidade e dados | [Identity](identity/README.md) + [data access](data-access/README.md) |
| governar tools e MCP | [Tool governance](tool-governance/README.md) + [MCP gateway pattern](patterns/tool-and-mcp-gateway.md) |
| governar modelos e provedores | [Model governance](model-governance/README.md) + [evaluations](evaluations/README.md) |
| governar mudança e retirement | [Lifecycle](lifecycle/README.md) + [lifecycle pattern](patterns/lifecycle-attestation-and-sunset.md) |
| publicar com evidência | [Evaluations](evaluations/README.md) + [control catalog](../controls/README.md) |
| operar e conter | [Operations](operations/README.md) + [runtime pattern](patterns/runtime-observability-and-quarantine.md) |
| medir maturidade | [Maturity model](guides/maturity-model.md) + [assessment example](../examples/maturity-assessment.example.json) |
| medir portfólio e valor | [Strategy and value](value/README.md) + [lifecycle pattern](patterns/lifecycle-attestation-and-sunset.md) |
| estruturar adoção e suporte | [Adoption](adoption/README.md) + [operations](operations/README.md) |
| estudar um caso Microsoft opcional | [Customer Zero case](explanations/microsoft-agent-governance-case-study.md) + [crosswalk histórico](../assessments/comparison-matrices/microsoft-case-study-framework-crosswalk.md) |
| seguir uma leitura linear | [Handbook](handbook/README.md) |

## Camadas do conhecimento

- **Normativo:** policy modular e decisões formalmente aprovadas.
- **Arquitetural:** princípios, operating model, boundaries e patterns.
- **Operacional:** playbooks, controls, schemas, templates e checklists.
- **Explicativo:** rationale, casos, mappings e referências.

Um documento de guidance não altera a policy. Um estudo de caso não comprova eficácia causal. Um mapping de fornecedor não redefine o núcleo.

A produtificação comercial pessoal está separada em [`consulting/`](../consulting/README.md). Ela reutiliza o conhecimento canônico, mas não integra estas camadas nem redefine a policy.

## Leitura completa

Para leitura linear, use o [handbook](handbook/README.md). A geração de uma publicação fica para uma etapa futura, quando o conteúdo estiver maduro.
