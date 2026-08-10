---
title: KPIs, KRIs e governance dashboard
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - finops.md
  - ../value/README.md
  - ../governance/operating-model.md
---

# KPIs, KRIs e governance dashboard

## Objetivo

Separar três coisas que dashboards costumam misturar — desempenho, exposição a risco e operação do processo — e garantir que **toda métrica apresentada a um fórum tenha owner, threshold contextualizado e ação esperada**.

Métrica sem ação associada é decoração. Dashboard que não muda uma decisão é observação.

## Três tipos, três usos

| Tipo | O que mede | Exemplo | Ação associada |
|---|---|---|---|
| **KPI** | desempenho ou resultado desejado | % de T2/T3 com identidade própria | priorizar remediação se abaixo da meta |
| **KRI** | exposição ou deterioração de risco | % de T3 com attestation vencida | suspender ou escalar conforme prazo |
| **operacional** | capacidade do processo | lead time da security review | ajustar intake, automação ou capacidade |
| **valor** | economia e resultado real | custo por caso bem-sucedido + cycle time | escalar, redesenhar ou aposentar |

## Indicadores de referência

Os alvos abaixo são **pontos de partida para a conversa**, não SLA universal. A regra: metas de higiene e accountability podem ser absolutas; métricas de adoção, custo, falso positivo e lead time precisam partir do baseline e do perfil operacional.

| Tipo | Indicador | Referência inicial |
|---|---|---|
| KPI | cobertura do inventário | ≥95% na implantação; ≥98% em operação madura |
| KPI | agentes em produção com owner | 100%; ownerless em T2/T3 igual a zero |
| KPI | lead time de aprovação por tier | T1 fast path imediato; T1 revisado até 1 dia; T2 de 3 a 5 dias; T3 de 5 a 15 dias; T4 sem rota normal |
| KPI | cobertura de attestation | ≥98% vigente; T3 vencido igual a zero |
| KRI | agentes de alto risco sem owner | zero em T2/T3/T4, com remediação imediata |
| KRI | anomalias de uso de ferramenta privilegiada | 100% investigadas; severidade alta dentro do SLA de resposta |
| KRI | agentes fora do padrão de identidade aprovado | zero em T2/T3 em produção; tendência decrescente nos demais |
| KRI | agentes T2/T3 dormentes | abaixo de 5% sem justificativa; 100% com ação de revisão ou retirada |
| Valor | custo por resultado bem-sucedido | baseline mais meta de melhoria acordada por caso |
| Valor | melhoria do KPI de negócio | alvo específico do caso; **adoção não é proxy de resultado** |
| Adoção | usuários ativos diários, semanais e mensais | sem alvo universal; usar tendência e frequência esperada do caso |

Registre a justificativa de cada threshold e a data de revisão. Revise após o primeiro ciclo com dados reais.

## Como interpretar métricas de adoção

Usuários ativos medem frequência e retenção, **não valor**. Um agente pode ter uso mensal alto porque virou etapa obrigatória de um fluxo e ainda assim piorar o cycle time. Adoção só significa algo junto de qualidade e outcome.

## Dashboard executivo mínimo

- **estate e crescimento:** conhecidos versus estimados, novos por semana, mix de tiers;
- **ownership e lifecycle:** sem owner, attestation vencida, dormentes, candidatos a retirada;
- **risco e segurança:** findings críticos, incidentes, quarentenas, exceções de alto impacto;
- **cobertura de controles:** identidade, dados certificados, registro de ferramentas, telemetria e conformidade com o [Minimum Production Bar](../risk-management/minimum-production-bar.md);
- **FinOps:** custo por agente, custo por resultado, variação de budget e principais anomalias;
- **valor:** adoção, KPI de outcome, valor observado e agentes sem valor demonstrado;
- **programa:** lead time por tier, retrabalho de review, cobertura de automação e progresso de maturidade.

Não coloque todo o detalhe em uma página. Mantenha navegação entre a visão de governança e a evidência operacional: a página executiva mostra postura; as páginas operacionais permitem drill-down até o trace e a ação de ferramenta.

## Como definir thresholds

Não transforme toda métrica em verde e vermelho arbitrários. Use baseline, risk appetite, SLA e tendência.

Para agentes T3 sem owner, a tolerância pode ser zero. Para falso positivo de uma regra de comportamento nova, a meta é calibrada gradualmente. Em ambos os casos, registre a razão do threshold e quando ele será revisto.

## Evidências

- definição de cada métrica com fórmula, fonte e owner;
- thresholds com rationale e data de revisão;
- histórico de decisões tomadas a partir do dashboard;
- lacunas de dados declaradas, em vez de preenchidas por estimativa.

## Métricas do próprio dashboard

- métricas exibidas sem owner ou sem ação definida;
- indicadores que nunca mudaram uma decisão;
- lacunas de cobertura de dados por perspectiva;
- tempo entre sinal e decisão registrada.

## Failure modes

- misturar KPI, KRI e métrica operacional na mesma leitura;
- média agregada que esconde uma dimensão crítica;
- alvo copiado de outro contexto sem baseline próprio;
- adoção apresentada como prova de valor;
- dashboard completo e ilegível em uma única página;
- precisão numérica sobre dados de baixa cobertura;
- verde e vermelho sem rationale registrado.

## Decision gate

Nenhuma métrica entra em um fórum de governança sem owner, threshold com rationale e ação esperada. Nenhum indicador de higiene crítica — ownership, attestation, identidade — é reportado sem cobertura declarada.
