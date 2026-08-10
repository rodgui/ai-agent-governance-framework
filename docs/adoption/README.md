---
title: Adoção, enablement e suporte
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../value/README.md
  - ../operations/README.md
  - ../governance/operating-model.md
  - ../guides/framework-implementation-playbook.md
---

# Adoção, enablement e suporte

## Objetivo

Preparar builders, usuários, líderes e suporte para criar, descobrir, usar e operar capacidades de IA com segurança e efetividade.

Adoção não é comunicação de lançamento. É a capacidade organizacional de usar o sistema de forma correta, obter suporte, reportar falhas e incorporar feedback ao governance lifecycle.

## Personas

| Persona | Necessidade |
|---|---|
| sponsor | value, risco, decisões e accountability |
| business owner | outcome, usuários, limites e attestation |
| maker/engineer | paved road, controls, templates e feedback rápido |
| end user | intended use, limitações, suporte e contestação |
| administrator | policy, inventory, access e remediation |
| support | triage, known issues, escalation e communication |
| domain authority | evidências relevantes e decision rights |
| auditor | acesso independente a records e rationale |

## Discovery e catalog

Um catálogo útil permite:

- encontrar capacidades aprovadas por tarefa e persona;
- distinguir status, owner, versão e tier;
- entender intended/prohibited use;
- acessar support e feedback;
- evitar duplicação;
- ocultar ou bloquear itens em quarantine/sunset;
- medir discovery separado de criação.

Publicar sem discovery gera agentes invisíveis; discovery sem lifecycle promove itens inadequados.

## Paved road para builders

- starter templates com identity, logging e policy hooks;
- schemas e self-assessment proporcionais;
- approved models, data connectors e tools;
- automated checks com feedback acionável;
- sandbox e test datasets;
- design clinic e office hours;
- exception process com owner e expiry;
- documentação de examples e failure modes.

O paved road deve ser mais simples que contornar a governança.

A sequência que o builder percorre nesse caminho — do registro do caso de uso à retirada — está em [developer experience e paved road](../devex/README.md), com os building blocks e as métricas de fricção correspondentes.

## Suporte em camadas

1. **Self-service:** documentação, status, FAQ e runbooks.
2. **AI-assisted:** busca e triage com handoff rastreável.
3. **Platform/IT backstop:** incidentes, acesso e operação.
4. **Domain SME:** security, privacy, RAI, legal, data ou negócio.
5. **Authority escalation:** containment, risk acceptance e policy decision.

## Change e comunicação

Mudanças materiais comunicam:

- o que mudou e por quê;
- quem é afetado;
- novos limites ou ações;
- data de vigência;
- treinamento ou suporte necessário;
- rollback/contingency;
- canal de feedback e owner.

## Feedback loop

```mermaid
flowchart LR
    U[Uso] --> F[Feedback/sinal]
    F --> T[Triage]
    T --> B[Backlog]
    B --> D[Decisão]
    D --> C[Change]
    C --> E[Evaluate]
    E --> U
```

Feedback é evidência contextual, não prova isolada de valor ou segurança.

## Playbook de implantação

Governança só escala quando cada papel consegue executá-la sem depender do time central para cada decisão. Adoção transforma regra em competência prática, suporte e hábito.

1. **Segmentar personas.** Citizen builder, desenvolvedor profissional, business owner, technical owner, reviewer, administrador de plataforma, operação de segurança, data owner, sponsor e usuário final. Cada persona tem objetivo de aprendizagem distinto.
2. **Separar awareness de competência.** Awareness ensina a reconhecer a regra e pedir ajuda; competência exige executar a atividade e demonstrar resultado. **Não habilite um reviewer de impact assessment porque ele concluiu um treinamento introdutório.**
3. **Montar currículo por papel e risco.** Builders precisam de registry, risco, dados, ferramentas, identidade e telemetria; owners precisam de accountability, valor e attestation; reviewers precisam de critérios e evidência; segurança precisa de contenção e forensics. Com laboratórios e casos calibrados.
4. **Implantar rede de champions.** Escolher áreas por volume e risco, definir tempo alocado e **limite de autoridade**. O champion orienta a primeira linha e escala; não substitui as funções de controle nem aprova localmente o que exige authority.
5. **Tornar o caminho governado o mais fácil.** Builders aprovados, templates, catálogos de fontes e ferramentas, office hours, policy gates self-service e exemplos. **Fricção desnecessária é o principal produtor de shadow AI.**
6. **Calibrar reviewers com casos comuns.** Os mesmos 10 a 20 casos aplicados por reviewers diferentes. Divergência vira discussão de critério, não preferência individual. Versionar os exemplos quando o standard mudar.
7. **Criar suporte e comunidade de prática.** Office hours, FAQ, canais de escalation e encontros regulares reduzem retrabalho. Perguntas recorrentes viram melhoria de documentação e automação.
8. **Medir eficácia, não conclusão.** Taxa de conclusão de treinamento é métrica fraca isolada. Medir verificação de conhecimento, retrabalho de review, violações de policy, tickets de suporte, tempo até assessment, qualidade da evidência e padrões de shadow AI — e ajustar o currículo com esses sinais.

## Evidências

- persona e stakeholder map;
- adoption/support plan;
- catalog entry e discovery analytics;
- learning assets;
- support model e escalation;
- training/competence records;
- feedback backlog e decisões;
- change communication;
- user research e accessibility findings.

## Métricas

- discovery-to-use conversion;
- active/recurring users por persona;
- duplicate creation;
- support demand e resolution time;
- training completion e task competence;
- misuse/incorrect-use reports;
- feedback-to-decision time;
- adoption com qualidade e outcome, não apenas login.

## Failure modes

- medir sucesso por agentes criados;
- publicar sem owner ou suporte;
- treinamento único para todos;
- champion network sem authority ou tempo;
- usar feedback positivo como prova de ROI;
- esconder limitation para aumentar adoção;
- ignorar resistência como “falta de cultura”;
- manter itens em discovery durante quarantine.

## Decision gate

Release para audiência ampla exige catalog entry, intended use, limitations, support owner, escalation, communication e feedback channel.
