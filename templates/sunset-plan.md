# Sunset Plan — Controlled Agent Decommissioning

Use when an agent is flagged for decommissioning.

---

Appendix D – Sunset Plan (controlled agent decommissioning)
Objective: avoid “zombies” (agents without an owner, duplicates, unused) and reduce risk/cost.
When an agent enters Sunset
No Business Owner or Technical Owner defined
Not in the Catalog
No minimum logs/telemetry
No usage for N days (e.g., 90)
Duplicate agent / replaced by an official version
Platform is no longer approved
Severe incident not remediated within the deadline
Standard process (3 phases)
Warning (D0): agent marked as a “Sunset Candidate”
Notifies owners + Run Authority
Defines a remediation deadline (e.g., 15 days)
Quarantine (D+15): limitations
Disables write actions, reduces scope, limits users
Keeps logs and evidence
Deactivate (D+30): deactivation
Removes access, disables integrations, revokes identity
Records the reason and artifacts in the Catalog
(Optional) archives configurations for X days for rollback
Mandatory items in Sunset
Sunset start date, reason, responsible owner
Migration plan (if there is a replacement)
Evidence of communication to users
Log retention after deactivation (per risk)
