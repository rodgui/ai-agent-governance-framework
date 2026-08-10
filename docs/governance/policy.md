---
title: AI Agent Governance Policy — fonte canônica modular
status: review
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - operating-model.md
  - ../architecture/overview.md
  - ../risk-management/README.md
  - ../../controls/README.md
  - ../architecture/decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md
---

# AI Agent Governance Policy — fonte canônica modular

## Propósito

Este repositório é a fonte modular a partir da qual a **policy final de governança de IA e agentes** será mantida, revisada e versionada. A policy não é um documento monolítico nem depende de uma plataforma específica: ela é composta por princípios, decision rights, requisitos, controls, evidências e regras de lifecycle distribuídos em módulos canônicos.

Uma organização só deve declarar uma release como `adopted` após aprovação pela authority competente. Até essa adoção, o conteúdo mantido neste repositório constitui a policy candidate e a referência técnica canônica do framework.

## Composição da policy

A policy candidate é formada por:

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
- mappings de fornecedores;
- a camada comercial em `consulting/`.

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

O guia externo "Governança de Agentes de IA em Escala", mantido anteriormente como documento independente, também é **origem histórica**. Seu conteúdo procedural foi absorvido por este repositório conforme a [ADR-0003](../architecture/decisions/0003-single-canonical-source-and-guide-absorption.md), reescrito no formato canônico. Cópias daquele documento não são normativas e podem conter taxonomia divergente: onde usarem uma faixa `T0`, aplica-se a conversão definida na [ADR-0004](../architecture/decisions/0004-risk-tier-taxonomy-and-fast-path.md).

Este repositório é a **fonte única e final**. Qualquer publicação em outro formato deve ser derivada destes módulos, nunca mantida como cópia editorial independente.
