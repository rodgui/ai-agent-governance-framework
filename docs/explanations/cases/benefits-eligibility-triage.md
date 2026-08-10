---
title: "Caso de referência — Benefits Eligibility Triage (T3, impacto sobre pessoas)"
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - service-desk-knowledge-agent.md
  - ../../responsible-ai/README.md
  - ../../human-oversight/README.md
---

# Caso de referência — Benefits Eligibility Triage (T3, impacto sobre pessoas)

> Caso fictício e sanitizado. Demonstra o percurso do framework; não representa deployment real, não é aceite de risco e seus thresholds não são recomendação.

## O caso em uma frase

Um agente que reúne a regra vigente e prepara uma recomendação de elegibilidade de benefício **para que um analista decida** — nunca decidindo.

| | |
|---|---|
| `agentId` | `benefits-eligibility-triage` |
| criticidade | **T3** |
| admissibilidade | **`conditional`** |
| capacidades | `observe`, `create` |
| decisão de release | `conditional`, cinco condições, expiry em seis meses |

## Por que T3 não foi uma escolha

O pre-screen disparou o escalador **decisão sobre emprego, crédito, elegibilidade ou acesso a serviço** (pergunta 6). Pela [tabela de escaladores](../../risk-management/README.md#red-flags-e-escaladores), isso impõe criticidade mínima T3 e impact assessment formal obrigatório — **independentemente do score**, e mesmo que o caso seja tecnicamente simples.

E ele é tecnicamente simples: uma fonte, uma tool, um modelo. Se a classificação dependesse só de complexidade técnica, este agente seria T1. É exatamente por isso que o escalador existe.

## As duas dimensões, separadas

Este é o primeiro caso do conjunto em que criticidade e admissibilidade **divergem**, e a divergência é o ponto:

- **criticidade T3** responde *quão severo pode ser o impacto* — decisão que afeta acesso de uma pessoa a um benefício;
- **admissibilidade `conditional`** responde *se e sob quais condições pode operar* — pode, enquanto a decisão permanecer humana, a contestação existir e o desempenho por slice for reavaliado.

Perder qualquer condição não rebaixa o tier: **suspende o uso**. Um T3 não vira T2 porque as condições foram cumpridas; ele continua T3 e continua exigindo o rigor do tier.

## Percurso pelos gates

### G4 — Controls e assurance

O impact assessment formal não foi opcional. Além dos controls de registry, identidade, dados, evaluation e operações, entram [`AGF-RAI-001`](../../../controls/README.md) (impact assessment), `AGF-RAI-002` (accountability humana e contestação) e `AGF-TOL-002` (gateway e validação de ação).

O residual risk ficou em `moderate` **com a decisão humana como controle**, não apesar dela. Sem a revisão humana, o mesmo caso teria residual alto e provavelmente não passaria.

### G5 — Release, com dois aprovadores

O manifesto registra **duas** authorities, e a ordem importa: Responsible AI decidiu às 11h, a Design Authority às 14h. Em T3, RAI é authority de veto — a decisão de release não existe sem ela.

Cinco condições, cada uma com owner e método de verificação:

| Condição | Como é verificada |
|---|---|
| a decisão permanece humana | gateway exige token de aprovação humana antes de gravar; ausência bloqueia a escrita |
| canal de contestação disponível | amostragem trimestral com tempo de resposta medido |
| desempenho por slice reavaliado a cada versão | pipeline bloqueia promoção sem relatório por slice da versão candidata |
| atributo protegido e proxy fora do critério e do log | verificação automatizada na entrada e no log, com alerta |
| perda de qualquer condição suspende o uso | alerta aciona quarentena automática e notifica a authority |

A quinta condição é a que dá sentido às outras quatro. Condição sem consequência declarada é intenção — e a consequência aqui é automática, não discricionária.

**Artefatos:** [registry](../../../examples/cases/benefits-eligibility-triage/registry.json) · [blueprint](../../../examples/cases/benefits-eligibility-triage/blueprint.json) · [manifesto](../../../examples/cases/benefits-eligibility-triage/release-manifest.json)

### G6 — Operação

A telemetria correlaciona caso, versão do agente, **regra citada** e decisão humana. Atributo protegido não é logado — o que significa que a verificação de fairness precisa ser desenhada para funcionar sem ele, e não que a fairness deixou de ser medida.

Contenção tem dois níveis: o gateway nega a escrita da recomendação, e a triagem manual é o fallback declarado. Um agente T3 sem caminho de degradação não é contível — é apenas desligável.

### G7 — Valor e lifecycle

Attestation de seis meses, não de um ano como no caso T1. A frequência acompanha o tier, e os gatilhos de mudança material incluem dois que os outros casos não têm: **mudança na regra de elegibilidade** e **disparidade material entre slices**. O segundo é um gatilho de comportamento observado, não de configuração — o agente pode continuar idêntico e ainda assim precisar de reavaliação.

## Onde os três casos divergem

| | [T1 Meeting Notes](meeting-notes-summarizer.md) | [T2 Service Desk](service-desk-knowledge-agent.md) | T3 Eligibility |
|---|---|---|---|
| admissibilidade | `permitted` | `permitted` | **`conditional`** |
| authority no G5 | policy gate automatizado | Design Authority | Design Authority **+ veto de RAI** |
| aprovação de ação | não se aplica | automatizada | **humana, por transação** |
| controls declarados no blueprint | 4 | 6 | 9 |
| condições de release | nenhuma | 4 | 5, com suspensão automática |
| attestation | 12 meses | 6 meses | 6 meses |
| gatilho de reavaliação | mudança de configuração | mudança de configuração | configuração **e comportamento observado** |

Lido na horizontal, é a proporcionalidade funcionando: o rigor cresce com o impacto, não com a complexidade técnica. O T3 é o mais simples dos três tecnicamente e o mais controlado dos três em governança.

## O que a construção deste caso encontrou

O blueprint declarava um control `AGF-HUM-001` que **não existe** no catálogo — inventado por analogia com um nome de domínio. O validador não pegou, porque `governance.controlIds` nunca era conferido contra o catálogo: só `controlEvidence` do manifesto era.

Um ID inexistente atravessava o gate parecendo cobertura. O guardrail foi acrescentado junto com o caso, e o control correto é `AGF-RAI-002`.

Vale registrar como o defeito apareceu: não por revisão do texto, mas por tentar **construir** o caso. Documentação que ninguém executa não revela esse tipo de coisa.

## O que este caso não demonstra

Não demonstra eficácia — é fictício, e a evidência de fairness citada é ilustrativa. Não cobre admissibilidade `restricted` nem `prohibited`, nem T4. E nenhum de seus controles foi exercitado contra um estate real, que é o critério 10 do [checklist de autossuficiência](../../reference/self-sufficiency-checklist.md) e permanece aberto.
