---
title: "Atributos de qualidade para governança de agentes"
status: review
maturity: observed
last_reviewed: 2026-08-09
review_cycle: 180d
owners: [rodgui]
tags: [architecture, quality-attributes, agent-governance]
---

# Atributos de qualidade para governança de agentes

## Auditability

Toda decisão relevante precisa de owner, timestamp, evidência, versão e vínculo com agent ID.

## Observability

A operação deve expor ações, ferramentas, dados acessados, erros, custo, policy signals e uso suficiente para decisão.

## Remediability

O sistema deve permitir restringir, quarentenar, corrigir, reverter e aposentar dentro de SLAs proporcionais ao risco.

## Accountability

Business owner, technical owner e authorities precisam ter responsabilidade e autoridade claramente separadas.

## Interoperability

Registry, evidence e policy controls devem funcionar em múltiplas plataformas, inclusive ferramentas de terceiros.

## Security and privacy

Least privilege, workload identity, secrets management, DLP, data boundaries e secure-by-default são propriedades de base.

## Reliability

Agentes críticos exigem métricas, error handling, rollback, fallback e continuidade compatíveis com o processo afetado.

## Usability

Builders e usuários precisam entender limites, approvals, status e próximos passos sem depender de especialistas para casos simples.

## Evolvability

Risk matrix, connector catalog, model/tool inventory e policy templates devem aceitar novas capacidades sem reescrita completa.

## Measurability

Criação, descoberta, uso, qualidade, risco, custo e valor precisam ser distinguíveis e comparáveis a baselines.
