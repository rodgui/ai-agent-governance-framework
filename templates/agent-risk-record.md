---
title: Agent Risk Record
status: maintained
owner: Risk Authority
last_reviewed: 2026-08-10
review_cycle: annual
supersedes: null
related:
  - ../docs/risk-management/README.md
  - ../docs/risk-management/minimum-production-bar.md
  - ../docs/architecture/decisions/0009-risk-tier-and-admissibility.md
  - ../schemas/agent-registry.schema.json
---

# Agent Risk Record

Tier e admissibilidade são decisões separadas. Não use T4 como sinônimo de `restricted`, nem risk acceptance para autorizar uso `prohibited`.

## Identificação

| Campo | Valor |
| --- | --- |
| risk record ID | |
| agent ID | |
| blueprint version | |
| use case/purpose | |
| business owner | |
| technical owner | |
| assessment date | |
| next review/trigger | |

## Contexto

| Dimensão | Descrição | Evidence ref |
| --- | --- | --- |
| affected decisions/processes | | |
| intended users/affected parties | | |
| reach and exposure | | |
| data classes and regions | | |
| autonomy and capabilities | | |
| tools and side effects | | |
| reversibility/detectability | | |
| legal/contractual context | | |
| uncertainty/novelty | | |

## Risk tier

| Campo | Valor |
| --- | --- |
| base tier | T1 / T2 / T3 / T4 |
| red flags/escalators | |
| final tier | T1 / T2 / T3 / T4 |
| tier rationale | |
| independent challenge | |

## Admissibilidade

| Campo | Valor |
| --- | --- |
| decision | `permitted` / `conditional` / `restricted` / `prohibited` |
| rationale | |
| policy/legal basis | |
| condition refs | |
| exception authority — se `restricted` | |
| exception ref — se `restricted` | |
| exception expiry — se `restricted` | |
| prohibition scope — se `prohibited` | |

## Risk scenarios

| Risk ID | Scenario/cause | Affected parties/assets | Inherent likelihood | Inherent impact | Controls | Residual risk | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Treatment e indicators

| Risk ID | Treatment | Due date | KRI/signal | Threshold | Response/runbook | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Material change triggers

- [ ] purpose or affected population
- [ ] model/provider/version or routing
- [ ] data source/classification/region
- [ ] identity, scope or tool
- [ ] autonomy, action class or delegation depth
- [ ] volume, reach or criticality
- [ ] approval/oversight flow
- [ ] incident, finding or external threat
- [ ] legal obligation or risk appetite
- [ ] admissibility, condition or exception expiry

## Decision

| Campo | Valor |
| --- | --- |
| disposition | approve / condition / hold / reject |
| residual risk authority | |
| decision date | |
| conditions and expiry | |
| MPB/evidence pack refs | |
| decision record ref | |

**Decision rationale:**

**Missing evidence — nunca preencher por suposição:**
