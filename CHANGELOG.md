# Changelog

Todas as alterações relevantes neste repositório são registradas aqui.

## [Unreleased]

Terceira auditoria do corpus contra o guia externo v3.4, executada sobre a release 1.1.0. Sete achados; nenhum deles havia sido fechado pela 1.1.0.

### Added

- Catálogo de artefatos do programa em `docs/reference/artifact-catalog.md`, com propósito, owner típico e fase de cada artefato — o instrumento de planejamento e controle de completude que o corpus descrevia e não entregava.
- Tabela normativa dos dez escaladores de risco, com criticidade mínima, efeito adicional e a pergunta correspondente do pre-screen.
- Colunas "quando evoluir para assessment formal" e "efeito na aprovação" no tiering de assurance de Responsible AI.
- Três níveis de leitura de um domínio (entender, decidir, executar) no handbook, e entrada por estágio da organização no índice.
- Termos que o corpus passou a usar e o glossário não definia, com destaque para `admissibilidade` — dimensão criada pela ADR-0009 e até aqui sem definição canônica.
- Casos de referência em `docs/explanations/cases/`, percorrendo os gates G0–G7 num agente só. O primeiro caso, T2, expôs três divergências que a leitura por domínio não expunha — entre elas um release registrado como `condition` em prosa e como `approved` no manifesto legível por máquina.
- Método de mapeamento de capability para tecnologia, separado da arquitetura para que trocar de produto não exija reescrever a arquitetura.
- Template de Agent Use-Case Portfolio, o registro que faltava para as decisões de portfólio que o domínio de valor já descrevia.
- Checklist de autossuficiência, com a autoavaliação declarada deste repositório contra ele — dois critérios abertos e um parcial.

### Changed

- O evidence pack de T2 declara herança de T1, como T3 e T4 já faziam.
- As invariantes cross-record operam sobre bundles de caso em vez de caminhos fixos, e casos em `examples/cases/<id>/` entram na validação de schema pela mesma convenção. Sem isso, um segundo caso ficaria no repositório com aparência de evidência e sem verificação.
- Release Evidence Manifest ganha `conditions` e `expiresAt`. Uma decisão `conditional` passa a exigir as duas, em vez de exigir `exceptionRefs`: pelo glossário do próprio framework, exceção autoriza desvio de requisito e condição limita o escopo aprovado. Exigir waiver para toda aprovação condicional empurra a organização a registrar exceção falsa — e exceção falsa contamina justamente a métrica que deveria detectar acúmulo de risco.
- Developer experience e paved road, atributos de qualidade e riscos arquiteturais entram na ordem editorial do handbook e na navegação do site. Eram conteúdo real inalcançável a partir de qualquer entrada do repositório.
- `docs/index.md` ganha navegação por pasta, ligando os índices de seção que existiam sem nenhum caminho de entrada.
- Os marcadores de tempo do sunset plan passam de `T0`/`T+15`/`T+30` para `D0`/`D+15`/`D+30`, eliminando a colisão com o rótulo de tier que a taxonomia canônica rejeita.

### Deprecated

### Removed

### Fixed

- O evidence pack de T1 exigia menos do que o Minimum Production Bar do mesmo tier: faltavam blueprint reduzido, referências de dados e tools, padrão de identidade aprovado, testes funcionais, rollback e aprovação de owner. O gate exigia controles cuja existência ninguém precisava demonstrar.
- A lista normativa de red flags tinha oito itens em prosa; o guia define dez. Os dois ausentes eram os de criticidade T4.
- Identidade, Responsible AI e operating model rotulavam tier como `baixo/moderado/alto/crítico`, anteriores à taxonomia canônica. `validate_tier_labels` passa a reprovar rótulo em prosa na primeira coluna de tabela.

### Security

## [1.1.0] — 2026-08-10

Correção editorial e contratual após revisão independente do guia v3.4 contra o corpus. Esta release fortalece o repositório como framework de referência; não declara adoção organizacional, certificação ou eficácia em estate real.

### Added

