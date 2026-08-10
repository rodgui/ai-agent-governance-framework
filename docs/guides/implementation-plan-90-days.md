---
title: Roadmap de implantação — 90 dias
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - framework-implementation-playbook.md
  - maturity-model.md
  - ../governance/operating-model.md
  - ../../schemas/README.md
---

# Roadmap de implantação — 90 dias

> **Referência acelerada, não SLA.** Os 90 dias ajudam equipes que precisam de uma sequência inicial. Adapte duração e sobreposição às dependências, ao estate e à capacidade da organização. O calendário nunca substitui G0–G7 nem cria obrigação de piloto.

## Objetivo

Estabelecer, em 90 dias, as fundações e os fluxos mínimos de um sistema de governança operável: mandato, baseline, registry, blueprint, tiers, decision rights, controls, release evidence, runtime response e roadmap priorizado.

O resultado não é “governança concluída”. É uma capacidade inicial verificável que pode ser ampliada sem perder accountability ou rastreabilidade.

## Constraints

- A policy modular é a fonte canônica; adoção organizacional requer release e authority explícitas.
- Core e controls são multiplataforma.
- Thresholds são aprovados no contexto da organização.
- Dados, identidade, segurança, privacy, legal e RAI mantêm suas authorities.
- Automação é aplicada somente a regras estáveis e testadas.
- Lacuna de evidência permanece visível; não é preenchida por suposição.
- Este roadmap não exige piloto: uma coorte de onboarding ou rollout controlado delimita o primeiro escopo operacional e usa os mesmos gates, controls e critérios de produção.

## Mapeamento entre calendário e gates

Os períodos abaixo organizam trabalho; os gates continuam sendo decisões independentes. Chegar ao último dia de uma fase não autoriza avanço automático.

| Período | Gates preparados ou decididos | Decisão esperada |
|---|---|---|
| dias 0–10 | G0 | aprovar, condicionar, suspender ou rejeitar mandato e scope |
| dias 11–25 | G1 | aceitar baseline e limitações ou exigir evidência/remediação |
| dias 26–40 | G2 | aceitar fundações mínimas ou bloquear onboarding |
| dias 41–55 | G3 e preparação de G4 | aprovar decision rights e autorizar desenho da baseline de controls |
| dias 56–70 | G4 e preparação de G5 | aceitar baseline/assurance e decidir readiness para release |
| dias 71–85 | G5 e G6 | decidir release condicionado ao tier e aceitar operação/containment |
| dias 86–90 | G7 | decidir continuidade, restrição, expansão, remediação ou sunset |

