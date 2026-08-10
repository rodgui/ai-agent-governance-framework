# Exemplo — Registro de gargalos manuais

> Fictício e sanitizado. Volumes e lead times são ilustrativos.

Demonstra o registro descrito em [descoberta contínua e forecast](../docs/registry/discovery-and-forecast.md). Ele é o insumo direto da decisão sobre **o que virar policy-as-code** — e sobre o que deve permanecer humano.

| Atividade manual | Volume/mês | Lead time | Risco de automatizar | Decisão inicial |
|---|---|---|---|---|
| aprovar agente T1 somente leitura | 400 | 2 dias | baixo | automatizar com policy gate após piloto |
| criar identidade de agente T2 | 40 | 4 dias | médio | workflow + API de IAM, mantendo caminho de exceção |
| aprovar fonte de dados já certificada | 60 | 3 dias | baixo | automatizar consulta ao catálogo |
| aprovar fonte fora do catálogo | 8 | 12 dias | alto | manter humano; automatizar o preparo da evidência |
| revisar ferramenta privilegiada T3 | 5 | 5 dias | alto | manter decisão humana; automatizar o preparo da evidência |
| montar evidence pack para gate | 45 | 2 dias | baixo | gerar automaticamente a partir do pipeline |
| reatribuir owner após desligamento | 6 | 9 dias | médio | automatizar a detecção; manter a reatribuição humana |

## Como ler a tabela

A leitura útil não é "automatizar o que tem mais volume". É esta:

**Automatizar a preparação da evidência é quase sempre seguro. Automatizar a decisão só quando a policy está estável.**

Repare em `aprovar fonte fora do catálogo` e `revisar ferramenta privilegiada`: volume baixo, lead time alto, risco alto. Automatizar a decisão nesses dois casos economizaria treze aprovações por mês e criaria exposição desproporcional. Mas montar a evidência que o revisor precisa — hoje manual — é puro desperdício e sai da conta sem custo de risco.

O oposto está em `aprovar agente T1 somente leitura`: 400 casos por mês a dois dias cada. Esse é o item que, se continuar manual, faz a organização contornar a governança — e o [fast path de T1](../docs/risk-management/README.md#fast-path-de-t1) existe exatamente para ele.

`Montar evidence pack` merece atenção separada: 45 ocorrências por mês de trabalho que **não deveria existir**. Evidence pack montado à mão é sintoma de processo não instrumentado, não de equipe indisciplinada.

## O que este exemplo não demonstra

- não mede o custo humano por atividade, que costuma mudar a priorização;
- lead time aqui é tempo de calendário, não esforço;
- a coluna de risco é julgamento e precisa de rationale registrado;
- automatizar reduz lead time mas cria dependência de plataforma — o caminho de exceção manual precisa continuar existindo e sendo testado.
