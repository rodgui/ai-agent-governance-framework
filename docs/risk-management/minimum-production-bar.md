---
title: Minimum Production Bar por tier
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - ../auditability/evidence-pack-by-tier.md
  - ../guides/framework-implementation-playbook.md
  - ../../controls/README.md
  - ../../templates/publication-checklist.md
  - ../architecture/decisions/0009-risk-tier-and-admissibility.md
---

# Minimum Production Bar por tier

## Objetivo

Transformar policy em gate objetivo. O Minimum Production Bar (MPB) é o conjunto mínimo de condições que precisam ser verdadeiras para um agente **entrar e permanecer** em produção.

O MPB define o **piso, não o teto**. Controles adicionais disparados por risco, impacto ou obrigação continuam se aplicando por cima dele.

## Como ler a tabela

- T1 inclui a rota automatizada do [fast path](README.md#fast-path-de-t1): os itens continuam obrigatórios, mas são verificados por policy em vez de revisão manual.
- T4 é o tier de risco crítico. `restricted` e `prohibited` pertencem à dimensão separada de admissibilidade; não são sinônimos de T4.
- Leia primeiro a baseline de risco e depois o gate de admissibilidade. As duas condições precisam ser satisfeitas.

## Baseline por tier

| Controle | T1 | T2 | T3 | T4 crítico |
|---|---|---|---|---|
| registro e descoberta | obrigatório, automatizável | obrigatório completo | obrigatório + delegado | obrigatório + owner/sponsor e dependências críticas reconciliadas |
| ownership | owner atribuído | business + technical | business + technical + delegado | sponsor executivo + owners accountable + Run Authority |
| classificação de risco | pre-screen registrado | tier record formal | tier formal + escaladores + reassessment | tier e cenários críticos revisados pela authority competente |
| identidade | padrão aprovado | identidade própria do agente | identidade própria + policy reforçada e step-up | identidade isolada, privilégio mínimo e dual control onde aplicável |
| dados | classes aprovadas e conhecidas | classificados + fonte certificada ou condicional | constraints explícitas + evidência | constraints críticas, lineage e containment demonstrados |
| tools | catálogo/allowlist, sem alto impacto | registradas + autorização com escopo | mediadas + controles de alto impacto | mediadas, segregadas e sujeitas a dual control quando irreversíveis |
| logging e telemetria | padrão, campos mínimos chegando ao pipeline | completa com correlação | completa + baseline de comportamento | telemetria forense completa |
| testes | funcionais | segurança e evals | adversariais + resiliência | adversariais, resilience e failure containment completos |
| impact assessment | por trigger | por trigger | obrigatório e aprofundado | obrigatório e aprovado pela authority compatível |
| rollback e kill switch | documentado | testável | testado + runbook de quarentena | containment, fail-safe e recuperação exercitados |
| evidência | pacote leve, recuperável | evidence pack do tier | evidence pack reforçado | evidence pack crítico com challenge e segregation demonstrados |
| attestation | periódica | periódica | frequente ou orientada a evento | frequente, orientada a evento e com executive review |

## Gate de admissibilidade

| Admissibilidade | Condição para produção |
| --- | --- |
| `permitted` | MPB do tier satisfeito e evidence pack aprovado |
| `conditional` | MPB satisfeito, condições testáveis, owner, prazo e monitoramento registrados |
| `restricted` | MPB satisfeito **e** exception record com authority, rationale, compensating controls e expiry |
| `prohibited` | produção não é permitida; preservar registro da decisão e evidências |

Admissibilidade não reduz o MPB. Uma exceção de uso `restricted` autoriza avaliar a publicação sob condições; não dispensa controls do tier.

## Como operacionalizar

1. **Converta cada item em teste objetivo ou evidência recuperável.** "Logging habilitado" precisa significar campos mínimos presentes e chegando ao pipeline — não uma caixa marcada.
2. Associe cada controle a um source of truth e a um owner nomeado.
3. Automatize as verificações onde o dado é confiável: owner, tier, identidade, telemetria, attestation.
4. Mantenha exceções explícitas, com compensating controls e expiry.
5. Execute o MPB **duas vezes**: como gate pré-produção e como verificação contínua em runtime. Um agente pode deixar de atender ao MPB depois de uma mudança.
6. Meça os motivos de falha. Os mais frequentes indicam onde melhorar templates de plataforma e enablement — não onde apertar o processo.

## Relação com o Publication Gate

O MPB é a **entrada** do gate de release (G5), não o gate inteiro. O gate verifica evidência já produzida; ele não reexecuta reviews.

Um agente T2 passa quando: registry, owner e tier estão válidos; a identidade própria foi provisionada; as fontes de dados constam no catálogo certificado; as ferramentas estão registradas com escopo; o rollback foi testado; a telemetria chega ao pipeline; existe budget; e o evidence pack contém as reviews que foram acionadas.

O gate **não** pede que segurança "reavalie tudo". Ele verifica que a evidência exigida pelo tier existe, é recuperável e foi aceita pela authority correta — conforme o [contrato comum dos decision gates](../guides/framework-implementation-playbook.md#contrato-comum-dos-decision-gates).

## Artefatos

- Minimum Production Bar Standard: controle, aplicabilidade por tier, evidência, automático ou manual, owner, condição de falha e rota de exceção;
- [checklist de decisão de release](../../templates/publication-checklist.md);
- [evidence pack por tier](../auditability/evidence-pack-by-tier.md).

## Evidências

- resultado do MPB por agente e versão, com data e método de verificação;
- checks automatizados versus verificações manuais, declarados;
- exceções abertas com compensating control e expiry;
- histórico de falhas do MPB e causas.

## Métricas

- agentes em produção que deixaram de atender ao MPB após mudança;
- itens do MPB verificados automaticamente versus manualmente;
- motivos de falha mais frequentes por tier;
- tempo entre falha de MPB em runtime e remediação;
- exceções de MPB vencidas.

## Failure modes

- MPB como checklist declaratório, sem teste objetivo por trás;
- verificar o MPB apenas antes do go-live e nunca mais;
- tratar exceção de MPB como aprovação silenciosa e sem prazo;
- confundir o piso com o teto e parar de aplicar controles por risco;
- tratar T4 como sinônimo automático de `restricted` ou `prohibited`;
- automatizar o check antes de o dado de origem ser confiável.

## Decision gate

Nenhum agente entra em produção sem o MPB do seu tier satisfeito e evidenciado **e** admissibilidade diferente de `prohibited`. Nenhum agente permanece em produção com item de MPB reprovado sem exceção registrada, compensating control e expiry; usos `restricted` exigem também exception authority e validade próprias.
