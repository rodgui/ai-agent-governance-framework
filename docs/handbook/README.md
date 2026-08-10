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
<!-- A numeração 1–30 é deliberadamente contínua entre as partes editoriais. -->

# Handbook de governança de IA e agentes

Esta é a ordem editorial da edição em português. Os capítulos permanecem em seus domínios canônicos. Uma publicação futura deve ser derivada desta ordem, sem criar uma segunda fonte editorial.

## Como ler

- **Leitura executiva:** capítulos 1, 2, 6, 10 e 30.
- **Implantação:** capítulos 1–26 na ordem.
- **Arquitetura:** capítulos 3, 7–19 e 21–25.
- **Assurance:** capítulos 8, 9 e 14–19.
- **Consultoria:** capítulos 1–10, 21–26 e 30.
- **Referência:** consulte por domínio; não precisa seguir a ordem.

## Parte I — Fundamentos

1. [Governar agentes em escala — brief executivo](../executive/governing-agents-at-scale.md)
2. [Fundamentos de governança de IA e agentes](../fundamentals/README.md)
3. [Princípios arquiteturais](../architecture/principles.md)
4. [Vocabulário canônico](../../references/glossary.md)

## Parte II — Política, operating model e risco

5. [Policy v1 — baseline adotada](../governance/ai-agent-policy-and-governance-v1.md)
6. [Operating model e decision rights](../governance/operating-model.md)
7. [Arquitetura de referência](../architecture/overview.md)
8. [Gestão proporcional de riscos](../risk-management/README.md)
9. [Maturity model](../guides/maturity-model.md)

## Parte III — Domínios de controle

10. [Estratégia, portfolio e evidência de valor](../value/README.md)
11. [Identidade e least privilege](../identity/README.md)
12. [Dados, acesso e provenance](../data-access/README.md)
13. [Tools, APIs e MCP](../tool-governance/README.md)
14. [Segurança de sistemas de IA e agentes](../security/README.md)
15. [Responsible AI e assurance](../responsible-ai/README.md)
16. [Human oversight e accountability](../human-oversight/README.md)
17. [Evaluations e release evidence](../evaluations/README.md)
18. [Auditabilidade e evidências](../auditability/README.md)
19. [Operações, resposta e lifecycle](../operations/README.md)
20. [Adoção, enablement e suporte](../adoption/README.md)

## Parte IV — Método, patterns e toolkit

21. [Implementation playbook](../guides/framework-implementation-playbook.md)
22. [Roadmap de 90 dias](../guides/implementation-plan-90-days.md)
23. [Catálogo de design patterns](../patterns/README.md)
24. [Control catalog](../../controls/README.md)
25. [Schemas e examples](../../schemas/README.md)
26. [Templates](../../templates/README.md)

## Parte V — Evidência externa e application mappings

27. [Microsoft Customer Zero — caso de estudo](../explanations/microsoft-agent-governance-case-study.md)
28. [Crosswalk Microsoft × framework](../../assessments/comparison-matrices/microsoft-case-study-framework-crosswalk.md)
29. [Fontes e bibliografia](../../references/sources.md)

## Parte VI — Aplicação profissional

30. [Modelo de engagement de consultoria](../executive/consulting-engagement-model.md)

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
