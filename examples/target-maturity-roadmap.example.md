# Exemplo — Target maturity roadmap

> Fictício e sanitizado. Níveis, alvos e dependências são ilustrativos.

Demonstra a seção de [target state do maturity model](../docs/guides/maturity-model.md#target-state). A regra que este exemplo materializa: **não é necessário atingir nível 4 em tudo**, e a sequência importa mais que a média.

Níveis: 0 inexistente · 1 ad hoc · 2 definido · 3 gerenciado · 4 adaptativo

| Capability | Atual | Confiança | Alvo 12m | Outcome observável | Iniciativa | Depende de |
|---|---|---|---|---|---|---|
| registry, blueprint e lifecycle | 1 | média | 3 | reconciliação e attestation operacionais | registry MVP + automação de discovery | — |
| identidade e acesso | 1 | alta | 3 | 100% de T2/T3 com identidade própria | padrão de identidade + JML | registry |
| tools, APIs e MCP | 0 | média | 3 | 100% das ferramentas de alto impacto registradas e mediadas | registro de tools + mediação | taxonomia de risco |
| dados e connectors | 1 | baixa | 2 | contratos de dados e gates de connector definidos | catálogo de fontes certificadas | ownership de dados |
| auditabilidade e operações | 1 | média | 3 | 95% dos agentes com telemetria unificada | schema de telemetria + pipeline | identidade + registry |
| risco, RAI e oversight | 2 | média | 3 | residual risk, slices e contestabilidade medidos | calibração de tiers + triggers | registry |
| policy e decision rights | 2 | alta | 3 | SLAs, handoffs e segregação medidos | operating model + fóruns | — |
| evaluations e release | 1 | baixa | 2 | estratégia, datasets e gates definidos | evaluation baseline por caso | model governance |
| estratégia e valor | 1 | baixa | 2 | criação, uso, qualidade e outcome medidos separadamente | business case e baseline | — |
| adoção e competência | 1 | média | 2 | personas, paved road e suporte definidos | enablement por papel | operating model |

## Por que os alvos não são uniformes

Quatro capabilities miram nível 3 e cinco miram nível 2. Isso é decisão, não falta de ambição.

**Identidade, tools, registry e telemetria vão a 3** porque são pré-condição de tudo que vem depois: sem identidade própria não há atribuição, sem registro de ferramentas não há controle de blast radius, e sem telemetria não há como demonstrar qualquer outra coisa. São o caminho crítico.

**Dados, evaluations, valor e adoção ficam em 2** no primeiro ciclo porque dependem de ownership organizacional que ainda não existe — elevá-los antes produziria documento, não capacidade.

Repare que **dados e evaluations têm confiança `baixa`**. Um alvo definido sobre baseline de baixa confiança é uma hipótese: o primeiro trabalho dessas duas linhas é melhorar a evidência, não a nota.

## O que a média esconderia

A média destas dez linhas é 1,1 — um número que não orienta nada. O que orienta é: **três capabilities estão em 0 ou 1 com dependência de outras**, e `tools` em nível 0 é o maior risco isolado do conjunto, porque agentes com capacidade de ação já existem no estate enquanto o controle não.

## O que este exemplo não demonstra

- não declara população, amostragem nem cobertura, que são obrigatórios no assessment real;
- confiança aqui é resumo; cada linha precisa de `evidenceRefs` no registro estruturado;
- alvos de 12 meses sem revisão trimestral viram ficção;
- nível alto de maturidade não reduz o tier de risco de nenhum agente específico.
