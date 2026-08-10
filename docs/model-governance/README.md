---
title: Governança de modelos, provedores e dependências de IA
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - ../architecture/overview.md
  - ../risk-management/README.md
  - ../evaluations/README.md
  - ../security/README.md
  - ../../controls/README.md
---

# Governança de modelos, provedores e dependências de IA

## Objetivo

Controlar as condições sob as quais um modelo pode ser usado — finalidade, classe de dados, região, retenção, logging, comportamento e custo — e manter a organização capaz de trocar, atualizar ou abandonar um provedor sem reescrever o sistema de governança.

Aprovar um modelo não é aprovar uma marca. A unidade governada é a **combinação**:

```text
provider × model × version × finalidade × data class × região × controles
```

O mesmo modelo pode ser adequado para dados públicos e inadequado para dados restritos. Uma atualização de versão pode mudar comportamento sem alterar o nome lógico usado pela aplicação.

## O que este domínio decide

| Decisão | Pergunta | Evidência mínima |
|---|---|---|
| admissão no catálogo | o provedor atende aos critérios de segurança, dados, observabilidade e continuidade? | provider assessment e termos contratuais |
| classe de dados permitida | quais classificações podem trafegar nesta combinação? | data handling record e residency |
| adequação ao caso | o modelo foi avaliado para *esta* tarefa, não apenas para linguagem geral? | evaluation baseline por use case |
| mudança de versão | a nova versão altera comportamento material? | regression evals e diff de comportamento |
| fallback e routing | o modelo alternativo tem os mesmos controles? | equivalência declarada e testada |
| saída | é possível substituir esta dependência? | exit plan e teste de substituição |

## Catálogo de modelos e provedores

O catálogo é por **combinação**, não por marca. Registro mínimo:

- provider, model, version e modalidade de serviço (API, managed, self-hosted ou embedded);
- allowed data classes e tiers;
- regiões permitidas e residency;
- retenção, uso para treinamento/reuso, subprocessadores e controles contratuais;
- capacidades de telemetria e atribuição de uso;
- evaluation baseline vinculado à versão;
- fallback aprovado e condições de acionamento;
- data de depreciação prevista e processo de notificação de incidente;
- status: `approved`, `conditional`, `experimental` ou `prohibited`.

Um provedor sem capacidade mínima de telemetria não é reprovado automaticamente, mas exige gateway ou proxy que produza a evidência ausente — o custo desse componente pertence à decisão.

## Avaliação vinculada à versão

Benchmark público de fornecedor não substitui avaliação do caso corporativo. Antes de aprovar uma versão, defina e meça:

- qualidade na tarefa real e nos slices relevantes;
- comportamento de tool calling e confiabilidade de execução;
- safety e recusa em cenários adversariais aplicáveis;
- latência, custo por tarefa e comportamento sob retry;
- failure modes: o que o modelo faz quando não sabe, quando a ferramenta falha e quando o contexto estoura.

Uma boa pontuação de linguagem não indica confiabilidade de execução. Agentes com capacidade de ação exigem avaliação de tool-use específica.

## Mudança de versão é change control

Uma nova major version pode alterar reasoning, seleção de ferramentas, postura de safety e custo sem qualquer mudança no código do agente. Trate como mudança potencialmente material e aplique o processo de [reavaliação de risco](../risk-management/README.md#mudança-material).

- rode regression evals antes do rollout, não depois;
- determine por agente se a mudança é material — a mesma versão pode ser irrelevante para um caso e material para outro;
- registre a versão avaliada no blueprint e no release evidence;
- preserve a capacidade de fixar versão quando o provedor permitir.

## Fallback, routing e equivalência de controles

Se o runtime pode trocar de modelo, o fallback é parte da superfície governada.

- o modelo alternativo precisa estar aprovado para a **mesma classe de dados e capacidade**;
- failover para provedor com políticas incompatíveis é violação de controle, não resiliência;
- routing por custo ou latência não pode reduzir silenciosamente o nível de assurance;
- a troca precisa aparecer na telemetria e no registro da execução.

## Dependência, portabilidade e saída

- documente as abstrações que isolam o agente do provedor;
- mantenha prompts, evals e configurações exportáveis;
- identifique dependências proprietárias que não têm equivalente;
- para funções críticas, **teste a substituição antes de precisar dela**;
- registre concentração por provedor e modelo no portfólio.

## Economia por tarefa, não por token

O modelo mais barato por token pode ser o mais caro por tarefa concluída. Meça custo considerando retries, tamanho de contexto, loops de ferramenta, cache e taxa de sucesso. A comparação relevante é **custo por outcome com qualidade preservada**.

## Incidente, advisory e depreciação

Defina antecipadamente como tratar incidente do provedor, security advisory, retirada de modelo e bloqueio emergencial. O registry e os blueprints precisam responder em minutos: **quais agentes dependem da combinação afetada?**

## Playbook de implantação

1. Definir critérios de entrada no catálogo por tier e classe de dados.
2. Criar evaluation baseline por use case, antes de aprovar qualquer versão.
3. Registrar a combinação aprovada com suas restrições explícitas.
4. Tratar mudança de versão como change control com regression evidence.
5. Definir fallback e routing com equivalência de controles demonstrada.
6. Integrar custo por tarefa e capacidade ao processo de decisão.
7. Preparar e testar a exit strategy das dependências críticas.
8. Manter processo de incidente, advisory e depreciação com busca reversa por dependência.

Execute em ordem na primeira implantação. Em ciclos posteriores, uma mudança material pode exigir apenas os passos afetados.

## Artefatos

- Model & Provider Governance Standard;
- Approved Model/Provider Catalog por classe de dados, caso e região;
- evaluation baseline e regression suite por combinação;
- provider assessment e data handling record;
- exit plan e teste de substituição;
- registro de depreciação e notificação de incidente.

## Evidências

- critérios de aprovação e decisão de admissão;
- data handling, residency e termos aplicáveis;
- evaluation results vinculados a provider, model e version;
- regression evidence de cada mudança de versão;
- equivalência de controles do fallback;
- custo por tarefa e por outcome;
- inventário de dependências por agente;
- decisões de depreciação e substituição.

## Métricas

- agentes usando combinação fora do catálogo;
- versões em produção sem evaluation vinculada;
- mudanças de versão sem regression evidence;
- acionamentos de fallback e quantos foram para combinação aprovada;
- concentração por provedor, modelo e região;
- custo por tarefa e variação após mudança de versão;
- tempo entre advisory do provedor e identificação dos agentes afetados;
- dependências críticas sem exit plan testado.

## Failure modes

- allowlist única de modelos sem contexto de dados ou tier;
- acoplar cada agente a um provedor específico sem abstração ou plano de saída;
- tratar mudança de major version como patch;
- comparar apenas preço por token, ignorando retries, contexto, loops de ferramenta e qualidade do resultado;
- permitir fallback para provedor não aprovado durante indisponibilidade;
- aprovar modelo por reputação de fornecedor em vez de avaliação no caso real;
- perder a rastreabilidade de qual versão produziu qual resultado.

## Decision gate

Nenhum agente entra em produção com combinação provider/model/version fora do catálogo aprovado para a sua classe de dados, sem evaluation vinculada à versão, sem fallback com equivalência de controles declarada e sem registro da dependência no blueprint.
