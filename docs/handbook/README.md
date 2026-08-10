---
title: Handbook de governança de IA e agentes
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../index.md
  - ../../README.md
---

<!-- markdownlint-disable MD029 -->
<!-- A numeração 1–32 é deliberadamente contínua entre as partes editoriais. -->

# Handbook de governança de IA e agentes

Esta é a ordem editorial da edição em português. Os capítulos permanecem em seus domínios canônicos. Uma publicação futura deve ser derivada desta ordem, sem criar uma segunda fonte editorial.

## Como ler

- **Leitura executiva:** capítulos 1, 2, 6 e 10.
- **Implantação:** capítulos 1–32 na ordem.
- **Arquitetura:** capítulos 3, 7, 11–17, 22 e 28–31.
- **Assurance:** capítulos 8, 9 e 18–21.
- **Referência:** consulte por domínio; não precisa seguir a ordem.

## Parte I — Fundamentos

1. [Governar agentes em escala — brief executivo](../executive/governing-agents-at-scale.md)
2. [Fundamentos de governança de IA e agentes](../fundamentals/README.md)
3. [Princípios arquiteturais](../architecture/principles.md)
4. [Vocabulário canônico](../../references/glossary.md)

## Parte II — Política, operating model e risco

5. [Policy modular — fonte canônica](../governance/policy.md)
6. [Operating model e decision rights](../governance/operating-model.md)
7. [Arquitetura de referência](../architecture/overview.md)
8. [Gestão proporcional de riscos](../risk-management/README.md)
9. [Maturity model](../guides/maturity-model.md)

## Parte III — Domínios de controle

10. [Estratégia, portfolio e evidência de valor](../value/README.md)
11. [Estate, registry, ownership e taxonomia](../registry/README.md)
12. [Lifecycle, mudança material, attestation e retirement](../lifecycle/README.md)
13. [Identidade e least privilege](../identity/README.md)
14. [Dados, acesso e provenance](../data-access/README.md)
15. [Tools, APIs e MCP](../tool-governance/README.md)
16. [Modelos, provedores e dependências de IA](../model-governance/README.md)
17. [Segurança de sistemas de IA e agentes](../security/README.md)
18. [Responsible AI e assurance](../responsible-ai/README.md)
19. [Human oversight e accountability](../human-oversight/README.md)
20. [Evaluations e release evidence](../evaluations/README.md)
21. [Auditabilidade e evidências](../auditability/README.md)
22. [Operações, resposta e runtime](../operations/README.md)
23. [Adoção, enablement e suporte](../adoption/README.md)

## Parte IV — Método, patterns e toolkit

24. [Implementation playbook](../guides/framework-implementation-playbook.md)
25. [Roadmap de 90 dias](../guides/implementation-plan-90-days.md)
26. [Programa de implantação em 24 semanas](../guides/implementation-program-24-weeks.md)
27. [Plano de piloto e critérios de expansão](../guides/pilot-plan.md)
28. [Catálogo de design patterns](../patterns/README.md)
29. [Control catalog](../../controls/README.md)
30. [Schemas e examples](../../schemas/README.md)
31. [Templates](../../templates/README.md)

## Parte V — Fontes e limitações

32. [Fontes e bibliografia](../../references/sources.md)

## Casos e mappings opcionais

- [Microsoft Customer Zero — caso de estudo](../explanations/microsoft-agent-governance-case-study.md)
- [Crosswalk histórico Microsoft × Policy v1](../../assessments/comparison-matrices/microsoft-case-study-framework-crosswalk.md)

Casos e mappings ajudam a interpretar implementações, mas não são capítulos necessários, componentes da solução ou requisitos do framework. A camada comercial também permanece fora do handbook, em [`consulting/`](../../consulting/README.md).

## Artefatos de manutenção do repositório

O [roadmap do produto de conhecimento](../../ROADMAP.md) orienta evolução e release do repositório, mas não é capítulo do handbook nem conteúdo previsto para publicação editorial.

## Critérios de completude de um capítulo

Um capítulo canônico deve declarar, quando aplicável:

- objetivo e boundaries;
- decisões e requisitos;
- artefatos e owners;
- controls e evidências;
- métricas e failure modes;
- relações com outros domínios;
- fontes e limitações.

## Convenção de status

| Status | Significado |
|---|---|
| `adopted` | decisão normativa aprovada |
| `maintained` | guidance canônico mantido |
| `review` | proposta em revisão |
| `draft` | conteúdo incompleto |
| `deprecated` | preservado apenas para referência |

Uma publicação futura não mudará o status do conteúdo-fonte.
