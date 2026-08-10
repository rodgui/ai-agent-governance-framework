---
title: ADR-0010 — Contratos estruturados de governança 2.0
status: accepted
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: 0005-control-catalog-scope-verification-and-mappings.md
related:
  - 0005-control-catalog-scope-verification-and-mappings.md
  - 0009-risk-tier-and-admissibility.md
  - ../../../schemas/README.md
  - ../../guides/schema-migration-2.0.md
  - ../../../specs/002-governance-contract-alignment/spec.md
---

# ADR-0010 — Contratos estruturados de governança 2.0

## Contexto

A ADR-0005 melhorou materialmente o Control Catalog, mas marcou como schema 1.1 uma mudança que tornou obrigatórios `scope`, `verification` e `blocking`. Catálogos 1.0 não validam sem migração: semanticamente, trata-se de major version.

A absorção do guia v3.4 também criou obrigações que permaneceram apenas em Markdown: lifecycle e operational state separados, discovery status, model version e evaluation binding, certified sources, enterprise tools, release evidence e audit events.

O repositório é documentação e governança, não um produto de execução. Ainda assim, exemplos estruturados são necessários para que organizações adaptem o framework sem reinventar o contrato básico.

## Decisão

1. Manter `catalogVersion` como versão independente do conteúdo do catálogo.
2. Publicar o contrato atual do Control Catalog como **schema 2.0**; o catálogo de controls evolui para 1.2.0 com um control explícito de admissibilidade.
3. Tornar `automation` e `frameworkMappings` campos obrigatórios. Um array de mappings vazio declara ausência deliberada; não autoriza referência inventada.
4. Publicar Agent Registry 2.0 com:
   - discovery status separado de confidence;
   - stage separado de operational state;
   - transition history com authority e evidence;
   - risk tier separado de admissibility.
5. Publicar Agent Blueprint 2.0 com bindings obrigatórios para model version/catalog/evaluation, certified source catalog e enterprise tool registry.
6. Adicionar contratos de referência 1.0 para:
   - Approved Model and Provider Catalog;
   - Certified Source Catalog;
   - Enterprise Tool Registry;
   - Release Evidence Manifest;
   - AI Agent Audit Event.
7. Verificar exemplos e referências cruzadas no repository validator.
8. Publicar guia de migração. Migração não pode inferir authority, evidence, admissibility ou versão ausentes; esses campos ficam pendentes para decisão humana.
9. Preservar templates humanos como interface principal para workshops e decisões; JSON schemas são contratos de interoperabilidade e exemplos, não workflow obrigatório.

## Consequências

### Positivas

- documentação e exemplos estruturados passam a dizer a mesma coisa;
- breaking changes ficam honestamente versionadas;
- organizações ganham artefatos reutilizáveis sem adotar plataforma específica;
- referências cruzadas tornam model, source, tool e evidence lineage verificáveis.

### Negativas

- exemplos 1.x precisam de migração;
- o validator e a suíte de testes ficam maiores;
- mais contratos exigem owner e revisão editorial contínua.

## Compatibilidade

| Contrato | Antes | Depois | Compatibilidade |
| --- | --- | --- | --- |
| Agent Registry | 1.0 | 2.0 | breaking |
| Agent Blueprint | 1.0 | 2.0 | breaking |
| Control Catalog schema | 1.1 declarado | 2.0 | correção de major version |
| Control Catalog conteúdo | 1.1 | 1.2.0 | aditivo; `AGF-RSK-004` governa admissibilidade |
| novos catálogos/eventos | inexistente | 1.0 | aditivo |

## Critérios de validação

- schemas Draft 2020-12 são válidos;
- todos os exemplos validam;
- bindings desconhecidos falham em cross-record validation;
- catálogo anterior requer migração explícita;
- IDs de controls permanecem estáveis;
- nenhuma referência normativa externa é inventada.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10 após revisão independente do DOCX v3.4 e aprovação explícita das correções contratuais.
