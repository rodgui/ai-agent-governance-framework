---
title: Checklist de autossuficiência
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - artifact-catalog.md
  - ../handbook/README.md
  - ../../ROADMAP.md
---

# Checklist de autossuficiência

## Objetivo

Instrumento de autoteste, aplicado antes de considerar um programa implantado ou antes de usar este material como entrega.

A pergunta não é "o documento existe?". É **"uma equipe diferente consegue executar e provar a capacidade sem depender de quem escreveu?"**. Um corpus pode estar completo e ainda assim não passar nesse teste, porque completude é sobre cobertura e autossuficiência é sobre transferência.

## Critérios

| # | Critério | Como verificar |
|---|---|---|
| 1 | cada domínio tem objetivo, dependências, procedimento, artefatos, evidências e decision gate | abra um domínio ao acaso e tente executá-lo sem consultar outro |
| 2 | cada decisão crítica tem critério explícito e não depende de julgamento informal de uma pessoa | procure a decisão e pergunte quem decide na ausência do autor |
| 3 | entregáveis têm owner, conteúdo mínimo, exemplo e critério de aceitação | confira contra o [catálogo de artefatos](artifact-catalog.md) |
| 4 | exemplos necessários estão junto do método; o toolkit é reutilização, não pré-requisito de compreensão | leia um capítulo sem abrir os templates e veja se ele se sustenta |
| 5 | controles críticos têm evidência, source of truth e mecanismo de revisão | tome três controls bloqueantes e siga a cadeia até a evidência |
| 6 | casos de referência percorrem risco, identidade, tools, lifecycle, observabilidade e assurance de forma coerente | siga um mesmo caso do intake à retirada |
| 7 | roadmap, planos curtos, piloto e backlog são visões do mesmo programa | procure dois cronogramas que se contradigam |
| 8 | a arquitetura é agnóstica de produto e o mapeamento para tecnologia está separado | veja se trocar de produto exigiria reescrever a arquitetura |
| 9 | o operating model funciona em todos os tiers e não cria fila central para baixo risco | conte quantas aprovações humanas um caso T1 exige |
| 10 | a organização consegue detectar, conter, investigar e retirar um agente em produção | exercite, não leia |
| 11 | valor e custo são medidos por outcome, não por uso ou número de agentes | procure adoção sendo apresentada como resultado |

O critério 10 é o único que não pode ser verificado por leitura. Se ele nunca foi exercitado, o programa não passou — independentemente da qualidade da documentação.

## Como este repositório se avalia

Aplicar o checklist a si mesmo é parte de usá-lo honestamente. O resultado abaixo é de 2026-08-10 e reflete o corpus, não uma implantação.

| # | Situação | Observação |
|---|---|---|
| 1 | atende | os domínios canônicos declaram objetivo, artefatos, evidências, métricas, failure modes e decision gate |
| 2 | atende para quem adota, **não atende para si** | os critérios estão escritos, mas o corpus tem um único owner e aprovador; nenhuma decisão passou por challenge independente |
| 3 | atende | o [catálogo de artefatos](artifact-catalog.md) fecha a lacuna de owner e fase que existia até a auditoria de agosto |
| 4 | atende | exemplos preenchidos em `examples/`, templates limpos em `templates/` |
| 5 | atende | control catalog com `verification`, `blocking` e `scope`; verificação mecânica no CI |
| 6 | atende | três [casos de referência](../explanations/cases/README.md) — T1, T2 e T3 — percorrem G0–G7 com registry, blueprint e manifesto validados pelo CI. A construção deles encontrou quatro defeitos que a leitura por domínio não encontrava |
| 7 | atende, com divergência declarada | o repositório trata roadmaps como patterns adaptáveis e mantém G0–G7 como únicos gates canônicos, em vez de um cronograma oficial único |
| 8 | atende | arquitetura agnóstica por [ADR-0002](../architecture/decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md); [mapeamento para tecnologia](../architecture/capability-to-technology.md) em documento separado |
| 9 | atende | o [fast path de T1](../risk-management/README.md#fast-path-de-t1) existe exatamente para não criar fila central em baixo risco |
| 10 | **não verificado** | o mecanismo está desenhado e documentado; nenhum control foi exercitado contra um estate real |
| 11 | atende | [unit economics](../operations/finops.md) e value review; o corpus afirma explicitamente que adoção não é proxy de resultado |

Um critério aberto e um parcial. O 10 pede execução contra um estate real e o 2 pede um segundo par de olhos com autoridade — nenhum dos dois se resolve escrevendo documentação.

O critério 6 fechou construindo os casos, não descrevendo-os. Foi a construção que expôs os defeitos: um release registrado como `condition` em prosa e `approved` em JSON, um contrato que confundia condição com exceção, e um control inexistente atravessando o gate como se fosse cobertura.

Declarar isso é mais útil do que um checklist todo verde. Um asset que se autoavalia sem falhar em nada não foi aplicado com seriedade.
