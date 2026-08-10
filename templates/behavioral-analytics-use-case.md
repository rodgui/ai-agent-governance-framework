---
title: Behavioral Analytics Use Case
status: maintained
owner: Run Authority
last_reviewed: 2026-08-10
review_cycle: annual
supersedes: null
related:
  - ../docs/operations/behavioral-analytics.md
  - ../docs/operations/kpi-kri-dashboard.md
  - ../schemas/audit-event.schema.json
---

# Behavioral Analytics Use Case

Behavioral analytics só é governança quando um sinal possui owner, threshold, decisão e ação. Use monitor-only até conhecer falsos positivos e efeitos sobre pessoas.

## Caso

| Campo | Valor |
| --- | --- |
| use case ID | |
| agent population/scope | |
| risk hypothesis | |
| expected behavior | |
| owner | |
| Run Authority | |
| privacy/worker authority | |
| mode | design / monitor-only / enforce |

## Sinais e features

| Signal/feature | Source | Granularity | Retention | Data class | Known bias/limitation |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Não use conteúdo sensível quando metadado suficiente responder à hipótese. Documente atributos que não podem ser usados para inferência sobre pessoas.

## Baseline e detecção

| Elemento | Definição |
| --- | --- |
| baseline population/window | |
| peer grouping | |
| threshold/model | |
| minimum sample | |
| seasonality handling | |
| cold-start behavior | |
| confidence requirement | |

## Decision and response contract

| Severity | Condition | Owner | Automated action | Human decision | SLA | Evidence preserved |
| --- | --- | --- | --- | --- | --- | --- |
| info | | | none | review trend | | |
| warning | | | rate-limit/step-up only if approved | triage | | |
| critical | | | contain according to runbook | Run Authority disposition | | |

## Calibration

| Período | Alerts | True positives | False positives | Unknown | Missed events | Threshold change |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| | | | | | | |

**Promotion criteria de monitor-only para enforce:**

- [ ] false-positive rate conhecido e aceitável
- [ ] impact assessment concluído quando pessoas podem ser afetadas
- [ ] response action testada e reversível
- [ ] override, appeal e escalation definidos
- [ ] owner e SLA operacionais
- [ ] retention/minimization aprovadas

## Review e sunset

| Campo | Valor |
| --- | --- |
| effectiveness metric | |
| next review | |
| change triggers | |
| disable/sunset criteria | |
| decision ref | |

**Limitações e usos proibidos:**
