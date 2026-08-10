# Examples

Exemplos fictícios e sanitizados que demonstram o uso dos schemas e templates.

## Records estruturados

- [`agent-registry.example.json`](agent-registry.example.json) — registry record de um agente interno fictício.
- [`agent-blueprint.example.json`](agent-blueprint.example.json) — blueprint técnico correspondente.
- [`control-catalog.example.json`](control-catalog.example.json) — catálogo mínimo para demonstrar o schema.
- [`maturity-assessment.example.json`](maturity-assessment.example.json) — assessment de organização fictícia.

## Evidence package operacional

- [`architecture.example.md`](architecture.example.md) — arquitetura, trust boundaries e failure boundaries.
- [`risk-assessment.example.md`](risk-assessment.example.md) — classificação e residual gaps ilustrativos.
- [`evaluation-report.example.md`](evaluation-report.example.md) — evaluation contract, slices, thresholds e limitações.
- [`release-decision.example.md`](release-decision.example.md) — decisão G5 condicionada e evidence refs.
- [`support-runbook.example.md`](support-runbook.example.md) — sinais, contenção e recuperação.
- [`slo.example.md`](slo.example.md) — objetivos e owner actions ilustrativos.

## Validação

Os exemplos são testados automaticamente contra os schemas em [`schemas/`](../schemas/README.md).

```bash
uv run --with-requirements requirements-ci.txt python3 tools/scripts/validate-repository.py
```

## Limites

- nomes, contatos, tenants e providers são fictícios;
- domínios usam `.invalid`;
- scores e outcomes não representam cliente real;
- exemplos não são recomendação de threshold;
- nenhum secret ou path pessoal é permitido.

Novos exemplos devem declarar claramente o que demonstram, quais assumptions usam e o que não pode ser inferido.
