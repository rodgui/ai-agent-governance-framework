---
title: Responsible AI e assurance
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - ../risk-management/README.md
  - ../human-oversight/README.md
  - ../evaluations/README.md
  - ../governance/operating-model.md
---

# Responsible AI e assurance

## Objetivo

Avaliar e controlar impactos em pessoas, grupos, direitos e sociedade ao longo do lifecycle, preservando accountability humana e independência suficiente entre build e assurance.

Responsible AI não é sinônimo de content filter. É a aplicação verificável de princípios, assessments, design choices, controles, avaliações, transparência e resposta.

## Assurance plane

O assurance plane reúne especialidades que testam se o sistema atende aos requisitos e ao contexto aprovado:

- Responsible AI;
- privacy e data protection;
- security e safety;
- legal e compliance;
- accessibility e inclusão;
- model/system evaluation;
- independent review quando exigido.

Ele complementa o control plane. Registry, postura técnica e telemetria não demonstram sozinhos tratamento adequado de impacto.

## Princípios de avaliação

- **validade e confiabilidade:** desempenho suficiente no contexto real;
- **safety:** danos previsíveis identificados e mitigados;
- **security e resilience:** resistência e recuperação;
- **accountability e transparência:** owners, decisões e comunicação;
- **explicabilidade proporcional:** informação útil para decisão e contestação;
- **privacy:** finalidade, minimização e direitos;
- **fairness:** impactos e desempenho entre grupos relevantes;
- **human agency:** supervisão, contestação e limites de automação.

Esses princípios orientam perguntas; não funcionam como checklist universal.

## Impact assessment

O assessment deve responder:

1. qual objetivo e qual alternativa não-IA foram considerados;
2. quem usa, quem é afetado e quem pode ser vulnerável;
3. quais decisões ou direitos podem ser influenciados;
4. quais dados, proxies e representações são usados;
5. quais harms, benefits e distributional effects são plausíveis;
6. onde automation bias, over-reliance ou contestability importam;
7. quais métricas e slices são materialmente relevantes;
8. quais human controls e redress mechanisms existem;
9. quais limitações precisam ser comunicadas;
10. qual residual impact permanece e quem pode aceitá-lo.

## Impact Trigger Screen

Run a short, recorded screen as part of risk classification. A positive answer does not itself prohibit the use case; it routes the case to a complete Impact Assessment and the relevant domain authorities.

Minimum trigger families:

- rights, opportunities, eligibility or decisions about people;
- access to services or material benefits;
- vulnerable groups or asymmetric ability to contest harm;
- physical safety, health or environmental impact;
- employment or workforce monitoring/management;
- public autonomous communication or impersonation risk;
- regulated or otherwise high-impact processes;
- profiling, monitoring or persistent personalization.

The screen records `yes/no`, rationale and evidence. `Unknown` is unresolved, not `no`. A positive trigger blocks completion of the risk record until `impactAssessmentRef` identifies a full assessment.

Use the [Risk and Impact Assessment Template](../../templates/risk-impact-assessment-template.md).

## Tiering de assurance

| Tier | Assurance mínima |
|---|---|
| baixo | intended use, limitations, basic quality e owner review |
| moderado | impact assessment, slices relevantes e user transparency |
| alto | domain review, adversarial/edge testing, human oversight e monitoring |
| crítico | challenge com segregation formal, contestability, continuous review e executive authority; usar `independent assurance` somente quando regras de independência, conflitos, amostragem, reporting e forma da conclusão estiverem aprovadas e demonstradas |

## Transparência

A comunicação adequada pode incluir:

- que IA está sendo usada;
- finalidade e limites;
- dados relevantes e fontes quando aplicável;
- grau de automação;
- necessidade de revisão humana;
- como reportar erro, contestar ou obter suporte;
- owner e canal de responsabilidade.

Transparência não exige expor secrets, dados pessoais ou detalhes que aumentem abuso. Precisa ser útil para a pessoa afetada.

## Fairness e performance

- selecionar grupos/slices com base em contexto e impacto, não apenas disponibilidade;
- comparar performance e harms com baseline adequado;
- registrar incerteza e tamanho de amostra;
- investigar proxies e feedback loops;
- definir threshold, owner e ação para disparidade;
- reavaliar após mudança material ou drift.

Uma métrica agregada pode esconder falha grave em um grupo relevante.

## Human agency e contestability

Quando o sistema influencia decisão material:

- a pessoa entende o papel da IA;
- um humano possui autoridade real, não ritual;
- há canal de contestação e correção;
- revisão humana recebe tempo, contexto e competência;
- o sistema registra override e outcome;
- automation bias é monitorado.

## Evidências

- intended use e prohibited use;
- impact assessment;
- affected-party map;
- dataset/model/system limitations;
- quality/fairness/safety evaluation;
- transparency artifacts;
- human oversight design;
- decisions, waivers e residual impact;
- runtime monitoring e incidents;
- attestation e improvement backlog.

## Métricas

- assessments aplicáveis concluídos antes do release;
- findings por princípio e tempo de remediação;
- performance por slices relevantes;
- harmful output e safety events;
- overrides e automation-bias indicators;
- complaints, contests e correction time;
- limitations comunicadas e compreendidas;
- drift em contexto, população ou impacto.

## Failure modes

- tratar Responsible AI como aprovação final;
- usar princípios sem controles ou evidências;
- medir fairness sem affected-party analysis;
- confundir explicação técnica com comunicação útil;
- usar humano como rubber stamp;
- não oferecer contestação;
- inferir ausência de impacto porque não houve reclamação;
- deixar o builder aceitar sozinho residual impact.

## Decision gate

Sistemas com impacto material em pessoas não passam pelo release gate sem impact assessment, oversight design, evaluation por slices relevantes, transparency plan e authority compatível com o tier.
