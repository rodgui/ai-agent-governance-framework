# Schemas

Schemas JSON Draft 2020-12 para artefatos estruturados de governança.

## Schemas canônicos

| Schema | Finalidade | Exemplo |
|---|---|---|
| [`agent-registry.schema.json`](agent-registry.schema.json) 2.0 | discovery, ownership, lifecycle stage, operational state, risco, admissibilidade e evidence links | [`agent-registry.example.json`](../examples/agent-registry.example.json) |
| [`agent-blueprint.schema.json`](agent-blueprint.schema.json) 2.0 | arquitetura, model/source/tool bindings, identidade, runtime e governança | [`agent-blueprint.example.json`](../examples/agent-blueprint.example.json) |
| [`control-catalog.schema.json`](control-catalog.schema.json) 2.0 | requirements, implementação, verification, automação, evidências e mappings | [`control-catalog.json`](../controls/control-catalog.json) 1.2.0 |
| [`maturity-assessment.schema.json`](maturity-assessment.schema.json) | score, confidence, coverage, gaps e target | [`maturity-assessment.example.json`](../examples/maturity-assessment.example.json) |
| [`model-provider-catalog.schema.json`](model-provider-catalog.schema.json) | combinações provider/model/version aprovadas e suas restrições | [`model-provider-catalog.example.json`](../examples/model-provider-catalog.example.json) |
| [`certified-source-catalog.schema.json`](certified-source-catalog.schema.json) | fontes certificadas, finalidades, restrições e validade | [`certified-source-catalog.example.json`](../examples/certified-source-catalog.example.json) |
| [`enterprise-tool-registry.schema.json`](enterprise-tool-registry.schema.json) | tools autorizadas, capabilities, scopes e containment | [`enterprise-tool-registry.example.json`](../examples/enterprise-tool-registry.example.json) |
| [`release-evidence-manifest.schema.json`](release-evidence-manifest.schema.json) | decisão de release e evidence lineage por control | [`release-evidence-manifest.example.json`](../examples/release-evidence-manifest.example.json) |
| [`audit-event.schema.json`](audit-event.schema.json) | envelope mínimo de evento auditável sem payload sensível | [`audit-event.example.json`](../examples/audit-event.example.json) |

## Validação

```bash
uv run --with jsonschema python3 tools/scripts/validate-repository.py
```

O CI valida:

- sintaxe e compatibilidade Draft 2020-12;
- exemplos contra seus schemas;
- guardrails negativos para lifecycle, discovery, model/source/tool bindings, admissibility, release evidence, tools state-changing e assessment review;
- invariantes entre records, incluindo catalog entry IDs, risk/admissibility, release manifest, audit event, reviewer distinto, sampling válido e attestation vigente no `lastReviewed`;
- IDs de controls referenciados nos blueprints;
- paths Markdown/JSON, inclusive traversal com fragmento, e manifestos locais.

## Convenções

- `schemaVersion` controla compatibilidade estrutural.
- IDs e versions são estáveis; mudanças incompatíveis exigem major version.
- `additionalProperties: false` evita campos silenciosos.
- Missing evidence permanece explícito; não use valores fictícios.
- Secrets, tokens e connection strings nunca entram nos records; use `[REDACTED]` em documentos humanos.
- Examples usam `.invalid` e nomes fictícios; não representam deployment real.
- O [guia de migração 2.0](../docs/guides/schema-migration-2.0.md) preserva versões anteriores e proíbe inferir decisão ausente.

## Registry versus blueprint

- **Registry:** o que existe, quem responde, discovery, stage/state, tier e admissibilidade.
- **Blueprint:** como funciona, quais versões de model e quais entradas de source/tool catalog usa, e qual blast radius possui.

Os objetos são relacionados, mas não devem ser fundidos em um registro impossível de manter.
