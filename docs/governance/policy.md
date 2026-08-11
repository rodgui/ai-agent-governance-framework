---
title: AI Agent Governance Policy — fonte canônica modular
status: adopted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - operating-model.md
  - ../architecture/overview.md
  - ../risk-management/README.md
  - ../../controls/README.md
  - ../architecture/decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md
  - ../architecture/decisions/0009-risk-tier-and-admissibility.md
  - ../architecture/decisions/0010-structured-governance-contracts-2.0.md
---

# AI Agent Governance Policy — fonte canônica modular

## Propósito

Este repositório é a fonte modular a partir da qual a **policy final de governança de IA e agentes** será mantida, revisada e versionada. A policy não é um documento monolítico nem depende de uma plataforma específica: ela é composta por princípios, decision rights, requisitos, controls, evidências e regras de lifecycle distribuídos em módulos canônicos.

## Adoção por uma organização

Adotar este framework é decisão de cada organização, pela sua própria authority competente, com escopo, exceções e obrigações próprias. Enquanto essa decisão não existir, o conteúdo é referência técnica — não a policy vigente daquela organização. Nenhum claim de certificação, auditoria independente ou conformidade decorre de usar este material.

## Se a organização já tem uma policy corporativa de IA

Esse é o caso mais comum numa organização grande.

Uma policy corporativa de IA governa **todos os AI systems e AI tools**, costuma pertencer a compliance ou a um conselho de IA, e é aprovada por instância executiva. Este framework governa **agentes**, que são um subconjunto — e o faz no nível de método, controls e evidência.

São camadas distintas, e **esta é a de baixo**:

| Camada | O que decide | Quem responde |
|---|---|---|
| policy corporativa de IA | princípios, obrigações mínimas, usos proibidos e conformidade regulatória, para toda a IA | compliance, jurídico, conselho de IA |
| **este framework** | como governar agentes em conformidade com aquela policy: tiers, gates, controls, evidência e runtime | governança de IA, arquitetura, plataforma |

Quando existe policy corporativa, **ela prevalece**. Este framework não a substitui, não a reinterpreta e não cria exceção a ela. O que ele faz é tornar executável, para agentes, aquilo que a policy exige em termos gerais.

Na prática:

1. **Mapeie as obrigações da policy corporativa** para os domínios canônicos daqui, e registre onde cada exigência é satisfeita. Obrigação sem control correspondente é gap; control sem obrigação correspondente é escolha do programa e precisa de rationale próprio.
2. **Onde a policy corporativa for mais restritiva, ela vence.** Onde for silenciosa, este framework preenche.
3. **Não duplique o que ela já cobre.** Conformidade regulatória por jurisdição, propriedade intelectual do output, classificação de dado pessoal e sanções por descumprimento normalmente já estão lá — e o framework as consome em vez de reescrevê-las.
4. **Declare a subordinação no charter do programa.** Sem isso, o framework parece competir com um instrumento já aprovado, e a rejeição vem por jurisdição, não por mérito técnico.

Apresentar este material a uma organização que já tem policy corporativa como se fosse "a policy" é o erro mais caro de posicionamento possível — e o mais fácil de evitar.

## Composição da policy

A policy canônica deste framework é formada por:

1. [princípios arquiteturais](../architecture/principles.md);
2. [operating model e decision rights](operating-model.md);
3. [arquitetura em cinco planos](../architecture/overview.md);
4. [gestão proporcional de riscos](../risk-management/README.md);
5. domínios canônicos de identidade, dados, tools, segurança, Responsible AI, oversight, evaluations, auditabilidade, operações, adoção e valor;
6. [control catalog](../../controls/README.md);
7. [implementation playbook e decision gates](../guides/framework-implementation-playbook.md);
8. schemas e evidence packages que tornam os requisitos verificáveis.

O [handbook](../handbook/README.md) define a ordem editorial desses módulos, sem duplicá-los.

## Conteúdo não normativo

Não integram a policy, salvo incorporação explícita e versionada:

- estudos de caso e explicações em `docs/explanations/`;
- crosswalks e avaliações comparativas em `assessments/`;
- fontes e referências externas em `references/`;
- exemplos fictícios em `examples/`;
- roadmap, specs e experimentos;
- calendários de 90 dias/24 semanas e o plano opcional de piloto;
- mappings de fornecedores.

Esses artefatos podem informar decisões, mas não criam dependência tecnológica nem requisito normativo por associação.

## Neutralidade de fornecedor

A policy define **capabilities, outcomes, controls, evidências e boundaries**, não produtos obrigatórios. Fornecedores e plataformas nomeados podem aparecer como fonte, caso observado ou mapping opcional. Nenhum deles é componente necessário do framework ou condição para conformidade com a policy.

Um mapping deve poder ser removido sem alterar princípios, controls, decision gates, schemas ou a arquitetura canônica.

## Evolução e versionamento

Mudanças normativas devem:

1. declarar o requisito alterado e sua justificativa;
2. registrar decisão e authority;
3. atualizar controls, evidências e impactos operacionais;
4. preservar versões anteriores;
5. incluir changelog e migration guidance quando necessário;
6. passar pelos quality gates do repositório antes de release.

## Origem histórica

A [AI Agent Policy and Governance v1](ai-agent-policy-and-governance-v1.md) foi o ponto inicial deste trabalho. Ela é preservada byte a byte para rastreabilidade histórica, mas não é usada como fonte normativa recorrente do framework modular.

O guia externo "Governança de Agentes de IA em Escala", mantido anteriormente como documento independente, também é **origem histórica**. Seu conteúdo procedural foi absorvido por este repositório conforme a [ADR-0003](../architecture/decisions/0003-single-canonical-source-and-guide-absorption.md), reescrito no formato canônico. Cópias daquele documento não são normativas e podem conter taxonomia divergente: a conversão para T1–T4 e a separação de `Restricted` como admissibilidade seguem a [ADR-0009](../architecture/decisions/0009-risk-tier-and-admissibility.md).

Este repositório é a **fonte única e final**. Qualquer publicação em outro formato deve ser derivada destes módulos, nunca mantida como cópia editorial independente.
