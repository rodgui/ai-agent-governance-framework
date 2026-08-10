---
title: Identidade de agentes e least privilege
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../governance/operating-model.md
  - ../tool-governance/README.md
  - ../data-access/README.md
  - ../patterns/registry-and-blueprint.md
---

# Identidade de agentes e least privilege

## Objetivo

Garantir que cada agente, execução e ação possam ser atribuídos a uma identidade apropriada, com privilégios mínimos, finalidade, duração e owner verificáveis.

## Princípio

Agentes não devem herdar implicitamente a identidade ampla de um usuário, builder, service account compartilhada ou runtime genérico. A identidade precisa refletir **quem opera**, **qual agente executa**, **em nome de quem**, **para qual finalidade** e **sob quais limites**.

## Modelos de identidade

| Modelo | Uso aceitável | Risco principal |
|---|---|---|
| identidade do usuário delegada | ação interativa, no escopo do usuário | privilege laundering e consentimento ambíguo |
| workload identity do agente | execução autônoma ou serviço | privilégio persistente e ownerless identity |
| identidade por execução | tarefas efêmeras ou sensíveis | complexidade de emissão e correlação |
| service account compartilhada | legado temporário com waiver | baixa atribuição e blast radius amplo |
| credencial embutida | nenhum | segredo exposto e impossível de governar |

Service accounts compartilhadas exigem plano de eliminação, controles compensatórios e expiração da exceção.

## Requisitos mínimos

1. Cada agente possui business owner, technical owner e identidade registrada.
2. Produção usa identidade não humana quando a plataforma suporta.
3. Secrets não ficam em prompt, código, blueprint público ou configuração não protegida.
4. Scopes são derivados de tarefas aprovadas, não da conveniência do builder.
5. Acesso privilegiado é just-in-time, time-bound e reautorizado quando possível.
6. A identidade é revogada no sunset, troca de owner ou fim da finalidade.
7. Ações registram actor humano, agent identity, delegated subject e correlation ID quando aplicável.
8. Mudanças de role, scope, tenant, região ou credencial são material changes.
9. Break-glass possui authority, logging, alerta e revisão posterior.
10. O agente não pode conceder a si mesmo novos privilégios.

## Matriz de autorização

O blueprint deve mapear:

| Campo | Exemplo de decisão |
|---|---|
| recurso | sistema, API, dataset, fila ou tool |
| ação | read, write, approve, execute, delete, delegate |
| condição | ambiente, horário, região, valor ou tipo de dado |
| subject | workload, usuário delegado ou equipe |
| duração | sessão, tarefa, janela ou prazo |
| approval | automático, owner, dual control ou proibido |
| evidence | policy, role binding, token claim ou log |

Permissões em produção devem ser testadas com casos positivos e negativos.

## Delegação e “on behalf of”

Quando um agente atua em nome de um usuário:

- a interface deixa claro qual ação será executada;
- o consentimento cobre objeto, destino e efeito;
- o token não amplia privilégios do usuário;
- a decisão distingue recomendação, preparação e execução;
- ações irreversíveis exigem confirmação compatível com o risco;
- logs preservam usuário, agente, tool e resultado.

A delegação não transfere accountability do sistema para o usuário final.

## Lifecycle de identidade

```mermaid
flowchart LR
    R[Registrar necessidade] --> D[Definir scopes]
    D --> A[Aprovar]
    A --> P[Provisionar]
    P --> V[Validar positivo/negativo]
    V --> M[Monitorar uso]
    M --> T[Revalidar]
    T -->|mantém| M
    T -->|muda| D
    T -->|encerra| X[Revogar e verificar]
```

## Controles por tier

| Tier | Controle adicional |
|---|---|
| T1 — baixo | identidade atribuível e scopes documentados |
| T2 — moderado | workload identity, expiry e teste negativo |
| T3 — alto | JIT, dual control para privilégio, session recording quando cabível |
| T4 — crítico | isolamento dedicado, autorização por transação e monitoramento contínuo |

## Playbook de implantação

Identidade é o ponto que transforma atividade do agente em **ação atribuível**. Execute em ordem na primeira implantação; em ciclos posteriores, uma mudança material pode exigir apenas os passos afetados.

1. **Classificar os modos de atuação.** Para cada agente: existe usuário presente? a ação ocorre exclusivamente no escopo dele? o agente executa de forma assíncrona ou para múltiplos usuários? Identidade delegada só quando a sessão humana e o escopo são reais; identidade própria quando o agente age por conta própria.
2. **Inventariar e remediar credenciais.** Descobrir chaves de API, service accounts, tokens pessoais e secrets em builders, CI/CD e runtimes. Classificar como aprovada, transitória ou proibida, com owner e prazo. **Credencial compartilhada em T2/T3 é finding, não detalhe técnico.**
3. **Padronizar emissão e ownership.** Convenção de nomes, owner, ambiente, expiry, tags, authority de criação e contato de recuperação. O registry precisa correlacionar `agent_id` ↔ `identity_id` ↔ owner — sem isso, JML e behavioral analytics ficam frágeis.
4. **Modelar autorização por recurso, ação e parâmetros.** Least privilege não é apenas limitar a API. Uma ferramenta de atualização pode editar descrição sem poder alterar prioridade crítica; uma ferramenta de pagamento pode consultar sem poder executar acima do limite sem aprovação humana.
5. **Definir tokens, secrets e sessão.** Tokens curtos, cofre, rotação e claims específicos. Proibir secrets em prompt, memória e código. Declarar o que acontece quando a identidade é revogada **durante** uma execução longa.
6. **Integrar JML e attestation.** Saída de owner produz reatribuição ou suspensão; mudança de área pode alterar authority e centro de custo; attestation confirma owner, necessidade e permissões. Preservar o histórico de ownership e de mudanças de permissão.
7. **Aplicar step-up e dual control em ações críticas.** A aprovação é vinculada a `agent_id`, ferramenta, alvo, parâmetros e validade. **Aprovação genérica em chat não é aprovação.** Para ações privilegiadas, autorização de curta duração e segregação de funções quando exigido.
8. **Fechar o ciclo com logs e investigação.** Registrar usuário, agente, delegação, resultado da policy, ferramenta, ação, alvo e hash dos parâmetros. Validar que é possível reconstruir **quem pediu, qual agente decidiu, qual identidade executou e qual política autorizou**.

## Evidências

- identity record e owner;
- role/scope mapping;
- configuração de autenticação;
- prova de armazenamento seguro de secrets;
- testes de autorização positiva e negativa;
- logs com correlation ID;
- attestation de acesso;
- evidência de revogação e orphan scan.

## Métricas

- agentes sem workload identity adequada;
- shared accounts e credenciais persistentes;
- scopes não usados ou excessivos;
- identities sem owner ou attestation;
- falhas de revogação;
- ações sem correlação entre usuário, agente e tool;
- exceções vencidas.

## Failure modes

- usar conta do builder em produção;
- compartilhar identidade entre múltiplos agentes;
- permitir refresh token sem prazo;
- confiar apenas no prompt para proibir ações;
- registrar “system” como actor de toda execução;
- manter acesso após sunset;
- tratar autenticação forte como autorização suficiente.

## Decision gate

Nenhum agente com capacidade de escrita, execução ou deleção passa pelo release gate sem identity model, permission matrix, testes negativos e revocation plan.
