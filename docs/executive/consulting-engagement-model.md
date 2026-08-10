---
title: Modelo de engagement de consultoria
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../guides/framework-implementation-playbook.md
  - ../guides/maturity-model.md
  - ../../controls/README.md
  - ../../templates/README.md
---

# Modelo de engagement de consultoria

## Proposta de valor

Ajudar organizações a transformar princípios e policies de IA em um operating model executável, com controls, evidências, decision rights, runtime response e roadmap proporcional ao risco.

A oferta não vende “um pacote de documentos”. O método produz decisões, artefatos verificáveis e transferência de capacidade para os owners do cliente.

## Guardrails comerciais

- não prometer conformidade, certificação ou ausência de incidentes;
- não afirmar ROI sem baseline e evidence;
- separar diagnóstico de implementação e challenge;
- não comercializar assurance ou attestation independente antes de definir e cumprir regras de conflitos, serviços incompatíveis, reporting line, amostragem e forma da conclusão;
- declarar assumptions, dependencies e exclusões;
- proteger confidencialidade e substituir secrets por `[REDACTED]`;
- adaptar a obrigações jurídicas e setoriais com especialistas do cliente;
- identificar mappings de fornecedor como implementação possível, não requisito universal.

## Oferta 1 — Governance Readiness Assessment

### Problema

A organização possui iniciativas, policies ou ferramentas, mas não conhece coverage, gaps, ownership ou capacidade operacional.

### Escopo

- strategy e portfolio;
- operating model;
- registry/lifecycle;
- identity, data e tools;
- risk/RAI/evaluations;
- runtime, auditability e adoption.

### Atividades

- document/system review;
- entrevistas e walkthroughs;
- maturity scoring com evidence;
- gap e dependency analysis;
- target-state workshop;
- roadmap priorization.

### Entregáveis

- maturity baseline com confidence/coverage;
- current-state architecture;
- gap/risk register;
- target maturity;
- roadmap 90 dias e 6–12 meses;
- executive decision memo.

### Critérios de aceite

- evidências e limitações rastreáveis;
- gaps críticos e altos têm owner, dependency e prazo;
- target aprovado pelos stakeholders;
- roadmap com outcomes e exit criteria.

### Duração indicativa

2–4 semanas, variando com escopo, disponibilidade de evidência e stakeholders.

### Exclusões

Certificação, auditoria estatutária, parecer jurídico e implementação de produto.

## Oferta 2 — Target Operating Model

### Problema

Decisões de IA estão fragmentadas, centralizadas em fila ou sem authority clara.

### Atividades

- definir governance charter e risk appetite;
- desenhar Council, Design Authority e Run Authority;
- mapear domain authorities e handoffs;
- criar RACI, decision rights, forums e SLAs;
- estruturar exception, containment e attestation.

### Entregáveis

- target operating model;
- authority/RACI matrix;
- lifecycle e gate map;
- forum charters;
- exception e escalation process;
- implementation backlog.

### Critérios de aceite

- decisões críticas possuem accountable;
- segregation é proporcional;
- containment authority e escalation são exercitáveis;
- handoffs têm evidence e receiver.

### Duração indicativa

3–6 semanas.

## Oferta 3 — Policy and Control Framework

### Problema

A policy é abstrata ou não mapeia controles, evidências e enforcement.

### Atividades

- revisar policy baseline e gaps;
- definir risk tiers e red flags;
- mapear requirements → controls → evidence;
- criar assessments e release gates;
- definir change/version process;
- integrar privacy, security, RAI e legal.

### Entregáveis

- policy/control crosswalk;
- control catalog;
- assessment suite;
- evidence package model;
- exception/waiver template;
- roadmap de implementação.

### Critérios de aceite

- cada requirement possui owner e evidence;
- missing/not-applicable/passed são distintos;
- residual risk authority é explícita;
- policy changes não são aplicadas silenciosamente.

### Duração indicativa

4–8 semanas.

## Oferta 4 — Agent Registry and Lifecycle Design

### Problema

A organização não consegue responder o que existe, quem responde e como mudar, conter ou aposentar.

### Atividades

- definir registry e blueprint schemas;
- mapear sources e reconciliation;
- desenhar lifecycle, attestation e sunset;
- integrar identity/data/tool records;
- definir discovery e orphan detection;
- selecionar implementation adapters.

### Entregáveis

- schemas e data model;
- source-of-truth decision;
- lifecycle state machine;
- attestation/sunset workflow;
- integration architecture;
- example records.

### Critérios de aceite

- campos obrigatórios validam;
- ownership e status são reconciliáveis;
- blueprint explica blast radius;
- revocation e sunset são testáveis.

### Duração indicativa

4–8 semanas; implementação de plataforma pode exigir fase adicional.

## Oferta 5 — Responsible AI Assurance Integration

### Problema

Responsible AI funciona separada de release, runtime e decision rights.

### Atividades

- mapear impact assessment e triggers;
- integrar privacy, safety, fairness e human oversight;
- definir evaluation e transparency evidence;
- criar review por tier;
- desenhar contestability e incident feedback.

### Entregáveis

- assurance operating model;
- impact assessment;
- human oversight patterns;
- evaluation/slice strategy;
- transparency e redress requirements;
- evidence package mapping.

### Critérios de aceite

- assurance complementa control plane;
- reviewers possuem authority e independence;
- impacts, limitations e residual risk são explícitos;
- runtime feedback reabre assessment quando necessário.

### Duração indicativa

4–8 semanas.

### Exclusões

