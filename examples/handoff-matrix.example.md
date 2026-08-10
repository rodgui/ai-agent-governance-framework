# Exemplo — Handoff matrix

> Fictício e sanitizado. Pré-condições, evidências e SLAs são ilustrativos.

Demonstra os [handoffs obrigatórios](../docs/governance/operating-model.md#handoffs-obrigatórios). A regra: **um handoff sem owner receptor e sem evidência não está concluído** — está apenas anunciado.

| Transição | De | Para | Pré-condições | Evidência transferida | SLA |
|---|---|---|---|---|---|
| intake → classificação | solicitante | Governance Office | caso descrito com problema, owner e processo afetado | intake + [risk pre-screen](../templates/risk-pre-screen.md) | 2 dias |
| design → security review | builder | Segurança | T2/T3; blueprint completo | blueprint + threat model + lista de ferramentas | 3 dias |
| design → data review | builder | Domínio de Dados | fonte fora do catálogo certificado | fonte, finalidade, classificação pretendida | 5 dias |
| security → publication gate | Segurança | Governance/Plataforma | findings críticos e altos fechados ou aceitos | resultado da review + residual risk | 1 dia |
| publicação → operação | Design Authority | Run Authority | release `approve` ou `condition` registrado | thresholds, telemetria, runbooks, owner de suporte | antes da exposição |
| produção → quarentena | SOC/policy | Plataforma/IAM | sinal crítico de segurança ou comportamento | ID do incidente + snapshot de evidência | imediato |
| quarentena → produção | Technical Owner | Run + Design Authority | causa identificada e corrigida | evidência de regressão + aprovação | após regression |
| dormente → retirada | automação de lifecycle | owner | threshold atingido, sem exceção vigente | `last_seen` + histórico de notificação | 15 dias de grace |
| owner sai da empresa | RH/IAM | Governance Office | evento de desligamento | lista de agentes sob ownership | antes do desligamento |

## O que a matriz revela

**O handoff mais frágil é o último.** O evento de desligamento costuma chegar ao IAM e nunca ao registry de agentes. Sem essa linha, agentes ficam com owner formal que não existe mais — e o problema só aparece na próxima attestation, meses depois.

**Quarentena é o único handoff sem SLA em dias.** Contenção com prazo em dias não é contenção.

**Reativar não tem SLA de tempo, tem SLA de evidência.** É deliberado: pressa para reativar é exatamente o que reintroduz o incidente.

## O que este exemplo não demonstra

- não define severidade de incidente nem critério de sinal crítico;
- SLAs precisam sair da capacidade real medida, não da aspiração;
- a matriz não substitui runbook: ela diz o que atravessa a fronteira, não como executar;
- handoffs entre domínios de negócio distintos podem exigir linhas adicionais.
