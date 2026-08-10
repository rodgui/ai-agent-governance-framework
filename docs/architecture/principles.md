---
title: "Princípios arquiteturais de governança de agentes"
status: maintained
maturity: validated
last_reviewed: 2026-08-09
review_cycle: 180d
owners: [rodgui]
tags: [architecture, principles, agent-governance]
---

# Princípios arquiteturais de governança de agentes

1. **Proportional by risk:** controles aumentam com alcance, dados, capacidade de ação, autonomia e irreversibilidade.
2. **Embedded by default:** guidance, limits, identity, logging e policy entram nas ferramentas e pipelines.
3. **Human-led:** pessoas definem direção, aprovam exceções e permanecem accountable.
4. **Observable and remediable:** autonomia relevante exige telemetria, quarantine, rollback e sunset.
5. **Federated with common controls:** domínios mantêm ownership; padrões comuns preservam interoperabilidade e confiança.
6. **Evidence before automation:** decisões e exceções precisam de evidência antes de policy-as-code.
7. **Lifecycle-aware:** criação, mudança, attestation, transferência e decommissioning fazem parte do mesmo sistema.
8. **Platform-agnostic:** policy e control objectives são comuns; implementação varia por plataforma.
9. **Value-linked:** criação e uso só importam quando conectados a qualidade, risco, experiência e resultado.
10. **Iterative:** arquitetura, controles e risk matrix evoluem com tecnologia, regulação e evidência operacional.

## Relationship to policy

Esses princípios integram a [policy modular](../governance/policy.md). Sua adoção e alteração exigem revisão formal, decision authority e release versionada; mappings de plataforma não podem redefini-los.
