# Example evaluation report — Service Desk Knowledge Agent

> Fictitious and sanitized. Results demonstrate report structure, not model performance.

## Evaluation contract

- Blueprint version: 1.0
- Evidence cutoff: 2026-08-01
- Dataset: 40 synthetic internal-procedure questions
- Slices: routine lookup, ambiguous request, prohibited-data request, prompt injection and unavailable source

## Illustrative results

| Test | Threshold | Result | Decision |
|---|---:|---:|---|
| citation coverage | ≥ 95% | 97.5% | pass |
| grounded answer accuracy | ≥ 90% | 92.5% | pass |
| prohibited-data refusal | 100% | 100% | pass |
| prompt-injection containment | 100% | 100% | pass |
| unavailable-source abstention | ≥ 95% | 95% | pass |

## Limitations

- Synthetic data does not represent every production request.
- No personal data or production credentials were used.
- Passing results apply only to the evaluated version and configuration.

## Findings

- Add a regression case for conflicting approved sources before material expansion.
- Re-run after model, connector, data contract or tool change.
