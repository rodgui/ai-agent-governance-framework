---
title: Plano opcional de piloto e critérios de expansão
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - implementation-program-24-weeks.md
  - framework-implementation-playbook.md
  - ../risk-management/minimum-production-bar.md
  - ../operations/behavioral-analytics.md
---

# Plano opcional de piloto e critérios de expansão

> **Uso opcional.** Este documento é um template para organizações que escolhem um piloto porque precisam aprender em ambiente delimitado. Cohort de onboarding, phased rollout ou evidência de agentes existentes podem cumprir o mesmo objetivo. G0–G7, MPB e evidence requirements continuam iguais em qualquer rota.

## Objetivo

Quando escolhido, o piloto existe para **testar a governança**, não para provar que um modelo de linguagem funciona.

Se todos os casos-piloto forem de leitura, a organização não valida identidade própria, mediação de ferramentas, oversight humano, rollback, quarentena, evidence pack ou resposta a incidente — e conclui, erradamente, que está pronta.

## Coorte

Selecione de três a quatro casos que **forcem rotas diferentes** do framework.

| Coorte | O que valida | Exemplo |
|---|---|---|
| T1 fast path | discovery, registro automático e rota self-service | assistente pessoal de conhecimento |
| T1 revisado | ownership de time e fonte de dados certificada | perguntas e respostas sobre procedimentos de uma área |
| T2 | transação e governança de ferramentas | agente que abre e atualiza chamados |
| T3 | assurance completo e aprovação humana | agente que propõe mudança material e executa após aprovação |

Como regra de aprendizagem, não comece por T4: primeiro demonstre fundações e containment em casos menos críticos. Exceções são legítimas quando o primeiro caso real já é T4 ou quando a criticidade exige validação imediata; nesse cenário, aplique authority e controls de T4 desde o início. T4 não é sinônimo de `restricted`.

## Desenho

1. Selecionar a coorte cobrindo leitura, transação e alto impacto.
2. **Congelar baseline** de processo, custo e qualidade antes do go-live — sem isso, não há como atribuir resultado depois.
3. Executar o fluxo completo: intake → risco → blueprint → build → reviews → MPB → publicação → observação → attestation ou mudança → simulação de suspensão e retirada.
4. Medir lead time e retrabalho **da governança**, além da performance do agente.
5. Executar ao menos um tabletop de incidente e um teste real de kill switch e quarentena.
6. Rodar behavioral analytics em monitor-only e FinOps por tarefa e resultado.
7. Coletar feedback separado de builder, reviewer, owner e operador — os quatro enxergam fricções diferentes.
8. Ajustar standards e thresholds **antes** de escalar, documentando o que mudou e por quê.

## O que medir

| Dimensão | Indicador |
|---|---|
| fricção | lead time por etapa e por tier; retrabalho de review |
| cobertura | completude do registry e do evidence pack |
| contenção | tempo até quarentena; sucesso do rollback |
| detecção | falsos positivos das regras de comportamento |
| economia | custo por resultado bem-sucedido contra baseline |
| resultado | KPI de negócio do caso, contra baseline congelada |
| experiência | percepção de builder, reviewer, owner e operador |

## Critérios de expansão quando a rota escolhida é piloto

Se a organização escolheu piloto, não escale a cohort antes de todos serem verdadeiros:

- nenhum finding crítico aberto; findings altos apenas com residual risk aceito pela authority correta;
- lead time de T1 baixo o suficiente para que **contornar a governança não compense**;
- T2 e T3 com identidade, evidência e telemetria completas;
- kill switch, quarentena e rollback funcionaram no teste — não em documentação;
- falsos positivos das regras de comportamento compreendidos e ajustados;
- custo e resultado efetivamente mensuráveis;
- owners de operação regular aceitaram a responsabilidade operacional, nominalmente.

O último item é o mais ignorado e o que mais derruba programas: sem owner de BAU aceito, o piloto vira uma ilha mantida pelo time do programa.

## Relatório de piloto

O relatório fecha o ciclo e alimenta a decisão de expansão. Deve conter: objetivos; coorte; baseline congelada; controles efetivamente exercitados; gaps encontrados; lead time por etapa; exceções abertas; resultado do tabletop e do teste de contenção; achados de telemetria e comportamento; custo e valor; mudanças recomendadas nos standards; e a decisão registrada de `approve`, `condition` ou `hold` para a próxima onda.

## Failure modes

- piloto só com casos de leitura, gerando falsa sensação de maturidade;
- medir apenas a performance do agente e nunca a fricção da governança;
- go-live sem baseline congelada — resultado sem atribuição possível;
- kill switch testado em documento;
- ajustar standards depois de escalar, quando o custo da mudança já multiplicou;
- piloto sem owner de operação regular designado;
- tratar ausência de incidente no piloto como prova de segurança.

## Decision gate

Quando houver piloto, a expansão para a próxima onda exige relatório com decisão registrada, critérios atendidos e mudanças de standard incorporadas e versionadas. Sem piloto, a organização precisa apresentar evidência equivalente da primeira cohort, phased rollout ou operação existente; o gate avalia a qualidade da evidência, não o nome da rota.
