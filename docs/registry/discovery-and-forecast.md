---
title: Descoberta contínua do estate e forecast de crescimento
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - ../lifecycle/README.md
  - ../guides/framework-implementation-playbook.md
  - ../value/README.md
  - ../../schemas/agent-registry.schema.json
  - ../../examples/agent-registry.example.json
---

# Descoberta contínua do estate e forecast de crescimento

## Objetivo

Produzir um baseline confiável de quais agentes já existem, com grau de confiança declarado, e transformar descoberta em capacidade contínua — não em inventário de workshop.

Uma organização que "começa do zero" raramente começa com zero agentes. Ela começa com **baixa visibilidade**.

## Por que discovery é disciplina, não projeto

O agent estate muda mais rápido que um CMDB tradicional porque agentes nascem de usuários, SaaS, low-code, IDEs, automações e código. Um inventário pontual fica obsoleto em semanas. O baseline é o ponto de partida; a capacidade contínua é o produto.

## Fontes de descoberta

| Fonte | O que procurar | Limitação típica | Como compensar |
|---|---|---|---|
| builders e low-code | agentes, apps, owners, status de publicação | não cobre agentes custom | correlacionar com repositórios e gateways |
| IAM e identidades não humanas | service principals, workload identities, secrets | a identidade pode não indicar que é agente | usar convenção de nomes, tags e telemetria de API |
| gateways de modelo e API | chamadas de modelo, chaves, metadados de ator | apenas o tráfego que passa pelo gateway | combinar com egress/proxy e dados de despesa |
| código-fonte e CI/CD | SDKs de agente, clientes de modelo, configurações MCP | protótipos locais podem não aparecer | survey com desenvolvedores e scanning de artefatos |
| inventário de SaaS e compras | produtos com recursos agentic | recurso licenciado pode não estar em uso | validar uso real e logs administrativos |
| rede e egress | destinos de APIs de modelo e endpoints MCP | baixa semântica | usar apenas como sinal de agente `suspected` |

Nenhuma fonte isolada é suficiente. A cobertura vem da correlação, e a correlação exige um schema mínimo comum.

## Status de confirmação e confidence

Dois campos diferentes evitam inflar métricas e descartar sinais de shadow AI:

- `discovery.status` descreve o quanto a existência e o contexto do agente foram confirmados;
- `discovery.confidence` expressa a confiança na correlação dos sinais disponíveis.

Status não deve receber `low|medium|high`, e confidence não deve receber `confirmed|probable|suspected`.

| Status | Significado | Ação |
|---|---|---|
| `confirmed` | evidência direta do agente e do seu contexto | registrar e atribuir owner |
| `probable` | múltiplos sinais apontam para uso agentic, sem confirmação | investigar dentro do SLA definido |
| `suspected` | indício isolado que merece verificação | manter no backlog de remediação |

Objetos incertos **não são descartados**. Eles entram no backlog com owner e prazo.

| Confidence | Uso |
| --- | --- |
| `high` | sinais independentes coerentes e recentes |
| `medium` | evidência útil com gap conhecido de cobertura ou contexto |
| `low` | sinal fraco, antigo ou ainda não reconciliado |

O [Agent Registry 2.0](../../schemas/agent-registry.schema.json) preserva `firstSeenAt`, `lastSeenAt` e `signals[]`, cada sinal com origem, tipo, timestamp e evidence reference.

## Procedimento

1. Definir o universo de descoberta: tenants, nuvens, repositórios, builders, SaaS, APIs de modelo, service accounts e integrações MCP conhecidas.
2. Coletar inventários e sinais das fontes acima.
3. Normalizar no schema mínimo: `agent_id`, nome, owner, plataforma, ambiente, lifecycle stage, operational state, fontes de dados, tools, modelo/provedor, audiência e o objeto `discovery`.
4. Deduplicar por identificadores e evidências, distinguindo **um agente** de **uma versão ou instância**.
5. Classificar confiança e registrar o que ficou incerto.
6. Entrevistar 5–10 áreas com maior probabilidade de adoção para revelar shadow agents e demanda futura.
7. Construir o forecast em três cenários.
8. Identificar e quantificar os gargalos manuais.
9. Fechar o baseline com **data de corte** e definir a cadência de redescoberta, preferencialmente automatizada.

