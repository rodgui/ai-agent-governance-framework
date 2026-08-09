---
title: "Plano de evolução do framework — 90 dias"
status: draft
maturity: hypothesis
last_reviewed: 2026-08-09
review_cycle: 30d
owners: [rodgui]
tags: [implementation-plan, policy-v2, agent-governance, roadmap]
related:
  policy: ../governance/ai-agent-policy-and-governance-v1.md
  study: ../explanations/microsoft-agent-governance-case-study.md
  crosswalk: ../../assessments/comparison-matrices/microsoft-case-study-framework-crosswalk.md
---

# Plano de evolução do framework — 90 dias

## Goal

Transformar a policy v1 e o estudo Microsoft Customer Zero em um modelo operacional testável, preservando a policy vigente e produzindo evidências suficientes para decidir uma futura v2.

O sucesso ao final de 90 dias não é “ter toda a governança pronta”. É demonstrar, em pilotos, que a organização consegue inventariar, classificar, avaliar, publicar, observar, remediar e aposentar agentes com ownership e métricas confiáveis.

## Constraints and non-goals

### Constraints

- A policy v1 não será reescrita silenciosamente.
- Novos controles precisam ser proporcionais ao risco e ao estágio de maturidade.
- O modelo deve permanecer multiplataforma.
- Dados, identidade, segurança, privacy e compliance continuam com seus owners especializados.
- Automação só entra depois de ownership, baselines e exceções estarem definidos.

### Non-goals

- selecionar ou implantar um produto de control plane em 90 dias;
- automatizar todas as aprovações;
- estabelecer thresholds universais sem pilotos;
- declarar data mesh como arquitetura adotada;
- publicar uma policy v2 sem revisão formal.

## Workstreams

1. **Operating model:** papéis, authority, RACI e handoffs.
2. **Registry and blueprint:** source of truth, schema, inventory e attestation.
3. **Data and identity:** AI-ready data, labels, connector gates e lifecycle de identidade.
4. **Risk and assurance:** matriz proporcional, impact assessment e release assessment.
5. **Tool and MCP governance:** catálogo, gateway, vetting e isolamento.
6. **Adoption and support:** coortes, champions, assets e support tiers.
7. **Runtime and value:** telemetria, quarantine, remediação e métricas.

## Phase 0 — decisões de partida (dias 0–10)

### Deliverables

- nomear sponsor, Design Authority, Run Authority e owners dos sete workstreams;
- escolher 2–3 pilotos representando baixo, médio e alto risco;
- decidir o source of truth provisório do catálogo;
- aprovar a definição de “AI-ready” como hipótese de trabalho;
- definir autoridade de quarantine e escalation path;
- registrar riscos, dependências e baseline disponível.

### Exit criteria

- owners nominativos;
- pilotos selecionados;
- decisões de source of truth e quarantine registradas;
- nenhuma lacuna crítica sem owner.

## Phase 1 — visibilidade e classificação (dias 11–30)

### Registry and blueprint

- definir schema mínimo do catálogo;
- reconciliar inventário de plataformas piloto;
- registrar business owner, technical owner, identidade, dados, conectores, alcance, capacidade, risco e lifecycle;
- criar primeiro agent blueprint separado do registry;
- classificar ownerless, unused, duplicados e expirados.

### Risk and assurance

- expandir blast radius com read/write/action/workflow, reversibilidade, regionalidade e método no/low/pro-code;
- definir triggers de impact assessment e release assessment;
- mapear assessments existentes para DPIA, security, privacy, RAI e accessibility.

### Exit criteria

- 100% dos pilotos registrados;
- owners e capabilities confirmados;
- risk matrix versão 0.1 aplicada;
- gaps de evidência visíveis, sem preenchimento fictício.

## Phase 2 — dados, identidade e publicação (dias 31–60)

### Data and identity

- identificar data owners e labels das fontes piloto;
- avaliar qualidade, permissões, provenance e suitability para IA;
- definir connector gates por classe de dado;
- testar lifecycle da identidade em mudança ou saída de owner;
- registrar workload identity e secrets handling.

