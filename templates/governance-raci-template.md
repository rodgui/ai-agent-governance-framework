---
title: Governance RACI Template
status: maintained
owner: AI Governance Office
last_reviewed: 2026-08-10
review_cycle: annual
supersedes: null
related:
  - ../docs/governance/operating-model.md
  - ../examples/governance-raci.example.md
  - governance-forum-tor.md
---

# Governance RACI Template

Use RACI para clarificar execução; use **decision rights** para clarificar authority. Cada decisão material possui um único accountable, mesmo quando várias funções são consulted.

## Escopo e papéis

| Campo | Valor |
| --- | --- |
| organization/unit | |
| estate scope | |
| effective date | |
| owner da matriz | |
| review trigger | |

| Sigla | Papel | Nome/função | Authority source | Delegate |
| --- | --- | --- | --- | --- |
| GOV | AI Governance Office | | | |
| BO | Business Owner | | | |
| TO | Technical Owner | | | |
| RA | Risk Authority | | | |
| DA | Design Authority | | | |
| RUN | Run Authority | | | |
| ASSURE | Assurance/Audit | | | |
| DATA | Data Authority | | | |
| SEC | Security Authority | | | |
| LEGAL | Legal/Privacy/Compliance | | | |

## Matriz de decisões

`R` = Responsible · `A` = Accountable · `C` = Consulted · `I` = Informed

| Decisão | GOV | BO | TO | RA | DA | RUN | ASSURE | DATA | SEC | LEGAL | Evidence/record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mandate e scope | | | | | | | | | | | |
| risk tier e admissibility | | | | | | | | | | | |
| design/blueprint | | | | | | | | | | | |
| data source certification | | | | | | | | | | | |
| tool/model admission | | | | | | | | | | | |
| release decision | | | | | | | | | | | |
| exception/expiry | | | | | | | | | | | |
| quarantine/reactivation | | | | | | | | | | | |
| risk acceptance | | | | | | | | | | | |
| attestation | | | | | | | | | | | |
| retirement/sunset | | | | | | | | | | | |
| policy/control change | | | | | | | | | | | |

## Handoffs e escalation

| From | To | Trigger | Preconditions | Evidence transferred | SLA | Escalation |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Segregation checks

- [ ] nenhum preparador é único approver da própria release T3/T4
- [ ] risk acceptance pertence à authority que suporta o impacto
- [ ] Run Authority pode conter sem depender do agente ou builder
- [ ] auditor/assurer não aprova o control que depois avaliará
- [ ] delegate tem prazo e scope explícitos
- [ ] ausência de role produz `hold`, não aprovação tácita

## Aprovação

| Authority | Disposition | Data | Evidence ref |
| --- | --- | --- | --- |
| | approve / condition / hold | | |
