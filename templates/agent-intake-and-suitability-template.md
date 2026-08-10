---
title: Agent Intake and Suitability Template
status: maintained
maturity: operational
last_reviewed: 2026-08-10
review_cycle: annual
owners: [governance, business-owner]
tags: [template, intake, suitability, g0]
related:
  - ../docs/fundamentals/README.md
  - ../docs/governance/policy.md
  - ../docs/value/README.md
  - risk-impact-assessment-template.md
---

# Agent Intake and Suitability Template

Use no G0 para decidir se o problema requer um agente. A resposta `agent` não é o default; workflow determinístico, busca, automação por regras ou processo humano podem ser superiores.

## 1. Identificação

- Intake ID:
- Data:
- Sponsor:
- Business owner:
- Technical owner:
- Usuários pretendidos:
- Affected parties:
- Jurisdições/regiões:
- Evidências analisadas até:

## 2. Problema e baseline

- Problema observável:
- Baseline atual:
- Volume/frequência:
- Gargalo:
- Outcome esperado:
- Métrica primária:
- Guardrail metrics:
- Custo de não agir:
- Prazo ou constraint legítimo:

Não use “adotar IA” ou “usar agentes” como problema.

## 3. Alternativas consideradas

| Alternativa | Desenho mínimo | Vantagem | Limitação/risco | Evidência | Disposição |
|---|---|---|---|---|---|
| processo humano | | | | | selected / rejected / combined / deferred |
| workflow determinístico | | | | | |
| automação por regras/RPA | | | | | |
| busca/retrieval sem geração | | | | | |
| modelo preditivo convencional | | | | | |
| agente | | | | | |
| híbrida | | | | | |

## 4. Teste de adequação do agente

| Pergunta | Sim/Não/Desconhecido | Evidência ou observação |
|---|---|---|
| O trabalho exige interpretação contextual ou adaptação que regras estáveis não cobrem? | | |
| Há interação iterativa com usuário, tools ou ambiente? | | |
| O outcome tolera incerteza residual sob controls verificáveis? | | |
| Sources, identity e tools podem ser limitados e observados? | | |
| A ação é reversível ou existe approval/containment proporcional? | | |
| Há owner capaz de aceitar o risco residual? | | |
| Existe evaluation approach antes de produção? | | |
| O benefício supera uma solução determinística mais simples? | | |

`Desconhecido` vira item de discovery ou floor de risco; nunca conta como aprovação.

## 5. Escopo inicial

- Intended use:
- Prohibited uses:
- Capabilities: observe / recommend / create / update / delete / execute
- Data classes:
- Tools/dependencies:
- Autonomy proposta:
- Human oversight:
- Environments:
- Blast radius:
- Rollback/containment concept:
- Material-change triggers já conhecidos:

## 6. Decisão G0

- Disposição: `proceed-agent` / `proceed-deterministic` / `proceed-hybrid` / `discovery-required` / `reject`
- Rationale:
- Decisor/authority:
- Data:
- Conditions:
- Expiry/review date:
- Evidence refs:
- Próximo gate/owner:

## 7. Completion rules

- [ ] problema e baseline são observáveis;
- [ ] pelo menos uma alternativa não agente foi comparada;
- [ ] intended e prohibited uses estão explícitos;
- [ ] business e technical owners estão nomeados;
- [ ] affected parties e failure modes foram considerados;
- [ ] unknowns têm owner e tratamento;
- [ ] a decisão registra rationale, authority, evidence e próximo passo.

Ausência de evidência, owner ou alternativa comparada impede `proceed-agent`.
