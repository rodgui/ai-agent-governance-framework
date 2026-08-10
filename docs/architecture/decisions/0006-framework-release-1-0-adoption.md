---
title: ADR-0006 — Adoção da release 1.0 do framework
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - 0003-single-canonical-source-and-guide-absorption.md
  - 0005-control-catalog-scope-verification-and-mappings.md
  - ../../governance/policy.md
  - ../../handbook/README.md
---

# ADR-0006 — Adoção da release 1.0 do framework

## Contexto

O handbook define cinco estados de status, entre eles `adopted` — "decisão normativa aprovada". Até esta decisão, **nenhum documento do corpus usava esse estado**. A entrada normativa, `docs/governance/policy.md`, estava em `review`, enquanto trinta e seis módulos dependentes estavam em `maintained`.

Isso produzia uma inversão desconfortável: a raiz normativa era menos estável que os seus ramos, e o corpus ensinava um vocabulário de adoção que não exercitava em si mesmo. Para um framework que exige de terceiros "authority, versão e evidência", não demonstrar o próprio ato de adoção é uma lacuna de credibilidade, não de conteúdo.

Após a absorção do guia externo (ADR-0003) e a revisão do control catalog (ADR-0005), o corpus atingiu um ponto em que a estrutura está estável: quinze domínios canônicos, dez com playbook executável, quarenta e três controls com verificação declarada, quatro schemas e nove quality gates em CI.

## Dois níveis de adoção que não podem ser confundidos

Esta é a razão principal do ADR existir separadamente.

| Nível | Quem decide | O que significa | Estado após esta decisão |
|---|---|---|---|
| **Release do framework** | o mantenedor deste repositório | esta versão é a baseline canônica estável; mudanças normativas passam a exigir proposta, rationale, authority, changelog e release versionada | `adopted` |
| **Adoção organizacional** | a authority competente de cada organização | a organização declara esta baseline como sua policy interna, com escopo, exceções e obrigações próprias | permanece uma decisão de cada organização |

Adotar a release **não** significa que qualquer organização adotou a policy. Um cliente que use este material continua precisando da própria decisão formal, com a própria authority — exatamente o que o framework exige em `AGF-ORG-001`.

Confundir os dois níveis seria vender adoção como conformidade. É o erro que o corpus critica em outros contextos e não pode cometer em si mesmo.

## Decisão

1. Declarar a **release 1.0 do framework como `adopted`**, com data de 2026-08-10.
2. `docs/governance/policy.md` passa de `review` para `adopted`, mantendo explícito no texto que a adoção organizacional é uma decisão separada de cada organização.
3. A partir desta release, mudança normativa segue o processo já declarado na policy: declarar o requisito alterado e a justificativa, registrar decisão e authority, atualizar controls e evidências, preservar versões anteriores, incluir changelog e passar pelos quality gates.
4. O CHANGELOG passa a registrar versões nomeadas; `[Unreleased]` volta a existir vazio para acumular a próxima.
5. Nenhum claim de certificação, auditoria independente ou conformidade decorre desta adoção. A release é uma decisão de versionamento, não uma atestação.

## Consequências positivas

- o corpus exercita o próprio vocabulário de adoção, em vez de apenas prescrevê-lo;
- a raiz normativa deixa de ser menos estável que os módulos que a compõem;
- passa a existir um ponto de referência versionado para citar em proposta, aula ou avaliação;
- mudanças futuras têm um baseline contra o qual são diffs, e não edições soltas.

## Consequências negativas

- mudança normativa fica mais cara: exige rationale, authority e changelog;
- uma release adotada expõe erros de forma mais permanente — corrigir passa a ser uma nova versão, não uma edição silenciosa;
- há risco de leitura apressada tratando `adopted` como validação externa.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| adoção do framework ser lida como conformidade organizacional | tabela dos dois níveis neste ADR e texto explícito na policy |
| `adopted` sugerir auditoria ou certificação | declaração explícita de que a release não é atestação; regras de linguagem de assurance permanecem vigentes |
| congelar erros conhecidos | as lacunas em aberto ficam declaradas no CHANGELOG e no README, não escondidas pela versão |
| release virar cerimônia sem consequência | mudança normativa passa a exigir o processo da policy, verificado em revisão |

## Lacunas conhecidas nesta release

Declaradas deliberadamente, para que a versão não sugira completude que não tem:

- ISO/IEC 42001, 23894 e 42005 não estão mapeadas control a control (ADR-0005);
- a distribuição de controls por domínio permanece aproximadamente uniforme, refletindo origem editorial e não risco observado;
- o corpus tem um único owner, que também é a authority que aprova — situação que o próprio `AGF-ORG-002` trata como exceção a declarar;
- nenhum control foi exercitado contra um estate real; a calibração de thresholds permanece hipótese.

## Critérios de validação

- `docs/governance/policy.md` declara `adopted` e preserva a distinção entre os dois níveis;
- o CHANGELOG registra a versão com data e conteúdo;
- nenhuma afirmação de certificação, auditoria ou conformidade acompanha a release;
- as lacunas conhecidas permanecem visíveis no corpus.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10, após a absorção do guia externo e a revisão do control catalog, com o corpus em quinze domínios canônicos, quarenta e três controls verificáveis e quality gates verdes.
