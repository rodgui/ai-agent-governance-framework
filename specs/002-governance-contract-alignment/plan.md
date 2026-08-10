---
title: Plano de alinhamento dos contratos de governança
status: approved
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
related:
  - spec.md
  - tasks.md
  - validation.md
---

# Plano de implementação

## Estratégia

Executar uma correção editorial e contratual em ondas pequenas. Schemas e validator recebem testes RED antes da implementação; documentação e templates são ajustados depois que os contratos estabilizam. O site continua buildável, mas sua publicação permanece manual e fora do escopo.

## Onda 1 — Decisões e testes de contrato

- registrar spec aprovada;
- criar testes que exijam Registry/Blueprint/Control Catalog 2.0;
- verificar falha pelos gaps conhecidos;
- documentar ADRs de supersession.

## Onda 2 — Contratos estruturados

- evoluir Agent Registry e Agent Blueprint para schema 2.0;
- separar risk tier de admissibility;
- adicionar model/source/tool catalog bindings;
- criar schemas e exemplos de catálogos, audit event e release manifest;
- atualizar validador e invariantes cruzadas;
- publicar guia de migração.

## Onda 3 — Corpus e toolkit

- alinhar risk, lifecycle, registry, model, data e tool governance;
- tornar cronogramas e piloto explicitamente sugestivos;
- expandir capability map para 15 capabilities com crosswalk;
- criar templates humanos priorizados;
- atualizar README, handbook, schemas/examples indexes, ROADMAP e changelog.

## Onda 4 — Release e revisão

- executar validações locais completas;
- revisar diff contra spec e ADRs;
- abrir PR e acompanhar CI;
- após merge, criar tags/releases imutáveis 1.0.0 e 1.1.0;
- não configurar GitHub Pages.

## Riscos e mitigação

| Risco | Mitigação |
| --- | --- |
| transformar documentação em produto de software | schemas apenas como contratos de referência; templates humanos permanecem first-class |
| quebra sem migração | major versions e guia de mapeamento explícito |
| taxonomias concorrentes | uma dimensão para risk tier e outra para admissibility |
| excesso de campos obrigatórios | exigir somente o que sustenta decisão, evidence e rastreabilidade |
| ADR reescrita | supersession explícita e índice atualizado |
| cronograma interpretado como policy | callouts claros de pattern sugestivo e equivalência de evidência |
