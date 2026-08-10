---
title: Control catalog de governança de IA e agentes
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - control-catalog.json
  - ../schemas/control-catalog.schema.json
  - ../docs/guides/framework-implementation-playbook.md
  - ../docs/patterns/README.md
---

# Control catalog de governança de IA e agentes

O catálogo 1.2.0 traduz policy e princípios em requirements verificáveis. A fonte estruturada é [`control-catalog.json`](control-catalog.json), validada pelo [`control-catalog.schema.json`](../schemas/control-catalog.schema.json) 2.0. Consulte a [migração dos contratos](../docs/guides/schema-migration-2.0.md).

## Estrutura de um control

Cada control declara:

- ID estável e domain;
- `scope`: `organization` quando é satisfeito uma vez para a organização, `agent` quando é avaliado por agente ou release;
- statement e rationale;
- tipos preventivo, detectivo, responsivo ou corretivo;
- owner role;
- tiers aplicáveis;
- implementation patterns;
- `verification`: os testes objetivos que decidem se o control passa;
- evidence esperada;
- `blocking`: se a reprovação impede release ou continuidade em produção;
- metrics;
- automation: `manual`, `assisted`, `automated` ou `mixed`;
- mappings externos quando houver referência verificável.

A distinção entre `evidence` e `verification` é deliberada. **Evidence é o artefato; verification é o teste.** "Governance charter" não diz o que faz o control passar — por isso todo control declara os dois.

`scope` existe porque duas classes diferentes de control conviviam no mesmo catálogo: "este agente tem decision rights?" não é uma pergunta com resposta. Controls organizacionais são evidenciados uma vez, no nível do programa; controls de agente são avaliados a cada release. Os tiers de um control organizacional indicam quais tiers a capacidade precisa suportar.

Os controls são módulos diretos da [policy canônica](../docs/governance/policy.md), não mappings de uma policy histórica. `frameworkMappings` documenta alinhamentos externos e não transforma standards ou fornecedores em dependências normativas.

## Como aplicar

1. classifique o agent/use case e decida admissibilidade;
2. selecione a baseline do tier e as condições/exception controls da admissibilidade;
3. avalie applicability e contexto;
4. registre implementation owner;
5. vincule evidence verificável;
6. teste design e eficácia;
7. registre missing, not-applicable, passed ou failed sem equivaler estados;
8. trate findings e residual risk;
9. reavalie após change, incident ou attestation.

O catálogo integra a policy canônica adotada deste repositório. Ele se torna baseline normativa de uma organização somente quando a release correspondente é explicitamente aprovada e adotada pela authority da própria organização.

O piso operacional que traduz esta baseline em gate verificável é o [Minimum Production Bar por tier](../docs/risk-management/minimum-production-bar.md).

## Cobertura

| Domínio | Controls | Domínio | Controls |
|---|---:|---|---:|
| adoption | 2 | organization | 3 |
| audit | 3 | registry | 3 |
| data | 3 | responsible-ai | 3 |
| evaluation | 3 | risk | 4 |
| identity | 3 | security | 3 |
| lifecycle | 2 | tools | 3 |
| model | 3 | value | 3 |
| operations | 3 | | |

Total: **44 controls** — 40 de escopo `agent` e 4 de escopo `organization`; 27 bloqueantes.

A distribuição é aproximadamente uniforme, e isso é um sinal a observar, não uma virtude: risco real não é simétrico entre domínios. Os números atuais refletem a origem editorial do catálogo. Conforme evidência operacional se acumular, espere que alguns domínios cresçam e outros encolham — e trate uma distribuição que **permanece** uniforme como indício de que o catálogo não está aprendendo com a operação.

## Índice