## Forecast do estate

Forecast serve para **dimensionar governança**, não para prometer número exato.

1. Definir baseline por população: agentes pessoais, de time, de processo, embarcados e de terceiros.
2. Identificar drivers: usuários habilitados, builders disponíveis, templates, iniciativas estratégicas, novos SaaS e automações previstas.
3. Criar cenários conservador, provável e acelerado em 6 e 12 meses.
4. Projetar o **mix de risco**, não apenas o volume. Crescer de 1.000 para 5.000 agentes T1 não demanda o mesmo esforço que adicionar 100 agentes T3.
5. Converter o forecast em volumes operacionais: attestations por mês, reviews T2/T3, incidentes esperados, identidades, registros de tools e volume de telemetria.
6. Revisar trimestralmente com dados reais e ajustar capacidade de fóruns, automação e plataforma.

Exemplo de dimensionamento: se 5.000 usuários habilitados podem criar agentes e apenas 10% criarem 2 agentes cada, o estate potencial já ultrapassa 1.000 agentes — antes de qualquer iniciativa corporativa.

## Registro de gargalos manuais

Backlog dos pontos onde a governança depende de trabalho humano repetitivo. É o insumo direto da decisão sobre o que virar policy-as-code.

| Atividade manual | Volume/mês | Lead time | Risco de automatizar | Decisão inicial |
|---|---|---|---|---|
| aprovar agente T1 somente leitura | 400 | 2 dias | baixo | automatizar com policy gate após calibração em cohort controlada ou evidência equivalente |
| criar identidade de agente T2 | 40 | 4 dias | médio | workflow + API de IAM, mantendo caminho de exceção |
| revisar ferramenta privilegiada T3 | 5 | 5 dias | alto | manter decisão humana; automatizar o preparo da evidência |

A leitura correta da tabela é: **automatizar a preparação da evidência é quase sempre seguro; automatizar a decisão só quando a policy está estável.**

## Artefatos

- Agent Estate Inventory com confiança e data de corte;
- [Agent Registry 2.0](../../schemas/agent-registry.schema.json) e [exemplo preenchido](../../examples/agent-registry.example.json);
- Agent Estate Forecast em três cenários, com mix de risco;
- Manual Bottleneck Register priorizado por volume, lead time e risco.

## Evidências

- fontes consultadas, cobertura e limitações declaradas;
- baseline com data de corte e distribuição de confiança;
- backlog de remediação de objetos `probable` e `suspected`;
- forecast com premissas explícitas e revisão trimestral;
- medição de volume e lead time dos gargalos.

## Métricas

- cobertura do registry contra fontes independentes de descoberta;
- agentes descobertos por fonte e tempo até atribuição de owner;
- proporção `confirmed` / `probable` / `suspected` ao longo do tempo;
- shadow agents encontrados por ciclo de redescoberta;
- desvio entre forecast e estate real;
- gargalos manuais eliminados por trimestre.

## Failure modes

- tratar o baseline como conclusão em vez de ponto de partida;
- descartar sinais incertos para não "poluir" a métrica;
- contar versões e instâncias como agentes distintos;
- forecast apresentado como previsão contratual;
- projetar volume sem projetar mix de risco;
- automatizar decisões antes de estabilizar a policy;
- baseline sem data de corte — impossível de auditar depois.

## Decision gate

O baseline só é aceito com data de corte, cobertura mensurável por fonte, gaps registrados com owner e distribuições de status e confidence declaradas separadamente. Cobertura desconhecida é gap crítico, não ausência de risco.
