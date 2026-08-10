---
title: Implementation playbook do framework de governança
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../governance/operating-model.md
  - maturity-model.md
  - implementation-plan-90-days.md
  - ../patterns/README.md
---

# Implementation playbook do framework de governança

## Objetivo

Implantar um sistema de governança proporcional, federado e verificável. O playbook organiza outcomes, atividades, artefatos e decision gates; não prescreve produto, organograma ou prazo universal.

## Como usar

1. Defina o mandato e o escopo organizacional.
2. Faça baseline com evidência, sem preencher lacunas por suposição.
3. Selecione os controls mínimos por risco e capacidade.
4. Implemente governance como fluxo, não como documento isolado.
5. Teste handoffs, enforcement, contenção e evidência.
6. Meça operação e valor separadamente.
7. Revise decisões quando contexto, risco ou evidência mudarem.

## Workstreams

- estratégia, portfólio e valor;
- operating model e accountability;
- registry, blueprint e lifecycle;
- identidade e dados;
- tools, APIs e MCP;
- risco, Responsible AI e assurance;
- evaluations e release;
- adoção, suporte e change;
- runtime, auditabilidade e resposta.

## Contrato comum dos decision gates

Os gates são decisões registradas, não nomes de fase. Workstreams podem avançar em paralelo, mas nenhum gate é concluído apenas porque o prazo terminou ou um documento foi produzido.

### Estados de decisão

| Estado | Significado | Requisito de registro |
|---|---|---|
| `approve` | critérios de saída atendidos para o escopo e versão avaliados | authority, data, versão e evidências aceitas |
| `condition` | avanço permitido com gap não crítico e compensação temporária | condição, owner, prazo, compensating control e expiry |
| `hold` | decisão suspensa por evidência insuficiente ou remediação necessária | finding, owner, ação, evidência esperada e nova data |
| `reject` | risco, desenho ou escopo não é aceitável no appetite vigente | rationale, authority, opções de redesign ou encerramento |

Todo decision record deve identificar `gate_id`, escopo, versão, tier, authority, participantes, evidence refs, estado, rationale, condições, expiry e próxima revisão. `Missing evidence` nunca equivale a aprovação. A mesma pessoa não pode construir, aprovar e desafiar o próprio artefato quando segregation of duties for exigida pelo tier ou por obrigação aplicável.

### Contratos por gate

| Gate | Critérios de entrada | Evidência mínima | Authority da decisão | Critérios de saída | Falha e remediação |
|---|---|---|---|---|---|
| G0 — Mandato | sponsor candidato, problema e boundary inicial | draft de charter, scope, authorities e obligations map | sponsor executivo, com governance owner | mandato, scope, appetite, containment authority e regra de exceção aprovados | `hold` para esclarecer escopo/authority; não automatizar approvals |
| G1 — Baseline | G0 aprovado e acesso às fontes e stakeholders | inventários com coverage, current-state map, gaps, limitações e confidence | governance owner, com domain owners; sponsor aceita limitações materiais | baseline separa observado de hipótese e todo gap crítico tem owner | `hold`; unknowns de alto impacto são restringidos ou isolados até avaliação |
| G2 — Fundações | G1 aceito e população in-scope identificada | registry, blueprints, ownership, identity/data/tool records e testes de revogação | Design Authority e authorities de identity, data e tools | records mínimos validam, owners aceitam responsabilidade e acessos são revogáveis | bloquear onboarding, restringir connector/tool ou retornar para correção |
| G3 — Operating model | G0 vigente, handoffs atuais conhecidos e G2 suficiente para atribuir responsabilidade | operating model, RACI, decision matrix, exception flow, SLAs e charters | sponsor/Governance Council, com aceite das domain authorities | cada decisão material possui accountable, receiver, prazo e escalation | `hold`; decisões não delegadas retornam à authority existente |
| G4 — Controls e assurance | tiering proposto, G2/G3 aceitos e obligations map disponível | risk rationale, baseline por tier, assessments, evaluation plan, evidence index e residual-risk record | Design Authority e domain authorities; residual risk pela authority designada | controles bloqueantes possuem design, owner, teste e evidence requirement | `hold` ou `reject`; remediar, reduzir capability/escopo ou elevar authority |
| G5 — Onboarding/release | G4 aprovado para o escopo e versão, suporte e operação preparados | blueprint versionado, checks, evidence package, conditions, run readiness e release record | release/Design Authority definida no operating model | release `approve`/`condition` registrado e catalog entry publicável | não liberar; corrigir, reclassificar, restringir ou rejeitar |
| G6 — Operação | G5 válido e sistema instrumentado antes de exposição material | telemetry map, thresholds, runbooks, on-call, drills, rollback/quarantine e incident evidence | Run Authority, com domain escalation | sinais possuem owner/action e containment, recovery e reactivation foram exercitados | conter, fazer rollback ou suspender; reativação exige cause e regression evidence |
| G7 — Valor e lifecycle | janela de operação definida, G6 aceito e baseline de outcome/custo disponível | owner attestation, use/quality/risk/value evidence, incidents, costs e sunset options | Business Owner; Governance Council para decisão de portfólio/material risk | decisão de manter, expandir, corrigir, restringir ou aposentar registrada | restringir/sunset ou abrir remediation; mudança normativa segue processo separado |

