---
title: ADR-0002 — Policy modular, neutralidade estrita e boundary comercial
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: major-change
supersedes: 0001-canonical-modular-framework-and-vendor-mappings.md
related:
  - ../../governance/policy.md
  - ../../../consulting/README.md
  - ../../index.md
  - ../../handbook/README.md
---

# ADR-0002 — Policy modular, neutralidade estrita e boundary comercial

> **Nota de nomenclatura.** O documento que esta decisão criou chama-se hoje [policy de governança de agentes](../../governance/policy.md). "Modular" descreve como ela é composta — em módulos canônicos distribuídos pelo repositório — e permanece verdadeiro; deixou apenas de ser o nome pelo qual ela é referenciada. O texto desta ADR é preservado como foi decidido.

## Contexto

A primeira consolidação tratou a Policy v1 como baseline normativa, usou referências Microsoft para acelerar a arquitetura e colocou o modelo de consultoria dentro da área executiva. Essa estrutura foi útil para iniciar o framework, mas cria três ambiguidades: a policy histórica parece ser fonte permanente, referências de fornecedor podem parecer componentes da solução e a camada comercial pode ser confundida com conhecimento canônico.

O objetivo atualizado é que o corpus modular evolua para constituir a policy final, mantendo neutralidade real de fornecedor e separando a oferta pessoal de consultoria do framework público.

## Forças e constraints

- preservar a rastreabilidade da Policy v1 sem mantê-la como dependência normativa;
- evitar uma policy monolítica divergente dos módulos canônicos;
- permitir referências e mappings sem lock-in conceitual ou técnico;
- reutilizar o conhecimento em consultoria sem misturar conteúdo público, normativo e comercial;
- manter handbook e futuras publicações derivados da mesma fonte;
- adiar ebook até decisão posterior.

## Opções consideradas

### Opção A — Manter Policy v1 como baseline e consultoria em `docs/executive/`

**Vantagens:** menor mudança estrutural e narrativa normativa simples.

**Desvantagens:** perpetua lacunas da v1, multiplica citações históricas e mistura comunicação do framework com produto pessoal.

### Opção B — Criar uma nova policy monolítica e manter mappings no núcleo

**Vantagens:** documento único de aprovação e leitura direta.

**Desvantagens:** duplica controls, arquitetura e playbooks; mappings podem contaminar o desenho canônico; manutenção tende a divergir.

### Opção C — Policy modular canônica, vendors opcionais e consultoria separada

**Vantagens:** uma única fonte de verdade, portabilidade, evolução versionada e boundary comercial explícito.

**Desvantagens:** exige índices claros, disciplina de status e release, além de atualização de links e validações.

## Decisão

Adotar a opção C:

1. `docs/governance/policy.md` é a entrada normativa do framework modular e define a composição da policy candidate/final.
2. A Policy v1 é preservada byte a byte e indexada como origem histórica, sem ser citada repetidamente como fonte corrente.
3. O núcleo define capabilities, outcomes, controls, evidências e boundaries sem exigir Microsoft, Agent 365, Cloudflare ou qualquer fornecedor.
4. Conteúdo de fornecedor fica limitado a fontes, estudos de caso, assessments e mappings opcionais e removíveis.
5. `consulting/` é uma camada comercial pessoal separada da policy, do handbook e de `docs/executive/`.
6. A oferta comercial usa três pacotes compostos pelos nove módulos existentes.
7. Ebook/PDF permanece adiado; publicação futura será derivada dos módulos canônicos.

## Consequências positivas

- a policy final pode evoluir sem ficar limitada pela v1;
- vendors não se tornam dependências implícitas do framework;
- readers distinguem conhecimento, policy, evidência externa e produto comercial;
- o handbook continua uma ordem editorial pura;
- packaging e pricing podem evoluir sem alterar o conteúdo canônico.

## Consequências negativas

- a adoção normativa exige release e authority explícitas;
- links históricos e crosswalks precisam ser mantidos separadamente;
- a modularidade requer boa navegação e prevenção de inconsistências entre módulos;
- propostas comerciais precisam declarar exatamente quais módulos foram incluídos.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| modularidade diluir a força normativa | entrada única de policy, statuses e release versionada |
| vendor retornar ao núcleo por exemplos | quality gate e revisão de paths/linguagem |
| consultoria redefinir o framework | boundary explícito e links unidirecionais para o conteúdo canônico |
| v1 ser apagada ou reescrita | arquivo histórico protegido por hash |

## Critérios de validação

- a Policy v1 mantém o mesmo SHA-256 histórico;
- `docs/handbook/` e `docs/executive/` não contêm produto comercial;
- os nove módulos estão mapeados uma única vez para três pacotes;
- core docs não tratam produtos ou fornecedores como requisito da solução;
- a remoção de um mapping de fornecedor não quebra policy, controls, schemas ou gates;
- CI, links, schemas e lint permanecem verdes.

## Evidência da decisão

Decisão aprovada por Rodrigo Garcia Guimarães em 2026-08-09, junto com tese, cinco planos, oito gates, maturity model, modelo comercial, visual, público principal, packaging `3 pacotes / 9 ofertas` e autorização de merge após incorporação destas mudanças.
