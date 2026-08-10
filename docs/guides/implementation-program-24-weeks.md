---
title: Programa de implantação em 24 semanas
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - framework-implementation-playbook.md
  - implementation-plan-90-days.md
  - pilot-plan.md
  - maturity-model.md
---

# Programa de implantação em 24 semanas

## Objetivo

Dar forma de **programa** ao que o [implementation playbook](framework-implementation-playbook.md) define como **decisões**. As fases organizam tempo, equipe e entregáveis; os gates G0–G7 continuam sendo o que autoriza avançar.

Uma fase pode terminar sem que o gate correspondente seja aprovado. Quando isso acontece, o programa não avança: o gate manda, o calendário não.

## Fases e gates

| Fase | Semanas | Objetivo | Entregáveis | Gate correspondente |
|---|---|---|---|---|
| **F0 — Mobilizar** | 1–2 | mandato e escopo | charter, scope statement, decision principles, fóruns, time do programa | G0 |
| **F1 — Descobrir** | 3–5 | baseline real | discovery do estate, forecast, gargalos manuais, capability map, maturity baseline | G1 |
| **F2 — Desenhar** | 6–8 | target operating model | target de maturidade, tiers calibrados, triggers de RAI, operating model, patterns de referência | G3 e preparação de G4 |
| **F3 — Construir** | 9–12 | controles de fundação | registry, padrões de identidade, catálogos de dados e tools, schema de telemetria, MPB, runbooks iniciais | G2 e G4 |
| **F4 — Pilotar** | 13–16 | validar ponta a ponta | coortes por tier, fluxo risco→RAI→publicação, observabilidade, tabletop de incidente, KPIs de valor | G5 e G6 |
| **F5 — Escalar** | 17–20 | automação e cobertura | automação de discovery, policy-as-code, JML, attestation, baselines de comportamento, FinOps, dashboards | G6 |
| **F6 — Institucionalizar** | 21–24 | operação regular e assurance | evidência e assurance, enablement, handoff para BAU, cadência de governança, roadmap de 12 meses | G7 |

O [roadmap de 90 dias](implementation-plan-90-days.md) é o caminho mínimo — corresponde a F0–F3 comprimidas. Este programa é a versão completa. Os dois são visões do mesmo conjunto de gates, não métodos concorrentes.

## F0 — Mobilizar (semanas 1–2)

1. Entrevistar sponsors e validar problema e mandato.
2. Produzir charter, scope statement e princípios de decisão.
3. Definir fóruns de governança, presidências, decision rights e cadência.
4. Nomear program manager e leads de domínio.
5. Montar o corpus de referência e a baseline de standards aplicáveis.

**Critério de saída:** existe autoridade para definir requisitos, exigir evidência e conter sistemas fora do envelope aprovado. Sem isso, não automatize aprovações nem prometa cobertura.

## F1 — Descobrir (semanas 3–5)

1. Executar [discovery do estate](../registry/discovery-and-forecast.md) em fontes técnicas e por entrevistas.
2. Produzir forecast de 6, 12 e 24 meses com mix de risco.
3. Mapear gargalos manuais e padrões de shadow AI.
4. Executar capability map e [maturity assessment](maturity-model.md) com evidência.
5. Publicar baseline, principais riscos e nível de confiança.

**Critério de saída:** o baseline separa o observado da hipótese, tem data de corte e todo gap crítico tem owner.

## F2 — Desenhar (semanas 6–8)

1. Definir target de maturidade por capability — não nível máximo em tudo.
2. Calibrar tiers, scoring e escaladores com casos reais.
3. Desenhar operating model, RACI e handoff matrix.
4. Definir a integração risco → impact trigger → RAI → domain reviews → gate de publicação.
5. Aprovar arquitetura de referência e patterns por tier.

**Critério de saída:** cada decisão material tem accountable, receptor, prazo e escalation.

## F3 — Construir (semanas 9–12)

1. Implementar o registry mínimo viável e os identificadores.
2. Implementar padrões de identidade e remediar credenciais compartilhadas nos casos-piloto.
3. Criar o standard de dados AI-ready e o catálogo inicial de fontes certificadas.
4. Criar o registro de tools e a mediação para ações de alto impacto.
5. Implementar schema de telemetria, dashboards básicos, [MPB](../risk-management/minimum-production-bar.md) e repositório de evidência.

**Critério de saída:** controles centrais demonstráveis em ambiente piloto — não apresentados em slide.

## F4 — Pilotar (semanas 13–16)

1. Selecionar de 8 a 15 agentes cobrindo T1 a T3 e padrões arquiteturais distintos.
2. Executar o lifecycle completo de pelo menos um T2 e um T3.
3. Testar contenção de incidente e kill switch de verdade.
4. Rodar [behavioral analytics](../operations/behavioral-analytics.md) em monitor-only.
5. Medir lead time, falsos positivos, fricção percebida e KPI de negócio.

O detalhamento está no [plano de piloto](pilot-plan.md).

**Critério de saída:** critérios de saída do piloto atendidos, controles ajustados e nenhum bloqueador crítico aberto.

## F5 — Escalar (semanas 17–20)

1. Automatizar discovery, registro e policy gates simples.
2. Integrar JML, reatribuição de owner e workflow de dormancy.
3. Expandir fontes certificadas, tools e identidades próprias.
4. Calibrar detecções de comportamento e budgets de [FinOps](../operations/finops.md).
5. Expandir enablement e a rede de champions.

**Critério de saída:** metas de cobertura atingidas e gargalos manuais mensuravelmente reduzidos.

## F6 — Institucionalizar (semanas 21–24)

1. Executar a revisão de evidência e assurance da primeira onda.
2. Transferir responsabilidades para a operação regular e documentar o modelo de suporte.
3. Publicar o [governance dashboard](../operations/kpi-kri-dashboard.md) e a cadência de fóruns.
4. Reavaliar maturidade e definir o target de 12 meses.
5. Planejar a automação restante com base nos dados do piloto.

**Critério de saída:** owners de BAU nomeados, cadência funcionando e próximos targets acordados.

## Como usar sem virar teatro de programa

- fases podem se sobrepor; gates não;
- prazo cumprido com evidência ausente é `hold`, não `approve`;
- escopo reduzido é decisão legítima e registrada, não fracasso silencioso;
- as 24 semanas dimensionam esforço, não prometem maturidade — maturidade se demonstra por evidência de operação, conforme o [maturity model](maturity-model.md).

## O que este programa não faz

- não substitui análise jurídica ou regulatória;
- não define threshold universal;
- não seleciona produto;
- não comprova maturidade por documentação;
- não certifica conformidade;
- não promete resultado financeiro.
