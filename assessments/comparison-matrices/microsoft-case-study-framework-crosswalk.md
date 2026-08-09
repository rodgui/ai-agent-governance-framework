---
title: "Crosswalk: Microsoft Customer Zero × AI Agent Policy v1"
status: review
maturity: observed
last_reviewed: 2026-08-09
review_cycle: 90d
owners: [rodgui]
tags: [assessment, crosswalk, policy-v2, microsoft, agent-governance]
related:
  policy: ../../docs/governance/ai-agent-policy-and-governance-v1.md
  study: ../../docs/explanations/microsoft-agent-governance-case-study.md
  plan: ../../docs/guides/implementation-plan-90-days.md
---

# Crosswalk: Microsoft Customer Zero × AI Agent Policy v1

## Objetivo

Comparar as capacidades descritas em cinco artigos do Microsoft Inside Track com a [AI Agent Policy and Governance v1](../../docs/governance/ai-agent-policy-and-governance-v1.md). O resultado identifica cobertura existente, lacunas e prioridades para uma futura v2.

Este assessment não altera a policy v1. Mudanças de policy exigem revisão formal, changelog e uma nova versão preservando o histórico.

## Escala de cobertura

- **Forte:** requisito explícito e operacionalizado na v1.
- **Parcial:** conceito existente, mas com escopo ou artefatos incompletos.
- **Lacuna:** capacidade não tratada de forma material.

## Crosswalk

| Capacidade | Evidência nos artigos Microsoft | Cobertura na policy v1 | Avaliação | Próxima ação proposta |
| --- | --- | --- | --- | --- |
| Operating model distribuído | AI admins, identity, platform, security/compliance e RAI atuam com visão comum[1][3] | Design Authority, Run Authority, Business Owner e Technical Owner | Parcial | Expandir RACI com data owner, identity admin, platform owner, adoption lead e RAI champion |
| Control plane multiplataforma | Registry, observabilidade e ações administrativas centralizam contexto[1][2] | Catálogo, dashboard unificado e regra multiplataforma | Forte | Definir contrato de integração e campos mínimos por plataforma |
| Registry corporativo | Owner, origem, lifecycle, dados, uso e postura[1][2] | Catálogo obrigatório com owners, dados, permissões, risco, custo e status | Forte | Acrescentar attestation, destinos, conectores, runtime risk e value metrics |
| Agent blueprint | Identidade, capacidades, constraints, acesso e lifecycle[2] | Não diferenciado do registro ou documentação técnica | Lacuna | Criar template/schema de blueprint e definir relação com o catálogo |
| Identidade do agente | Identidade, acesso, provisionamento e desprovisionamento[1][2] | RBAC/ABAC, auth strength, secrets e access reviews | Parcial | Definir workload identity, owner lifecycle e transferência/desativação por vínculo |
| Dados AI-ready | Certificação, labels, data owners e automação[5] | Data classification, DLP, DPIA e data owners | Parcial | Definir critério AI-ready, quality gate de dados e connector gate por label |
| Data mesh | Ownership por domínio com controles comuns automatizados[5] | Não há modelo de produtos de dados ou federação | Lacuna | Adotar apenas se compatível com a arquitetura de dados corporativa; registrar como proposta |
| Risk matrix por capacidade | Alcance, toolchain, fontes, ações, regionalidade e criticidade[5] | Blast radius, autonomia L0–L3, users e red flags | Parcial | Expandir matriz com read/write/action/workflow, no/low/pro-code, região e reversibilidade |
| Impact assessment | Avaliação inicial de danos, grupos afetados e mitigadores[3] | Self-Assessment e AI Impact Assessment para alto risco | Parcial | Tornar escopo, triggers e evidências explícitos; evitar duplicação com DPIA |
| Release assessment | Revisão detalhada antes da liberação[3] | Publication Checklist e Approval Matrix | Parcial | Mapear checklist para security, privacy, RAI, accessibility e regional reviews |
| Responsible AI network | Office, council, champions e especialistas distribuídos[3] | AI Governance Committee e princípios RAI | Parcial | Formalizar champion, reviewer, escalation path e authority model |
| Governança embutida | Defaults, guidance e guardrails nas ferramentas[4][5] | Plataformas aprovadas e configuration standards | Parcial | Criar policy-as-code/control library e templates por plataforma |
| Adoção e change management | Adoption lead, coortes, personas, champions e liderança[4] | Awareness e treinamento anual; plano 60–90 dias | Parcial | Criar workstream de adoção, comunidade de champions e biblioteca de assets |
| Suporte em camadas | Embedded governance, IT backstop, user education e agentes de suporte[4] | Run Authority e operação/suporte | Parcial | Definir L0 self-service, L1 AI support, L2 IT backstop e L3 SME/escalation |
| MCP governance | Gateway, vetting, identity, isolation e context trimming[5] | Não citado; pode ser tratado genericamente como integração | Lacuna | Criar controle específico para MCP servers e tool provenance |
| Runtime defense | Telemetria, detecção, quarantine e remediation[1][2][5] | Logs, alerts, dashboard, quarantine, kill switch e incident flow | Forte | Testar drill de quarentena e medir time-to-remediate |
| Lifecycle individual/equipe | User lifecycle versus tenant attestation[2][5] | Owners, access review, periodic review e sunset | Parcial | Formalizar transferência/desativação por saída e attestation por equipe |
| Métricas de criação/uso/valor | Criação, descoberta, uso e valor são distintos[4][5] | KPIs de controle, performance, custos e incidentes | Parcial | Adicionar discovery, adoption, quality, business outcome e retirement decisions |
| Regionalidade | Dados e ações podem exigir tratamento diferente por região[5] | LGPD/GDPR, DPIA, residency e compliance | Parcial | Definir triggers para works councils, labor/privacy review e region-specific release |
| Enforcement automatizado | Inventory + agile policy + workflow automatizado[5] | Quarantine, deadlines e deactivation process | Parcial | Automatizar apenas após estabilizar ownership, baselines e exceções |

