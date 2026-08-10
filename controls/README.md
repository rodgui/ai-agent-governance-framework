---
title: Control catalog de governança de IA e agentes
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - control-catalog.json
  - ../schemas/control-catalog.schema.json
  - ../docs/guides/framework-implementation-playbook.md
  - ../docs/patterns/README.md
---

# Control catalog de governança de IA e agentes

O catálogo traduz policy e princípios em requirements verificáveis. A fonte estruturada é [`control-catalog.json`](control-catalog.json), validada pelo [`control-catalog.schema.json`](../schemas/control-catalog.schema.json).

## Estrutura de um control

Cada control declara:

- ID estável e domain;
- statement e rationale;
- tipos preventivo, detectivo, responsivo ou corretivo;
- owner role;
- tiers aplicáveis;
- implementation patterns;
- evidence esperada;
- metrics;
- mappings externos opcionais quando houver referência verificável.

Os controls são módulos diretos da [policy canônica](../docs/governance/policy.md), não mappings de uma policy histórica. `frameworkMappings` documenta alinhamentos externos e não transforma standards ou fornecedores em dependências normativas.

## Como aplicar

1. classifique o agent/use case;
2. selecione a baseline do tier;
3. avalie applicability e contexto;
4. registre implementation owner;
5. vincule evidence verificável;
6. teste design e eficácia;
7. registre missing, not-applicable, passed ou failed sem equivaler estados;
8. trate findings e residual risk;
9. reavalie após change, incident ou attestation.

O catálogo integra a policy candidate. Ele se torna baseline normativa de uma organização somente quando a release correspondente é explicitamente aprovada e adotada.

O piso operacional que traduz esta baseline em gate verificável é o [Minimum Production Bar por tier](../docs/risk-management/minimum-production-bar.md).

## Cobertura

- **adoption:** 2 controls
- **audit:** 3 controls
- **data:** 3 controls
- **evaluation:** 3 controls
- **identity:** 3 controls
- **operations:** 3 controls
- **organization:** 3 controls
- **registry:** 3 controls
- **responsible-ai:** 3 controls
- **risk:** 3 controls
- **security:** 3 controls
- **tools:** 3 controls
- **value:** 3 controls

Total: **38 controls**.

## Índice

| ID | Domínio | Controle | Tiers |
|---|---|---|---|
| `AGF-ORG-001` | organization | Mandato e ownership | T1, T2, T3, T4 |
| `AGF-ORG-002` | organization | Decision rights e segregation | T2, T3, T4 |
| `AGF-ORG-003` | organization | Exceção com expiração | T1, T2, T3, T4 |
| `AGF-REG-001` | registry | Registry e ownership | T1, T2, T3, T4 |
| `AGF-REG-002` | registry | Blueprint e mudança material | T2, T3, T4 |
| `AGF-REG-003` | registry | Attestation e sunset | T1, T2, T3, T4 |
| `AGF-IDN-001` | identity | Workload identity atribuível | T2, T3, T4 |
| `AGF-IDN-002` | identity | Least privilege e autorização | T1, T2, T3, T4 |
| `AGF-IDN-003` | identity | Secrets e revogação | T1, T2, T3, T4 |
| `AGF-DAT-001` | data | Data contract e owner | T1, T2, T3, T4 |
| `AGF-DAT-002` | data | Autorização e minimização | T2, T3, T4 |
| `AGF-DAT-003` | data | Provenance, retenção e exclusão | T1, T2, T3, T4 |
| `AGF-TOL-001` | tools | Tool/MCP registry e provenance | T2, T3, T4 |
| `AGF-TOL-002` | tools | Gateway e validação de ação | T3, T4 |
| `AGF-TOL-003` | tools | Kill switch e circuit breaker | T3, T4 |
| `AGF-SEC-001` | security | Threat model do sistema agentic | T2, T3, T4 |
| `AGF-SEC-002` | security | Sandbox, egress e supply chain | T3, T4 |
| `AGF-SEC-003` | security | Adversarial testing e regression | T2, T3, T4 |
| `AGF-RSK-001` | risk | Tiering e red flags | T1, T2, T3, T4 |
| `AGF-RSK-002` | risk | Assessment e residual risk | T2, T3, T4 |
| `AGF-RSK-003` | risk | Reavaliação contínua | T1, T2, T3, T4 |
| `AGF-RAI-001` | responsible-ai | Impact assessment | T2, T3, T4 |
| `AGF-RAI-002` | responsible-ai | Human accountability e contestação | T2, T3, T4 |
| `AGF-RAI-003` | responsible-ai | Transparência, fairness e monitoramento | T2, T3, T4 |
| `AGF-EVA-001` | evaluation | Evaluation strategy e thresholds | T1, T2, T3, T4 |
| `AGF-EVA-002` | evaluation | Release evidence gate | T1, T2, T3, T4 |
| `AGF-EVA-003` | evaluation | Runtime evaluation e regression | T2, T3, T4 |
| `AGF-AUD-001` | audit | Correlation e version traceability | T2, T3, T4 |
| `AGF-AUD-002` | audit | Evidence package e integridade | T1, T2, T3, T4 |
| `AGF-AUD-003` | audit | Acesso, retenção e export | T1, T2, T3, T4 |
| `AGF-OPS-001` | operations | Observabilidade orientada a ação | T2, T3, T4 |
| `AGF-OPS-002` | operations | Quarantine, rollback e reactivation | T2, T3, T4 |
| `AGF-OPS-003` | operations | Change, incident e attestation loop | T1, T2, T3, T4 |
| `AGF-ADP-001` | adoption | Discovery, guidance e suporte | T1, T2, T3, T4 |
| `AGF-ADP-002` | adoption | Competência e feedback loop | T2, T3, T4 |
| `AGF-VAL-001` | value | Business case e baseline | T1, T2, T3, T4 |
| `AGF-VAL-002` | value | Métricas separadas | T1, T2, T3, T4 |
| `AGF-VAL-003` | value | Portfolio review e decisão | T1, T2, T3, T4 |

## Evidência versus implementação

O catálogo especifica outcomes e evidências, não produtos. Por exemplo, `AGF-TOL-002` pode ser implementado por API gateway, MCP proxy, broker ou policy engine. A escolha é válida se caller, policy, argumentos, destino, limits, approval e outcome forem controlados e demonstráveis.

## Estados recomendados

| Estado | Significado |
|---|---|
| `missing` | não há evidence suficiente |
| `not-applicable` | rationale e authority confirmam não aplicabilidade |
| `planned` | implementation possui owner e prazo |
| `implemented` | design/configuração existe |
| `effective` | teste ou operação demonstra eficácia no escopo |
| `failed` | control não atende ao requisito |
| `excepted` | exceção válida com compensating controls e expiry |

`implemented` não deve ser automaticamente tratado como `effective`.

## Mappings externos

Mappings para NIST, ISO, OECD, EU AI Act, OWASP ou outros frameworks são informativos. Eles ajudam crosswalks, mas não constituem declaração de conformidade, certificação ou equivalência jurídica.
