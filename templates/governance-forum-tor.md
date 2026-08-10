# Template — Terms of reference de fórum de governança

Use para instituir qualquer fórum do [operating model](../docs/governance/operating-model.md): Governance Council, Design Authority, Run Authority, review de risco ou review de valor.

Um fórum sem decision rights explícitos vira reunião de status. Se o fórum não pode decidir nada sozinho, ele não precisa existir — o assunto pertence a quem tem a authority.

## 1. Identificação

- Nome do fórum:
- Propósito em uma frase:
- Data de instituição:
- Authority que o instituiu:
- Próxima revisão destes termos:

## 2. Decisões que este fórum toma

Liste apenas decisões que o fórum pode tomar sem escalar. Se toda decisão precisa de aprovação externa, o fórum é consultivo — declare isso.

| Decisão | Estados possíveis | Quórum mínimo | Evidência exigida antes da pauta |
|---|---|---|---|
| | `approve` / `condition` / `hold` / `reject` | | |

## 3. Decisões que este fórum NÃO toma

Explicitar o que fica de fora evita que o fórum vire fila operacional.

- Decisões que pertencem a domain authorities:
- Decisões que pertencem à Run Authority e não esperam este fórum:
- Decisões que exigem escalation:

## 4. Composição

| Papel | Função no fórum | Presença | Pode votar? | Substituto designado |
|---|---|---|---|---|
| | presidência / membro / convidado | obrigatória / sob demanda | | |

- Presidência:
- Secretaria (quem registra a decisão):
- Regra de conflito de interesse:
- Regra quando o membro é também o proponente:

## 5. Cadência e pauta

- Cadência regular:
- Convocação extraordinária: quem pode convocar e com que antecedência
- Prazo de submissão de pauta:
- Critério de rejeição de pauta por evidência insuficiente:
- SLA de decisão por tipo de item:

Item sem evidência completa não entra na pauta. Entrar e receber `hold` por falta de material consome a capacidade do fórum e ensina que a preparação é opcional.

## 6. Registro da decisão

Toda decisão registra, no mínimo:

- `gate_id` ou identificador do item;
- escopo e versão avaliados;
- tier;
- authority e participantes presentes;
- evidence refs aceitas;
- estado: `approve` / `condition` / `hold` / `reject`;
- rationale;
- condições e compensating controls;
- expiry;
- próxima revisão.

Conforme o [contrato comum dos decision gates](../docs/guides/framework-implementation-playbook.md#contrato-comum-dos-decision-gates). Divergência registrada permanece registrada — não é apagada por consenso posterior.

## 7. Escalation

- Quando este fórum escala:
- Para quem:
- Prazo máximo antes da escalation automática:
- O que acontece com o item enquanto a escalation corre:

## 8. Métricas do fórum

- itens decididos dentro do SLA;
- itens devolvidos por evidência incompleta;
- decisões revertidas ou revisadas fora de ciclo;
- exceções aprovadas e quantas venceram sem regularização;
- tempo médio entre submissão e decisão, por tier;
- quórum não atingido.

## 9. Revisão destes termos

- Gatilhos de revisão:
- Authority que aprova mudanças:
- Versão atual e histórico:

Um fórum que nunca revisa seus próprios termos acumula pauta que não lhe pertence.
