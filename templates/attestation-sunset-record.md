---
title: Attestation and Sunset Record
status: maintained
owner: Lifecycle Authority
last_reviewed: 2026-08-10
review_cycle: annual
supersedes: null
related:
  - ../docs/lifecycle/README.md
  - ../schemas/agent-registry.schema.json
  - sunset-plan.md
---

# Attestation and Sunset Record

Attestation revalida necessidade, owner, acesso e controls; não prolonga aprovação automaticamente. Sunset remove capabilities, custo e acesso com evidência preservada.

## Identificação

| Campo | Valor |
| --- | --- |
| record ID | |
| agent ID | |
| blueprint/release version | |
| lifecycle stage | discovered / draft / under-review / approved / production / retirement-review / retired / archived |
| operational state | not-deployed / enabled / suspended / quarantined / disabled |
| attestation due date | |
| reason/trigger | periodic / owner JML / dormancy / material change / incident / value review |

## Attestation checks

| Check | Resultado | Evidence ref | Finding/owner/due date |
| --- | --- | --- | --- |
| business purpose continua válido | pass / fail / unknown | | |
| business, technical e run owners estão ativos | pass / fail / unknown | | |
| tier e admissibilidade permanecem válidos | pass / fail / unknown | | |
| exception/conditions estão válidas e não expiradas | pass / fail / N/A | | |
| identities e scopes continuam mínimos | pass / fail / unknown | | |
| model/source/tool catalog bindings estão válidos | pass / fail / unknown | | |
| MPB e control evidence permanecem válidos | pass / fail / unknown | | |
| custo, uso e outcome justificam continuidade | pass / fail / unknown | | |
| incidents/findings foram considerados | pass / fail / unknown | | |

## Disposition

`continue` · `continue-with-conditions` · `suspend` · `quarantine` · `retirement-review`

| Campo | Valor |
| --- | --- |
| authority | |
| decision date | |
| rationale | |
| conditions | |
| next attestation | |
| decision ref | |

## Sunset execution — quando aplicável

| Ação | Owner | Due date | Concluída em | Evidence ref |
| --- | --- | --- | --- | --- |
| bloquear novas execuções | | | | |
| revogar identity, secrets e tokens | | | | |
| remover tool/source/model bindings ativos | | | | |
| encerrar budget, licença e infraestrutura | | | | |
| preservar logs/evidence conforme retenção | | | | |
| notificar usuários/downstream owners | | | | |
| atualizar registry para `retired/disabled` | | | | |
| após retenção, mover para `archived/disabled` | | | | |

## Transition record

| Campo | Valor |
| --- | --- |
| transition type | stage / operational / both |
| from stage/state | |
| to stage/state | |
| occurred at | |
| authority | |
| reason | |
| evidence ref | |

**Gaps que impedem encerramento:**
