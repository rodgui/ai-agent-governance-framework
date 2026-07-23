# AI Agent Policy and Governance Framework

A practical, enterprise-grade governance framework for the creation, publication, and operation of AI Agents across corporate platforms.

## Why this framework exists

As organizations deploy AI agents at scale — across platforms like n8n, AWS Bedrock, Azure AI Foundry, Microsoft Copilot Studio, and others — governance gaps emerge fast:

- Agents with no designated owner
- Irreversible actions without human oversight
- Data leakage through ungoverned LLM calls
- No audit trail, no kill-switch, no sunset plan

This framework was developed in **January 2026** for a large industrial enterprise and submitted to its AI Governance Committee. The organization's official Responsible AI Policy, published in June 2026, aligned closely with the structure proposed here.

## What's included

| Area | Contents |
|---|---|
| `docs/governance/` | Core policy — governance model, autonomy levels, HITL, blast radius, approval matrix, lifecycle |
| `templates/` | Self-assessment form and example, publication checklist, sunset plan |
| `docs/identity/` | Agent identity, authentication, authorization and workload identity |
| `docs/tool-governance/` | Tool approval, sandbox, least-privilege and approval gates |
| `docs/data-access/` | Data classification, DLP, lineage, provenance and consent |
| `docs/risk-management/` | Risk taxonomy, blast radius assessment and mitigation |
| `docs/evaluations/` | Quality gates, evals and continuous assessment |
| `docs/auditability/` | Logging, trail retention and compliance evidence |
| `docs/human-oversight/` | HITL design, approval flows and escalation |
| `docs/responsible-ai/` | Principles, controls, safety and monitoring |
| `docs/executive/` | Briefs, recommendations and executive communication |
| `schemas/` | JSON/YAML schemas for agent catalog and self-assessment |
| `controls/` | Control library mapping policy requirements to implementations |
| `examples/` | Real-world examples and case studies |
| `assessments/` | Technology and maturity evaluations |
| `experiments/` | Hypotheses, PoCs and benchmarks |
| `references/` | Sources, glossary and bibliography |

## Core concepts

### Autonomy Levels (L0–L3)

- **L0** — AI only suggests; human executes everything
- **L1** — AI executes routine, bounded, reversible tasks with logging
- **L2** — AI executes with periodic human review; HITL at key decision points
- **L3** — High autonomy; requires exceptional approval, continuous monitoring, kill-switch mandatory

### Blast Radius

Every agent is assessed before deployment on:

- **Probability** = f(Permissions, Autonomy, Interconnectivity, Auth Strength)
- **Impact** = data/privacy · financial · operational · reputational

Result maps directly to the Approval Matrix.

### HITL (Human-in-the-Loop)

All irreversible, high-impact actions require explicit human confirmation through an approved channel. No exceptions without documented waiver and rollback plan.

### Approval Matrix

Scales with user count, environment (PoC vs Production), and risk triggers (personal data, financial controls, critical systems). Any red flag escalates to Production-level regardless of size.

## How to use

1. Review the core policy at [`docs/governance/ai-agent-policy-and-governance-v1.md`](docs/governance/ai-agent-policy-and-governance-v1.md).
2. Adapt the policy to your platforms, regulatory framework, and governance structure.
3. Use the templates as-is or extend them.
4. Register every agent in a catalog before Production (catalog fields defined in policy section 11).

## License

[Creative Commons Attribution 4.0 International](LICENSE) — free to use, adapt, and share with attribution.

## Author

**Rodrigo Garcia Guimarães**  
Infrastructure Senior Architect | AI Governance | Hybrid Cloud & Industrial Edge  
[LinkedIn](https://linkedin.com/in/rodgui) · [GitHub](https://github.com/rodgui)

*Framework created January 2026.*