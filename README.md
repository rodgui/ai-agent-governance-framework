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

| File | Description |
|------|-------------|
| `policy/AI_Agent_Policy_and_Governance_v1.md` | Core policy — 13 sections: governance model, autonomy levels, HITL, blast radius, approval matrix, lifecycle |
| `templates/self-assessment-form.md` | Mandatory self-assessment before creating/publishing any agent |
| `templates/self-assessment-example.md` | Filled example of the self-assessment |
| `templates/publication-checklist.md` | Pre-production gate checklist |
| `templates/sunset-plan.md` | Controlled agent decommissioning template |

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

1. Fork or clone this repo
2. Adapt the policy to your platforms, regulatory framework, and governance structure
3. Use the templates as-is or extend them
4. Register every agent in a catalog before Production (catalog fields defined in policy section 11)

## Author

**Rodrigo Garcia Guimarães**  
Infrastructure Senior Architect | AI Governance | Hybrid Cloud & Industrial Edge  
[LinkedIn](https://linkedin.com/in/rodgui) · [GitHub](https://github.com/rodgui)

*Framework created January 2026. Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).*

## License

[Creative Commons Attribution 4.0 International](LICENSE) — free to use, adapt, and share with attribution.
