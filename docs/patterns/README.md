---
title: Catálogo de design patterns de governança
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../architecture/overview.md
  - ../guides/framework-implementation-playbook.md
  - ../../controls/README.md
---

# Catálogo de design patterns de governança

Patterns descrevem soluções reutilizáveis para problemas recorrentes. Não são produtos, policy automática nem checklist universal. A seleção depende de risco, arquitetura, capacidade organizacional e obrigações.

## Catálogo

| Pattern | Problema principal | Lifecycle |
|---|---|---|
| [Registry and Blueprint](registry-and-blueprint.md) | inventário não explica arquitetura e blast radius | todos |
| [Risk-Tiered Governance](risk-tiered-governance.md) | processo uniforme ou risco inconsistente | map/release/run |
| [Federated Governance](federated-governance-operating-model.md) | silo central ou authorities fragmentadas | todos |
| [Control and Assurance Planes](control-and-assurance-planes.md) | visibilidade confundida com assurance | design/run |
| [Human Accountability Boundary](human-accountability-boundary.md) | humano nominal, sem authority real | design/action |
| [AI-Ready Data Gate](ai-ready-data-gate.md) | connector disponível tratado como dado adequado | build/change |
| [Tool and MCP Gateway](tool-and-mcp-gateway.md) | tools ampliam agência sem enforcement | build/run |
| [Runtime Observability and Quarantine](runtime-observability-and-quarantine.md) | dashboard sem resposta | run/incident |
| [Lifecycle Attestation and Sunset](lifecycle-attestation-and-sunset.md) | aprovação nunca expira | operate/retire |
| [Evidence Package as Code](evidence-package-as-code.md) | decisões sem rastreabilidade | build/release/run |

## Seleção rápida

| Sinal | Pattern recomendado |
|---|---|
| “Não sabemos quantos agentes existem” | Registry and Blueprint |
| “O approval é igual para tudo” | Risk-Tiered Governance |
| “Tudo vai para o comitê” | Federated Governance |
| “Temos dashboard, então estamos governados” | Control and Assurance Planes + Runtime Observability |
| “O usuário clicou OK” | Human Accountability Boundary |
| “Se está no SharePoint, pode usar” | AI-Ready Data Gate |
| “O MCP server descobre tools sozinho” | Tool and MCP Gateway |
| “Conseguimos detectar, mas não bloquear” | Runtime Observability and Quarantine |
| “Foi aprovado há dois anos” | Lifecycle Attestation and Sunset |
| “A aprovação está no e-mail” | Evidence Package as Code |

## Antipatterns

### Registry decorativo

Inventário sem reconciliation, owner, lifecycle ou ações. Corrija com [Registry and Blueprint](registry-and-blueprint.md).

### Dashboard sem remediação

Sinal sem threshold, owner ou runbook. Corrija com [Runtime Observability and Quarantine](runtime-observability-and-quarantine.md).

### Agent sprawl

Métrica de criação incentiva duplicidade e abandono. Combine registry, portfolio review e sunset.

### Shared identity

Múltiplos agentes atuam como uma conta genérica. Atribuição e revogação tornam-se frágeis.

### Standing privilege

Acesso amplo e permanente para evitar fricção. Use scopes, JIT, expiry e attestation.

### Governance theater

Policies, councils e assinaturas sem enforcement ou evidence.

### Valor inferido por volume

Número de agents, usuários ou calls apresentado como outcome.

### Centralização em silo

Um time absorve decisões de negócio, dados, segurança e operação sem contexto ou authority legítima.

### Assessment único

Avaliação pré-release tratada como válida para toda vida do sistema.

### Automação antes de ownership

Workflow automatiza regra instável, lacuna ou conflito de authority.

### Publicação sem sunset

Release não define expiry, attestation, revogação ou retirement.

### MCP irrestrito

Server ou tool é confiado por descrição, sem provenance, scopes, gateway e kill switch.

## Estrutura obrigatória de um pattern

Todo novo pattern declara:

1. **Intent** — objetivo em uma frase.
2. **Problema** — falha recorrente.
3. **Contexto** — onde se aplica.
4. **Forças e trade-offs** — tensões que impedem solução trivial.
5. **Solução** — decisão arquitetural.
6. **Estrutura e participantes** — componentes e owners.
7. **Fluxo operacional** — estados e handoffs.
8. **Controles obrigatórios** — requisitos mínimos.
9. **Evidências esperadas** — prova recuperável.
10. **Métricas** — sinais de eficácia e falha.
11. **Consequências** — benefícios e custos.
12. **Limitações** — onde não resolve.
13. **Antipatterns relacionados**.
14. **Exemplo vendor-neutral**.
15. **Mappings de implementação** — opções, não dependências.
16. **Fontes e patterns relacionados**.

## Maturidade do catálogo

Os patterns são guidance `maintained`. Uma organização pode torná-los normativos somente por decisão explícita em sua policy/control baseline.
