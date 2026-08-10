---
title: Release Evidence Manifest Template
status: maintained
owner: Release Authority
last_reviewed: 2026-08-10
review_cycle: annual
supersedes: null
related:
  - ../docs/auditability/evidence-pack-by-tier.md
  - ../schemas/release-evidence-manifest.schema.json
  - ../examples/release-evidence-manifest.example.json
  - publication-checklist.md
---

# Release Evidence Manifest Template

Este é o formato humano para preparar a decisão. A versão final machine-readable deve validar contra o [schema](../schemas/release-evidence-manifest.schema.json). O manifesto aponta para evidências; não duplica nem substitui os artefatos de origem.

## Release

| Campo | Valor |
| --- | --- |
| release ID | |
| agent ID | |
| blueprint version | |
| environment/region | |
| risk tier | T1 / T2 / T3 / T4 |
| admissibility | permitted / conditional / restricted / prohibited |
| decision | approved / conditional / rejected / expired |
| created at | |

## Approvers

| Role | Authority | Decision | Timestamp | Evidence ref |
| --- | --- | --- | --- | --- |
| | | | | |

## Control evidence

| Control ID | Applicability | Status | Evidence refs | Verification result | Finding/exception |
| --- | --- | --- | --- | --- | --- |
| | applicable / not-applicable | pass / conditional / fail | | | |

## Evaluations e operational readiness

| Artefato | Version/scope | Result | Evidence ref |
| --- | --- | --- | --- |
| risk/impact assessment | | | |
| model evaluation/regression | | | |
| source/tool validation | | | |
| MPB | | | |
| rollback/kill-switch drill | | | |
| support/runbook/SLO | | | |

## Conditions e exceptions

| ID | Type | Authority | Compensating controls | Owner | Expiry | Monitoring |
| --- | --- | --- | --- | --- | --- | --- |
| | condition / exception | | | | | |

## Artifact integrity

| Path/URI | SHA-256 | Produced by | Produced at |
| --- | --- | --- | --- |
| | | | |

## Final checks

- [ ] `prohibited` resultou em `rejected`
- [ ] `restricted` possui exception authority e expiry
- [ ] blueprint, registry e manifest usam tier/admissibility coerentes
- [ ] model/source/tool catalog IDs existem e estão válidos
- [ ] findings bloqueantes foram fechados ou a decisão é `hold/rejected`
- [ ] evidence refs são recuperáveis e respeitam retenção/classificação
- [ ] nenhum secret ou payload sensível foi incluído

**Decision rationale:**
