# Example release decision — Service Desk Knowledge Agent

> Fictitious and sanitized. This record does not authorize a real deployment.

## Decision record

- Gate: G5 — Onboarding/release
- Scope: internal service-desk analysts
- Blueprint: 1.0
- Tier: T2
- Decision: `condition`
- Authority: Example Design Authority
- Date: 2026-08-01
- Expiry: 2026-11-01

## Evidence accepted

- [Architecture](architecture.example.md)
- [Risk assessment](risk-assessment.example.md)
- [Evaluation report](evaluation-report.example.md)
- [Support runbook](support-runbook.example.md)
- [SLO](slo.example.md)

## Conditions

1. external responses require human review;
2. personal data and credentials remain prohibited;
3. any new connector or state-changing tool returns to G4/G5;
4. quarantine and rollback must be exercised before reactivation after incident.

## Rationale

The limited read-and-draft scope, evidence package and revocation path support conditional release. The decision does not cover new populations, tools, data classes or model versions.