### Tool and MCP governance

- inventariar tools, APIs, destinos e MCP servers usados pelos pilotos;
- definir requisitos mínimos de vetting, gateway, isolation, logging e kill switch;
- proibir integrações sem owner ou provenance.

### Publication flow

- atualizar a evidência do Publication Checklist sem alterar a policy v1;
- executar impact/release assessment nos pilotos aplicáveis;
- testar rollback, quarantine e reactivation;
- capturar tempo e fricção de cada gate.

### Exit criteria

- fontes e connectors classificados;
- identidade e secrets validados;
- um drill de quarantine e rollback executado;
- evidências de release armazenadas e recuperáveis.

## Phase 3 — adoção, runtime e valor (dias 61–90)

### Adoption and support

- definir coortes de builders, usuários, admins e especialistas;
- ativar uma pequena champion network;
- criar guidance e assets para os pilotos;
- implantar suporte em quatro níveis: self-service, AI-assisted, IT backstop e SME;
- registrar feedback e resistência como backlog, não como anedota.

### Runtime and value

- consolidar logs, uso, custos, dados acessados e policy signals;
- criar dashboard mínimo orientado a decisão;
- medir detecção, decisão, quarantine e remediation;
- separar criação, descoberta, uso, qualidade e valor;
- executar primeira attestation e decisão de continuidade.

### Policy v2 proposal

- revisar o crosswalk com evidências dos pilotos;
- classificar recomendações em manter, alterar, rejeitar ou experimentar;
- produzir proposta de policy v2 sem modificar a v1;
- registrar limitações e decisões ainda abertas.

### Exit criteria

- pilotos com telemetria e owner review;
- uma attestation concluída;
- métricas de uso e pelo menos um outcome por piloto;
- proposta de v2 pronta para revisão, não autoaprovada.

## Decision gates

### Gate A — depois do dia 10

Decidir se os pilotos e owners são suficientes. Sem owner ou source of truth, não avançar para automação.

### Gate B — depois do dia 30

Validar registry, blueprint e matriz de risco. Se os campos não forem preenchíveis com evidência, simplificar antes de escalar.

### Gate C — depois do dia 60

Validar publicação, quarantine e rollback. Agentes sem controle de ação ou evidência não avançam para maior alcance.

### Gate D — depois do dia 90

Decidir se há evidência para policy v2, novos pilotos ou revisão do modelo.

## Metrics

### Controle

- cobertura do catálogo;
- agents with valid owners;
- fontes e connectors classificados;
- assessments concluídos quando aplicáveis;
- policy violations e tempo de remediação;
- ownerless, unused, duplicados e exceções vencidas.

### Adoção e valor

- descoberta versus criação de duplicados;
- usuários ativos e recorrência por persona;
- qualidade e erro por cenário;
- produtividade sem perda de qualidade;
- satisfação e support demand;
- custo por outcome;
- decisão de manter, promover, corrigir ou aposentar.

## Risks and mitigations

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Transformar assessments em burocracia | Alto | Gates proporcionais, formulários curtos e feedback ao builder |
| Catálogo incompleto gerar falsa confiança | Alto | Mostrar missing evidence explicitamente; reconciliar fontes |
| Centralizar governança em um único time | Alto | RACI distribuído, authority e handoffs explícitos |
| Automatizar policy instável | Alto | Pilotar manualmente e medir antes de automatizar |
| Métricas de vaidade | Médio | Ligar cada agente a outcome e baseline |
| Copiar thresholds da Microsoft | Médio | Validar em contexto local e registrar racional |
| MCP ampliar blast radius | Alto | Gateway, vetting, identity, isolation e kill switch |

## Immediate next actions

1. Aprovar owners e pilotos.
2. Revisar o [crosswalk](../../assessments/comparison-matrices/microsoft-case-study-framework-crosswalk.md).
3. Criar schema mínimo de registry e blueprint como primeiro incremento executável.
