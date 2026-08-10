---
title: ADR-0004 — Taxonomia de tiers T1–T4 e fast path de baixo risco
status: superseded
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
superseded_by: 0009-risk-tier-and-admissibility.md
related:
  - 0003-single-canonical-source-and-guide-absorption.md
  - ../../risk-management/README.md
  - ../../../controls/README.md
  - ../../../schemas/README.md
---

# ADR-0004 — Taxonomia de tiers T1–T4 e fast path de baixo risco

> **Superseded:** a [ADR-0009](0009-risk-tier-and-admissibility.md) preserva T1–T4 e o fast path, mas separa risk tier de admissibilidade e corrige o mapeamento de `Restricted`.

## Contexto

A absorção do guia externo ([ADR-0003](0003-single-canonical-source-and-guide-absorption.md)) trouxe um conflito direto de taxonomia.

O repositório usa **T1–T4**, com T1 como menor tier. A taxonomia está travada em três enums de schema — `control-catalog`, `agent-blueprint` e `agent-registry` — e declarada em `appliesToTiers` nos 38 controls do catálogo. Dezessete arquivos citam tiers.

O guia usa **T0–T4**, onde T0 é "self-service governado" com quatro controles sempre presentes: descoberta e registro, logging básico, fontes aprovadas e termos de uso. O guia também exige evidence pack para T0.

Ou seja: o T0 do guia **não é ausência de governança**. Ele corresponde aproximadamente ao T1 do repositório, subtraindo testes básicos e somando termos de uso. O guia divide em duas faixas aquilo que o repositório trata como uma.

O problema real que o T0 endereça é legítimo: em um estate com milhares de agentes de baixo risco, exigir a mesma rota de todos torna a governança o gargalo — e a organização passa a contorná-la.

## Forças e constraints

- adicionar um tier é breaking change em três schemas, nos 38 controls e nas tabelas de segregation, assurance tiering e maturity;
- a proporcionalidade precisa ser real: alto volume e baixo risco não podem seguir a mesma rota de um agente transacional;
- "T0" lido isoladamente sugere ausência de governança, contradizendo o princípio de que todo agente tem owner, registro e logging;
- o guia é explícito em que todos os tiers possuem controles — a intenção nunca foi criar uma classe isenta;
- estabilidade de taxonomia tem valor próprio: mudanças frequentes de tier comprometem métricas históricas e evidências.

## Opções consideradas

### Opção A — Adotar T0–T4 do guia

**Vantagens:** alinhamento literal com o guia e com o workbook de classificação derivado dele.

**Desvantagens:** breaking change em três schemas e no catálogo inteiro; risco de o rótulo ser lido como isenção; ganho conceitual pequeno frente ao custo de migração.

### Opção B — Manter T1–T4 sem rota diferenciada

**Vantagens:** custo zero e máxima estabilidade.

**Desvantagens:** não resolve o problema de volume. Mantém o incentivo a contornar a governança nos casos de baixo risco.

### Opção C — Manter T1–T4 e definir um fast path dentro de T1

**Vantagens:** preserva schemas, controls e histórico; entrega a proporcionalidade pretendida pelo guia; deixa explícito que a rota rápida é uma rota, não uma isenção.

**Desvantagens:** divergência nominal com o guia e com materiais derivados dele, que precisam ser mapeados.

## Decisão

Adotar a opção C.

1. **T1–T4 é a taxonomia canônica de risco.** T0 não é adotado como tier.
2. Define-se o **fast path de T1**: rota automatizada para agentes de baixo risco e alto volume, na qual os gates são policy-driven em vez de manuais.
3. O fast path **não dispensa** os controles mínimos. Permanecem obrigatórios: descoberta e registro com `agent_id` e owner, logging básico, uso restrito a fontes aprovadas, termos de uso aceitos e evidência recuperável proporcional.
4. O que o fast path elimina é **revisão humana caso a caso**, não registro, controle ou evidência.
5. Um agente sai do fast path automaticamente quando qualquer escalador, red flag ou impact trigger se aplica — a saída é automática, a entrada é que precisa ser conquistada.
6. Materiais externos que usem T0–T4 são mapeados na importação: T0 e T1 do guia convergem para T1; T2, T3 e T4 permanecem equivalentes.

## Consequências positivas

- schemas, control catalog e evidências históricas permanecem válidos;
- a proporcionalidade pretendida pelo guia é entregue sem inventar tier;
- fica explícito, no vocabulário, que nenhum agente opera sem governança;
- o mapeamento de materiais externos é determinístico e documentável.

## Consequências negativas

- divergência nominal com o guia e com qualquer ferramenta de classificação derivada dele;
- exige nota de mapeamento em todo material importado;
- organizações que já usam T0 internamente precisam de uma tabela de conversão.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| fast path ser interpretado como isenção | controles mínimos declarados no próprio nome da rota e no decision gate de T1 |
| agentes permanecerem no fast path após mudança material | saída automática por escalador, red flag ou impact trigger |
| divergência com materiais externos gerar classificação incorreta | tabela de conversão obrigatória em qualquer importação |
| pressão para reintroduzir T0 por conveniência de ferramenta | ferramenta se adapta à taxonomia canônica, não o contrário |

## Critérios de validação

- os enums `T1|T2|T3|T4` permanecem íntegros nos três schemas;
- nenhum documento canônico usa `T0` como tier de risco;
- o fast path de T1 tem controles mínimos declarados e testáveis;
- existe tabela de conversão para materiais que usem T0–T4;
- `validate-repository.py` verifica a integridade da taxonomia.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10, com base no custo de migração medido (três enums de schema, 38 controls e dezessete arquivos afetados) e na constatação de que o T0 do guia corresponde funcionalmente ao T1 canônico com rota automatizada.