O [contrato comum dos gates](framework-implementation-playbook.md#contrato-comum-dos-decision-gates) define evidence mínima, authority, estados e caminho de falha. Uma decisão `hold` ou `reject` altera o plano; o calendário deve ser replanejado, não usado para contornar o gate.

## Dias 0–10 — Mandato e escopo

### Atividades

- nomear sponsor, governance owner e authorities iniciais;
- aprovar escopo organizacional e ambientes;
- definir risk appetite, red flags e autoridade de containment;
- mapear policies, processos, inventários e ferramentas existentes;
- selecionar um portfólio inicial representativo para onboarding controlado;
- registrar decisões e dependências.

### Entregáveis

- governance charter;
- scope e stakeholder map;
- authority matrix inicial;
- risk appetite v0.1;
- decision/risk log.

### Exit criteria

- sponsor e owners nominativos;
- scope explícito;
- containment authority definida;
- nenhuma lacuna crítica sem owner.

## Dias 11–25 — Diagnóstico e baseline

### Atividades

- aplicar maturity assessment;
- reconciliar inventários de plataformas;
- mapear lifecycle e handoffs reais;
- identificar ownerless, duplicados, inativos e high-risk unknowns;
- avaliar qualidade da evidência;
- priorizar gaps por impacto, dependência e reversibilidade.

### Entregáveis

- maturity baseline;
- current-state map;
- preliminary registry;
- gap/risk register;
- prioritized backlog.

### Exit criteria

- situação atual separa observado de hipótese;
- inventário possui coverage declarado;
- gaps críticos e altos têm owner e prazo;

## Dias 26–40 — Registry, blueprint, dados e identidade

### Atividades

- aprovar schemas mínimos;
- definir source of truth e reconciliation;
- registrar business/technical owners e lifecycle;
- preencher blueprints do portfólio inicial;
- mapear workload identities e permissions;
- criar data contracts e connector gates;
- inventariar tools, APIs e MCP servers.

### Entregáveis

- registry e blueprints versionados;
- identity/permission matrix;
- data contracts;
- tool/MCP registry;
- material-change triggers.

### Exit criteria

- todos os itens do escopo inicial têm owner e status;
- identities, data e tools são rastreáveis;
- gaps aparecem como missing evidence.

## Dias 41–55 — Operating model e controls

### Atividades

- formalizar Council, Design Authority e Run Authority;
- definir RACI e decision rights por tier;
- aprovar risk tiers e red flags;
- mapear control catalog e evidence;
- definir exception/waiver e expiry;
- estabelecer forums, handoffs e SLAs.

### Entregáveis

- target operating model;
- RACI e decision matrix;
- risk/control baseline;
- exception process;
- forum charter.

### Exit criteria

- cada decisão material possui accountable;
- segregation of duties é proporcional;
- exceções não podem ser permanentes por padrão.

## Dias 56–70 — Assurance, evaluations e release

### Atividades

- definir triggers de assessments;
- criar evaluation strategy e thresholds;
- documentar human oversight e transparency;
- montar release evidence package;
- testar negative paths, rollback, quarantine e kill switch;
- registrar residual risk e conditions.

### Entregáveis

- assessment suite;
- evaluation/release criteria;
- evidence package;
- run readiness checklist;
- drill records.

### Exit criteria

- controls aplicáveis possuem evidence;
- release authority consegue aprovar, condicionar ou negar;
- containment e rollback foram exercitados.

## Dias 71–85 — Onboarding, operação e suporte

### Atividades

- colocar o workflow de onboarding em uso no escopo inicial;
- configurar telemetry, dashboards e alerts;
- publicar catalog entries, guidance e support paths;
- ligar incident, support e domain escalation;
- medir fricção, gaps e bypass attempts;
- corrigir controls e templates pelo processo versionado da policy modular.

### Entregáveis

- onboarding workflow operacional;
- observability e runbooks;
- catalog/discovery;
- support model;
- remediation backlog.

### Exit criteria

- cada signal possui owner e action;
- ações state-changing têm correlation;
- support e escalation funcionam ponta a ponta.

## Dias 86–90 — Attestation e roadmap

### Atividades

- executar primeira owner attestation do escopo;
- revisar criação, discovery, uso, qualidade e value hypothesis separadamente;
- registrar decisões de manter, corrigir, restringir ou aposentar;
- atualizar maturity baseline com evidência;
- aprovar roadmap de expansão e automation backlog.

### Entregáveis

- attestation records;
- portfolio/value review;
- maturity delta com limitações;
- roadmap 6–12 meses;
- executive decision memo.

### Exit criteria

- decisões ligadas a evidência;
- próximos increments possuem owner, dependency e acceptance criteria;
- nenhuma mudança normativa é autoaprovada.

## Métricas dos 90 dias

### Cobertura e controle

- coverage do registry;
- owners e attestations válidos;
- identities/connectors/tools classificados;
- evidence packages completos por tier;
- exceptions e findings vencidos;
- containment e rollback drill pass rate.

### Fluxo

- cycle time por gate e tier;
- devoluções por evidência incompleta;
- time to decide/contain/remediate;
- bypass attempts e causes;
- suporte e escalation resolution time.

### Uso, qualidade e valor

- discovery, adoption e use separados;
- task success e erro por scenario;
- safety/security signals;
- support burden;
- baseline e outcome evidence disponível;
- custo de operação e assurance.

## Riscos de execução

| Risco | Mitigação |
|---|---|
| burocracia uniforme | tiering, paved road e forms proporcionais |
| catálogo decorativo | reconciliation, owners, lifecycle e actions |
| falso senso de coverage | declarar sources, missing evidence e confidence |
| centralização em silo | authorities distribuídas e handoffs |
| automação prematura | manual first para regras instáveis; automate after evidence |
| métricas de vaidade | separar criação, uso, qualidade e outcome |
| vendor lock-in | capabilities e schemas neutros; adapters separados |
| rollout sem containment | quarantine/rollback como exit criteria |

## Próximo passo após 90 dias

Expandir coverage, automatizar controles estáveis, aprofundar domains com maior residual risk e revisar o roadmap. Uma futura Policy v2, se necessária, deve seguir processo formal de mudança e não é consequência automática deste roadmap.
