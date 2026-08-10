---
title: Lifecycle, mudança material, attestation e retirement
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - ../registry/README.md
  - ../identity/README.md
  - ../operations/README.md
  - ../patterns/lifecycle-attestation-and-sunset.md
  - ../guides/framework-implementation-playbook.md
---

# Lifecycle, mudança material, attestation e retirement

## Objetivo

Governar o agente ao longo do tempo, não apenas no momento do deploy. Sem lifecycle explícito, o estate acumula agentes publicados que mantêm permissões, identidades, conectores e custo depois de perder owner, finalidade ou evidência válida.

O resultado esperado: **qualquer agente em produção possui estado conhecido, owner válido, próxima attestation, regras de mudança material e um caminho testado para suspensão, quarentena e retirada.**

## Duas unidades distintas

| Unidade | O que é | O que carrega |
|---|---|---|
| **agent asset** | o ativo estável, com `agent_id` permanente | identidade, ownership, histórico, finalidade |
| **version/release** | a versão publicada em um ambiente | configuração, evidências, approval, expiry |

Confundir as duas produz o erro mais comum do domínio: aprovar uma versão e tratar a aprovação como permanente para o ativo.

## Etapa da jornada não é estado de lifecycle

**Etapa** descreve o trabalho em andamento (ideia, design, build, avaliação, operação). **Estado** é a condição machine-readable usada por workflow, IAM e automação. Uma etapa pode conter mais de um estado, e o estado precisa refletir consequência operacional — não atividade de projeto.

| Etapa | O que produz | Gate para avançar |
|---|---|---|
| ideia | intake, hipótese de valor, decisão `agent` vs `workflow` determinístico | problema e owner inicial claros |
| registro | `agent_id`, owners, ambiente, finalidade, status inicial | nenhum build compartilhado ou produção sem ID e owner |
| classificação | tier, escaladores, red flags, impact trigger screen | tier e triggers válidos; T4 segue exceção explícita |
| design | blueprint, identidade, dados, tools, modelo, oversight, telemetria, failure behavior | design atende ao baseline do tier; gaps têm owner |
| build | configuração versionada, integrações, bindings de observabilidade | build reproduz o blueprint; secrets e permissões dentro da policy |
| avaliação | evals funcionais, abuse cases, testes de dados/tools, resiliência, rollback | findings bloqueadores fechados ou aceitos pela authority correta |
| review e aprovação | domain reviews acionadas, MPB, evidence pack, risk acceptance | Publication Gate `approve` ou `condition` registrado |
| publicação | deploy, health checks, políticas e budget ativos, baseline de runtime | containment e rollback disponíveis antes da exposição |
| operação | telemetria, incidentes, mudanças, custo, valor | sinais podem acionar reassessment ou contenção |
| attestation e mudança | revalidação de owner, necessidade e acessos; classificação de mudanças | continuar, remediar, suspender ou reaprovar |
| suspensão ou quarentena | limitação administrativa ou contenção de risco | reativação exige causa, correção e regression evidence |
| retirada | revogação de acessos, encerramento de custo, arquivamento de evidência | o ativo não retorna sem novo ciclo completo |

Gate não significa reunião. Em T1, vários gates podem ser policy-driven. O que importa é que a condição de avanço seja objetiva, verificável e registrada.

## State machine

Estados mínimos que **mudam permissões ou tratamento operacional**:

`draft` · `under-review` · `approved` · `production` · `suspended` · `quarantine` · `retirement-review` · `retired`

Regras estruturais:

- `draft` não vai diretamente a `production`;
- `quarantine` não retorna a `production` sem correção, reteste e aprovação;
- cada transição registra evento disparador, authority, evidência e ações automáticas;
- a state machine é versionada e o histórico é preservado — a auditoria precisa saber em que estado o agente estava no momento de um evento.

### Matriz de transição

| Estado atual | Evento | Próximo estado | Authority | Ações automáticas |
|---|---|---|---|---|
| `draft` | solicitação de publicação | `under-review` | workflow | congelar versão do blueprint; executar pre-screen |
| `under-review` | evidências e gates completos | `approved` | authority de publicação do tier | emitir approval record com expiry |
| `approved` | deploy concluído e health check OK | `production` | plataforma | ativar policy de runtime, telemetria e budget |
| `production` | sinal crítico de segurança ou comportamento | `quarantine` | Run Authority | desabilitar tools/identidade conforme runbook; preservar evidência |
| `production` | dormancy threshold atingido | `retirement-review` | serviço de lifecycle | notificar owner; iniciar grace period |
| `production` | mudança material declarada | `under-review` | Design Authority | reabrir apenas as etapas afetadas |
| `retirement-review` | owner confirma desuso | `retired` | owner + plataforma | remover acessos e secrets; arquivar evidência |

### Suspensão, quarentena e retirada são ações diferentes

Um único botão "disable" para os três casos destrói a rastreabilidade.

| Ação | Motivo | Evidência preservada | Reversível |
|---|---|---|---|
| `suspended` | administrativo ou planejado | configuração e histórico | sim, por decisão do owner |
| `quarantine` | risco ou incidente | evidência forense preservada deliberadamente | somente com causa, correção e regression evidence |
| `retired` | fim de vida | arquivada conforme retenção | não — exige novo ciclo completo |

## Mudança material

Mudança material é a que pode alterar risco, impacto ou comportamento e, por isso, reabre avaliação. Cada trigger aponta para o ponto do processo que precisa ser reexecutado — o reassessment recomeça do ponto afetado, **não do zero**.

