# Examples

Exemplos fictícios e sanitizados que demonstram o uso dos schemas e templates.

## Records estruturados

- [`agent-registry.example.json`](agent-registry.example.json) — registry record de um agente interno fictício.
- [`agent-blueprint.example.json`](agent-blueprint.example.json) — blueprint técnico correspondente.
- [`control-catalog.example.json`](control-catalog.example.json) — catálogo mínimo para demonstrar o schema.
- [`maturity-assessment.example.json`](maturity-assessment.example.json) — assessment de organização fictícia.
- [`model-provider-catalog.example.json`](model-provider-catalog.example.json) — combinação provider/model/version aprovada.
- [`certified-source-catalog.example.json`](certified-source-catalog.example.json) — fontes certificadas e restrições estruturadas.
- [`enterprise-tool-registry.example.json`](enterprise-tool-registry.example.json) — tools catalogadas com scopes e containment.
- [`release-evidence-manifest.example.json`](release-evidence-manifest.example.json) — decisão e evidence lineage de release.
- [`audit-event.example.json`](audit-event.example.json) — envelope auditável de uma tool request sem payload sensível.

## Casos de referência

Records agrupados por caso em [`cases/`](cases/), validados pelos mesmos schemas e invariantes dos exemplos da raiz. Cada caso tem a narrativa correspondente em [`docs/explanations/cases/`](../docs/explanations/cases/README.md).

- [`cases/meeting-notes-summarizer/`](cases/meeting-notes-summarizer/) — T1 na rota rápida, somente leitura.

## Evidence package operacional

- [`architecture.example.md`](architecture.example.md) — arquitetura, trust boundaries e failure boundaries.
- [`risk-assessment.example.md`](risk-assessment.example.md) — classificação e residual gaps ilustrativos.
- [`evaluation-report.example.md`](evaluation-report.example.md) — evaluation contract, slices, thresholds e limitações.
- [`release-decision.example.md`](release-decision.example.md) — decisão G5 condicionada e evidence refs.
- [`support-runbook.example.md`](support-runbook.example.md) — sinais, contenção e recuperação.
- [`slo.example.md`](slo.example.md) — objetivos e owner actions ilustrativos.

## Operating model e estate

- [`governance-charter.example.md`](governance-charter.example.md) — mandato, authority e scope statement com prazo de exclusão.
- [`governance-raci.example.md`](governance-raci.example.md) — decision rights preenchidos, com um único accountable por decisão material.
- [`handoff-matrix.example.md`](handoff-matrix.example.md) — transições, pré-condições, evidência transferida e SLA.
- [`manual-bottleneck-register.example.md`](manual-bottleneck-register.example.md) — onde a governança depende de trabalho manual repetitivo.
- [`target-maturity-roadmap.example.md`](target-maturity-roadmap.example.md) — alvos por capability com dependências e confiança declarada.

## Dados e runtime

- [`certified-source-catalog.example.md`](certified-source-catalog.example.md) — critérios de certificação, catálogo de fontes e backlog de remediação.
- [`behavioral-analytics-catalog.example.md`](behavioral-analytics-catalog.example.md) — casos, thresholds, modo de operação e métrica de falso positivo.

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