## Gate 0 — Mandato, escopo e sponsorship

### Outcome

Existe autoridade para definir requisitos, exigir evidências e conter sistemas fora do envelope aprovado.

### Atividades

- nomear sponsor e governance owner;
- definir sistemas, unidades, regiões e ambientes cobertos;
- declarar risk appetite e red flags;
- mapear obrigações e authorities existentes;
- definir o que permanece fora de escopo e por quanto tempo;
- estabelecer princípios e regra de versionamento.

### Entregáveis

- governance charter;
- scope map;
- stakeholder/authority map;
- initial risk appetite;
- decision log;
- communication plan.

### Gate questions

- quem pode aprovar, condicionar, conter e aposentar?
- o escopo inclui SaaS, low-code, shadow AI e agentes adquiridos?
- exceções têm authority e expiry?

Sem mandato, não automatize approvals nem prometa cobertura.

## Gate 1 — Diagnóstico e baseline

### Outcome

A organização conhece sua situação atual, lacunas e limitações de evidência.

### Atividades

- aplicar maturity assessment;
- reconciliar inventários e sources;
- entrevistar owners e domain authorities;
- mapear lifecycle real, approvals e handoffs;
- revisar incidentes, findings, exceções e métricas;
- identificar duplicidade, ownerless assets e high-risk unknowns.

### Entregáveis

- maturity baseline;
- current-state map;
- preliminary inventory;
- gap/risk register;
- evidence quality statement;
- prioritized decisions.

### Gate questions

- quais conclusões são observadas e quais são hipóteses?
- quais lacunas críticas não possuem owner?
- onde a organização possui policy sem enforcement ou evidence?

## Gate 2 — Fundações de dados, identidade e ownership

### Outcome

Cada agente possui identidade, owner, finalidade, dados e capabilities rastreáveis.

### Atividades

- aprovar schemas de registry e blueprint;
- escolher source of truth e reconciliation strategy;
- registrar business/technical owner;
- definir workload identity e permission mapping;
- criar data contracts e connector gates;
- inventariar tools, APIs e MCP servers;
- definir material changes e lifecycle states.

### Entregáveis

- registry operacional;
- agent blueprints;
- identity records;
- data contracts;
- tool/MCP registry;
- ownership e attestation rules.

### Gate questions

- é possível responder o que existe e quem responde?
- blueprint explica arquitetura e blast radius?
- identidades, connectors e tools podem ser revogados?

## Gate 3 — Operating model e decision rights

### Outcome

Decisões têm authority, handoffs, SLA e evidência definidos.

### Atividades

- instituir Governance Council, Design Authority e Run Authority adequados ao contexto;
- definir domain authorities;
- criar RACI e decision matrix;
- separar build, approval, run e challenge conforme tier; usar `independent assurance` somente quando segregation e conflict rules estiverem formalizadas;
- desenhar exception e waiver process;
- definir forums e cadences.

### Entregáveis

