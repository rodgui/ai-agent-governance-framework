# Roadmap do AI Agent Governance Framework

## Objetivo do produto

Evoluir uma fonte canônica, vendor-neutral e verificável para:

- governança organizacional de IA e agentes;
- implantação por decision gates;
- padrões e controls reutilizáveis;
- toolkit de diagnóstico, design, assurance e operação;
- futura publicação executiva quando o conteúdo estiver maduro.

O roadmap evolui a [policy de governança de agentes](docs/governance/policy.md), mas cada mudança normativa ainda exige proposta, revisão, authority, changelog e release.

## Estado atual

- fonte canônica modular e jornadas por persona;
- brief executivo, fundamentos, operating model e arquitetura;
- domínios de control e implementation playbook;
- maturity model, capability map de 15 capacidades e guias sugestivos de 90 dias/24 semanas;
- 10 design patterns e catálogo de antipatterns;
- 44 controls estruturados em 15 domínios, com verificação, automação, mappings e bloqueio declarados;
- 9 schemas, examples vinculados e toolkit humano ampliado;
- caso Microsoft separado do framework neutro;
- visual principal vendor-neutral.

## Trilha A — Qualidade canônica

### A1. Vocabulário e taxonomia

- [ ] estabilizar glossary e synonyms;
- [x] versionar lifecycle stage e operational state no Registry 2.0;
- [ ] alinhar IDs de domains, risks, controls e evidence types;
- [x] publicar regras de migration para contratos 2.0;

**Gate:** termos centrais têm definição única, owner e uso consistente.

### A2. Crosswalk de controls

- [x] mapear controls para NIST AI RMF;
- [ ] mapear controls para ISO/IEC 42001 e 23894;
- [x] mapear security controls para OWASP e MITRE ATLAS;
- [ ] separar equivalência, cobertura parcial e evidência inexistente.

**Gate:** mappings são informativos, revisados e não afirmam certificação.

### A3. Threat e failure pattern catalog

- [ ] modelar prompt injection, excessive agency, confused deputy e supply chain;
- [ ] vincular failure modes a controls e evaluations;
- [ ] criar exemplos de containment e recovery;
- [ ] versionar negative scenario packs.

**Gate:** cada threat pattern possui prevenção, detecção, resposta e evidência.

## Trilha B — Toolkit operacional

### B1. Registry e blueprint lifecycle

- [ ] definir reconciliation algorithm e source precedence;
- [ ] criar material-change diff;
- [x] validar cross-record references;
- [ ] criar attestation e sunset records estruturados.

**Gate:** um record de exemplo percorre create, change, attest e retire sem campos ambíguos.

### B2. Assessment toolkit

- [ ] formalizar risk assessment schema;
- [ ] produzir facilitation guide do maturity assessment;
- [ ] criar evidence sampling guide;
- [ ] separar self-assessment de independent assessment.

**Gate:** dois assessors conseguem produzir resultados comparáveis com as mesmas evidências.

### B3. Evaluation e release toolkit

- [ ] criar evaluation strategy template estruturado;
- [x] criar release evidence manifest;
- [ ] vincular thresholds a risk tier;
- [ ] definir regression e expiry rules.

**Gate:** decision authority consegue aprovar, condicionar ou rejeitar usando apenas o package.

### B4. Runtime governance

- [x] definir event schema vendor-neutral;
- [ ] documentar policy decision e action logs;
- [ ] criar drill scripts para quarantine, rollback e reactivation;
- [ ] modelar evidence continuity durante incident.

**Gate:** runtime signal alcança action, owner, incident record e attestation.

## Trilha C — Evidência e application mappings

### C1. Casos de estudo

- [ ] adicionar casos de outros ecossistemas e open source;
- [ ] separar source claim, observation e inference;
- [ ] registrar evidence cutoff e limitações;
- [ ] evitar ROI ou causalidade sem dados independentes.

**Gate:** nenhum fornecedor domina a arquitetura canônica.

### C2. Platform mappings

- [ ] criar template de mapping por capability;
- [ ] mapear identity, data, tools, runtime e evidence export;
- [ ] declarar gaps e compensating controls;
- [ ] adicionar portability e exit criteria.

**Gate:** mapping pode ser removido sem alterar policy, patterns ou controls.

## Trilha D — Publicação futura

Esta trilha não está no escopo da etapa atual.

Quando o conteúdo estiver maduro:

- [ ] congelar uma edição com evidence cutoff;
- [ ] revisar coesão e redundância editorial;
- [ ] definir manifesto a partir do handbook canônico;
- [ ] gerar formatos de leitura sem criar segunda fonte;
- [ ] executar revisão técnica, editorial e executiva;
- [ ] publicar errata e política de atualização.

**Gate:** conteúdo canônico está estável e a publicação é reproduzível e revisada.

## Regras de priorização

1. corrigir falha normativa ou de segurança;
2. fechar ambiguidade que afeta decisão ou evidência;
3. completar toolkit necessário para implantação;
4. ampliar mappings e casos;
5. melhorar apresentação e publicação.

## Definition of done

Uma evolução só está concluída quando possui:

- owner e status;
- rationale e boundaries;
- documentação e artifact quando aplicável;
- evidence e validation;
- links e references íntegros;
- no secrets ou dados não autorizados;
- compatibility ou migration explícita;
- reviewer independente para mudança material.
