---
title: "Riscos arquiteturais da governança de agentes"
status: review
maturity: observed
last_reviewed: 2026-08-09
review_cycle: 90d
owners: [rodgui]
tags: [architecture, risks, agent-governance]
---

# Riscos arquiteturais da governança de agentes

| Risco | Consequência | Mitigação arquitetural |
| --- | --- | --- |
| Catálogo incompleto | Falsa confiança e agentes órfãos | Reconciliation, missing-evidence status e coverage metrics |
| Centralização excessiva | Gargalo, shadow AI e baixa accountability local | Ownership federado, common controls e handoffs explícitos |
| Aprovação igual para todos | Burocracia em baixo risco e revisão insuficiente em alto risco | Risk matrix proporcional por alcance e capacidade |
| Telemetria sem ação | Dashboard decorativo e incidentes sem owner | Alert-to-workflow, authority, SLA e remediation states |
| Automação prematura | Enforcement incorreto e exceções ocultas | Pilotos manuais, baselines e evidence before automation |
| Dados não confiáveis | Respostas erradas, oversharing e decisões inválidas | AI-ready data, labels, connector gates e lineage |
| Identidade fraca ou compartilhada | Acesso indevido e baixa rastreabilidade | Workload identity, least privilege e lifecycle de credenciais |
| MCP sem governança | Tool poisoning, exfiltration e blast radius ampliado | Gateway, vetting, inventory, isolation e context trimming |
| Métricas de vaidade | Investimento em agentes sem valor | Separar criação, descoberta, uso, qualidade e outcomes |
| Dependência de fornecedor | Lock-in e perda de controle | Policy e schemas multiplataforma, exportable logs e adapters |
| Owners nominais | Reviews e incidents sem decisão efetiva | Authority explícita, attestation e escalation path |
| Policy drift | Agentes ficam não conformes após mudanças | Versionamento, review triggers, compliance monitoring e remediation |

## Review triggers

Revisar este registro quando houver:

- nova plataforma, model provider, connector ou MCP server;
- expansão regional ou exposição externa;
- mudança de autonomia ou capacidade de escrita/ação;
- incidente relevante;
- alteração regulatória;
- evidência dos pilotos do plano de 90 dias.
