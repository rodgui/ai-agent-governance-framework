---
title: "Crosswalk de conteúdo: Guia de Governança de Agentes de IA v3.4 × framework canônico"
status: maintained
maturity: observed
last_reviewed: 2026-08-10
review_cycle: major-change
owners: [rodgui]
tags: [assessment, crosswalk, content, source-integration]
related:
  - ../../docs/governance/policy.md
  - ../../docs/fundamentals/README.md
  - ../../docs/governance/operating-model.md
  - ../../docs/risk-management/README.md
  - ../../docs/responsible-ai/README.md
---

# Crosswalk de conteúdo: Guia v3.4 × framework canônico

## Objetivo

Comparar o conteúdo de `Guia_Governanca_Agentes_IA_Escala_v3.4.docx` com o repositório canônico e registrar o que já estava coberto, o que foi útil para complementar e o que permanece apenas como referência histórica ou contextual.

## Escopo efetivamente lido

O DOCX foi extraído integralmente: 1.760 parágrafos, 101 tabelas, 31 capítulos e anexos A–F. Foram inspecionados títulos, corpo, tabelas, propriedades e ausência de revisions pendentes.

A análise é de **conteúdo**. Não avalia layout visual, eficácia operacional, adoção organizacional nem validade independente dos claims e fontes citados pelo guia.

O repositório não estabelece autoria, origem organizacional, data de aprovação ou authority formal do DOCX. A identificação disponível para este crosswalk é o nome do arquivo e sua versão declarada. Nenhum claim de aprovação, compliance ou adoção é inferido.

## Autoridade relativa

O guia v3.4 é uma fonte de guidance e procedimentos. Ele não substitui:

1. `docs/governance/policy.md` como entrada normativa corrente;
2. a taxonomia T1–T4;
3. o maturity model canônico 0–4;
4. os oito decision gates;
5. ADRs e boundaries comerciais vigentes.

Quando há conflito, o repositório prevalece e a divergência é registrada sem reconciliação silenciosa.

## Conclusão executiva

O guia e o repositório são fortemente convergentes em arquitetura, lifecycle, data, identity, tools, security, operations, evidence, Responsible AI e FinOps. A maior parte do guia já foi absorvida pelo framework em forma mais modular, vendor-neutral e verificável.

As lacunas reais estavam na **operacionalização humana** de quatro pontos:

1. decidir se o problema realmente exige um agente;
2. registrar risk/impact assessment com model/config version, uncertainty e impact triggers;
3. formalizar handoffs entre owners e gates;
4. formalizar mandato, authority e records dos fóruns.

Esses pontos foram incorporados como templates e complementos concisos nos capítulos existentes. Não foi criado um segundo handbook nem copiados capítulos inteiros.

## Matriz de cobertura

| Conteúdo do guia | Localizador no guia v3.4 | Estado anterior no repositório | Decisão |
|---|---|---|---|
| princípios, definições e agent boundary | §§1–2 | coberto em `docs/fundamentals/` e policy | manter corpus; adicionar decisão de adequação em G0 |
| comparação com workflow determinístico | §2.4 e fluxo inicial | implícita em value/fundamentals | **complementar** com intake estruturado |
| taxonomia multidimensional de agentes | §3 e Anexo B.16 | registry e blueprint já cobrem metadados principais | não criar taxonomia paralela; usar campos atuais nos templates |
| strategy, value, funding e unit economics | §4 | coberto em `docs/value/`, FinOps e maturity | sem duplicação |
| maturity M0–M5 | §5 e Anexo B.11 | maturity canônico é 0–4 | não incorporar escala concorrente |
| governance forums e RACI | §6 e Anexo A | decision rights, forums e cadência já existiam | **complementar** com forum charter |
| handoffs | §6.4 e Anexo B.7 | handoffs obrigatórios existiam, mas sem contrato preenchível | **complementar** com handoff matrix |
| discovery, inventory e lifecycle | §§7–9 | registry, discovery, gates, runtime e sunset cobertos | sem duplicação |
| AI-ready data, source catalog e remediation | §10 e anexos relacionados | coberto em `docs/data-access/`, controls e blueprint | sem duplicação |
| identity, JIT/JEA, secrets e access review | §11 | coberto em identity/access e controls | sem duplicação |
| tool/MCP governance | §12 | coberto em tool governance, patterns e controls | sem duplicação |
| risk classification, red flags e residual risk | §13 | conteúdo principal já existia; faltavam model/config binding e record operacional | **complementar** risk guidance e template |
| Impact Trigger Screen e RAI routing | §13.6 e Anexo C | impact assessment existia, triagem explícita não | **complementar** Responsible AI e risk template |
| security baseline e threat modeling | §§14–15 | coberto em security, patterns e controls | sem duplicação |
| human oversight e autonomy | §§16–17 | coberto em human oversight e policy | sem duplicação |
| observability, behavior, incidents e lifecycle operations | §§18–20 | coberto em observability, operations e incident patterns | sem duplicação |
| platform/control plane e provider/model governance | §§21–22 | coberto em architecture, platform, model/provider controls | sem duplicação |
| analytics, KPIs/KRIs e FinOps | §23 | coberto em value, observability, controls e maturity | sem duplicação |
| evidence quality e evidence packages | §§24–25 | coberto em auditability, schemas/templates e evidence package pattern | apenas referenciar nos novos templates |
| Responsible AI program e enablement | §26 | coberto em Responsible AI; trigger screen era lacuna | complementar somente a triagem |
| roadmap “oficial” de 24 semanas | §27 | roadmap canônico é adaptável e piloto não é obrigatório | não incorporar como norma |
| standards e external evidence | §28 | `references/` e método de evidência já separam fonte, claim e limite | sem duplicação |
| Minimum Production Bar | §29 | controls, G5, checklist e implementation playbook cobrem o outcome | melhorar checklist G5, sem criar gate paralelo |
| operating routines e assets | §30 e Anexo A | grande parte já tem equivalente em templates/patterns | incorporar apenas os quatro templates faltantes |
| síntese executiva | §31 | README e architecture overview já cumprem papel | sem duplicação |