## Leitura consolidada

A v1 é particularmente forte em **controle operacional**:

- owners nominativos;
- autonomia e HITL;
- blast radius;
- approval matrix;
- catálogo;
- observabilidade;
- quarantine, kill switch e sunset;
- governança multiplataforma.

As principais lacunas estão menos na proteção básica e mais na evolução para um **sistema operacional em escala**:

1. dados AI-ready e connector gates;
2. blueprint distinto do registry;
3. governança proporcional por capacidade e método de construção;
4. adoption/change/support como workstreams próprios;
5. MCP e tool provenance;
6. attestation por equipe e lifecycle vinculado à identidade;
7. métricas que conectem criação, uso, qualidade e valor.

## Backlog recomendado para policy v2

### P0 — antes de escalar novos pilotos

- ampliar o catálogo com identidade, conectores, destinos, assessment, attestation e valor;
- definir matriz de risco por capacidade, alcance e reversibilidade;
- separar impact assessment de release assessment;
- criar critérios de AI-ready data;
- estabelecer controles mínimos de MCP;
- corrigir e tornar verificáveis as referências primárias da policy.

### P1 — durante os primeiros 90 dias

- criar agent blueprint e schema de catálogo;
- formalizar champion network, adoption lead e suporte em camadas;
- mapear controles da policy para plataformas e automações;
- criar métricas de discovery, adoption, quality e business outcome;
- testar lifecycle de saída do usuário e attestation de equipe.

### P2 — após evidência dos pilotos

- propor policy v2 preservando a v1;
- converter controles estáveis em policy-as-code;
- avaliar integração com um control plane corporativo;
- decidir se data mesh é aplicável à arquitetura de dados da organização;
- automatizar enforcement de baixo risco.

## Decisões que ainda exigem owner

- Qual sistema será o source of truth do catálogo?
- Quem aprova o status AI-ready de uma fonte?
- Quais capacidades exigem release assessment formal?
- Qual autoridade pode quarentenar um agente?
- Quem mantém o inventário e aprovação de MCP servers?
- Que métricas de valor têm baseline confiável?

## Limitações

- O crosswalk compara documentos, não controles implantados em produção.
- “Forte” significa cobertura documental explícita, não eficácia operacional comprovada.
- A experiência Microsoft pode não refletir regulação, estrutura ou tolerância de risco locais.
- Thresholds e exemplos da policy v1 devem ser validados antes de adoção ampla.

## Sources

1. [Implementing Agent 365][1]
2. [Deploying Microsoft Agent 365][2]
3. [Responsible AI at Microsoft][3]
4. [Becoming a Frontier Firm][4]
5. [Governing AI agents at scale][5]

[1]: https://www.microsoft.com/insidetrack/blog/implementing-agent-365-how-were-governing-and-managing-ai-agents-at-microsoft/
[2]: https://www.microsoft.com/insidetrack/blog/deploying-microsoft-agent-365-how-were-extending-our-infrastructure-to-manage-agents-at-microsoft/
[3]: https://www.microsoft.com/insidetrack/blog/responsible-ai-why-it-matters-and-how-were-infusing-it-into-our-internal-ai-projects-at-microsoft/
[4]: https://www.microsoft.com/insidetrack/blog/becoming-a-frontier-firm-a-guide-for-deploying-ai-agents-based-on-our-experience-at-microsoft/
[5]: https://www.microsoft.com/insidetrack/blog/governing-ai-agents-at-scale-lessons-from-our-journey-at-microsoft/
