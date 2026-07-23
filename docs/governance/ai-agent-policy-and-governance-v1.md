# AI Agent Policy and Governance — V1

**Author:** Rodrigo Garcia Guimarães  
**Date:** 2026-01-30  
**Version:** 1.0

> This document establishes the policy, processes, and controls for the creation, publication,
> and operation of AI Agents across enterprise platforms. Goal: enable innovation with security,
> compliance, and accountability.

---


## AI AGENT POLICY AND GOVERNANCE — V1
Authors: Rodrigo Garcia Guimarães
Date: 30/01/2026

## 1. Introduction and Objective
This document establishes the policy, processes, and corporate controls for the creation, publication, and operation of Artificial Intelligence Agents ("AI agents") across multiple platforms (e.g., your-agent-platform, N8N, AWS Bedrock, Foundry, Copilot Studio). The objective is to enable innovation with security, compliance, and accountability, ensuring transparency, traceability, and business value.

## 2. Scope and Principles

### 2.1 Scope
This policy applies to all AI agents created, acquired, or operated within the organization, on any approved platforms.
It covers test/PoC, staging, and production environments; includes legacy and new agents.

### 2.2 Principles (aligned with Responsible AI)
Transparency and Explainability (documentation, auditability, XAI when applicable).
Justice and Bias Mitigation.
Privacy and applicable data protection law (e.g., GDPR/LGPD) (DPO, DPIA when necessary).
Robustness, Security, and Reliability.
Human responsibility (HITL) and accountability.
Proportionality of risk and business value.

## 3. Key Definitions
AI agent: a system that performs tasks autonomously or semi-autonomously using AI/LLMs, orchestrating tools, data, and APIs.
HITL (Human-in-the-loop): a mechanism in which relevant decisions/actions of the agent require explicit human confirmation.
Blast radius: measure of the potential impact if a risk materializes (data, finance, operation, reputation).

## 4. Governance Model (Design/Run/Human Accountability)

### 4.1 Design Authority (Architecture/Governance)
Define policies, standards, architecture, approval matrix, risk criteria, and exceptions (waivers).
Ensures alignment with the AI Governance Committee and Digital Council.

### 4.2 Run Authority (Operation/Support)
Manages agent platforms, access, observability, incidents, and catalog/registry.
Ensures the implementation of controls (RBAC/ABAC, DLP, SIEM) and consumption/cost limits.

### 4.3 Human Accountability (per agent)
Business Owner: value, scope, budget (cap), risks, and periodic review.
Technical Owner: permissions, integrations, security, compliance, and agent operation.

### 4.4 Right to Create and Publish (Create vs Promote to Prod)
Creation (Test/PoC): allowed only on approved platforms and in non-production environments. Requires a completed Self-Assessment and designated Owners (Business Owner and Technical Owner) before first use. The creator must have a formally granted license and access profile (Agent Creator role), with minimum training and acceptance of the usage rules.
Publication/Promotion to Production: only after approval according to the Approval Matrix, registration in the Catalog, and completion of the Publication Checklist. Promotion to Production must be performed by an Agent Publisher profile (Run Authority or formally delegated), ensuring segregation of duties when applicable (SOX/ITGC).
Granting of accesses and permissions: requested by the Business Owner; validated by the Technical Owner; approved by the Data Owner/DPO when involving personal/sensitive data and by Cyber/ITGC when involving critical systems. Run Authority implements and maintains evidence (RBAC/ABAC, audit trails).
Access review: periodic reviews (e.g., semiannual) for agents in Production and whenever there is a change in scope, data, integrations, or level of autonomy.

### 4.5 Representation Rule in the Organizational Chart (when applicable)
AI agents are not positions (FTE) on the organizational chart; they are digital capabilities linked to a business domain, with explicit human accountability.
An agent must be indicated in the detailed organizational chart (or capabilities catalog) when it meets at least one criterion:
Use in Production with >100 users; or
Execution of a critical process (operational, financial, security, quality) or subject to SOX/ITGC; or
Official corporate channel (broad interaction with employees) or interface with external public; or
Autonomy level L2 or higher (see section 8.1).
The representation must reference: agent name, domain/area, Business Owner, Technical Owner, responsible Run Authority, and link/ID in the Catalog.

