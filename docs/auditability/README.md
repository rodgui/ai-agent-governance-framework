---
title: Auditabilidade, evidence package e traceability
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - ../governance/operating-model.md
  - ../operations/README.md
  - ../evaluations/README.md
  - ../../controls/README.md
  - ../../schemas/audit-event.schema.json
  - ../../schemas/release-evidence-manifest.schema.json
  - ../../templates/release-evidence-manifest.md
---

# Auditabilidade, evidence package e traceability

## Objetivo

Permitir que uma pessoa autorizada reconstrua o que o sistema era, o que fez, com qual autoridade, quais dados e tools usou, quais controles se aplicaram e qual decisão resultou.

## Auditabilidade não é “logar tudo”

Logs indiscriminados podem aumentar risco de privacy, custo e exposição. O desenho precisa equilibrar:

- traceability;
- minimização;
- integridade;
- retenção;
- acesso;
- utilidade para investigação;
- separação entre telemetria e record oficial.

## Eventos mínimos

- criação e alteração de registry/blueprint;
- classificação e approvals;
- model, prompt, tool e policy version;
- authentication e authorization decision;
- user/agent/tool correlation;
- retrieval source IDs e data classification quando aplicável;
- state-changing action e result;
- human approval, edit, deny e override;
- policy denial e alert;
- incident, quarantine, rollback e reactivation;
- attestation, exception e sunset.

## Event envelope

| Campo | Propósito |
|---|---|
| timestamp e timezone | ordenar e correlacionar |
| event ID / correlation ID | rastrear a chain |
| agent ID e version | identificar o sistema |
| user/delegated subject | atribuir contexto humano |
| tool/action | identificar capability |
| target/resource | localizar efeito |
| policy/control decision | explicar allow/deny |
| outcome/status | registrar resultado |
| evidence reference | apontar artefato protegido |
| sensitivity | aplicar acesso e retenção |

Sensitive payloads devem ser referenciados ou protegidos, não copiados sem necessidade.

O [AI Agent Audit Event schema](../../schemas/audit-event.schema.json) oferece um envelope mínimo vendor-neutral. Ele não obriga ferramenta ou pipeline específico e deliberadamente evita payload completo.

## Evidence package

Um package de release ou attestation deve ser:

- versionado;
- immutable ou tamper-evident;
- ligado a agent/version;
- completo segundo tier;
- acessível somente a roles autorizados;
- retido conforme policy;
- exportável para review;
- capaz de distinguir missing, not-applicable e passed.

“Sem evidência” não significa “controle passou”.

A composição mínima de cada package por nível de risco está em [evidence pack proporcional por tier](evidence-pack-by-tier.md).
Use o [Release Evidence Manifest schema](../../schemas/release-evidence-manifest.schema.json) para lineage machine-readable e o [template humano](../../templates/release-evidence-manifest.md) para preparar a decisão.

## Integridade e acesso

- clock synchronization;
- append-only ou controles de integridade;
- segregação de administradores e auditores;
- access logging;
- redaction/tokenization;
- legal hold quando aplicável;
- test de restauração e export;
- retention/deletion verificáveis.

## Traceability graph

```text
Business outcome
  ↕
Agent ID/version
  ↕
Blueprint → model/prompt/data/tool versions
  ↕
Risk/control/evaluation decisions
  ↕
Runtime events/incidents
  ↕
Attestation/value/sunset decision
```

## Evidências

- logging specification;
- sample events e schema;
- [audit event estruturado](../../schemas/audit-event.schema.json);
- access/retention configuration;
- integrity test;
- evidence package index;
- [release evidence manifest](../../schemas/release-evidence-manifest.schema.json);
- audit export test;
- deletion e legal-hold records;
- findings e remediação.

## Métricas

- actions sem correlation ID;
- events atrasados, incompletos ou duplicados;
- agents sem version identificável;
- evidence packages incompletos;
- unauthorized log access;
- retention/deletion failures;
- tempo para reconstruir um incident;
- controls com evidence link quebrado.

## Failure modes

- logar prompt completo por padrão;
- usar dashboard agregado como audit trail;
- não versionar prompt/model/tool;
- permitir que o mesmo admin altere ação e evidência;
- guardar logs sem capability de busca/export;
- apagar evidência no sunset antes de cumprir retenção;
- marcar missing como not-applicable.

## Decision gate

A release authority exige event model, retention, access, correlation e evidence package compatíveis com o tier antes de produção.
