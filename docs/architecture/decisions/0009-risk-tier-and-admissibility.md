---
title: ADR-0009 — Separação entre risk tier e admissibilidade
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: 0004-risk-tier-taxonomy-and-fast-path.md
related:
  - 0004-risk-tier-taxonomy-and-fast-path.md
  - ../../risk-management/README.md
  - ../../risk-management/minimum-production-bar.md
  - ../../../schemas/agent-registry.schema.json
  - ../../../schemas/agent-blueprint.schema.json
---

# ADR-0009 — Separação entre risk tier e admissibilidade

## Contexto

A [ADR-0004](0004-risk-tier-taxonomy-and-fast-path.md) preservou corretamente T1–T4 e o fast path de T1. Na absorção do guia v3.4, porém, o rótulo externo `Restricted` foi associado a T4. Isso fez T4 significar simultaneamente criticidade e default deny.

As perguntas são diferentes:

- **risk tier:** quão severa é a exposição se o agente falhar ou for abusado?
- **admissibilidade:** esta finalidade e este desenho podem operar, sob quais condições?

Misturá-las produz decisões contraditórias. Um caso de baixo impacto pode ser proibido por finalidade, enquanto um caso crítico pode ser permitido sob authority e controles reforçados.

## Decisão

1. **T1–T4 permanece a taxonomia canônica de risco/criticidade.**
2. O fast path de T1 permanece uma rota proporcional, nunca uma isenção.
3. Criar dimensão independente `admissibility`:

   | Valor | Significado |
   | --- | --- |
   | `permitted` | uso admitido dentro do blueprint e dos controls aprovados |
   | `conditional` | admitido somente enquanto condições documentadas permanecerem satisfeitas |
   | `restricted` | default deny; exceção explícita, temporária e rastreável é necessária |
   | `prohibited` | não pode entrar ou permanecer em produção naquele escopo |

4. `restricted` exige authority, exception reference e expiry. `prohibited` não pode ser publicado em production.
5. Risk tier e admissibility devem aparecer no Registry, Blueprint, risk record e release evidence manifest.
6. Alteração em qualquer dimensão é material change e exige reavaliação.
7. Na importação do guia v3.4, `Restricted` é mapeado para admissibility; não redefine T4.
8. O mapeamento T0/T1 para o fast path de T1 continua válido. As demais classificações externas precisam ser decompostas em risco e admissibilidade antes de uso.

## Consequências

### Positivas

- elimina duas semânticas concorrentes para T4;
- permite policy bans independentes da severidade;
- preserva histórico e métricas T1–T4;
- deixa exceções temporárias explícitas e expiráveis.

### Negativas

- adiciona uma segunda dimensão aos registros e formulários;
- classificadores antigos precisam de migração;
- nenhuma tabela unidimensional representa sozinha toda a decisão de onboarding.

## Critérios de validação

- enums T1–T4 permanecem idênticos nos três schemas canônicos;
- Registry e Blueprint exigem admissibility e rationale;
- production rejeita `prohibited`;
- `restricted` exige exception reference e expiry;
- documentação não chama T4 de `Restricted` sem qualificar que são dimensões distintas.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10 após gap analysis do guia v3.4 contra o corpus e aprovação explícita da separação entre criticidade e admissibilidade.