### 4.5 AI Governance Awareness
All employees authorized to create, publish, or operate AI agents must complete corporate AI Governance training before access is granted and undergo annual refresher training.
The minimum content covers: principles of responsible AI, risk assessment (blast radius), levels of autonomy and HITL, data protection (applicable data protection law (e.g., GDPR/LGPD)), security and proper use of logs and kill switch.

## 5. Do’s & Don’ts (Usage Rules)
This section establishes simple and objective rules to guide the responsible use of AI agents within the company. The goal is to reduce recurring risks (data leakage, misuse, decisions without accountability, harassment/inappropriate behavior, dependence on unreliable sources) while simultaneously accelerating adoption through clear “guardrails.” The rules apply at all levels (Group/Segment/Local) and to any approved platform, serving as a reference for self-assessment and auditing.
Suppliers and partners who develop or operate agents on behalf of the company must fully comply with this policy and its annexes.

### 5.1 Allowed
Use only data and systems with explicit authorization;
Operate with HITL at decision points;
Record agent actions in an immutable log;
Display visible identification ("Governed Agent").

### 5.2 Requires Approval
Access to personal/sensitive data (DPIA when applicable);
Integration with critical systems;
Use for decisions that impact critical KPIs (production, safety, quality, OWCR, etc.);

### 5.3 Prohibited
Agents without designated owners;
Irreversible actions without HITL;
Storing personal data outside of approved repositories;
Bypass security controls, jailbreaks, or unauthorized data usage.
Do not use platforms, models, or AI tools provided by third parties without formal platform approval and full adherence to this policy.

## 6. Self-Assessment (Mandatory)
To scale agents safely, every agent must undergo a standardized evaluation before being released, expanded, or significantly changed. This section defines the Self-Assessment as a mandatory screening and accountability recording tool, allowing teams to conduct an initial evaluation of risk, compliance, and minimum controls. The Self-Assessment also acts as an escalation trigger: when there are “red flags,” approval must follow higher levels according to the Approval Matrix.
A 1-page form must be completed before creating/publishing an agent. Minimum fields:
Objective and use cases;
Justification for the Use of AI
Data (types/sensitivity, databases, owners);
Permissions and scope of action;
Autonomy and HITL (control points);
Interconnections (systems/APIs);
AI Impact Assessment (for high risk)
Users/reach (number and profiles);
Impact on KPIs;
Risks (privacy, SOX, reputation, etc.);
Controls (audit, rate-limit, budget cap);
User Feedback Evidence (when applicable)
Owners and sunset plan.

## 7. Approval Matrix
The Approval Matrix transforms governance into fast and consistent decisions, avoiding ad hoc analyses and discrepancies between units. This section defines how the approval level is determined by objective criteria (examples: development maturity, PoC/Production environment, number of users and/or blast radius, as well as risk triggers such as SOX and sensitive data). The purpose is to balance speed and control: enabling agile pilots and ensuring rigor in higher-impact deployments.
Approval varies according to maturity and number of users. Any "red flag" (high risk, applicable data protection law (e.g., GDPR/LGPD)/SOX) immediately escalates to Production level.
For an initial scenario, a matrix based on the number of affected users is proposed, but other criteria can be added.
Whenever there is a change in the AI model, a significant change in the data used, or a relevant increase in scope/users, the agent must revert to the approval level corresponding to the new risk.

