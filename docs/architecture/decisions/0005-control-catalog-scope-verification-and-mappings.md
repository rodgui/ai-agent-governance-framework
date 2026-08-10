---
title: ADR-0005 — Control catalog 1.1: escopo, verificação, bloqueio e mappings
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - 0004-risk-tier-taxonomy-and-fast-path.md
  - ../../../controls/README.md
  - ../../../schemas/control-catalog.schema.json
  - ../../guides/framework-implementation-playbook.md
---

<!-- markdownlint-disable MD029 -->
<!-- A numeração 1–13 da decisão é deliberadamente contínua entre as subseções. -->

# ADR-0005 — Control catalog 1.1: escopo, verificação, bloqueio e mappings

## Contexto

Uma revisão crítica do catálogo em sua versão 1.0 encontrou seis problemas, todos verificáveis nos dados:

1. **Simetria artificial.** 38 controls distribuídos como 3 por domínio em 12 dos 13 domínios, e 2 em adoption. Risco real não é simétrico; a distribuição indicava origem editorial, não derivação de risco observado.
2. **`automation: "mixed"` em 38 de 38 registros.** Um campo com valor idêntico em todos os registros não carrega informação.
3. **Lacuna de tier em ferramentas.** `AGF-TOL-002` (gateway e validação de ação) e `AGF-TOL-003` (kill switch) aplicavam-se apenas a T3 e T4. T2 é o tier onde a escrita aparece — um agente transacional não exigia nem gateway nem circuit breaker. A lacuna contradizia o Minimum Production Bar, que exige rollback e kill switch testáveis em T2.
4. **Requisito de mudança material espalhado.** `AGF-REG-002`, `AGF-RSK-003` e `AGF-OPS-003` declaravam a mesma obrigação, com mais quatro controls mencionando-a de passagem. Requisito em três lugares diverge no primeiro dia em que alguém edita um deles.
5. **Duplicação de ownership.** `AGF-ORG-001` e `AGF-REG-001` exigiam ambos business owner e technical owner.
6. **Duas classes de control no mesmo contrato.** `AGF-ORG-001`, `AGF-ORG-002` e `AGF-ADP-002` são capacidades organizacionais, mas carregavam `appliesToTiers`, implicando avaliação por agente. "Este agente possui decision rights?" não é uma pergunta com resposta.

Além disso, o schema tinha `additionalProperties: false` sem campo para marcar controls bloqueantes — apesar de o gate G4 do playbook exigir que "controles bloqueantes possuam design, owner, teste e evidence requirement" — e `frameworkMappings` estava presente no contrato e vazio em 38 de 38 controls, enquanto o README afirmava alinhamento a NIST, ISO, OECD, EU AI Act, OWASP e MITRE.

## Forças e constraints

- IDs de control são identificadores estáveis: renomear ou mover quebra rastreabilidade de evidências já produzidas;
- adicionar campos obrigatórios é mudança de contrato e exige bump de schema e atualização dos exemplos;
- afirmar alinhamento a norma paga sem o texto da norma produziria referência inventada — pior que a lacuna declarada;
- os domínios `model-governance` e `lifecycle` passaram a existir na documentação sem qualquer control, o que os torna documentação, não governança.

## Decisão

Publicar o **control catalog 1.1** com as seguintes mudanças de contrato e conteúdo.

### Contrato

1. `scope` passa a ser obrigatório, com valores `organization` e `agent`. Controls organizacionais são evidenciados uma vez, no nível do programa; controls de agente são avaliados por agente ou release. Para um control organizacional, `appliesToTiers` indica quais tiers a capacidade precisa suportar.
2. `verification` passa a ser obrigatório: os **testes objetivos** que decidem se o control passa. `evidence` continua listando o artefato. Evidence é o artefato; verification é o teste.
3. `blocking` passa a ser obrigatório: declara se a reprovação impede release ou continuidade em produção. Isso torna o requisito do G4 satisfazível.
4. O enum de `domain` recebe `model` e `lifecycle`.
5. `schemaVersion` e `catalogVersion` passam a `1.1`.

### Conteúdo

6. `AGF-TOL-002` e `AGF-TOL-003` passam a aplicar-se a **T2, T3 e T4**, eliminando a contradição com o Minimum Production Bar.
7. `AGF-RSK-003` torna-se a **fonte única** do requisito de reavaliação por mudança material. `AGF-REG-002` e `AGF-OPS-003` passam a referenciá-lo em vez de reafirmá-lo.
8. `AGF-ORG-001` é reescrito como mandato e authority de governança, com escopo organizacional. O requisito de ownership por agente permanece apenas em `AGF-REG-001`.
9. Cinco controls novos: `AGF-MDL-001`, `AGF-MDL-002` e `AGF-MDL-003` para governança de modelos e provedores; `AGF-LFC-001` e `AGF-LFC-002` para state machine e para dormência e sucessão de ownership.
10. `automation` passa a ser diferenciado por control, com base em quanto da verificação pode ser produzida por máquina.
11. `frameworkMappings` é populado em todos os controls, **apenas com referências públicas e verificáveis**: NIST AI RMF por função, EU AI Act por artigo, OWASP para riscos agentic e MCP, MITRE ATLAS por tática. Cada mapping carrega nota de que representa alinhamento direcional, não conformidade.

### O que deliberadamente não foi feito

12. **ISO/IEC 42001, 23894 e 42005 não são mapeadas.** O texto é pago e um número de cláusula inventado seria pior que a ausência. Enquanto não houver acesso ao texto, o alinhamento a ISO é afirmação de leitura, não rastreabilidade — e deve ser comunicado assim.
13. Nenhum ID de control foi renomeado ou movido de domínio, mesmo onde a alocação é imperfeita. Estabilidade de identificador vale mais que arrumação temática.

## Consequências positivas

- o gate de release pode distinguir o que bloqueia do que apenas informa;
- a coleta de evidência pode ser automatizada de forma diferente para as duas classes de control;
- cada control passa a declarar como é testado, e não apenas qual papel produz;
- os dois domínios novos deixam de ser documentação sem controle;
- a afirmação de alinhamento externa passa a ser rastreável onde é verificável, e explicitamente declarada como pendente onde não é.

## Consequências negativas

- catálogos de terceiros validados contra o schema 1.0 precisam de migração;
- `verification` acrescenta trabalho de autoria a cada control novo — é o ponto, mas tem custo;
- a distribuição por domínio continua aproximadamente uniforme; o problema de origem editorial foi documentado, não resolvido.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| `verification` virar repetição do statement | o texto precisa descrever um teste executável, com resultado observável |
| `blocking` ser marcado por conveniência | invariante em CI: nenhum control de escopo organizacional pode ser bloqueante |
| mapping ser lido como conformidade | nota obrigatória em cada mapping e seção explícita no README |
| distribuição uniforme persistir | registrada como sinal a observar; revisão do catálogo deve olhar a forma, não só o conteúdo |

## Critérios de validação

- os três enums de tier permanecem `T1|T2|T3|T4` (ADR-0004);
- todo control declara `scope`, `verification` e `blocking`;
- nenhum control de escopo `organization` é bloqueante;
- os exemplos validam contra o schema 1.1;
- nenhum mapping cita norma cujo texto não foi consultado.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10, a partir de revisão crítica do catálogo 1.0 que mediu a distribuição por domínio, a uniformidade de `automation`, a lacuna de tier em ferramentas, a tripla declaração de mudança material e a ausência total de `frameworkMappings`.
