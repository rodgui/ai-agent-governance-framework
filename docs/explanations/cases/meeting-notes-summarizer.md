---
title: "Caso de referência — Meeting Notes Summarizer (T1, fast path)"
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - service-desk-knowledge-agent.md
  - ../../risk-management/README.md
  - ../../auditability/evidence-pack-by-tier.md
---

# Caso de referência — Meeting Notes Summarizer (T1, fast path)

> Caso fictício e sanitizado. Demonstra o percurso do framework; não representa deployment real e seus thresholds não são recomendação.

## O caso em uma frase

Um agente interno que resume notas de reunião já registradas — somente leitura, nenhuma ação sobre sistema, nenhum dado pessoal.

| | |
|---|---|
| `agentId` | `meeting-notes-summarizer` |
| criticidade | **T1** |
| admissibilidade | `permitted` |
| capacidades | `observe` |
| rota | **fast path** — policy gate automatizado, sem review manual caso a caso |

## Por que este caso existe

Um estate real tem centenas de casos assim. Se cada um exigir revisão humana, a governança vira gargalo e a organização passa a contorná-la — que é o failure mode que o [fast path](../../risk-management/README.md#fast-path-de-t1) existe para evitar.

O que este caso demonstra, e nenhum outro demonstra: **o fast path não dispensa evidência, ele a gera automaticamente.**

## O percurso, e por que ele é curto

Nem todo gate produz reunião. Em T1 a maioria é satisfeita por verificação automática, e o percurso curto é o ponto — não uma concessão.

| Gate | Como foi satisfeito |
|---|---|
| G0–G1 | mandato e baseline vêm do programa; o agente entra por descoberta no control plane |
| G2 | identidade `delegated-user`, um escopo, fonte e tool herdadas do catálogo corporativo |
| G3 | operating model existente; nenhuma decisão nova a delegar |
| G4 | pre-screen sem nenhum escalador; sem capacidade de escrita, sem dado pessoal, sem alcance externo |
| G5 | **policy gate automatizado** — `Example Automated Policy Gate` como authority, sem review manual |
| G6 | observabilidade com correlação; quarentena bloqueia sessões e não há estado a reverter |
| G7 | attestation válida por um ano, sunset previsto |

**Artefatos:** [registry](../../../examples/cases/meeting-notes-summarizer/registry.json) · [blueprint](../../../examples/cases/meeting-notes-summarizer/blueprint.json) · [manifesto de release](../../../examples/cases/meeting-notes-summarizer/release-manifest.json)

## O que o fast path não dispensa

Comparando o manifesto deste caso com o [Minimum Production Bar de T1](../../risk-management/minimum-production-bar.md):

| Exigência do MPB em T1 | Onde está neste caso |
|---|---|
| registro e descoberta | `discovery` com sinal de control plane e confiança declarada |
| ownership | business, technical e run owner nomeados |
| classificação de risco | `risk.tier` T1 com rationale de admissibilidade e `redFlags` vazio explícito |
| identidade em padrão aprovado | `delegated-user`, escopo único, segredo fora do prompt |
| dados em classes aprovadas | uma fonte, `internal`, vinculada ao catálogo corporativo |
| tools em catálogo | uma tool `observe`, `catalogEntryId` verificado no catálogo |
| logging padrão | correlação declarada, sem retenção do conteúdo da nota |
| rollback documentado | retorno à última versão aprovada do blueprint |
| attestation periódica | válida até 2027-06-20 |

Nove exigências, nove satisfeitas — **sem uma única reunião de aprovação**. É isso que "reduz trabalho humano, não evidência" significa na prática.

## O que tira um caso da rota rápida

A saída do fast path é automática, não discricionária. Os gatilhos estão declarados no próprio blueprint, em `materialChangeTriggers`:

- qualquer tool que altere estado;
- dado acima de `internal`;
- uso por população externa;
- mudança de modelo ou provedor.

A entrada é que precisa ser conquistada. Na dúvida, o caso não entra — porque o custo de um T2 tratado como T1 é maior que o custo de um T1 tratado como T2.

## Contraste com o caso T2

| | Meeting Notes (T1) | [Service Desk (T2)](service-desk-knowledge-agent.md) |
|---|---|---|
| capacidades | `observe` | `observe`, `create` |
| identidade | `delegated-user` | `hybrid`, com principal próprio |
| authority no G5 | policy gate automatizado | Example Design Authority |
| decisão | `approved` | `conditional`, com quatro condições e expiry |
| controls exigidos | 4 | 5 |
| evidência | gerada pela rota | evidence pack com evaluation report |

A diferença entre os dois não é qualidade de documentação: é **capacidade de ação**. O T2 pode criar rascunho e por isso ganha uma authority humana e condições verificáveis. O T1 não pode fazer nada além de ler, e por isso a rota automatizada é suficiente.

Se os dois exigissem o mesmo, o framework estaria errado — proporcionalidade é o que separa governança de burocracia.

## O que este caso não demonstra

Não demonstra eficácia — é fictício. Não exercita admissibilidade diferente de `permitted`, nem impacto sobre pessoas, nem oversight humano com autoridade real. Para isso, veja o caso T3 quando estiver disponível.
