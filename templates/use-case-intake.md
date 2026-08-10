# Template — Intake de caso de uso

Aplicado **antes de o agente existir**. Captura problema, processo atual, baseline e hipótese de valor.

Se o formulário começar perguntando "qual modelo?" ou "qual builder?", ele já induziu a solução antes de entender a necessidade. Por isso a tecnologia aparece no fim, e só depois que a alternativa determinística foi considerada.

Complementa o [risk pre-screen](risk-pre-screen.md), que cobre risco. Este cobre problema e valor.

## 1. Identificação

- ID do caso de uso:
- Nome proposto:
- Solicitante e área:
- Business owner candidato:
- Data:

## 2. Problema

| Campo | Pergunta | Exemplo |
|---|---|---|
| problema | qual problema **mensurável** existe hoje? | tempo médio de resolução de incidentes P3 é de 18 horas |
| usuários e processo | quem usa e em qual etapa? | analistas de service desk L1 e L2, durante triagem e atualização |
| baseline | como funciona hoje? | busca manual em 5 fontes, 4 handoffs, 12% de retrabalho |
| volume | qual a frequência e o volume? | 1.200 incidentes P3 por mês |

Problema sem número não é problema: é incômodo. Se não houver medida, o primeiro entregável é obter a baseline, não construir o agente.

## 3. Por que um agente

- Qual alternativa determinística foi considerada (workflow, busca, regra, integração)?
- Por que ela não resolve?
- O que exige interpretação, contexto variável, planejamento ou seleção dinâmica de ferramentas?

Percorra a [árvore de decisão arquitetural](../docs/architecture/agent-or-not.md) e registre o resultado aqui. **Se a resposta for "não precisamos de agente", registre isso e encerre o intake** — é uma conclusão válida e barata.

## 4. Resultado esperado

- KPI de outcome que deve melhorar:
- Baseline atual desse KPI:
- Meta e horizonte:
- Como será medido e por quem:
- Critérios de parada: adoção baixa, outcome estagnado, custo acima do limite ou duplicidade

Adoção não é resultado. Uso alto pode significar que o agente virou etapa obrigatória de um fluxo pior.

## 5. Sinais de risco

Preenchimento rápido, para roteamento. O detalhamento é do [risk pre-screen](risk-pre-screen.md).

- Haverá escrita ou ação com efeito externo?
- Quais classes de dados são necessárias?
- Há impacto sobre pessoas, direitos, oportunidades ou processo regulado?
- Alcance previsto: usuário, time, unidade, corporativo ou externo?

## 6. Duplicidade

- Existe capacidade semelhante já registrada?
- Existe iniciativa paralela em outra área?
- Este caso poderia consumir um componente compartilhado em vez de uma stack própria?

Dois times propondo agentes para resumir contratos não precisam de duas stacks: precisam de um componente comum de sumarização e de dois contextos de processo. O ganho de governança vem de reduzir duplicidade técnica e de controle — não de proibir autonomia local.

## 7. Custo esperado

Estimativa grosseira, para dimensionar — não para aprovar orçamento.

- Inferência e plataforma:
- Engenharia de construção:
- Suporte e operação:
- **Revisão e supervisão humana:**
- Assurance proporcional ao tier previsto:

O custo de supervisão humana é o mais esquecido e frequentemente o maior em casos de alto tier.

## 8. Decisão de intake

- Encaminhamento: `seguir para classificação` / `alternativa determinística` / `consolidar com caso existente` / `recusar`
- Rationale:
- Business owner confirmado:
- Data e responsável pela decisão:

## Como medir valor sem inflar

1. Observe a baseline por 4 a 8 semanas quando for possível.
2. Separe volume de uso de resultado.
3. Use outcomes que já importam ao processo: cycle time, taxa de erro, receita, custo evitado, nível de serviço, qualidade ou redução de risco.
4. Inclua o custo total, incluindo revisão humana.
5. Meça por coorte e período; não extrapole um piloto de dez usuários para a empresa.
6. Declare os critérios de parada **no intake**, não depois que o investimento já foi feito.
