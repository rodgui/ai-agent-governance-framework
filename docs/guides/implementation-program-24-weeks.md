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

> **Pattern de referência, não calendário normativo.** As 24 semanas oferecem um ponto de partida para equipes que ainda não sabem como organizar a implantação. Adapte duração, sobreposição, ordem e nomenclatura ao contexto. Os únicos decision gates canônicos são G0–G7; nem este programa nem um piloto são requisitos universais.

## Objetivo

Dar forma de **programa** ao que o [implementation playbook](framework-implementation-playbook.md) define como **decisões**. As fases organizam tempo, equipe e entregáveis; os gates G0–G7 continuam sendo o que autoriza avançar.

Para uma organização que adote este pattern, uma fase pode terminar sem que o gate correspondente seja aprovado. Quando isso acontece, o escopo não avança: o gate manda, o calendário não.

## Fases e gates

| Fase | Semanas | Objetivo | Entregáveis | Gate correspondente |
|---|---|---|---|---|
| **F0 — Mobilizar** | 1–2 | mandato e escopo | charter, scope statement, decision principles, fóruns, time do programa | G0 |
| **F1 — Descobrir** | 3–5 | baseline real | discovery do estate, forecast, gargalos manuais, capability map, maturity baseline | G1 |
| **F2 — Desenhar** | 6–8 | target operating model | target de maturidade, tiers calibrados, triggers de RAI, operating model, patterns de referência | G3 e preparação de G4 |
| **F3 — Construir** | 9–12 | controles de fundação | registry, padrões de identidade, catálogos de dados e tools, schema de telemetria, MPB, runbooks iniciais | G2 e G4 |
| **F4 — Validar** | 13–16 | validar ponta a ponta | piloto opcional, cohort de onboarding ou estate existente; fluxo risco→RAI→publicação, observabilidade, tabletop e KPIs | G5 e G6 |
| **F5 — Escalar** | 17–20 | automação e cobertura | automação de discovery, policy-as-code, JML, attestation, baselines de comportamento, FinOps, dashboards | G6 |
| **F6 — Institucionalizar** | 21–24 | operação regular e assurance | evidência e assurance, enablement, handoff para BAU, cadência de governança, roadmap de 12 meses | G7 |

O [roadmap de 90 dias](implementation-plan-90-days.md) é uma referência acelerada — corresponde aproximadamente a F0–F3 comprimidas. Este programa é uma referência mais detalhada. Os dois são guias adaptáveis do mesmo conjunto de gates, não métodos concorrentes nem prazos de compliance.

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
2. Implementar padrões de identidade e remediar credenciais compartilhadas na primeira cohort selecionada.
3. Criar o standard de dados AI-ready e o catálogo inicial de fontes certificadas.
4. Criar o registro de tools e a mediação para ações de alto impacto.
5. Implementar schema de telemetria, dashboards básicos, [MPB](../risk-management/minimum-production-bar.md) e repositório de evidência.

**Critério de saída:** controles centrais demonstráveis em ambiente controlado ou por evidência operacional equivalente — não apresentados apenas em slide.

## F4 — Validar (semanas 13–16)

Escolha uma rota de validação proporcional: piloto dedicado, cohort de onboarding, phased rollout ou avaliação retrospectiva de agentes já operacionais. O [plano de piloto](pilot-plan.md) é um template útil quando a organização escolhe piloto; não é prerequisite deste programa.

1. Selecionar de 8 a 15 agentes cobrindo T1 a T3 e padrões arquiteturais distintos.
2. Executar o lifecycle completo de pelo menos um T2 e um T3.
3. Testar contenção de incidente e kill switch de verdade.
4. Rodar [behavioral analytics](../operations/behavioral-analytics.md) em monitor-only.
5. Medir lead time, falsos positivos, fricção percebida e KPI de negócio.

**Critério de saída:** evidence suficiente para os gates G5/G6, controls ajustados e nenhum bloqueador crítico aberto. Se a rota escolhida for piloto, aplique também os critérios do [plano de piloto](pilot-plan.md).

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
5. Planejar a automação restante com base nos dados da rota de validação escolhida.

**Critério de saída:** owners de BAU nomeados, cadência funcionando e próximos targets acordados.

## Workstreams

Workstream é trilha de execução paralela dentro do **mesmo** roadmap — não um segundo cronograma.

| Workstream | Lead típico | F0–F2 | F3–F4 | F5–F6 |
|---|---|---|---|---|
| governança e risco | governança/risco | charter, tiers, triggers de RAI, operating model | workflow, evidência, reviews da primeira cohort | automação, assurance, exceções |
| arquitetura e plataforma | arquitetura/plataforma | patterns de referência | integração registry, runtime e policy | escala, resiliência, APIs |
| identidade e segurança | IAM/segurança | patterns e ameaças | identidade própria, controles, runbooks | JML, integração com SOC, tuning |
| dados e ferramentas | dados/API | desenho de standards e catálogos | fontes certificadas, tool registry | cobertura, remediação, recertificação |
| observabilidade e custo | SRE/FinOps | desenho da telemetria | dashboards, baseline, budget | automação de comportamento, unit economics |
| adoção e valor | negócio/change | portfólio, personas | enablement da primeira cohort, KPI | champions, operação regular, value review |