- Agent Registry 2.0 com discovery status/confidence, lifecycle stage, operational state e transition history.
- Agent Blueprint 2.0 com model version/evaluation binding e referências a catálogos de models, sources e tools.
- Schemas e exemplos vendor-neutral para Model/Provider Catalog, Certified Source Catalog, Enterprise Tool Registry, Release Evidence Manifest e Audit Event.
- `AGF-RSK-004` para admissibilidade e exceções temporárias; Control Catalog conteúdo 1.2.0.
- Templates de Capability Assessment, Agent Risk Record, Behavioral Analytics Use Case, Governance RACI, Attestation/Sunset e Release Evidence Manifest.
- Capability map de 15 capacidades com crosswalk para as dez dimensões de maturity e os quinze domínios de controls.
- Guia de migração dos contratos estruturados para 2.0.
- Site de documentação gerado a partir do corpus canônico, com navegação pela ordem do handbook, busca e Mermaid renderizado.
- `references/standards/` com escopo de cada norma ISO referenciada e o motivo de não haver mapeamento control a control.
- Capability map atual versus alvo, com procedimento e perguntas de challenge.
- Decisão arquitetural "agente é o mecanismo certo?", com árvore de decisão e exemplos.
- Template de intake de caso de uso, orientado a problema e não a tecnologia.
- Método de execução do maturity assessment: preparação, evidence request list, workshop de scoring, dependências quebradas e definition of done.
- Workstreams, prioridade de backlog e cadência no programa sugestivo de 24 semanas; ciclo trimestral de melhoria contínua e critérios de reassessment.
- Exemplo preenchido de governance charter e scope statement.

### Changed

- Risk tier T1–T4 representa criticidade; admissibilidade usa `permitted`, `conditional`, `restricted` e `prohibited` como dimensão independente ([ADR-0009](docs/architecture/decisions/0009-risk-tier-and-admissibility.md)).
- Control Catalog usa schema 2.0, com `automation` e `frameworkMappings` obrigatórios; `catalogVersion` permanece independente ([ADR-0010](docs/architecture/decisions/0010-structured-governance-contracts-2.0.md)).
- Roadmaps de 90 dias/24 semanas e piloto são guidance adaptável; G0–G7 permanecem os únicos decision gates canônicos.
- Build do site permanece quality gate; publicação é opcional e manual, sem prerequisite de GitHub Pages ([ADR-0008](docs/architecture/decisions/0008-manual-documentation-site-publication.md)).
- Lifecycle, registry, model governance, data, tools, auditability e templates agora usam os mesmos contratos estruturados.

### Fixed

- Eliminada a semântica concorrente que tratava T4 simultaneamente como criticidade e default deny.
- Eliminada a incompatibilidade entre a state machine documentada e o Agent Registry.
- Breaking change do Control Catalog deixa de ser apresentado como schema minor.
- Validator verifica bindings de catálogo, coerência de tier/admissibilidade, release manifest, audit event e hash dos artefatos.
- O validador do repositório deixa de inspecionar artefatos de build (`site/`, `site_src/`).

### Security

- Production rejeita admissibilidade `prohibited`; `restricted` exige exception reference e expiry.
- Model/source/tool bindings e artifact hashes passam a ser verificáveis nos exemplos canônicos.

## [1.0.0] — 2026-08-10

Primeira release adotada do framework modular ([ADR-0006](docs/architecture/decisions/0006-framework-release-1-0-adoption.md)). Adoção da release é decisão de versionamento deste repositório; a adoção organizacional continua sendo decisão separada de cada organização.

**Lacunas conhecidas e declaradas nesta release:** ISO/IEC 42001, 23894 e 42005 não estão mapeadas control a control; a distribuição de controls por domínio reflete origem editorial e não risco observado; o corpus tem um único owner e aprovador; nenhum control foi exercitado contra um estate real.

### Added

- Control catalog 1.1 com `scope`, `verification` e `blocking` obrigatórios, cinco controls novos de model governance e lifecycle, e `frameworkMappings` populado em todos os 43 controls ([ADR-0005](docs/architecture/decisions/0005-control-catalog-scope-verification-and-mappings.md)).
- Playbooks de implantação em dez domínios canônicos.
- Domínios de registry, lifecycle e model governance, com descoberta contínua e forecast do estate.
- Minimum Production Bar e evidence pack proporcionais por tier.
- Behavioral analytics, FinOps com unit economics e modelo de KPI/KRI dashboard.
- Programa de implantação em 24 semanas mapeado aos decision gates, plano de piloto e risk pre-screen.
- Seis exemplos preenchidos e templates de terms of reference de fórum e dicionário de taxonomia.
- Princípios arquiteturais com pergunta de decisão, aplicação e antipattern por princípio.

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
