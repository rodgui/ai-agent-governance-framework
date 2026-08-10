# Template — Agent Blueprint

> Use para revisão humana. A versão estruturada deve validar contra [`schemas/agent-blueprint.schema.json`](../schemas/agent-blueprint.schema.json).

## Metadados

- Agent ID:
- Blueprint version:
- Technical Owner:
- Última revisão:
- Registry record:
- Risk tier:

## 1. Intended architecture

- Pattern: assistant / workflow-agent / tool-using-agent / multi-agent / embedded-ai / other
- Descrição end-to-end:
- Diagram:
- Ambientes e regiões:

### Trust boundaries

1.
2.

### Dependências

| Nome | Tipo | Criticality | Owner | Failure effect |
|---|---|---|---|---|
| | | | | |

## 2. Modelos

| Model ID | Provider | Purpose | Hosting | Version pinned? | Data use | Limitações |
|---|---|---|---|---|---|---|
| | | | | | | |

## 3. Dados e memória

### Sources/connectors

| Source ID | Classificação | Purpose | Owner | Authorization | Retention | Região |
|---|---|---|---|---|---|---|
| | | | | | | |

### Memory

- Mode: none / session / user / team / organization
- Categories allowed:
- Sensitive data allowed:
- Retention:
- Correction/deletion mechanism:
- Poisoning controls:

## 4. Identidade e autorização

- Identity model:
- Principal:
- Scopes:
- Token/expiry:
- Secret management:
- Delegated-user behavior:
- Break-glass:
- Revocation path:

## 5. Tools, APIs e MCP

> Na taxonomia estruturada v1.0, a classe `create` representa criação/persistência de artefato ou registro fora da resposta transitória e exige `stateChanging: true`.

| Tool ID | Class | Protocol | State-changing | Reversible | Approval | Scopes | Owner | Gateway | Kill switch |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## 6. Agent logic e boundaries

- Planning/orchestration:
- Maximum steps/delegation depth:
- Budget/rate limits:
- Allowed actions:
- Human approval actions:
- Prohibited actions:
- Output validation:
- Fallback behavior:

## 7. Security e Responsible AI

- Threat model:
- Impact assessment:
- Affected parties:
- Transparency:
- Human oversight:
- Contestability/redress:
- Safety/security tests:
- Residual risk:

## 8. Evaluations

- Intended scenarios:
- Critical/negative scenarios:
- Metrics e thresholds:
- Test data provenance:
- Slice analysis:
- LLM-as-judge calibration:
- Promotion/rollback criteria:

## 9. Runtime

- Observability:
- SLOs:
- Signals/thresholds:
- Run Authority:
- Quarantine:
- Rollback:
- Kill switch:
- Support/escalation:

## 10. Governance

- Control IDs:
- Assessment refs:
- Release evidence:
- Attestation expiry:
- Material change triggers:
- Exceptions/conditions:

## 11. Failure modes

| Failure scenario | Detection | Containment | Recovery | Owner |
|---|---|---|---|---|
| | | | | |

## Reviewer checklist

- [ ] Blueprint explica dados, identidade, tools e blast radius.
- [ ] Controls são externos ao prompt quando necessário.
- [ ] State-changing actions possuem enforcement.
- [ ] Runtime, containment e rollback são concretos.
- [ ] Mudanças materiais são identificáveis.
- [ ] Secrets foram substituídos por `[REDACTED]`.