## 8. Autonomy Policy (HITL)
This section defines how the company controls the autonomy of AI agents to ensure that decisions and actions remain under human responsibility, with traceability and the ability to intervene. The goal is to enable automation safely: the agent can propose suggestions and perform tasks within defined limits, but actions with significant impact must have explicit human approval (Human-in-the-Loop) and recorded evidence. The policy also defines when exceptions may exist, what additional controls apply, and how to handle escalation and rollback.
All relevant executive actions require explicit human confirmation through the approved channel (e.g., Teams, system UI, ServiceNow).
Irreversible, high-impact actions are not allowed without HITL.
Temporary exceptions require approval according to the Matrix, with justification and a rollback plan.
Changes to the model or decision rules that affect the agent’s autonomous behavior require new security validation, minimum testing, and reassessment of the autonomy level.

### 8.1 Autonomy Levels (L0–L3) and link to the Approval Matrix
Definition of levels to standardize what 'autonomy' means and reduce ambiguity in decision-making. Regardless of the level, any red flag (personal/sensitive data, critical systems, SOX/ITGC, high blast radius) escalates to the Production path and may require additional controls.

## 9. Risk Assessment (Blast Radius)
AI agents differ from traditional applications because they can access multiple data sources, trigger tools, and operate at scale (users, systems, and volume). This section establishes a standardized method to assess an agent's "blast radius" before its release and during changes, considering: data accessed, privileges, output channels, action capability, and number of users. The assessment result guides the approval level, minimum controls, and applicable monitoring/cost regime.

### 9.1 Evaluation Dimensions
Probability = f(Permissions, Autonomy, Interconnectivity, Authentication Strength).
Impact = data/privacy, financial, operational, reputation (domain-dependent).

### 9.2 Classification and decision
Low/Medium/High with direct linkage to the Approval Matrix;
High → escalation, DPIA (if involving personal data), and additional controls.

## 10. Consumption and Costs (Cap/Alerts)
Each agent in production (≥10 users) must have a budget (cap) defined by the business owner, with alerts and re-approval when thresholds are exceeded.
Monitor consumption (e.g., tokens, calls, GPU minutes) and monthly cost; block in case of abuse/anomaly.

## 11. Agent Catalog/Registry and KPIs
Without visibility, there is no governance. This section defines the Corporate Catalog as the “single source of truth” for agents in use in the company, ensuring traceability of owners, purpose, data, permissions, integrations, autonomy level, costs/consumption, and lifecycle status. Beyond the registry, this section establishes the minimum KPIs to monitor adoption, risk, and efficiency (e.g., catalog coverage, agents without an owner, HITL compliance, incidents, spend, usage by domain). The Catalog also enables auditing, duplication control, and execution of the sunset plan.
Model changes require catalog update and new validation before use in production.

### 11.1 Minimum fields of the catalog/record
ID, Name, Business Owner, Technical Owner, Objective/Use Cases, Data and Owners, Permissions/Systems, Defined HITL, Number of Users, Environment, Risk, AI Model Version, Date of Last Model Validation, Source and Type of Data Used, DPIA (yes/no), Cap/alerts, Next Review, Status (pilot/prod/sunset).

### 11.2 Governance KPIs
% agents with owners; % with DPIA when applicable; % with HITL tested; deviations/month; spend vs cap; review SLA; incidents by severity.

### 11.3 Compliance and Enforcement (Catalog, Owners, Logs)
Minimum conditions for Production: agent registered in the Catalog, Owners defined, logs/audit enabled, HITL configured according to the autonomy level, cap/alerts configured, and approvals evidenced.
Non-conformity in Production:
Quarantine: Run Authority can immediately suspend the agent (kill-switch) when there is high risk, data leakage, policy violation, or consumption anomaly.
Regularization: for non-critical cases, the agent enters operational quarantine within up to 5 business days and must be regularized (catalog/owners/logs/cap) within up to 30 calendar days.
Deactivation: if not regularized within the deadline, the agent is deactivated and reported to the Business Owner, Technical Owner, and Design Authority.
Non-compliance in Test/PoC: allowed only in non-production environments and for a limited time (e.g., 30 days). After this period, it requires minimum regularization (Self-Assessment + Owners + registration) or deactivation.
Audit: periodic reviews (e.g., monthly for production) to identify agents without registration/owners, logging gaps, excessive consumption, and scope deviations.

