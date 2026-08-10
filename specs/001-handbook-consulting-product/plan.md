---
title: Plano de implementação do handbook e produto de consultoria
status: approved
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: major-change
supersedes: null
related:
  - spec.md
  - tasks.md
  - validation.md
---

# Plano de implementação

## Estratégia

Evoluir a branch existente em quatro commits coerentes e verificáveis, mantendo a Policy v1 intacta.

## Commit 1 — Arquitetura editorial e núcleo

- registrar ADR e spec;
- reposicionar README e índice;
- criar handbook e jornadas de leitura;
- preencher fundamentos, operating model e domínios de controle;
- ampliar glossário e referências.

## Commit 2 — Método, patterns e toolkit

- substituir orientação centrada em piloto por playbook de implantação;
- criar maturity model;
- criar catálogo de patterns e antipatterns;
- criar control catalog;
- criar schemas, templates e exemplos;
- documentar modelo de consultoria.

## Commit 3 — Visual e prontidão editorial

- separar visual neutro e caso Microsoft;
- atualizar renderer e links;
- manter a ordem linear do handbook;
- registrar a publicação executiva como evolução futura, sem gerar formatos agora.

## Commit 4 — Quality gates e revisão

- criar validador de links, schemas e outputs visuais;
- adicionar workflow de CI;
- executar lint, render e validações;
- revisar diff e confirmar Policy v1;
- atualizar PR com escopo, outputs e evidências.

## Arquitetura da informação

```text
README — proposta de valor e mapa
  docs/index — jornadas por persona e objetivo
    handbook — ordem editorial e critérios de leitura
      fundamentos
      policy e operating model
      arquitetura e domínios de controle
      método de implantação
      patterns e toolkit
      estudos de caso e mappings
      aplicação em consultoria
```

## Modelo de implantação

O método usa oito decision gates:

0. mandato, escopo e sponsorship;
1. diagnóstico e baseline;
2. fundações de dados, identidade e ownership;
3. operating model e decision rights;
4. controles mínimos e assurance;
5. onboarding por tier de risco;
6. operação, observabilidade e resposta;
7. revisão de valor, attestation e melhoria contínua.

Um piloto pode existir em uma organização, mas não é pressuposto, entregável nem etapa obrigatória deste trabalho.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Conteúdo duplicado | Documentos modulares canônicos e handbook apenas como ordem editorial |
| Vendor lock-in conceitual | Core neutro; mappings separados |
| Policy v1 alterada acidentalmente | Comparação de blob antes do push |
| Densidade excessiva | Jornadas por persona e resumos por domínio |
| Claims comerciais frágeis | Linguagem de hipótese, limites e critérios de aceite |
| Artefatos inválidos | Schemas e exemplos testados por script/CI |
| Publicação futura divergente | Derivação a partir do handbook canônico, sem segunda fonte manual |
| PR grande demais | Commits por camada e checklist de validação |
