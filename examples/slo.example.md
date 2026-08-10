# Example SLO — Service Desk Knowledge Agent

> Fictitious and sanitized. Thresholds are illustrative, not universal recommendations.

## Service objectives

| Indicator | Illustrative objective | Window | Owner action on breach |
|---|---:|---|---|
| successful approved-source retrieval | ≥ 99% | 30 days | investigate connector and source health |
| p95 response latency | ≤ 8 seconds | 7 days | review model, retrieval and gateway latency |
| prohibited tool execution | 0 | continuous | quarantine and escalate immediately |
| support acknowledgment for severity high | ≤ 30 minutes | per incident | escalate to Run Authority |

## Error budget and review

- Availability objectives do not override safety or authorization controls.
- Safety/security signals can trigger containment before an SLO breach.
- Thresholds must be reapproved after material scope or architecture change.