### 11.3 Agent Performance Metrics
Each agent in production must have minimum technical metrics defined by the Technical Owner (e.g., accuracy rate, response time, error rate, or user satisfaction), monitored continuously.

## 12. Life Cycle and MLOps for Agents
Agents require continuous governance: it is not enough to simply "create and publish." This section defines the corporate lifecycle of the agent, from ideation and PoC to production, operation, changes, and deactivation (sunset), and the MLOps/AgentOps controls required to maintain quality, security, and compliance over time. The focus is to ensure repeatability, traceability (versions, prompts, tools, data), observability, and change management without disrupting the business.
Case Selection/Prioritization (value, feasibility, risk).
Development and testing (including fairness/robustness when applicable).
Deployment with CI/CD, versioning, and rollback.
Performance monitoring and drift; action auditing.
Automatic mechanisms for monitoring the quality and stability of the agent must be configured.
Alerts should be generated in case of performance degradation, abnormal increase in errors, or unexpected behavior.
Periodic reviews of prompt injection tests, attempts at data exfiltration, and bypassing autonomy controls, with recording of results.
Creation and review of sunset plan*.
* Sunset:
No Business Owner or Technical Owner defined
Out of Stock
Without logs/minimal telemetry
No use for N days (e.g., 90)
Agent duplicated/replaced by official version
Platform is no longer approved
Serious incident without correction within the deadline

## 13. Security, Data, and Compliance (applicable data protection law (e.g., GDPR/LGPD)/SOX)
Agents may process personal data, sensitive data, and confidential information, as well as interact with systems subject to internal control requirements (SOX/ITGC). This section consolidates the minimum security, privacy, and compliance requirements applicable to agents, including access governance, segregation of duties, leakage prevention (DLP/egress), secrets management, log retention, and DPIA requirements when applicable. The goal is to reduce legal, financial, and reputational risk without hindering innovation.
Access controls (RBAC/ABAC), segregation of duties, and least privileges.
Encryption in transit and at rest; DLP; SIEM; vulnerability management.
applicable data protection law (e.g., GDPR/LGPD): principles, processing record, DPIA, data subject rights, DPO.
SOX/ITGC: audit trails, formal approvals, segregation for critical actions.
Models and data used by agents must be evaluated for bias, quality, and suitability for the intended use before publication and whenever they are updated.

## 14. Multi-Platform Rule
The agent ecosystem evolves rapidly, and the company may operate on more than one cloud or platform. This section defines the principle of platform-agnostic governance: corporate rules are the same, but the company only allows agents on platforms that support minimum controls (identity, logs, consumption/cost telemetry, data security, blocking/quarantine capability). The goal is to preserve technological flexibility with governability — reducing lock-in without sacrificing security, compliance, and visibility.
Governance is platform-agnostic.
Approved platforms must expose minimum telemetry (catalog, logs, consumption) and support the controls of this policy.
Preference for visibility integration (e.g., your-agent-platform as a source) without exclusivity.
Suppliers and external platforms may only be used if they contractually agree to adhere to the requirements of this policy (exportable logs, kill switch, traceability, access controls, and data retention).

### 14.1 Platform Approval Process (Onboarding/Offboarding)
Request: a Sponsor (IT or Business) submits a request to the Design Authority with a description of the platform, expected use cases, involved data, regions, and cost model.
Technical assessment (Run Authority + Cyber): minimum requirements for IAM/SSO, RBAC/ABAC, exportable logs/audit, consumption/cost telemetry, egress controls, secrets/keys management, encryption, and kill-switch capability.
Risk and compliance assessment (Compliance/DPO/ITGC): applicable data protection law (e.g., GDPR/LGPD)/DPIA when applicable, SOX/ITGC requirements, contractual terms, data retention and residency.
Controlled pilot: enable in sandbox with integration to the Catalog and logs/consumption pipeline; validate controls and evidence.
Decision:
classify the platform as:
(a) Approved for Production,
(b) Restricted to Pilots, or
(c) Not Approved.
Record decision and justification.
Operationalization: publish configuration standards (guardrails), access profiles (Creator/Publisher/Operator), and continuous telemetry integration.
Revalidation and Offboarding: periodic review (e.g., annual) and discontinuation/migration process with a transition window and rollback plan.

