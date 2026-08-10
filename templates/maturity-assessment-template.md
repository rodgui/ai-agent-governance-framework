# Template — Maturity Assessment

> Use com o [maturity model](../docs/guides/maturity-model.md). A versão estruturada deve validar contra [`schemas/maturity-assessment.schema.json`](../schemas/maturity-assessment.schema.json).

## Metadados

- Assessment ID:
- Method version: 1.0
- Organização/unidade:
- Data:
- Evidence cutoff:
- Assessment mode: self-assessment / facilitated-assessment / peer-review / limited-scope-review
- Assessor, role e organização:
- Conflitos declarados:
- Status:

## Escopo

### Incluído

-

### Excluído

-

### Limitações

-

## Sampling statement

- Method: full-population / judgmental / random / stratified / not-applicable
- Population description:
- Population size:
- Sample size:
- Rationale:
- Sampling limitations:

Amostra judgmental pode apoiar decisão de risco, mas não deve ser descrita como estatisticamente representativa.

## Evidence register

| Evidence ID | Título | Tipo | Reference | Observed at | Collected by | Scope | Limitações | SHA-256 opcional |
|---|---|---|---|---|---|---|---|---|
| EV- | | policy / process-record / system-record / interview / walkthrough / test / metric / sample / other | | | | | | |

Cada referência precisa ser recuperável dentro do ambiente autorizado. Não inclua secrets; use `[REDACTED]` e preserve apenas o identificador controlado.

## Escala

| Score | Definição |
|---:|---|
| 0 | inexistente ou desconhecido |
| 1 | ad hoc |
| 2 | definido |
| 3 | gerenciado |
| 4 | adaptativo |

## Dimensões

| Dimensão | Score | Confidence | Coverage | Target | Owner |
|---|---:|---|---:|---:|---|
| Estratégia e valor | | | | | |
| Operating model | | | | | |
| Registry e lifecycle | | | | | |
| Identidade e acesso | | | | | |
| Dados e connectors | | | | | |
| Tools e MCP | | | | | |
| Risco e Responsible AI | | | | | |
| Evaluations e release | | | | | |
| Auditabilidade e operações | | | | | |
| Adoção e suporte | | | | | |

## Detalhe por dimensão

Repita esta seção para as dez dimensões.

### [Dimensão]

- Score:
- Confidence: low / medium / high
- Confidence rationale:
- Coverage: 0–100%
- Coverage basis:
- Evidence refs: EV-...
- Owner:
- Target:

#### Gaps

-

#### Rationale do score

Explique como as evidências demonstram o nível e por que o nível seguinte não foi atingido.

-

#### Dependencies

-

## Síntese

- Mediana:
- Faixa min–max:
- Dimensões abaixo do target:
- Evidence confidence global:
- Blockers críticos e altos:

A média não deve ser apresentada como nota de compliance.

## Prioridades

| Severidade | Outcome | Owner | Target date | Acceptance criteria | Dependency |
|---|---|---|---|---|---|
| critical / high / medium / low | | | | | |

Severidade de gap não é risk tier T1–T4 nem prioridade de um control no catálogo.

## Target-state decisions

-

## Review e disposition

- Reviewer, role e organização:
- Reviewed at:
- Conflicts checked: yes / no
- Disposition: accepted / accepted-with-conditions / disputed
- Conditions ou divergências:

## Reviewer checklist

- [ ] Reviewer é diferente do assessor e conflitos foram declarados.
- [ ] Scores possuem evidence refs recuperáveis, não apenas opinião.
- [ ] Population, sampling, coverage basis e limitações são explícitos.
- [ ] Confidence segue as âncoras do método.
- [ ] Documentação sem operação não excede nível 1–2.
- [ ] Rationale explica por que o próximo nível não foi demonstrado.
- [ ] Maturidade não foi confundida com risco.
- [ ] Roadmap prioriza severidade, risco e dependência.
- [ ] Limitações e conflitos de evidência são visíveis.
- [ ] A conclusão não reivindica audit, certification ou independent assurance.
