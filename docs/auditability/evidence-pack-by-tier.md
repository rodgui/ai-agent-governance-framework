---
title: Evidence pack proporcional por tier
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - ../risk-management/minimum-production-bar.md
  - ../patterns/evidence-package-as-code.md
  - ../guides/framework-implementation-playbook.md
---

# Evidence pack proporcional por tier

## Objetivo

Definir qual evidência cada tier precisa produzir, em que formato e por quanto tempo — de modo que auditoria, investigação e reassessment sejam rápidos e que o custo da evidência seja proporcional ao risco.

**Todos os tiers produzem evidência.** Governança proporcional não significa ausência de registro; significa que evidência simples e gerada automaticamente é suficiente quando o risco é baixo. Sem isso, a organização perde rastreabilidade exatamente onde o volume é maior.

T4 também exige evidência, mesmo quando a decisão é rejeitar ou manter o uso restrito: a decisão e qualquer exceção precisam ser auditáveis.

## Evidence pack mínimo por tier

| Tier | Pacote mínimo | Objetivo |
|---|---|---|
| **T1** | `agent_id` e registro de descoberta; resultado do pre-screen e tier; contexto de owner e usuário; resultado do policy gate; log básico de runtime; owner e data de attestation | comprovar que o caso foi descoberto, classificado e permaneceu dentro do padrão automatizado |
| **T2** | blueprint versionado; risk record formal com escaladores; domain reviews acionadas; aprovações de dados e tools; identidade e permissões; resultados de evals e testes de segurança; rollback testado; telemetria; residual risk; aprovação de publicação | permitir assurance formal, investigação e reassessment de agente transacional |
| **T3** | tudo de T2 + threat model e abuse cases; impact assessment quando aplicável; testes adversariais e de resiliência; design de oversight humano e step-up; teste de kill switch e quarentena; baseline de comportamento; aceitação explícita de residual risk pela authority; attestation frequente | demonstrar que autonomia e impacto elevados receberam assurance reforçado e capacidade de contenção |
| **T4** | registro de uso restrito ou rejeição; rationale; evidência do padrão proibido; pedido de exceção quando existir; aprovações executiva, jurídica e de risco; compensating controls; expiry; escopo do teste permitido; evidência de contenção | comprovar o default deny e tornar qualquer exceção explícita, temporária, limitada e auditável |

## Qualidade da evidência

Um artefato só conta como evidência quando é:

- **recuperável** — existe endereço estável e alguém consegue abri-lo meses depois;
- **atribuída** — quem produziu, quando e com qual escopo;
- **versionada** — vinculada à versão do agente e do modelo de risco que a originou;
- **íntegra** — protegida contra alteração silenciosa; hash recomendado para snapshots;
- **interpretável** — um terceiro competente entende o que ela demonstra sem o autor presente.

Uma caixa marcada não é evidência. Um print sem contexto, data ou origem não é evidência.

## Evidência é produto do processo

Evidence pack montado depois, para satisfazer uma auditoria, custa mais e vale menos. A evidência precisa ser subproduto natural de executar o processo: o eval gera o relatório, o gate gera o decision record, o deploy gera o baseline, o incidente gera a timeline.

Quando a evidência exige trabalho extra significativo, isso é sinal de que o processo não está instrumentado — não de que falta disciplina das equipes.

## Retenção e acesso

- defina retenção por tier e por tipo de evidência, alinhada às obrigações aplicáveis;
- preserve a evidência de versões anteriores: uma nova release não sobrescreve o histórico da anterior;
- em quarentena e incidente, a preservação é deliberada e vem antes da remediação;
- em retirada, arquive conforme a retenção antes de revogar acessos.

## Artefatos

- Agent Evidence Pack Standard: lista por tier, formato, repositório, retenção, vínculo de versão e verificação de completude;
- índice de evidências por agente e release;
- [evidence package as code](../patterns/evidence-package-as-code.md).

## Evidências

- índice do pacote por release, com endereços recuperáveis;
- verificação de completude executada no gate;
- registro de retenção e de expurgo;
- histórico de acesso quando exigido pela obrigação aplicável.

## Métricas

- releases com evidence pack incompleto no momento do gate;
- evidências referenciadas que não abrem;
- tempo médio para reunir o pacote de um agente sob investigação;
- proporção de evidência gerada automaticamente versus montada manualmente;
- evidências fora da política de retenção.

## Failure modes

- montar o pacote depois, para a auditoria;
- tratar caixa marcada como evidência;
- pacote pesado em T1 que ninguém consegue sustentar no volume real;
- pacote leve em T3 que não sustenta investigação;
- sobrescrever evidência ao publicar nova versão;
- evidência sem vínculo com a versão do modelo de risco que a produziu.

## Decision gate

Nenhum release é aprovado com item obrigatório do pacote do tier ausente. Ausência de evidência é registrada como `missing` e nunca convertida em `passed`.
