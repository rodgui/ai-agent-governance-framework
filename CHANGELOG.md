# Changelog

Todas as alterações relevantes neste repositório são registradas aqui.

## [Unreleased]

### Added

- ADR-0003 establishing this repository as the single canonical source and absorbing the external scale guide as historical origin.
- ADR-0004 fixing T1–T4 as the canonical risk-tier taxonomy and defining the T1 fast path for high-volume, low-risk agents.
- Registry domain covering enterprise agent taxonomy, minimum registry capabilities and quality rules that generate findings.
- Continuous estate discovery and forecast guidance with confidence grading and a manual bottleneck register.
- Lifecycle domain with state machine, transition matrix, material-change triggers, attestation, dormancy calibration and owner joiner/mover/leaver handling.
- Model and provider governance domain covering approved combinations, version-bound evaluations, fallback control equivalence and exit strategy.
- Minimum Production Bar per tier and proportional evidence packs per tier.
- Behavioral analytics, agent FinOps with unit economics, and a consolidated KPI/KRI dashboard model.
- 24-week implementation program mapped to the existing decision gates, plus a pilot plan with expansion criteria.
- Risk pre-screen template with explicit reading rules for escalators and impact triggers.
- Canonical modular policy entry point and explicit normative boundaries.
- Separate personal consulting product with three packages and nine delivery modules.
- ADR-0002 for policy evolution, strict vendor neutrality and commercial separation.
- Microsoft Customer Zero case study based on five Inside Track articles.
- Crosswalk between the Microsoft operating model and Policy v1.
- Five-plane reference architecture and end-to-end lifecycle diagrams.
- 90-day implementation plan with workstreams, gates and exit criteria.
- Executive brief for leadership decision-making.
- Reproducible 1800 × 2400 governance infographic and Pillow renderer.
- Source register entries and bibliography for the Microsoft series.

### Changed

- Release disposition in the publication checklist now uses the four decision-gate states; `expired` is a decision lifecycle state rather than a disposition.
- Handbook chapters renumbered to 1–32 and the architecture overview now maps canonical domains to the five planes.
- Source register extended with ISO/IEC 42005:2025, the OWASP Top 10 for Agentic Applications, the OWASP MCP Top 10 and the CSA AI Controls Matrix.
- The Policy v1 is now preserved as historical origin rather than used as the current normative source.
- Vendor material is optional evidence or mapping and never a required framework component.
- README, handbook, documentation index and roadmaps now separate canonical knowledge from commercial packaging.
- Control records no longer carry thematic `policyRefs` to the historical Policy v1.

### Deprecated

### Removed

### Fixed

- Repository validation now enforces the canonical tier taxonomy across the three tier enums and every control record.
- Repository validation now rejects extra commercial offers and case-insensitive vendor references outside allowed mapping areas.
- Malformed schema examples now produce actionable findings instead of uncaught validator exceptions.
- Schema-invalid records are excluded from secondary invariant and guardrail checks after their schema findings are recorded.
- Control catalogs must declare `lastReviewed`, and negative tests preserve duplicate-ID enforcement.
- Canonical self-assessment and release templates now use the modular policy instead of historical Policy v1 labels and assumptions.

### Security

## [[previous version(s)]]
