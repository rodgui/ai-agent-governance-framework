# Template — Agent Registry Record

> Use para coleta e revisão humana. A versão machine-readable deve validar contra [`schemas/agent-registry.schema.json`](../schemas/agent-registry.schema.json).

## Identificação

- Agent ID:
- Nome:
- Descrição:
- Finalidade:
- Usuários pretendidos:
- Usos proibidos:
- Tags:

## Ownership

| Papel | Nome | Função | Contato | Unidade |
|---|---|---|---|---|
| Business Owner | | | | |
| Technical Owner | | | | |
| Run Owner | | | | |
| Data Owner(s) | | | | |

## Lifecycle

- Lifecycle stage: `discovered` / `draft` / `under-review` / `approved` / `production` / `retirement-review` / `retired` / `archived`
- Operational state: `not-deployed` / `enabled` / `suspended` / `quarantined` / `disabled`
- Criado em:
- Entrou no stage em:
- Aprovado em:
- Sunset previsto:
- Motivo do stage/state:
- Attestation válida até:

### Transition history

| Type | From stage/state | To stage/state | Occurred at | Authority | Reason | Evidence ref |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Risco

- Tier: T1 / T2 / T3 / T4
- Admissibilidade: `permitted` / `conditional` / `restricted` / `prohibited`
- Admissibility rationale:
- Condition refs:
- Exception ref/authority/expiry — se `restricted`:
- Assessment:
- Classificado em:
- Red flags:
- Residual risk:
- Decision authority:

## Blueprint atual

- Versão:
- Path/URL:
- SHA-256:

## Plataformas

| Plataforma | Ambiente | Tenant | Região | External ID |
|---|---|---|---|---|
| | | | | |

## Capabilities

- [ ] observe
- [ ] create
- [ ] modify
- [ ] execute
- [ ] approve
- [ ] delete
- [ ] delegate

## Evidências

| Tipo | Path/URL | Hash | Validade |
|---|---|---|---|
| Assessment | | | |
| Controls | | | |
| Evaluation | | | |
| Approval | | | |
| Attestation | | | |
| Sunset | | | |

## Discovery e reconciliação

- Discovery status: `confirmed` / `probable` / `suspected`
- Confidence:
- First seen:
- Last seen:

| Source system | Signal type | Observed at | Evidence ref |
| --- | --- | --- | --- |
| | | | |

- Conflitos encontrados:
- Decisão de reconciliação:

## Reviewer checklist

- [ ] Owners foram confirmados.
- [ ] Purpose e prohibited use são claros.
- [ ] Tier e admissibilidade possuem rationale e evidence.
- [ ] Blueprint atual está ligado.
- [ ] Stage, operational state, transition history e attestation são válidos.
- [ ] Discovery status e confidence não foram confundidos.
- [ ] Missing evidence permanece explícito.