Parecer jurídico, auditoria, certificação, independent assurance e implementação de produto não contratada separadamente.

## Oferta 6 — Runtime Governance and Observability

### Problema

Há dashboards, mas não há thresholds, owners, containment ou learning loop.

### Atividades

- definir observability model;
- mapear signals → decisions → actions;
- criar severity, runbooks e SLOs;
- desenhar quarantine, rollback e reactivation;
- executar drills;
- integrar incident evidence e regression.

### Entregáveis

- telemetry/control map;
- dashboard requirements;
- incident/runbook suite;
- quarantine architecture;
- drill report;
- improvement backlog.

### Critérios de aceite

- cada signal material possui owner/action;
- containment independe do agente;
- evidence é preservada;
- reactivation exige cause e regression proof.

### Duração indicativa

4–8 semanas para design e drills delimitados.

### Exclusões

Operação 24×7, resposta gerenciada a incidentes, implantação integral de observability platform e garantia de ausência de incidentes.

## Oferta 7 — MCP and Tool Governance

### Problema

Tools, APIs e MCP ampliam agência sem provenance, scopes ou enforcement adequados.

### Atividades

- inventariar capabilities;
- classificar read/write/action/delegate;
- threat model e provenance review;
- definir gateway, allowlist e policy;
- desenhar identity, data e egress controls;
- testar kill switch e chain behavior.

### Entregáveis

- tool/MCP registry;
- risk/control baseline;
- gateway reference architecture;
- approval workflow;
- test suite;
- operational runbooks.

### Critérios de aceite

- state-changing tools têm owner e enforcement;
- arguments/results são validados;
- scopes e egress são limitados;
- revocation e kill switch funcionam.

### Duração indicativa

3–6 semanas para assessment e design; implementação de gateway ou adapters exige escopo próprio.

### Exclusões

Penetration test, operação contínua, homologação universal de tools e implementação de produto não contratada separadamente.

## Oferta 8 — Governance Enablement and Adoption

### Problema

Governança é vista como burocracia, builders contornam o fluxo e usuários não conhecem limites ou suporte.

### Atividades

- segmentar personas;
- criar paved road e templates;
- desenhar catalog/discovery;
- estruturar support tiers e champions;
- criar learning assets e office hours;
- medir friction e feedback.

### Entregáveis

- enablement strategy;
- builder/user journeys;
- support model;
- catalog requirements;
- training assets;
- adoption/feedback metrics.

### Critérios de aceite

- caminho governado é utilizável;
- limitações e support são claros;
- feedback alimenta backlog;
- adoção é separada de qualidade e valor.

### Duração indicativa

4–10 semanas, conforme personas, canais e materiais existentes.

### Exclusões

Operação permanente do suporte, plataforma de treinamento, comunicação corporativa contínua e garantia de adoção ou produtividade.

## Oferta 9 — Limited-Scope Evidence Review

### Problema

Owners precisam de challenge documentado sobre claims, controls e evidências selecionados sem transformar a revisão em audit, certification, attestation ou assurance independente.

### Pré-condições

- objeto, período, population e sample delimitados;
- criteria e evidence cutoff aprovados;
- assessor, implementadores e reviewer identificados;
- conflitos e serviços anteriores declarados;
- owner do cliente mantém accountability e residual-risk decision.

### Atividades

- definir scope, criteria e sampling rationale;
- registrar e testar evidence refs selecionadas;
- executar walkthroughs e reperform testes acordados;
- registrar findings, severity e divergências;
- acompanhar evidência de remediação dentro do período contratado;
- emitir conclusão limitada ao escopo e à amostra.

### Entregáveis

- limited-scope review plan;
- evidence register e sampling statement;
- findings report;
- remediation tracker;
- limited-scope conclusion com limitações e conflitos declarados.

### Critérios de aceite

- scope, criteria, population, sample e evidence cutoff são explícitos;
- reviewer não revisa o próprio trabalho e conflitos estão registrados;
- findings são reproduzíveis a partir das referências autorizadas;
- conclusão não excede evidência nem usa o termo `independent assurance`;
- owner aceita, contesta ou trata residual gaps.

### Duração indicativa

2–4 semanas para um escopo e uma amostra delimitados; remediação e reteste podem exigir incremento adicional.

### Exclusões

Auditoria interna ou estatutária, certificação, parecer jurídico, attestation, opinião de compliance, assurance independente e continuous assurance.

A oferta só poderá evoluir para independent assurance após aprovação das regras previstas na trilha D4 do roadmap.

## Participantes do cliente

- sponsor e business owners;
- architecture/platform;
- security, identity e operations;
- data/privacy/legal/compliance;
- Responsible AI e risk;
- engineering/makers;
- internal audit/assurance;
- procurement/vendor management quando aplicável.

## Estrutura de proposta

Toda proposta deve declarar:

1. contexto e problema;
2. objectives e outcomes;
3. scope e exclusões;
4. assumptions e prerequisites;
5. approach e workstreams;
6. entregáveis;
7. roles e governance;
8. timeline indicativa;
9. acceptance criteria;
10. risks e dependencies;
11. metrics;
12. confidentiality, IP e licensing;
13. próximos passos.

## Métricas de sucesso do engagement

- decisões tomadas com authority;
- artifacts aceitos e em uso;
- coverage e confidence do baseline;
- controls com owner/evidence;
- handoffs e drills concluídos;
- gaps priorizados e remediados;
- capacidade transferida aos owners;
- roadmap financiável e executável.

A métrica não deve ser quantidade de workshops ou páginas entregues.
