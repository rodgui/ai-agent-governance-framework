# Example risk assessment — Service Desk Knowledge Agent

> Fictitious and sanitized. This is not a legal opinion, certification or real risk acceptance.

## Scope

- Version: 1.0
- Intended users: internal service-desk analysts
- Capabilities: approved retrieval and draft creation
- Prohibited: system changes, personal data, credentials and unreviewed external responses

## Classification

| Dimension | Observation | Rating |
|---|---|---|
| Data | internal approved knowledge; no personal data intended | moderate |
| Action capability | read and draft only; no system mutation | low |
| Reach | internal analysts in one operating unit | moderate |
| Reversibility | sessions can be blocked and blueprint rolled back | high |
| Interconnectivity | one gateway and one retrieval service | moderate |

**Illustrative tier:** T2.

## Required controls

- `AGF-REG-001`
- `AGF-IDN-001`
- `AGF-DAT-001`
- `AGF-EVA-001`
- `AGF-OPS-001`

## Residual gaps and decision

- Connector authorization must be re-tested after a data-source change.
- Any state-changing tool or external-user expansion triggers reassessment.
- Residual risk: moderate, accepted only for this fictitious scope and evidence cutoff.
