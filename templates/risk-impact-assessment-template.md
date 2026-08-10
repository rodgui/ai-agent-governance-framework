---
title: Risk and Impact Assessment Template
status: maintained
maturity: operational
last_reviewed: 2026-08-10
review_cycle: major-change
owners: [risk, responsible-ai, business-owner]
tags: [template, risk, impact, responsible-ai, g1]
related:
  - ../docs/risk-management/README.md
  - ../docs/responsible-ai/README.md
  - publication-checklist.md
---

# Risk and Impact Assessment Template

Use this content template to produce a decision-grade assessment in the organization's approved system of record.

This assessment classifies risk and impact. It does **not** approve release or publication; G5 remains a separate decision record.

## 1. Record identity

- Assessment ID/version:
- Agent ID/version:
- Status: draft / review / decided / expired
- Assessed at:
- Assessor:
- Evidence cutoff:
- Last reviewed:

## 2. Risk-model manifest

- Model ID/version:
- Effective date:
- Configuration reference:
- Automation use: manual / decision-support / automated-routing
- Calibration status: not-calibrated / calibrating / calibrated
- Calibration evidence refs:

Automated routing requires calibrated evidence, controlled configuration, monitoring and rollback. A score cannot lower a floor or replace authority.

## 3. Scope and alternatives

- Intended use:
- Prohibited uses:
- Baseline:
- Affected parties:
- Environments/regions:

| Alternativa | Descrição | Disposição | Rationale |
|---|---|---|---|
| | | selected / rejected / combined / deferred | |

## 4. Contextual dimensions

Rating: `low`, `moderate`, `high`, `critical` ou `unknown`.

| Dimension | Rating | Observation | Evidence refs |
|---|---|---|---|
| purpose and affected decisions | | | |
| reach | | | |
| data | | | |
| autonomy | | | |
| capability | | | |
| privilege | | | |
| interconnectivity | | | |
| reversibility | | | |
| detectability | | | |
| exposure | | | |
| affected parties and vulnerability | | | |
| legal and contractual context | | | |
| novelty and uncertainty | | | |
| business criticality | | | |

## 5. Uncertainty

- Level:
- Tier floor:
- Rationale:
- Unknowns:
- Discovery or monitoring treatment:

Unknown or missing evidence does not reduce tier.

## 6. Active red flags

| Red-flag ID | Category | Minimum tier | Rationale | Evidence refs |
|---|---|---|---|---|
| | | T1 / T2 / T3 / T4 | | |

The final tier must be at least the highest active red-flag floor.

## 7. Impact Trigger Screen

- Triggered: yes / no
- Triggers:
  - rights or opportunities;
  - access, eligibility or decisions about people;
  - vulnerable groups;
  - physical safety;
  - employment or workforce;
  - public autonomous communication;
  - regulated/high-impact process;
  - profiling or monitoring;
  - other.
- Rationale:
- Evidence refs:
- Full Impact Assessment ref, when triggered:

A positive trigger blocks completion without an Impact Assessment reference.

## 8. Classification

- Candidate tier:
- Uncertainty floor:
- Highest red-flag floor:
- Final tier:
- Disposition: confirm / raise / hold / reject
- Rationale:
- Authority:
- Decided at:
- Optional score/method/threshold ref:
- Score marked non-authoritative: yes / no

## 9. Residual risk

- Level:
- Decision: accepted / conditioned / not-accepted / pending
- Rationale:
- Owner:
- Authority:
- Conditions:
- Expiry:
- Evidence refs:

## 10. Change and release linkage

- Material-change triggers:
- Reassessment owner:
- Optional G5 release-decision ref:

The release reference points to a separate record. Do not paste approval into this assessment.

## 11. Evidence register

| Evidence ID | Title | Type | Reference | Observed at | Source | Scope | Limitation |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 12. Completion rules

- [ ] record and risk-model versions are present;
- [ ] all dimensions contain observation and evidence;
- [ ] uncertainty and unknowns have a tier floor/treatment;
- [ ] final tier respects candidate, uncertainty and red-flag floors;
- [ ] positive impact triggers reference a complete assessment;
- [ ] registry and blueprint carry the same agent ID/version/tier;
- [ ] residual-risk decision has owner, authority and expiry when accepted/conditioned;
- [ ] limitations and material-change triggers are explicit;
- [ ] G5 decision remains separate.
