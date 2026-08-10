# Template — Dicionário de taxonomia e metadados de agentes

Use para transformar as categorias conceituais do domínio de [estate e registry](../docs/registry/README.md) em campos implementáveis no registry, no blueprint e no risk pre-screen.

Regra de seleção: **inclua apenas dimensões que alteram decisão, controle, métrica ou lifecycle.** Uma categoria que não muda nada não deve ser obrigatória — ela só adiciona campo para preencher e campo para errar.

## 1. Dimensões

Para cada dimensão, declare o que ela muda. Se a coluna "o que muda" ficar vazia, remova a dimensão.

| Dimensão | Código | Categorias válidas | O que muda na governança | Obrigatória a partir de | Fonte do valor |
|---|---|---|---|---|---|
| | | | | T1 / T2 / T3 / T4 | autodescoberta / declarada / derivada |

Preencha `fonte do valor` com honestidade: um campo marcado como autodescoberto que na prática é digitado por alguém vai divergir da realidade silenciosamente.

## 2. Definições operacionais

Categoria sem critério operacional produz classificação inconsistente. Para cada categoria ambígua, escreva o teste que decide.

| Categoria | Definição operacional | Teste que decide | Exemplo que pertence | Exemplo que não pertence |
|---|---|---|---|---|
| | | | | |

Exemplo do problema: `autônomo` não pode significar "o builder acha que é autônomo". Precisa de critério — por exemplo, "executa ação de efeito externo sem confirmação humana no caminho".

## 3. Normalização por plataforma

Cada builder nomeia as coisas do seu jeito. Sem mapeamento, o registry mistura vocabulários.

| Plataforma de origem | Termo nativo | Categoria corporativa | Regra de conversão | Ambiguidades conhecidas |
|---|---|---|---|---|
| | | | | |

## 4. Campos no registry e no blueprint

| Dimensão | Campo no registry | Campo no blueprint | Tipo | Enum validado? | Consumidor automatizado |
|---|---|---|---|---|---|
| | | | | sim / não | policy gate / dashboard / IAM / nenhum |

Se a coluna `consumidor automatizado` for `nenhum` em muitas linhas, o dicionário está descrevendo documentação, não governança.

## 5. Teste de concordância

Antes de publicar, classifique de 20 a 30 casos reais com pelo menos dois avaliadores independentes.

- Casos classificados:
- Avaliadores:
- Dimensões com divergência acima do aceitável:
- Definições refinadas em consequência:
- Data do teste e responsável:

Divergência sistemática indica **definição fraca**, não avaliador fraco. Refine a definição antes de treinar as pessoas.

## 6. Versionamento

- Versão do dicionário:
- Mudanças desde a versão anterior:
- Impacto em registros existentes: reclassificar / manter / migrar
- Authority que aprovou:
- Próxima revisão:

Alterar uma categoria depois que milhares de agentes foram classificados tem custo de migração. Prefira acrescentar a redefinir.

## 7. Limites

- taxonomia não é risk tier: dois agentes na mesma categoria podem receber tiers diferentes;
- não derive categorias de produto — o produto informa onde o agente foi construído, não o que ele pode fazer;
- categoria ausente é `desconhecida`, nunca o valor mais benigno por padrão.
