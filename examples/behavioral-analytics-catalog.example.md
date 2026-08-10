# Exemplo — Behavioral analytics catalog

> Fictício e sanitizado. Thresholds são ilustrativos e não devem ser copiados sem calibração local.

Demonstra [behavioral analytics de agentes](../docs/operations/behavioral-analytics.md). Cada caso combina **desvio relativo com piso absoluto**, declara o modo atual e nomeia como o falso positivo é medido.

| Caso | Feature e baseline | Threshold relativo | Piso absoluto | Contexto | Modo | Resposta | Métrica de falso positivo |
|---|---|---|---|---|---|---|---|
| runaway loop | `tool_calls/min` vs. baseline próprio de 30 dias | > 5× p95 | > 50 chamadas/min | janela de mudança e deploy | enforce | throttle + alerta; quarentena em T3 | alertas revertidos / total |
| pico de custo | `cost/session` vs. baseline próprio | > 4× p95 | > limite de budget do caso | volume de negócio, versão do modelo | alert | alerta; throttle em T2/T3 | correlação com evento de negócio |
| anomalia de privilégio | primeira ocorrência de ferramenta privilegiada | primeira vez | — | tier e risco da ferramenta | enforce | exigir aprovação + ticket de segurança | histórico de mudança e exceção |
| expansão de acesso | novo `source_id` ou aumento de amplitude | > 2× fontes distintas/dia | > 3 fontes novas | change record vigente | monitor-only | validar autorização | expansões legítimas registradas |
| mudança após release | delta de comportamento pós-deploy | > 3× p95 em 24h | — | diff de versão de modelo, prompt ou ferramenta | monitor-only | comparar versões; avaliar rollback | releases com mudança esperada |
| manipulação de aprovação | eventos de falha ou bypass de aprovação | ≥ 3 em 1h | — | histórico do ator | enforce | bloquear ação + incidente | tentativas legítimas mal roteadas |

## Por que os modos são diferentes

Três casos estão em `enforce` e três em `monitor-only` ou `alert`. A diferença não é importância — é **maturidade do baseline**.

`Runaway loop`, `anomalia de privilégio` e `manipulação de aprovação` têm assinatura determinística suficiente para agir: primeira ocorrência de ferramenta privilegiada não é ambígua. Já `expansão de acesso` e `mudança após release` dependem de contexto que a organização ainda está aprendendo a correlacionar — em enforcement gerariam ruído e treinariam a operação a ignorar o alerta.

`Pico de custo` fica em `alert` por um motivo específico: ele é simultaneamente sinal financeiro e sinal de segurança. Automatizar throttle antes de saber distinguir os dois pode cortar um processamento legítimo de fim de mês.

## Versionamento

Cada regra carrega `rule_id` e versão. Um incidente precisa indicar **qual lógica gerou a decisão** — sem isso, não é possível explicar a contenção depois nem melhorar a regra.

Mudança material no agente invalida o baseline: o caso volta a `monitor-only` pelo período de reaprendizagem.

## O que este exemplo não demonstra

- não define o pipeline de telemetria que produz as features;
- os thresholds são de partida — 5× p95 num agente de baixo volume dispara sem significado, e é para isso que existe o piso absoluto;
- não substitui regra determinística: o que já é proibido é bloqueado por policy, não detectado por desvio;
- ausência de alerta não é evidência de ausência de anomalia enquanto a cobertura de features não for declarada.
