---
title: Pattern — Lifecycle Attestation and Sunset
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - ../operations/README.md
  - ../../templates/sunset-plan.md
---

# Pattern — Lifecycle Attestation and Sunset

## Intent

Fazer aprovação expirar e exigir reconfirmação periódica de purpose, owners, risk, controls, evidence, uso e valor.

## Problema

Agents permanecem ativos após mudança de owner, dados, model, tools ou contexto. “Aprovado” vira status permanente; identidades, indexes e custos ficam órfãos.

## Contexto

Portfólio com múltiplas versões, mudanças frequentes, agents de uso sazonal ou capacidades state-changing.

## Forças e trade-offs

- continuidade versus revisão;
- cadência fixa versus event-driven;
- retention versus deletion;
- sunk cost versus sunset;
- owner convenience versus orphan risk;
- stable ID versus version approval.

## Solução

Use lifecycle state machine e attestation com expiry:

```text
discovered → registered → assessed → approved → active
                              ↘ conditional
active → changed → reassess
active → quarantined → remediated → active
active → sunset-planned → retired → archived
```

Attestation confirma condições atuais; não apenas assinatura.

## Estrutura e participantes

Participantes: business/technical owner, registry owner, Design Authority, Run Authority, data/identity/tool owners e records management.

## Fluxo operacional

1. definir cadence por tier;
2. coletar current state e missing evidence;
3. owner reconfirma purpose/usage/value;
4. domains reconfirmam access/controls quando aplicável;
5. authority decide maintain, condition, restrict ou sunset;
6. executar revocation/retention;
7. verificar órfãos e archive.

## Controles obrigatórios

- lifecycle states e valid transitions;
- approval/attestation expiry;
- material-change triggers;
- owner reminders/escalation;
- inactive/orphan detection;
- sunset plan;
- identity/tool/data revocation;
- retention/communication;
- completion verification.

## Evidências esperadas

- attestation record;
- current blueprint/version;
- usage/quality/value review;
- exceptions/findings;
- decision e expiry;
- sunset checklist;
- revocation/deletion/retention proof;
- orphan scan.

## Métricas

- expired attestations;
- agents sem owner/uso;
- time-to-sunset;
- orphan identities/connectors;
- recurring exceptions;
- approvals not re-opened after material change;
- retired assets ainda gerando custo.

## Consequências

**Positivas:** reduz sprawl, privilégios órfãos e approval stale.

**Custos:** stewardship, owner engagement e integrações de revogação.

## Limitações

Attestation por formulário pode virar teatro. Precisa de system evidence e decisões de portfólio.

## Antipatterns relacionados

- approval permanente;
- attestation como assinatura;
- UI desativada com backend ativo;
- deletion sem retention review;
- agent inativo mantido por sunk cost.

## Exemplo vendor-neutral

Um agent T3 vence em 90 dias. O registry detecta novo owner e tool version. A attestation reabre; sem evidence, status vira conditional. Se não regularizado, sunset revoga identity, connector e catalog discovery.

## Mappings de implementação

- GRC campaigns;
- identity access reviews;
- CMDB/service lifecycle;
- Git issues/workflows;
- control-plane attestation APIs.

## Patterns relacionados

- [Registry and Blueprint](registry-and-blueprint.md)
- [Runtime Observability and Quarantine](runtime-observability-and-quarantine.md)
- [Evidence Package as Code](evidence-package-as-code.md)
