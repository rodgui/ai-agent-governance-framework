---
title: Migração dos contratos estruturados para 2.0
status: maintained
owner: AI Governance Office
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - ../architecture/decisions/0010-structured-governance-contracts-2.0.md
  - ../../schemas/README.md
  - ../../examples/README.md
---

# Migração dos contratos estruturados para 2.0

Este guia migra registros de referência. Ele **não inventa** decisões, owners, evidências, versões ou exceções que não existam. Quando a origem não contém a informação, registre a lacuna e encaminhe-a à authority competente.

## Estratégia segura

1. preserve o arquivo 1.x imutável;
2. crie cópia 2.0 com novo commit e provenance;
3. aplique somente mapeamentos determinísticos;
4. marque campos sem fonte como pendentes — não use valores plausíveis;
5. valide o record;
6. faça revisão humana de risk, admissibility, ownership e evidence;
7. só então altere o ponteiro de versão ativa.

## Agent Registry 1.0 → 2.0

### Lifecycle

| `status` 1.0 | `stage` 2.0 | `operationalState` 2.0 | Revisão necessária |
| --- | --- | --- | --- |
| `discovered` | `discovered` | `not-deployed` | confirmar sinais e ownership |
| `registered` | `draft` | `not-deployed` | nenhuma inferência de aprovação |
| `assessed` | `under-review` | `not-deployed` | anexar assessment evidence |
| `conditional` | `under-review` | `not-deployed` | mover condições para decision/evidence |
| `approved` | `approved` | `not-deployed` | confirmar `approvedAt` e authority |
| `active` | `production` | `enabled` | confirmar ambiente e attestation |
| `quarantined` | `production` | `quarantined` | registrar containment authority |
| `sunset-planned` | `retirement-review` | decidir pelo estado observado | não inferir enabled/suspended |
| `retired` | `retired` | `disabled` | anexar retirement evidence |
| `archived` | `archived` | `disabled` | confirmar retention |

Crie pelo menos uma entrada em `transitionHistory` representando a migração, com `authority`, `reason`, `occurredAt` e `evidenceRef`. Não fabrique o histórico anterior.

### Discovery

O objeto 1.0 `source` vira `discovery.signals[]`. `confidence` permanece confidence. `discovery.status` precisa ser decidido separadamente:

- `confirmed`: dois ou mais sinais independentes ou declaração reconciliada;
- `probable`: sinal forte sem reconciliação completa;
- `suspected`: indicador que ainda requer triage.

### Risk e admissibility

`tier` permanece T1–T4. Adicione `admissibility` e `admissibilityRationale` por decisão explícita. T4 não implica automaticamente `restricted`; o valor externo `Restricted` não deve ser copiado para `tier`.

## Agent Blueprint 1.0 → 2.0

Para cada model binding, adicione:

- `modelVersion`;
- `catalogEntryId` no Approved Model and Provider Catalog;
- `evaluationRef` vinculada à versão;
- `role`, classes de dados e regiões permitidas;
- fallback aprovado, fail closed ou rationale para `not-required`.

Se o provider não oferece pinning, mantenha `versionPinned: false` e registre `changeDetectionRef` e `serviceChangePolicyRef`.

Para cada source e tool, crie primeiro a entrada nos catálogos correspondentes e só depois preencha `catalogEntryId` no Blueprint.

Em governance, adicione admissibility. `restricted` exige exception reference e expiry; `prohibited` não pode incluir production.

## Control Catalog

O catálogo canônico 1.2.0 preserva todos os IDs 1.1 e adiciona `AGF-RSK-004`. Atualize as versões:

```json
{
  "schemaVersion": "2.0",
  "catalogVersion": "1.2.0"
}
```

Todo control precisa declarar `scope`, `verification`, `blocking`, `automation` e `frameworkMappings`. Use `frameworkMappings: []` quando não houver mapping público verificável; nunca invente referência. Adote `AGF-RSK-004` quando a organização usar a dimensão de admissibilidade.

## Novos contratos de referência

A ordem recomendada é:

1. model/provider catalog;
2. certified source catalog;
3. enterprise tool registry;
4. Agent Blueprint bindings;
5. release evidence manifest;
6. audit event envelope.

Esses contratos podem ser implementados em CMDB, GRC, catálogo interno, planilha controlada ou API. O JSON do repositório define semântica mínima, não plataforma obrigatória.

## Validação

```bash
uv run --with-requirements requirements-ci.txt python tools/scripts/validate-repository.py
```

Para registros organizacionais, valide também qualidade de decisão: authority real, referências recuperáveis, datas coerentes e nenhuma lacuna mascarada por placeholder.