## 15. RACI (Roles and Responsibilities)
Agents create new types of responsibility: it is not enough for "IT to approve" or "business to request." This section defines clear roles and responsibilities (RACI) to ensure consistent decision-making, secure operation, and human accountability by agent, separating policy design functions (Design Authority), operation and technical controls (Run Authority), and nominative responsibility (Business Owner and Technical Owner). The goal is to avoid gaps ("no one owns it"), conflicts ("two areas decide differently"), and segregation risks (SOX/ITGC), making governance executable at any level of the organization.
Design Authority: Responsible/Accountable for policies and standards; Consulted for segments; Informed by Run.
Run Authority: Responsible for operation and observability; Accountable for incidents; Consulted for Design; Informed for owners.
Business Owner (by agent): Accountable for value/risk/budget; Responsible for requirements; Consulted for compliance; Informed for Run; Review the agent's value and risk quarterly and decide on continuity, adjustment, or sunset.
Technical Owner (by agent): Responsible for integrations and security; Accountable for permissions; Responsible for quarterly review of technical performance, security, logs, and access controls.
Legend
R = Responsible (executes the activity)
A = Accountable (owns the decision and outcome)
C = Consulted (provides input)
I = Informed (kept informed)
Notes
Cells show A / R where the context indicated both accountability and responsibility.
Business Owner
leads value/risk decisions and requirements; Technical Owner leads technical integrations, security, permissions, and technical reviews; Run Authority leads operations and incident response; Design Authority defines policies and is consulted on segments and design.

## 16. Processes and Flows (High Level)
For governance to be adoptable at scale (Group/Segments/Locations), processes must be simple, repeatable, and auditable. This section presents the high-level flows that connect the annexes and artifacts (Self-Assessment, Publication Checklist, Catalog, and Approval Matrix), defining inputs, responsible parties, and decision points. The goal is to standardize “how” agents are created, assessed, approved, published, monitored, and closed, ensuring clarity of roles and consistency across platforms and regions.

### 16.2 Creation
Creation flow → approval → publication → operation → review/sunset:
1) Proponent fills out Self-Assessment → 2) Risk assessment (blast radius) → 3) Approval via Matrix (local/segment/group) → 4) Registration in the Catalog → 5) Publication with HITL, cap, and logs → 6) Monitoring and KPIs → 7) Periodic review and sunset.

### 16.2 AI Incidents
Isolate or disable the agent (kill switch or quarantine)
Notify Business Owner, Technical Owner, and Run Authority
Register incident and evidence in the catalog
Perform root cause analysis and correction plan
Revalidate controls before reactivating

## 17. Monitoring and Observability
Observability is a mandatory corporate requirement for all AI agents in Production and is directly linked to the principles of transparency, human accountability, and risk management established in this policy. Its purpose is to ensure safe, auditable operation aligned with Responsible AI practices and the controls defined in the Self-Assessment, Publication Checklist, Catalog, and the periodic review process.

### 17.1 Principles
Complete operational visibility over actions, consumption, accessed data, and agent behavior.
Risk proportionality, following the blast radius classification and autonomy level defined in the policy.
Traceability and auditability, with immutable logs, proper retention, and evidence available for internal audits.
Integration with human accountability, ensuring the ability to intervene via HITL, quarantine, or kill-switch as established.
Continuous compliance, with early signs of operational, behavioral, or financial deviation that may trigger review, correction, or sunset.

### 17.2 Minimum Requirements
All agents in Production must have, at a minimum:
Logs enabled, including executed actions, triggered integrations, and operational errors (required in the Publication Checklist).
Consumption telemetry, including tokens/calls/cost and cap alerts defined in the Self-Assessment and in the policy (cap/thresholds).
Monitoring of permissions and accessed data, as declared in the Self-Assessment (types of data, bases, and owners).
Risk alerts for critical incidents, inappropriate behavior, or policy violations, which may trigger incident or sunset procedures as defined in the policy.
Integration with the Catalog, recording risk, consumption, status, owners, and operational compliance evidence.

