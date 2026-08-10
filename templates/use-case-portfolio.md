# Template — Agent Use-Case Portfolio

Catálogo de iniciativas e agentes com outcome, owner, tier e estado. Serve para **priorizar investimento, detectar duplicidade e medir valor** — não para inventariar tecnologia.

O portfólio e o [registry](../docs/registry/README.md) respondem perguntas diferentes e não devem ser o mesmo artefato. O registry responde "o que existe e quem responde por isso". O portfólio responde "isso deveria continuar existindo".

Os critérios de decisão e a tabela de value review estão em [estratégia, portfólio e evidência de valor](../docs/value/README.md).

## Identificação

- Portfolio owner:
- Período de referência:
- Data da última review:
- Fonte dos dados de custo e uso:

## Registro

| Campo | O que registrar | Por que importa |
|---|---|---|
| `agent_id` | identificador do registry, quando o agente já existe | liga a decisão de portfólio à evidência operacional |
| use case | nome curto e reconhecível pelo negócio | evita que a mesma ideia entre duas vezes com nomes diferentes |
| problem statement | problema mensurável que existe hoje | intake orientado a problema, não a tecnologia |
| sponsor | quem responde pelo investimento | sem sponsor não há decisão de parar |
| business owner | quem responde por finalidade e outcome | separado de quem constrói |
| tier | criticidade T1–T4 | determina proporcionalidade dos controles |
| admissibilidade | `permitted`, `conditional`, `restricted` ou `prohibited` | dimensão independente do tier |
| status | ideia, intake, em construção, piloto, produção, contido, aposentado | permite ver o funil e onde ele trava |
| expected value | hipótese de valor com baseline declarado | sem baseline, ganho é opinião |
| actual value | valor observado, com incerteza | a comparação com o esperado é o dado que ninguém tem |
| cost | inferência, plataforma, revisão humana, suporte e incidentes | custo só de token subestima sistematicamente |
| duplication flag | sobreposição conhecida com outro item | é o campo que mais economiza dinheiro e menos é preenchido |
| decisão da última review | manter, expandir, corrigir, restringir, substituir ou aposentar | portfólio sem decisão registrada é planilha |

## Linhas do portfólio

| agent_id | Use case | Sponsor | Business owner | Tier | Admissibilidade | Status | Expected value | Actual value | Custo | Duplicação | Decisão |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |

## Review de portfólio

Cadência sugerida: mensal para status e duplicidade, trimestral para valor observado contra baseline.

A review precisa produzir decisão registrada para cada item, inclusive "manter sem mudança". Uma review que só atualiza números não é governança de portfólio — é relatório.

Três perguntas que costumam revelar mais do que o dashboard:

1. Qual item entrou em produção e nunca teve valor observado medido?
2. Quais dois itens resolvem o mesmo problema para departamentos diferentes?
3. Qual item continua operando porque ninguém decidiu aposentá-lo?

## Antipatterns

- usar o portfólio como inventário técnico, duplicando o registry;
- registrar expected value e nunca voltar para medir actual value;
- deixar `duplication flag` em branco por padrão, o que o torna inútil;
- tratar número de agentes como indicador de progresso;
- aceitar adoção como prova de valor.
