---
title: Catálogo de artefatos do programa
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - ../guides/implementation-program-24-weeks.md
  - ../handbook/README.md
  - ../../templates/README.md
  - ../../examples/README.md
  - ../../schemas/README.md
---

# Catálogo de artefatos do programa

## Objetivo

Índice consolidado dos artefatos de uma implantação, com **propósito, owner típico e fase**. Serve para planejamento, atribuição de responsabilidade e controle de completude — não para leitura sequencial.

A definição, o procedimento e o exemplo de cada artefato ficam no domínio correspondente. Aqui está a visão de programa: o que precisa existir, sob responsabilidade de quem e em que momento.

Duas ressalvas sobre a coluna de fase. Ela referencia as fases F0–F6 do [programa de 24 semanas](../guides/implementation-program-24-weeks.md), que é **pattern de referência, não calendário normativo** — os únicos gates canônicos são G0–G7. E owner típico é ponto de partida, não prescrição: cada organização mapeia para as próprias funções.

## Mandato e diagnóstico

| Artefato | Para que serve | Owner típico | Fase | Onde está |
|---|---|---|---|---|
| Governance charter | mandato, escopo e authority do programa | sponsor + governança | F0 | [template](../../templates/governance-charter-template.md) · [exemplo](../../examples/governance-charter.example.md) |
| Scope statement | fronteira do programa e exclusões com prazo | governança + arquitetura | F0 | [exemplo](../../examples/governance-charter.example.md) |
| Princípios de decisão | critérios que orientam escolhas recorrentes | arquitetura + risco | F0 | [princípios arquiteturais](../architecture/principles.md) |
| Governance forums ToR | mandato, decision rights e cadência de cada fórum | presidência do fórum | F0/F2 | [template](../../templates/governance-forum-tor.md) |
| Agent estate inventory | baseline de agentes com confiança declarada | governança + plataforma | F1 | [descoberta e forecast](../registry/discovery-and-forecast.md) |
| Agent estate forecast | projeção de volume e mix de risco | governança + FinOps | F1 | [descoberta e forecast](../registry/discovery-and-forecast.md) |
| Manual bottleneck register | onde a governança depende de trabalho repetitivo | gestão do programa | F1 | [exemplo](../../examples/manual-bottleneck-register.example.md) |
| Capability map | capacidades atuais versus alvo, em 15 capacidades | arquitetura | F1 | [capability map](../guides/capability-map.md) · [worksheet](../../templates/capability-assessment-worksheet.md) |
| Maturity assessment report | maturidade evidenciada com confidence e coverage | arquitetura + governança | F1 | [maturity model](../guides/maturity-model.md) · [template](../../templates/maturity-assessment-template.md) · [schema](../../schemas/maturity-assessment.schema.json) |

## Operating model e risco

