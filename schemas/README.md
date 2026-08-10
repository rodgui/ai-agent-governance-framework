# Schemas

Schemas JSON Draft 2020-12 para artefatos estruturados de governança.

## Schemas canônicos

| Schema | Finalidade | Exemplo |
|---|---|---|
| [`agent-registry.schema.json`](agent-registry.schema.json) | inventory, ownership, lifecycle, risk e evidence links | [`agent-registry.example.json`](../examples/agent-registry.example.json) |
| [`agent-blueprint.schema.json`](agent-blueprint.schema.json) | arquitetura, modelos, dados, identidade, tools e runtime | [`agent-blueprint.example.json`](../examples/agent-blueprint.example.json) |
| [`control-catalog.schema.json`](control-catalog.schema.json) | requirements, implementação, evidências e métricas | [`control-catalog.json`](../controls/control-catalog.json) |
| [`maturity-assessment.schema.json`](maturity-assessment.schema.json) | score, confidence, coverage, gaps e target | [`maturity-assessment.example.json`](../examples/maturity-assessment.example.json) |

## Validação

```bash
uv run --with jsonschema python3 tools/scripts/validate-repository.py
```

O CI valida:

- sintaxe e compatibilidade Draft 2020-12;
- exemplos contra seus schemas;
- guardrails negativos para lifecycle, release evidence, tools state-changing e assessment review;
- invariantes entre records, incluindo IDs de evidência existentes, reviewer distinto, sampling válido e attestation vigente no `lastReviewed`;
- IDs de controls referenciados nos blueprints;
- paths Markdown/JSON, inclusive traversal com fragmento, e manifestos locais.

## Convenções

- `schemaVersion` controla compatibilidade estrutural.
- IDs e versions são estáveis; mudanças incompatíveis exigem major version.
- `additionalProperties: false` evita campos silenciosos.
- Missing evidence permanece explícito; não use valores fictícios.
- Secrets, tokens e connection strings nunca entram nos records; use `[REDACTED]` em documentos humanos.
- Examples usam `.invalid` e nomes fictícios; não representam deployment real.

## Registry versus blueprint

- **Registry:** o que existe, quem responde, status, tier e lifecycle.
- **Blueprint:** como funciona, quais dados/identidades/tools usa e qual blast radius possui.

Os objetos são relacionados, mas não devem ser fundidos em um registro impossível de manter.
