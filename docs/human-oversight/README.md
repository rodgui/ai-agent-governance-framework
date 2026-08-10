---
title: Human oversight e accountability
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: quarterly
supersedes: null
related:
  - ../governance/policy.md
  - ../governance/operating-model.md
  - ../responsible-ai/README.md
  - ../patterns/human-accountability-boundary.md
---

# Human oversight e accountability

## Objetivo

Projetar supervisão humana com autoridade, informação, tempo e competência suficientes para prevenir, detectar, interromper ou corrigir efeitos inadequados.

## AI-operated, human-led

Um humano “no loop” não garante controle. Oversight efetivo exige:

- decision right explícito;
- visibilidade do que o agente pretende fazer;
- informação sobre risco e incerteza;
- capacidade técnica de bloquear ou reverter;
- tempo compatível com a decisão;
- competência e independência;
- registro de decisão e resultado.

## Modos de supervisão

| Modo | Descrição | Uso |
|---|---|---|
| human-in-command | humano define finalidade, limites e autoridade | todos os tiers |
| human-in-the-loop | aprovação antes da ação | ação material ou irreversível |
| human-on-the-loop | monitoramento e intervenção durante operação | volume alto com contenção rápida |
| human-out-of-the-loop | sem revisão por execução | somente escopo aprovado, reversível e observado |

O modo é escolhido por risco e capability, não por preferência de UX.

## Accountability boundary

Para cada decisão, registrar:

- o que o agente pode decidir;
- o que apenas prepara ou recomenda;
- o que exige aprovação humana;
- o que é proibido;
- qual humano ou função é accountable;
- quando escalonar;
- como interromper e reverter;
- como contestar e corrigir.

## Approval UX

Uma confirmação de alto impacto deve mostrar:

- ação e alvo;
- dados ou sistemas afetados;
- consequência esperada;
- irreversibilidade e rollback;
- evidência ou rationale do agente;
- alertas e policy conditions;
- opção clara de negar ou editar;
- identity de quem aprova.

Botão genérico “OK” sem contexto não constitui informed approval.

## Quando exigir aprovação

Triggers incluem:

- delete, payment, approval ou privileged change;
- decisão sobre emprego, crédito, saúde, segurança ou direito;
- comunicação pública ou em nome da organização;
- acesso/transferência de dado sensível;
- code execution em ambiente relevante;
- mudança de policy, identidade ou permissão;
- ação sem rollback confiável;
- confiança ou evidência abaixo do threshold.

## Evitar rubber stamping

- reduzir volume de approvals por melhor tiering, não por remover controle;
- agrupar apenas ações homogêneas e reversíveis;
- mostrar diferenças e exceções;
- medir tempo, override e concordância automática;
- rotacionar reviewer em atividades repetitivas;
- permitir amostragem para baixo risco e revisão total para red flags;
- treinar reviewers sobre failure modes.

## Escalation e break-glass

Break-glass exige:

- condição de uso definida;
- identidade forte e authority;
- privilege temporário;
- registro e alerta imediato;
- limitação de escopo;
- revisão posterior obrigatória;
- revogação automática.

Urgência não transforma ação desconhecida em baixo risco.

## Contestability e redress

Pessoas afetadas devem ter, quando aplicável:

- canal acessível;
- identificação do decision owner;
- revisão humana significativa;
- correção de dados ou resultado;
- prazo e comunicação;
- registro para análise sistêmica.

## Evidências

- accountability matrix;
- approval rules e screenshots/UX specs;
- logs de approve, deny, edit e override;
- training/competence records;
- break-glass logs;
- contest e redress records;
- drill de kill switch ou rollback;
- review de automation bias.

## Métricas

- approval rate e override rate;
- tempo de decisão por tier;
- ações executadas sem authority correta;
- rubber-stamp indicators;
- break-glass frequency e findings;
- contest volume e correction time;
- failed rollback/kill-switch drills;
- decisões sem rationale recuperável.

## Failure modes

- humano sem autoridade real;
- aprovação depois da ação;
- reviewer sem informação ou tempo;
- confirmação escondida em termos genéricos;
- exigir approval em excesso e induzir fadiga;
- não registrar edits e overrides;
- accountability atribuída a “o time”;
- break-glass permanente.

## Decision gate

A release authority verifica se o oversight mode, approval UX, escalation, contestability e rollback correspondem ao tier e às ações possíveis.
