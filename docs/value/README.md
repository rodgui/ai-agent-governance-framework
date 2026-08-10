---
title: Estratégia, portfólio e evidência de valor
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../fundamentals/README.md
  - ../adoption/README.md
  - ../operations/README.md
  - ../governance/operating-model.md
---

# Estratégia, portfólio e evidência de valor

## Objetivo

Conectar cada agente a um problema, owner, baseline e decisão de portfólio, sem inferir valor a partir de volume, uso ou narrativa de fornecedor.

## Cadeia de valor

```text
Problema observado
  → hipótese de intervenção
  → capability do agente
  → mudança de comportamento/processo
  → output mensurável
  → outcome
  → impacto, custo e efeitos colaterais
```

Cada seta é uma hipótese que precisa de evidência. Um bom output pode não gerar outcome; um outcome pode ter outras causas.

## Business case mínimo

- problema e população afetada;
- processo atual e baseline;
- alternativa não-IA;
- intended/prohibited use;
- business e technical owner;
- benefits esperados e harms possíveis;
- custos build/run/change/support/assurance;
- métricas de adoção, qualidade e outcome;
- condições para manter, expandir, corrigir ou aposentar;
- horizonte de revisão.

## Métricas separadas

| Camada | Exemplos |
|---|---|
| criação | agentes, versões, tempo de build |
| descoberta | busca, visualização, seleção correta |
| adoção | usuários ativos, recorrência, workflow integration |
| uso | tarefas, sessões, tool calls, volume |
| qualidade | task success, erro, safety, groundedness |
| eficiência | tempo/custo por tarefa com qualidade preservada |
| outcome | backlog reduzido, cycle time, disponibilidade, erro operacional |
| impacto | financeiro, humano, regulatório, ambiental ou estratégico |

Não agregue essas camadas em uma única “AI adoption score” sem preservar significado.

## Baseline e atribuição

- medir o processo antes ou reconstruir baseline com limitações declaradas;
- comparar grupos, períodos ou tarefas equivalentes quando possível;
- registrar outras mudanças que afetam o outcome;
- distinguir correlação de causalidade;
- incluir custo de revisão humana, suporte e incidentes;
- comunicar intervalo, incerteza e qualidade do dado.

## Portfolio governance

Decisões de portfólio consideram:

- alinhamento estratégico;
- valor esperado e evidence strength;
- risco e residual impact;
- duplicidade e reuse;
- dependências e concentração;
- custo total e capacidade operacional;
- timing e reversibilidade;
- opportunity cost.

## Value review

| Decisão | Condição típica |
|---|---|
| manter | outcome e risco dentro do envelope |
| expandir | evidência suficiente, controls escaláveis e demanda legítima |
| corrigir | valor plausível, mas quality/control gap tratável |
| restringir | risco ou incerteza exige menor scope |
| substituir | alternativa entrega melhor relação valor-risco-custo |
| aposentar | sem owner, sem uso, sem outcome ou risco/custo injustificável |

## Evidências

- business case e baseline;
- metric definitions e data lineage;
- cost model;
- adoption/quality/outcome reports;
- incidents e externalities;
- portfolio decision e rationale;
- benefit hypothesis changes;
- sunset ou reinvestment decision.

## Métricas do portfólio

- itens sem business owner ou baseline;
- duplicated capabilities;
- custo por outcome e por tier;
- agentes com uso mas sem qualidade/outcome suficiente;
- agents inativos ainda operando;
- concentração por provider/model/tool;
- time-to-decision para corrigir ou aposentar;
- benefícios esperados versus observados, com incerteza.

## Failure modes

- valor inferido por número de agentes;
- horas “economizadas” sem medir qualidade ou deslocamento de trabalho;
- ROI calculado com adoção projetada como fato;
- ignorar custo de assurance e suporte;
- manter agente porque já foi construído;
- atribuir outcome ao agente sem baseline;
- premiar volume e criar agent sprawl;
- esconder externalities negativas.

## Decision gate

Nenhum item entra no portfólio financiado sem problema, owner, baseline ou plano explícito para obtê-lo, value hypothesis, costs, metrics e sunset criteria.