| ID | Domínio | Título | Escopo | Tiers | Bloqueia? |
|---|---|---|---|---|---|
| `AGF-ADP-001` | adoption | Discovery, guidance e suporte | agent | T1, T2, T3, T4 | não |
| `AGF-ADP-002` | adoption | Competência e feedback loop | organization | T2, T3, T4 | não |
| `AGF-AUD-001` | audit | Correlation e version traceability | agent | T2, T3, T4 | sim |
| `AGF-AUD-002` | audit | Evidence package e integridade | agent | T1, T2, T3, T4 | sim |
| `AGF-AUD-003` | audit | Acesso, retenção e export | agent | T1, T2, T3, T4 | não |
| `AGF-DAT-001` | data | Data contract e owner | agent | T1, T2, T3, T4 | sim |
| `AGF-DAT-002` | data | Autorização e minimização | agent | T2, T3, T4 | sim |
| `AGF-DAT-003` | data | Provenance, retenção e exclusão | agent | T1, T2, T3, T4 | não |
| `AGF-EVA-001` | evaluation | Evaluation strategy e thresholds | agent | T1, T2, T3, T4 | sim |
| `AGF-EVA-002` | evaluation | Release evidence gate | agent | T1, T2, T3, T4 | sim |
| `AGF-EVA-003` | evaluation | Runtime evaluation e regression | agent | T2, T3, T4 | não |
| `AGF-IDN-001` | identity | Workload identity atribuível | agent | T2, T3, T4 | sim |
| `AGF-IDN-002` | identity | Least privilege e autorização | agent | T1, T2, T3, T4 | sim |
| `AGF-IDN-003` | identity | Secrets e revogação | agent | T1, T2, T3, T4 | sim |
| `AGF-LFC-001` | lifecycle | State machine e transições autorizadas | agent | T1, T2, T3, T4 | sim |
| `AGF-LFC-002` | lifecycle | Dormência e sucessão de ownership | agent | T1, T2, T3, T4 | não |
| `AGF-MDL-001` | model | Catálogo de combinações aprovadas | agent | T2, T3, T4 | sim |
| `AGF-MDL-002` | model | Evaluation vinculada à versão | agent | T2, T3, T4 | sim |
| `AGF-MDL-003` | model | Fallback, portabilidade e saída | agent | T2, T3, T4 | não |
| `AGF-OPS-001` | operations | Observabilidade orientada a ação | agent | T2, T3, T4 | sim |
| `AGF-OPS-002` | operations | Quarantine, rollback e reactivation | agent | T2, T3, T4 | sim |
| `AGF-OPS-003` | operations | Change, incident e attestation loop | agent | T1, T2, T3, T4 | não |
| `AGF-ORG-001` | organization | Mandato e authority de governança | organization | T1, T2, T3, T4 | não |
| `AGF-ORG-002` | organization | Decision rights e segregation | organization | T2, T3, T4 | não |
| `AGF-ORG-003` | organization | Exceção com expiração | agent | T1, T2, T3, T4 | não |
| `AGF-RAI-001` | responsible-ai | Impact assessment | agent | T2, T3, T4 | sim |
| `AGF-RAI-002` | responsible-ai | Human accountability e contestação | agent | T2, T3, T4 | sim |
| `AGF-RAI-003` | responsible-ai | Transparência, fairness e monitoramento | agent | T2, T3, T4 | não |
| `AGF-REG-001` | registry | Registry e ownership | agent | T1, T2, T3, T4 | sim |
| `AGF-REG-002` | registry | Blueprint e mudança material | agent | T2, T3, T4 | sim |
| `AGF-REG-003` | registry | Attestation e sunset | agent | T1, T2, T3, T4 | não |
| `AGF-RSK-001` | risk | Tiering e red flags | agent | T1, T2, T3, T4 | sim |
| `AGF-RSK-002` | risk | Assessment e residual risk | agent | T2, T3, T4 | sim |
| `AGF-RSK-003` | risk | Reavaliação contínua | agent | T1, T2, T3, T4 | não |
| `AGF-RSK-004` | risk | Admissibilidade e exceções temporárias | agent | T1, T2, T3, T4 | sim |
| `AGF-SEC-001` | security | Threat model do sistema agentic | agent | T2, T3, T4 | sim |
| `AGF-SEC-002` | security | Sandbox, egress e supply chain | agent | T3, T4 | sim |
| `AGF-SEC-003` | security | Adversarial testing e regression | agent | T2, T3, T4 | não |
| `AGF-TOL-001` | tools | Tool/MCP registry e provenance | agent | T2, T3, T4 | sim |
| `AGF-TOL-002` | tools | Gateway e validação de ação | agent | T2, T3, T4 | sim |
| `AGF-TOL-003` | tools | Kill switch e circuit breaker | agent | T2, T3, T4 | sim |
| `AGF-VAL-001` | value | Business case e baseline | agent | T1, T2, T3, T4 | sim |
| `AGF-VAL-002` | value | Métricas separadas | organization | T1, T2, T3, T4 | não |
| `AGF-VAL-003` | value | Portfolio review e decisão | agent | T1, T2, T3, T4 | não |

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

Todos os 44 controls declaram `frameworkMappings` para as referências **públicas e verificáveis**: NIST AI RMF 1.0 (funções `GOVERN`, `MAP`, `MEASURE`, `MANAGE`), EU AI Act (Regulamento (UE) 2024/1689, no nível de artigo), OWASP para riscos agentic e MCP, e MITRE ATLAS para táticas adversariais.

Cada mapping carrega a nota de que representa **alinhamento direcional declarado pelo framework** — não equivalência, conformidade nem atestação. Um mapping é uma afirmação sobre intenção de desenho, não sobre o resultado de uma avaliação.

**ISO/IEC 42001, 23894 e 42005 não estão mapeadas.** O mapeamento exige o texto das normas, que é pago, e um número de cláusula inventado seria pior que a ausência declarada. Enquanto isso não for resolvido, o alinhamento a ISO permanece uma afirmação de leitura, não uma rastreabilidade control a control — e deve ser apresentado como tal.