## Conteúdo incorporado

### 1. Agent suitability em G0

Adicionado a `docs/fundamentals/README.md` e ao template `templates/agent-intake-and-suitability-template.md`:

- problema e baseline observáveis;
- comparação com alternativas não agente;
- intended/prohibited uses;
- affected parties e unknowns;
- decisão `proceed-agent`, determinística, híbrida, discovery ou reject;
- authority, rationale, evidence e próximo gate.

### 2. Risk e Impact Assessment operacional

Adicionado a `docs/risk-management/README.md`, `docs/responsible-ai/README.md` e `templates/risk-impact-assessment-template.md`:

- vínculo entre agent version e risk-model/config version;
- dimensões contextuais além de score isolado;
- uncertainty floor;
- red flags e floors;
- Impact Trigger Screen;
- residual-risk decision;
- material-change triggers;
- separação entre assessment e decisão G5.

### 3. Forum charter

Adicionado a `docs/governance/operating-model.md` e `templates/governance-forum-charter-template.md`:

- mandato e authority limits;
- quorum, conflicts e recusal;
- inputs, allowed decisions e records;
- conditions, expiry e escalation;
- métricas de fluxo e decisão.

### 4. Handoff matrix

Adicionado a `docs/governance/operating-model.md` e `templates/handoff-matrix-template.md`:

- sender/receiver;
- preconditions e evidence;
- acceptance criteria;
- return/rollback path;
- escalation;
- record owner e métricas.

### 5. Evidence readiness no G5

Atualizado `templates/publication-checklist.md` para distinguir:

- readiness do evidence package;
- decisão humana separada;
- outcomes `approve`, `condition`, `hold`, `reject`;
- impact trigger/assessment;
- residual risk, conditions e expiry;
- material-change triggers.

### 6. Controls existentes

Os controls `AGF-RSK-001` e `AGF-RSK-002` foram complementados com:

- risk-model/config version;
- uncertainty floor;
- calibração para automated routing;
- Impact Trigger Screen;
- referência ao assessment completo quando aplicável.

Não foi criado um novo domínio nem uma nova família de controls.

## Conteúdo deliberadamente não incorporado

| Conteúdo | Motivo |
|---|---|
| T0 | conflita com a taxonomia canônica T1–T4 |
| maturity M0–M5 | conflita com o maturity model canônico 0–4 |
| roadmap obrigatório de 24 semanas | deve permanecer adaptável ao contexto |
| piloto como etapa obrigatória | piloto é opção, não gate universal |
| `full assurance` como consequência automática de tier | assurance depende de arrangement e independência demonstrados |
| products/providers como arquitetura normativa | vendors permanecem exemplos, mappings ou fontes substituíveis |
| targets e SLAs sugeridos como policy | exigem calibração local e owner |
| capítulos integrais e tabelas duplicadas | aumentariam divergência e custo de manutenção |

## Itens úteis, mas já cobertos

Não foram copiados por já existirem materialmente no framework:

- certified sources e data remediation;
- workload identity e JIT/JEA;
- tool registry, scopes e kill switch;
- provider/model cards e exit strategy;
- behavior analytics e incident response;
- evidence packages e attestation;
- FinOps e unit economics;
- Responsible AI principles, contestability e human oversight;
- sunset e decommissioning.

## Resultado

A consolidação preserva o repositório como corpus canônico, modular e vendor-neutral. O guia v3.4 passa a funcionar como fonte de comparação e inspiração operacional, não como uma segunda policy. Foram absorvidos apenas os elementos que aumentam executabilidade sem reabrir decisões já estabilizadas.