### Prioridade do backlog

`P0` · `P1` · `P2` é prioridade de backlog, **não** severidade nem fase paralela. Cada item continua vinculado a uma fase, a um workstream, a dependências e a um critério de saída.

| Prioridade | Significado | Exemplos |
|---|---|---|
| **P0** | obrigatório para iniciar a primeira release/cohort com segurança e rastreabilidade — sem isso o programa não deve se declarar pronto | charter, registry mínimo, tiers, blueprint, MPB, identidade para T2/T3, catálogos de fontes e ferramentas, logging, gate de publicação, kill switch, repositório de evidência |
| **P1** | necessário para escalar sem criar gargalo manual ou perda de controle | discovery automatizado, JML, automação de attestation, integração com SOC, behavioral analytics, dashboard de custo, policy-as-code, rede de champions |
| **P2** | otimização e automação avançada; antecipável quando houver dependência ou risco específico | scoring assistido, routing de modelos, detecção de duplicidade, grafo entre agentes, atribuição avançada de valor, remediação automática |

### Um item de backlog de qualidade

| Campo | Exemplo |
|---|---|
| outcome | 100% dos T2/T3 com identidade própria correlacionada ao registry |
| por quê | eliminar credencial compartilhada e habilitar atribuição e baseline de comportamento |
| dependências | `agent_id` no registry, API de IAM, dados de owner, eventos de lifecycle |
| trabalho | standard, workflow de provisionamento, migração, JML, enriquecimento de telemetria |
| evidência | export de registry e IAM mostrando cobertura; teste de revogação |
| critério de saída | zero credencial compartilhada em T2/T3 sem exceção; 100% com owner válido |

### Dependências entre workstreams

Workstreams distribuem execução, mas **não podem otimizar localmente**. Identidade pode declarar "entregue" enquanto o registry ainda não associa identidade a `agent_id`: tecnicamente há entrega, operacionalmente a capacidade continua incompleta.

Behavioral analytics depende de registry (identificar o ativo), identidade (atribuir a ação), telemetria (coletar as features) e runtime (responder ao desvio). Faltando qualquer uma, o backlog prioriza fundação — e essa relação precisa aparecer no plano integrado, não em listas separadas de cada time.

**Milestones se definem por outcome cross-domain**, não por entrega de trilha.

### Cadência

| Frequência | Fórum | O que decide |
|---|---|---|
| semanal | workstream | entregas, dependências e bloqueios |
| quinzenal | revisão integrada de arquitetura e governança | outcomes cross-domain |
| mensal | sponsor e council | risco, prioridade, funding e exceções |
| trimestral | revisão de maturidade | alvo e ajuste do roadmap |

## Depois do horizonte de referência — ciclo de melhoria contínua

O framework não pode ficar estático enquanto agentes, modelos e protocolos evoluem. Mudança de policy precisa ser **impulsionada por evidência**: incidentes, exceções, falsos positivos, novos padrões de ataque, anomalias de custo, lacunas de maturidade, feedback de builders e mudança regulatória.

Ciclo trimestral:

1. Revisar KPIs, KRIs e tendências do estate.
2. Analisar principais incidentes, quase-incidentes e eventos de quarentena.
3. Revisar exceções e verificar se viraram padrão legítimo ou dívida de governança.
4. Avaliar falsos positivos e negativos das regras de comportamento e dos policy gates.
5. Revisar gargalos manuais e oportunidades de automação.
6. Atualizar standards com changelog e data de vigência.
7. Priorizar as próximas capacidades no roadmap de maturidade.

O item 3 é o mais revelador: uma exceção que se repete não é exceção — é requisito que a policy ainda não reconheceu, ou controle que a operação não consegue cumprir. Os dois casos exigem mudança, não renovação.

### Sinais de maturidade adaptativa

- mudanças de policy são baseadas em dados de runtime e resultados de risco;
- novos agentes são descobertos e registrados automaticamente;
- mudança material dispara reavaliação proporcional;
- sinais de comportamento reduzem capacidade ou exigem step-up automaticamente, com override governado;
- custo e valor orientam retirada e arquitetura;
- **evidência é produzida continuamente, não preparada para a auditoria.**

## Como usar sem virar teatro de programa

- fases podem se sobrepor; gates não;
- prazo cumprido com evidência ausente é `hold`, não `approve`;
- escopo reduzido é decisão legítima e registrada, não fracasso silencioso;
- as 24 semanas dimensionam esforço, não prometem maturidade — maturidade se demonstra por evidência de operação, conforme o [maturity model](maturity-model.md).
- encurtar, estender ou substituir fases é legítimo quando rationale, dependências e evidências permanecem explícitos.

## O que este programa não faz

- não substitui análise jurídica ou regulatória;
- não define threshold universal;
- não seleciona produto;
- não impõe calendário, piloto ou ordem universal;
- não comprova maturidade por documentação;
- não certifica conformidade;
- não promete resultado financeiro.
