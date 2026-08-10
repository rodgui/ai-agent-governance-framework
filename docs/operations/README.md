---
title: Operações, observabilidade, resposta e lifecycle
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../auditability/README.md
  - ../security/README.md
  - ../evaluations/README.md
  - ../patterns/runtime-observability-and-quarantine.md
---

# Operações, observabilidade, resposta e lifecycle

## Objetivo

Operar agentes como sistemas dinâmicos: observar comportamento e efeitos, decidir, conter, remediar, revalidar e aposentar com responsabilidade definida.

## Run readiness

Antes do release, deve existir:

- Run Authority e technical owner;
- SLOs e error budgets adequados;
- telemetry e dashboards orientados a decisão;
- policy thresholds e alerts;
- incident severity matrix;
- runbooks de containment, rollback e reactivation;
- support model e escalation;
- change e attestation cadence;
- sunset e retention plan.

## Observability model

| Camada | Sinais |
|---|---|
| experiência | task success, user feedback, correction e abandonment |
| modelo | quality, safety, drift, refusal e uncertainty |
| retrieval/data | source, freshness, authorization e leakage |
| agent | plan depth, retries, loops e delegation |
| tool | allow/deny, latency, side effect, failure e cost |
| identity | authn/authz, scope e anomalies |
| business | outcome, error, control impact e value |
| governance | exception, finding, attestation e lifecycle status |

Dashboards precisam de owner, threshold e action; caso contrário são visualização, não governança.

Três leituras derivam deste modelo e têm documento próprio:

- [behavioral analytics](behavioral-analytics.md) — quando o comportamento muda em relação ao normal do agente;
- [FinOps e unit economics](finops.md) — quanto custa por resultado e onde está o desperdício;
- [KPIs, KRIs e governance dashboard](kpi-kri-dashboard.md) — o que vai a um fórum e com qual ação associada.

## Incident lifecycle

```mermaid
flowchart LR
    S[Signal] --> T[Triage]
    T --> C[Contain]
    C --> P[Preserve evidence]
    P --> A[Assess blast radius]
    A --> R[Remediate]
    R --> V[Validate regression]
    V --> D{Reauthorize?}
    D -->|sim| O[Reactivate]
    D -->|não| X[Sunset]
    O --> L[Learn/update controls]
    X --> L
```

## Containment ladder

1. negar operação específica;
2. reduzir scope ou rate;
3. bloquear tool/connector;
4. revogar identidade/token;
5. quarentenar agent/version;
6. rollback para versão conhecida;
7. desativar serviço ou integração;
8. executar sunset.

Escolha o menor blast radius que controla o risco; escale quando incerteza ou impacto exigirem.

## Quarantine

Quarantine deve:

- impedir novas ações relevantes;
- preservar logs e evidence;
- indicar status no registry;
- comunicar owners e suporte;
- evitar reativação automática;
- exigir cause, remediation e regression evidence;
- registrar authority e timestamps.

## Change management

Material changes reabrem gates proporcionais:

- model/provider;
- prompt/policy relevante;
- tool, MCP server ou permission;
- connector, dataset ou region;
- autonomy/capability;
- target population ou exposure;
- support/oversight mode;
- dependency com efeito de security ou reliability.

Mudanças emergenciais seguem break-glass e revisão posterior.

## Attestation

Periodic attestation confirma:

- owners válidos;
- finalidade e usuários atuais;
- risk tier e controls;
- identidade, dados e tools;
- evidence e exceptions;
- qualidade e incidents;
- uso e value evidence;
- necessidade de manter, corrigir, restringir ou aposentar.

Frequência aumenta com risco; evento material pode antecipar.

## Sunset

Sunset inclui:

- stop de novas utilizações;
- comunicação e alternativa;
- revogação de identidade, tokens, tools e connectors;
- tratamento de memória, indexes e records;
- retenção de evidência;
- remoção de discovery/catalog ativo;
- encerramento de contratos/custos quando aplicável;
- verificação de órfãos e dependências downstream.

## Playbook de implantação

Observabilidade completa não é um dashboard único. É um **modelo de correlação** que permite responder perguntas de estate, runtime, segurança, comportamento, custo e valor sem reconstruir manualmente a história de cada agente.

1. **Definir o schema canônico de telemetria.** `agent_id`, versão, tarefa e sessão, usuário ou gatilho, modelo e provedor, ferramenta, ação, alvo, resultado da policy, tokens e custo, latência, erro e outcome. Os campos podem vir de produtos diferentes; **precisam ser correlacionáveis**.
2. **Medir estate e lifecycle.** Total conhecido versus estimado, novos agentes, mix de tiers, sem owner, dormentes, attestation vencida e candidatos a retirada. Responde "o que existe e está higienizado?".
3. **Definir SLI e SLO de runtime por classe.** Taxa de sucesso, latência, retries, falhas de ferramenta, profundidade de loop e timeout são interpretados conforme o caso — um agente em lote aceita latência que um assistente interativo não aceita.
4. **Integrar telemetria de segurança.** Anomalias de autenticação e permissão, perda de dados, ataques via prompt ou ferramenta, destinos inesperados, ações de alto impacto e negações de policy. **Segurança não pode trabalhar com uma cópia desconectada do `agent_id`.**
5. **Implantar [behavioral analytics](behavioral-analytics.md) em monitor-only.** Dois ou três casos com baseline claro, comparando cada agente com o próprio histórico e com o peer group, combinando regra determinística e desvio, medindo falso positivo antes de automatizar resposta.
6. **Fazer [FinOps](finops.md) por tarefa e por resultado.** Distribuir custo de modelo, ferramenta, armazenamento e egress por agente e tarefa. Comparar custo por caso bem-sucedido, não gasto de tokens. Budget e threshold de anomalia por perfil de uso.
7. **Conectar uso a valor de negócio.** Usuários ativos mostram frequência; valor exige outcome — cycle time, qualidade, esforço evitado, receita, custo ou redução de incidente. **Um agente popular pode não gerar valor.**
8. **Construir dashboards por decisão.** Executivo precisa de estate, risco e valor; segurança precisa de comportamento e incidentes; plataforma precisa de runtime e custo; owner precisa de adoção, outcome e attestation. Um painel único serve a ninguém.
9. **Definir alert-to-action e tuning.** Toda regra crítica tem owner, severidade, threshold contextualizado e ação: observar, abrir ticket, throttle, exigir step-up ou colocar em quarentena. Revisar baselines após mudança material e drift.

## Evidências

- run readiness checklist;
- dashboards com owner/threshold/action;
- alerts e incident records;
- containment/rollback drills;
- change approvals;
- attestation;
- support tickets e user feedback;
- value review;
- sunset completion.

## Métricas

- mean time to detect, decide, contain e recover;
- incidents por severity e recurrence;
- failed actions, loops e retries;
- policy denials e anomalous tool chains;
- agents com expired attestation;
- orphaned identity/tool/data access;
- change sem reauthorization;
- quarantine/reactivation outcomes;
- inactive agents ainda gerando custo.

## Failure modes

- monitorar somente uptime;
- alert sem owner ou runbook;
- quarantine que não revoga tool access;
- reativar antes de regression test;
- alterar prompt em produção sem version;
- attestation como assinatura sem evidência;
- manter agent sem uso por medo de sunset;
- encerrar UI e deixar integrações ativas.

## Decision gate

Produção exige Run Authority, observability, containment, rollback, incident process, support e sunset verificáveis.