### 17.3 Unified Governance Dashboard
Run Authority will maintain a Corporate Dashboard consolidating data from approved platforms and the Catalog (single source of truth) as defined in the policy and annexes.
The dashboard must display, at a minimum:
Total number of agents, by status (Test, Production, Sunset).
Creators and Owners, as registered in the Self-Assessment and Catalog.
Databases and types of data accessed, with indication of the respective Data Owners.
Consumption / Token Spending, comparing actual value vs. defined cap (including 70% and 90% alerts).
Identified risks, including blast radius, sensitive/personal data, autonomy, and critical integrations.
Inappropriate behavior alerts, including HITL violations, unsafe responses, or recorded incidents.

### 17.4 Responsibilities
Run Authority: dashboard operation, telemetry collection, alert maintenance, incident analysis, and Catalog update.
Technical Owner: ensure that the agent provides the necessary logs and metrics for observability.
Business Owner: periodically review usage and KPIs, acting on deviations or decisions regarding continuity.
Data Owner / DPO / Compliance / Cyber: monitor alerts related to privacy, security, integrity, and compliance.

### 17.5 Integration with Life Cycle
Observability data must feed the Operation, Incident Management, Change Management, and Periodic Review processes described in this policy, including influencing sunset decisions when there are persistent deviations, inactivity, or high risk.

## 17. Suggested Action Plan
0–30 days: Do’s & Don’ts + Self-Assessment + Approval Matrix + HITL Policy + Minimum Catalog; initial alignment with stakeholders.
30–60 days: Complete agent policy; audit and observability playbook; pilots in 1–2 segments; review by the Digital Council (1 week).
60–90 days: Corporate publication; training; progressive adoption (require Self-Assessment for new agents and migration of legacy ones to the catalog).

## 18. Attachments (Templates)
Annex A — Self-Assessment Template (1 page)
Objective/Use cases; Data (sensitivity/owners); Permissions; HITL (decision points); Interconnections; Users; Impact on KPIs; Risks; Controls; Owners; Sunset.
Annex B — Publication Checklist
Owners defined; HITL implemented; Logs enabled; Cap and alerts configured; Registration in the Catalog; DPIA (if applicable); Rollback plan.
Annex C — Agent Registry/Catalog Template
Minimum fields according to section 11.1 (ID, owner names, data/permissions, risk, cap, etc.).
Annex D – Sunset Plan
Objective: to avoid "zombies" (agents without owners, duplicates, unused) and reduce risk/cost.

## 19. Sources
NIST AI RMF (AI Risk Management Framework)
NIST AI 100-1 — “Artificial Intelligence Risk Management Framework (AI RMF 1.0)” (source)
Roadmap of AI RMF 1.0 (complementary activities, evolution, and operationalization). (source)
AI RMF “Generative AI Profile” (NIST AI 600-1) (source)
Crosswalks of AI RMF 1.0 (mappings to other standards/controls). source 1 and source 2
ISO/IEC 42001 (AIMS — AI Management System)
Primary sources (ISO):
ISO/IEC 42001:2023 — “Information technology — Artificial intelligence Management system”
Complementary ISO sources:
ISO/IEC 23894:2023 — “Guidance on risk management”
ISO/IEC 22989:2022 — “AI concepts and terminology” (source)
Microsoft Responsible AI (Principles + Responsible AI Standard)
Microsoft Responsible AI — Principles and approach – (source)
Microsoft Responsible AI Standard v2 — General Requirements (PDF) – (source)
Microsoft Learn — Service Assurance: Artificial Intelligence overview – (source)
Microsoft Learn — _Responsible Generative AI Development on Windows – (source)

---

*Templates: [`templates/`](../../templates/)*