| Artefato | Para que serve | Owner típico | Fase | Onde está |
|---|---|---|---|---|
| Target maturity roadmap | evolução de capacidades com dependências | sponsor do programa | F2 | [exemplo](../../examples/target-maturity-roadmap.example.md) |
| Operating model | papéis, decision rights, fóruns e handoffs | governança | F2 | [operating model](../governance/operating-model.md) |
| RACI de governança | accountable único por decisão material | governança + owners | F0/F2 | [template](../../templates/governance-raci-template.md) · [exemplo](../../examples/governance-raci.example.md) |
| Handoff matrix | transições com pré-condição, evidência e SLA | gestão do programa | F2 | [exemplo](../../examples/handoff-matrix.example.md) |
| Risk classification standard | tiers, escaladores, red flags e admissibilidade | risco + segurança | F2 | [gestão de riscos](../risk-management/README.md) · [ADR-0009](../architecture/decisions/0009-risk-tier-and-admissibility.md) |
| Use-case intake | problema, baseline e hipótese de valor | negócio + governança | F2 | [template](../../templates/use-case-intake.md) |
| Risk pre-screen | roteamento rápido e acionamento de escaladores | governança | F2 | [template](../../templates/risk-pre-screen.md) |
| Agent risk record | tier, admissibilidade, residual risk e authority por agente | risco + owners | F2/F3 | [template](../../templates/agent-risk-record.md) |
| Impact assessment | impactos sobre pessoas, mitigações e residual | Responsible AI + risco | F2 | [Responsible AI](../responsible-ai/README.md#impact-assessment) |
| Approval e publication workflow | gates por tier e por gatilho | governança + plataforma | F2/F3 | [decision gates](../guides/framework-implementation-playbook.md) · [checklist](../../templates/publication-checklist.md) |

## Fundações técnicas

| Artefato | Para que serve | Owner típico | Fase | Onde está |
|---|---|---|---|---|
| Agent registry data standard | schema, obrigatoriedade por tier e quality rules | governança + plataforma | F3 | [registry](../registry/README.md) · [schema](../../schemas/agent-registry.schema.json) · [template](../../templates/agent-registry-template.md) |
| Agent taxonomy e metadata dictionary | classificação canônica e normalização por plataforma | governança + arquitetura | F2/F3 | [template](../../templates/agent-taxonomy-dictionary.md) |
| Agent blueprint | desired state machine-readable por versão, com bindings governados | arquitetura + plataforma | F3 | [schema](../../schemas/agent-blueprint.schema.json) · [template](../../templates/agent-blueprint-template.md) |
| Agent lifecycle standard | estados, transições, dormancy e retirada | plataforma + governança | F3 | [lifecycle](../lifecycle/README.md) |
| Identity e access standard | modo de identidade, autorização e JML | IAM | F3 | [identidade](../identity/README.md) |
| AI-ready data standard | critérios de certificação de fonte | governança de dados | F3 | [dados](../data-access/README.md) |
| Certified source catalog | fontes aprovadas com restrições e revisão | governança de dados | F3 | [schema](../../schemas/certified-source-catalog.schema.json) · [exemplo](../../examples/certified-source-catalog.example.md) |
| Data remediation backlog | fontes legítimas que ainda não passam | owners de dados | F3+ | [exemplo](../../examples/certified-source-catalog.example.md) |
| Tool, API e MCP governance standard | classificação por ação e mediação | segurança + API | F3 | [tools e MCP](../tool-governance/README.md) |
| Enterprise tool registry | catálogo de ferramentas com proveniência e escopo | plataforma + API | F3 | [schema](../../schemas/enterprise-tool-registry.schema.json) · [exemplo](../../examples/enterprise-tool-registry.example.json) |
| Model e provider governance standard | critérios, versão, fallback e saída | plataforma de IA | F3 | [modelos e provedores](../model-governance/README.md) |
| Approved model/provider catalog | combinações permitidas por classe de dados | plataforma de IA | F3 | [schema](../../schemas/model-provider-catalog.schema.json) · [exemplo](../../examples/model-provider-catalog.example.json) |
| Reference architecture | planos, fluxos e pontos de enforcement | arquitetura corporativa | F2 | [arquitetura de referência](../architecture/overview.md) · [exemplo](../../examples/architecture.example.md) |
| Decisão arquitetural por caso | agente é o mecanismo certo? | arquitetura | F2 | [árvore de decisão](../architecture/agent-or-not.md) |

## Assurance, runtime e valor

| Artefato | Para que serve | Owner típico | Fase | Onde está |
|---|---|---|---|---|
| Minimum production bar | piso de controles por tier e gate de admissibilidade | governança + plataforma | F3 | [MPB](../risk-management/minimum-production-bar.md) |
| Evidence pack standard | composição do pacote por tier e release | assurance | F3 | [evidence pack por tier](../auditability/evidence-pack-by-tier.md) |
| Release evidence manifest | manifesto verificável do que sustentou o release | assurance + plataforma | F3/F4 | [schema](../../schemas/release-evidence-manifest.schema.json) · [template](../../templates/release-evidence-manifest.md) |
| Audit event standard | evento auditável com correlação e integridade | plataforma + assurance | F3 | [schema](../../schemas/audit-event.schema.json) · [exemplo](../../examples/audit-event.example.json) |
| Security standard | baseline secure-by-design para agentes | segurança | F3 | [segurança](../security/README.md) |
| Threat e abuse case library | cenários de teste adversarial | segurança | F3/F4 | [segurança](../security/README.md) |
| AgentSecOps runbook pack | contenção, quarentena e recuperação | operação de segurança | F4 | [operações](../operations/README.md) · [exemplo](../../examples/support-runbook.example.md) |
| Observability standard | schema de telemetria e correlação | SRE + plataforma | F3 | [operações](../operations/README.md) · [SLO de exemplo](../../examples/slo.example.md) |
| Behavioral analytics catalog | detecções, thresholds e modo de operação | analytics + SRE | F4/F5 | [behavioral analytics](../operations/behavioral-analytics.md) · [template](../../templates/behavioral-analytics-use-case.md) |
| FinOps standard | custo por resultado, budget e quota | FinOps | F4/F5 | [FinOps](../operations/finops.md) |
| Governance dashboard specification | KPIs, KRIs e audiências | governança + SRE | F4/F5 | [KPIs e KRIs](../operations/kpi-kri-dashboard.md) |
| Business value scorecard | outcomes contra baseline declarado | negócio + portfólio | F4 | [estratégia e valor](../value/README.md) |
| Attestation e sunset record | revalidação, dormancy e retirada evidenciadas | governança + plataforma | F5 | [lifecycle](../lifecycle/README.md) · [template](../../templates/attestation-sunset-record.md) · [sunset plan](../../templates/sunset-plan.md) |
| Plano da rota de validação | como a implantação será validada ponta a ponta | gestão do programa | F4 | [plano de piloto](../guides/pilot-plan.md), quando a rota escolhida for piloto |
| Role-based enablement plan | currículo por papel e rede de champions | change lead | F4/F5 | [adoção](../adoption/README.md) |

## Como usar para controle de completude

Um artefato **existe** quando tem owner nomeado, conteúdo mínimo e é referenciado por quem o consome. Documento produzido e não consumido por nenhum processo é dívida, não entrega.

Duas leituras úteis:

- **por fase** — o que precisa existir antes do próximo gate;
- **por owner** — quantos artefatos uma mesma função acumula. Se uma função concentra muitos, ou o escopo dela está errado ou o programa vai gargalar nela.

A segunda leitura é a que costuma revelar o problema antes dele acontecer.