| Trigger | O que reabrir |
|---|---|
| passagem de leitura para escrita, ou classe de ação mais crítica | classificação, controls, testes de rollback |
| nova fonte de dados de classificação superior | data review, impact screen, controls de acesso |
| novo provider, modelo ou região com data handling diferente | [governança de modelos](../model-governance/README.md), regression evals |
| aumento de autonomia, profundidade de cadeia ou delegação entre agentes | classificação, threat model, oversight |
| novo público externo ou ampliação relevante de alcance | classificação, transparência, impact assessment |
| mudança de owner ou de processo crítico | ownership, authority, attestation |
| alteração ou remoção de etapa de aprovação humana | oversight design, classificação |
| nova ferramenta com escrita ou privilégio | tool review, identidade, containment |

Defina a lista corporativa **antes** de automatizar qualquer reassessment. Automatizar um gatilho mal definido gera ruído e treina a organização a ignorá-lo.

## Attestation

Revalidação periódica de owner, necessidade, acesso e controles — não uma assinatura ritual.

- cadência proporcional ao tier, no máximo anual;
- o owner confirma que o agente continua necessário, que os acessos continuam adequados e que a finalidade não mudou;
- attestation vencida é um estado, não um aviso: aciona grace period e depois suspensão;
- attestation não substitui reassessment após mudança material.

## Dormancy

Dormancy threshold é **gatilho de revisão, não regra cega de exclusão**. Um agente financeiro trimestral pode ficar 80 dias sem execução e continuar legítimo; um agente de service desk sem uso por 30 dias provavelmente foi abandonado.

Valores iniciais sugeridos, a calibrar com evidência:

| Tier | Threshold inicial | Grace period |
|---|---|---|
| T1 | 120 dias | 30 dias |
| T2 | 90 dias | 21 dias |
| T3 | 60 dias | 14 dias |
| T4 | 30 dias | 7 dias, com revisão da exceção vigente |

Procedimento de calibração:

1. segmentar por frequência esperada e tier;
2. definir threshold inicial e grace period;
3. rodar 60–90 dias em **report-only**;
4. analisar falsos positivos e sazonalidade;
5. ajustar e só então automatizar a cadeia notificação → attestation → suspensão → retirada;
6. manter exceções sazonais com data de expiração.

## Joiner, Mover e Leaver aplicado a agentes

A identidade de um agente não pode permanecer silenciosamente vinculada a alguém que mudou de função ou saiu.

- **Joiner:** ao assumir, o novo owner tem role, competência e authority validadas antes da transferência de accountability.
- **Mover:** mudança de área do owner dispara revisão de ownership, centro de custo e permissões. Se a nova função não puder responder pelo agente, reatribua.
- **Leaver:** antes do desligamento, consulte o registry por ownership, nomeie delegado temporário e suspenda os casos sem sucessor conforme o tier.
- Em nenhum caso apague o histórico de ownership — a timeline é evidência de auditoria.

## Playbook de implantação

1. Definir o objeto governado (`agent asset` vs `version`) e quem opera o lifecycle.
2. Desenhar estados a partir de consequências operacionais, não de atividades de projeto.
3. Transformar cada transição em gate auditável com evento, authority, evidência, SLA e automação.
4. Definir a lista de mudanças materiais **antes** de automatizar reassessment.
5. Calibrar attestation e dormancy pelo padrão real de uso, em report-only primeiro.
6. Integrar JML de owners ao registry, com consulta reversa por ownership.
7. Implementar suspensão, quarentena e retirada como ações distintas.
8. Pilotar manualmente em 10–20 agentes — incluindo ao menos um T3, um leaver, uma mudança material e um incidente simulado — antes de virar policy-as-code.

## Artefatos

- Agent Lifecycle Standard: estados, transições, triggers, roles, timers, JML, quarentena, retirada e retenção;
- matriz de transição e runbook operacional;
- registro de attestation e de mudanças materiais;
- [plano de sunset](../../templates/sunset-plan.md).

## Evidências

- estado atual e histórico de transições por agente e versão;
- approval record com authority, condições e expiry;
- attestation records e vencimentos;
- classificação de mudanças materiais e reassessments derivados;
- evidência de contenção e de reativação;
- registro de retirada com remoção de acessos e arquivamento.

## Métricas

- agentes em produção sem attestation válida;
- agentes sem owner ou com owner desligado;
- mudanças materiais detectadas por auditoria em vez de declaradas pelo owner;
- tempo entre trigger e reassessment concluído;
- agentes dormentes por tier e desfecho após grace period;
- transições executadas fora da matriz autorizada;
- tempo entre decisão de retirada e revogação efetiva de acesso;
- reativações após quarentena sem regression evidence.

## Failure modes

- state machine documentada que não altera permissão, evidência ou comportamento real;
- tratar aprovação de versão como aprovação permanente do ativo;
- usar um único "disable" para suspensão, quarentena e retirada;
- automatizar dormancy antes de calibrar sazonalidade;
- reassessment que recomeça do zero e, por custo, deixa de ser executado;
- retirada que remove o agente do catálogo mas não revoga identidade e secrets;
- histórico de ownership sobrescrito em vez de versionado.

## Decision gate

Nenhum agente permanece em produção sem estado válido na state machine, owner ativo, attestation dentro do prazo do tier e caminho de contenção e retirada exercitado. Mudança material sem reassessment registrado é motivo de suspensão, não de exceção informal.