- target operating model;
- RACI/decision rights;
- forum charter;
- handoff map;
- exception process;
- service levels.

### Gate questions

- accountability está atribuída a funções reais, não a “o time”?
- Run Authority pode conter sem depender de council?
- exceção sem expiry é bloqueada?

## Gate 4 — Controls mínimos e assurance

### Outcome

Risco é classificado e traduzido em controls, assessments, tests e residual-risk decisions.

### Atividades

- aprovar tiers e red flags;
- mapear control catalog à policy e aos domínios;
- definir triggers de impact, privacy, security e release assessments;
- criar evaluation strategy e evidence package;
- definir human oversight e transparency;
- testar negative paths, rollback e kill switch;
- estabelecer risk acceptance authority.

### Entregáveis

- risk matrix;
- control baseline por tier;
- assessment suite;
- evaluation/release criteria;
- human oversight design;
- evidence package index.

### Gate questions

- cada control tem owner e evidence?
- ausência de evidência aparece como missing, não como passed?
- approval é proporcional e possui caminho de remediation?

## Gate 5 — Onboarding por tier de risco

### Outcome

Existe um paved road para registrar, avaliar, liberar e suportar agentes em cada tier.

### Atividades

- integrar registry, blueprint, controls e release flow;
- criar starter templates e approved components;
- configurar automated checks onde policy está estável;
- publicar guidance, examples e support channels;
- validar experience de maker, reviewer, owner e operator;
- impedir bypass de paths críticos.

### Entregáveis

- onboarding workflow;
- release checklist;
- approved component catalog;
- builder guidance;
- support/escalation model;
- audit trail do gate.

### Gate questions

- o paved road é mais simples que contornar a governança?
- o workflow diferencia risco e capability?
- condições e findings chegam ao owner correto?

## Gate 6 — Operação, observabilidade e resposta

### Outcome

Sinais geram decisões e ações de contenção, remediação e recuperação.

### Atividades

- instrumentar agent, identity, data e tool chain;
- definir SLOs, thresholds e alerts;
- implementar quarantine, rollback e reactivation;
- executar incident e containment drills;
- ligar support, SOC/SRE e domain escalation;
- preservar evidence e update regression suite.

### Entregáveis

- observability model;
- dashboards com owner/threshold/action;
- incident severity e runbooks;
- quarantine/rollback evidence;
- runtime control mapping;
- post-incident loop.

### Gate questions

- o dashboard muda uma decisão?
- containment funciona sem cooperação do agente?
- reactivation exige cause e regression evidence?

## Gate 7 — Valor, attestation e melhoria contínua

### Outcome

O portfólio é revisado por ownership, risco, qualidade, uso, outcome e custo.

### Atividades

- separar criação, discovery, adoção, uso, qualidade e valor;
- revisar business case e baseline;
- executar attestation conforme tier;
- analisar concentração, duplicidade e agents inativos;
- decidir manter, expandir, corrigir, restringir ou aposentar;
- atualizar policy, controls e patterns somente por processo versionado.

### Entregáveis

- value review;
- attestation record;
- portfolio decisions;
- improvement backlog;
- sunset records;
- change proposal versionada.

### Gate questions

- há outcome observável ou apenas uso?
- custo inclui operação, suporte e assurance?
- policy changes estão separadas de guidance?

## Sequenciamento

Os gates possuem dependências lógicas, mas workstreams podem avançar em paralelo. Não espere perfeição para começar; também não use urgência para pular ownership, identidade, risco ou containment.

## Definition of done

A implantação está operacional quando:

- o inventário é reconciliável e possui owners;
- tier determina controls e authority;
- release evidence é recuperável;
- identities, data e tools são revogáveis;
- runtime signals acionam runbooks;
- quarantine, rollback e sunset foram exercitados;
- attestation e value review mudam o portfólio;
- exceptions vencem;
- policy e guidance são versionados separadamente.

## O que este playbook não faz

- não substitui análise jurídica ou regulatória;
- não define threshold universal;
- não seleciona produto;
- não comprova maturidade por documentação;
- não certifica conformidade;
- não promete resultado financeiro.
