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
---

# Minimum Production Bar por tier

## Objetivo

Transformar policy em gate objetivo. O Minimum Production Bar (MPB) é o conjunto mínimo de condições que precisam ser verdadeiras para um agente **entrar e permanecer** em produção.

O MPB define o **piso, não o teto**. Controles adicionais disparados por risco, impacto ou obrigação continuam se aplicando por cima dele.

## Como ler a tabela

- T1 inclui a rota automatizada do [fast path](README.md#fast-path-de-t1): os itens continuam obrigatórios, mas são verificados por policy em vez de revisão manual.
- **T4 não é um tier de produção mais rigoroso.** É a categoria de uso restrito ou proibido. A coluna T4 deve ser lida como *default deny + controles de exceção*, não como rota normal de go-live. Ela aparece na tabela para preservar rastreabilidade: mesmo uma rejeição precisa de registro auditável.

## Baseline por tier

| Controle | T1 | T2 | T3 | T4 (default deny) |
|---|---|---|---|---|
| registro e descoberta | obrigatório, automatizável | obrigatório completo | obrigatório + delegado | registro obrigatório mesmo quando rejeitado |
| ownership | owner atribuído | business + technical | business + technical + delegado | sponsor executivo + owners accountable |
| classificação de risco | pre-screen registrado | tier record formal | tier formal + escaladores + reassessment | uso restrito + registro de exceção e authority |
| identidade | padrão aprovado | identidade própria do agente | identidade própria + policy reforçada e step-up | identidade isolada, controles máximos, se a avaliação for permitida |
| dados | classes aprovadas e conhecidas | classificados + fonte certificada ou condicional | constraints explícitas + evidência | tratamento restrito explícito; nenhuma transferência não aprovada |
| tools | catálogo/allowlist, sem alto impacto | registradas + autorização com escopo | mediadas + controles de alto impacto | apenas ferramentas mediadas sob exceção |
| logging e telemetria | padrão, campos mínimos chegando ao pipeline | completa com correlação | completa + baseline de comportamento | telemetria forense completa |
| testes | funcionais | segurança e evals | adversariais + resiliência | adversariais completos + específicos da exceção |
| impact assessment | por trigger | por trigger | obrigatório e aprofundado | obrigatório se a exceção for sequer considerada |
| rollback e kill switch | documentado | testável | testado + runbook de quarentena | contenção testada antes de qualquer teste da exceção |
| evidência | pacote leve, recuperável | evidence pack do tier | evidence pack reforçado | dossiê de exceção com evidência para a authority |
| attestation | periódica | periódica | frequente ou orientada a evento | expiry da exceção e revisão frequente |

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
- ler a coluna T4 como rota de produção;
- automatizar o check antes de o dado de origem ser confiável.

## Decision gate

Nenhum agente entra em produção sem o MPB do seu tier satisfeito e evidenciado. Nenhum agente permanece em produção com item de MPB reprovado sem exceção registrada, compensating control e expiry.
