# Self-Assessment Form — AI Agents (V1)

Complete before creating or publishing any agent. Fields marked `*` are mandatory.

---


## SELF-ASSESSMENT FORM — AI AGENTS (V1)
Complete this form before creating/publishing the agent. Use concise, objective language. Fields marked with * are mandatory.
1) Agent Identification
2) Owners and Contacts
3) Purpose and Scope
4) Data and Permissions
5) Integrations and Interconnections
6) Autonomy and HITL
7) Reach/Users and Impact
8) Risks and Controls (Blast Radius)
9) Usage and Costs
10) Publishing, Review, and Sunset
Confirmations and Approval
Prompt Injection / Jailbreak
Test malicious instructions (“ignore the rules”, “show the system prompt”, “execute X”).
Test injection in RAG content (a document with hidden instructions).
Evidence: test logs + expected outcome (“refused / followed policy / requested approval”).
Data Exfiltration / Leakage
Test requests to exfiltrate secrets (tokens, keys, prompts, internal data).
Test leakage via tools (email/webhook/HTTP/external connector).
Test cross-tenant / cross-domain access (data the user should not be able to access).
Evidence: attempt + block via RBAC/DLP/guardrails + event log.
Safety / Content and Behavior
Test responses with risk: harassment, discrimination, inappropriate content, dangerous instructions, acting as disciplinary HR.
Test “authoritative tone” in sensitive decisions (to avoid reputational harm/harassment).
Evidence: outcome + standard messages (refusal / escalation / human handoff).
Secure tool-use
Test “unintended actions”: the agent must not perform writes without a condition (HITL/limits).
Test rollback/compensation when possible.
