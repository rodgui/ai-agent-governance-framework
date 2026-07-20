# AI Agent Publication Checklist (V1)

Complete before go-live. Attach evidence (links to docs, logs, approvals) for each item.

---

Appendix B — AI Agent Publication Checklist (V1)
Use this checklist before go-live. Check off each completed item and attach evidence (links to documentation, logs, and approvals).
1) Identification and Scope
Agent ID / Name: _________________________________
Platform / Environment (Dev/UAT/Prod): ______________
Business Unit/Segment: _____________________________________
Business Owner: _____________________________________
Technical Owner: ________________________________________
No. of users (1–10 / 10–100 / >100): _____________________
Risk: Likelihood ____  Impact ____  Rating ____
DPIA (Yes/No/In review): _____________________________
2) Owners and Governance
☐ Owners (business and technical) defined and communicated
☐ RACI published (Design/Run/Human Accountability)
☐ Approval recorded per Matrix (Local / Segment / Digital Council)
☐ HITL defined (decision points with documented human confirmation)
3) Data and Privacy
☐ Databases and respective data owners identified
☐ Data classification (personal/sensitive/confidential) recorded
☐ DPIA completed or formally waived by the DPO (when applicable)
☐ Legal basis (applicable data protection law (e.g., GDPR/LGPD)) defined and recorded
4) Security and Permissions
☐ Least-privilege permissions (RBAC/ABAC) applied and reviewed
☐ Segregation of duties (SOX/ITGC) met for critical actions
☐ Secrets/credentials stored securely (e.g., Key Vault)
☐ Encryption in transit and at rest validated
☐ DLP policies active for sensitive data
5) Observability and Audit
☐ Immutable logs enabled (agent actions and integrations)
☐ Audit trail available for verification (retention per policy)
☐ Monitoring dashboard (errors, latency, consumption) published
☐ Anomaly/error alerts defined and tested
6) Usage and Costs
☐ Monthly cap (R$ or tokens) defined
☐ Alerts configured for 70% and 90% of the cap
☐ Blocking/quarantine mechanism in case of abuse or drift
☐ Budget owner assigned
7) Quality and Testing
☐ Test cases approved (functional and integration)
☐ HITL test executed (decision points verified)
☐ Regression test (when applicable)
☐ UAT (user acceptance testing) completed and recorded
8) Documentation and Repositories
☐ Functional and technical documentation published
☐ Runbook and ROLLBACK PLAN documented and tested
☐ Agent registered in the Catalog with all required minimum fields
☐ Repository/versioning set up (code, IaC, pipelines)
9) Go-live and Post Go-live
☐ Deployment window defined and communicated
☐ Communication plan to users/stakeholders
☐ Rollback tested and reversion window defined
☐ T+7 / T+30 / T+90 reviews scheduled on the calendar
10) Final Approvals
Business Owner — Signature/Date: __________________________
Technical Owner — Signature/Date: _____________________________
Local Compliance/IT — Signature/Date: ________________________
Segment Approval — Signature/Date: ________________________
Digital Council Approval — Signature/Date: __________________
