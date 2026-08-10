---
title: Capability map — atual versus alvo
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - maturity-model.md
  - implementation-program-24-weeks.md
  - ../architecture/overview.md
  - ../../examples/target-maturity-roadmap.example.md
---

# Capability map — atual versus alvo

## Objetivo

Separar **o que a organização precisa saber fazer** de **qual ferramenta vai implementar**. O capability map existe para evitar o erro mais caro de um programa de governança: comprar tecnologia para um problema que é, na verdade, ausência de processo, ownership, dados ou decision rights.

## O que é uma capability

Uma capacidade organizacional de produzir um resultado **de forma repetível**. Não é uma ferramenta, um time nem um projeto.

"Agent registry" é uma capability quando a empresa consegue descobrir, registrar, manter e consultar agentes com qualidade conhecida. Uma plataforma pode implementar parte dela — não é ela.

O teste: se você trocar o produto e a capacidade desaparecer, você comprou uma ferramenta e chamou de capability.

## As capacidades do framework

Ponto de partida: os [domínios canônicos](../architecture/overview.md#domínios-canônicos-por-plano). Quebre uma capability em duas apenas quando a filha tiver owner, processo **ou** evidência diferentes.

| Capacidade | Pergunta de diagnóstico | Sinal típico de estado inicial | Alvo comum |
| --- | --- | --- | --- |
| estratégia e governança | existe mandato, portfólio, funding e decisão clara? | política genérica de IA, sem charter ou priorização de agentes | charter aprovado, fóruns, decision rights, risk appetite e portfolio review |
| estate inventory e registry | sabemos quais agentes existem, onde operam e quem responde? | planilhas por plataforma e baixa cobertura de shadow agents | discovery contínuo + registry corporativo reconciliável |
| risco e Responsible AI | risco, admissibilidade e impacto roteiam controles? | mesma review para todos os casos | tiers, admissibilidade, escaladores e impact assessment por gatilho |
| lifecycle e Agent SDLC | versões, estados e mudanças estão governados? | publicação ad hoc e approvals permanentes | stage/state, gates, transition history, attestation e retirada |
| identidade e acesso | cada ação é atribuível e autorizada? | chaves e contas de serviço compartilhadas | identidade própria por agente, least privilege, JML e delegação quando aplicável |
| dados e conhecimento | as fontes são classificadas, permitidas e AI-ready? | recuperação sobre qualquer pasta autorizada | catálogo de fontes certificadas com lineage, restrictions e recertification |
| tools, APIs e MCP | as ações são catalogadas, limitadas e mediadas? | ferramentas embutidas por time | enterprise tool registry, gateway e autorização por ação/parâmetro |
| modelos e provedores | combinações e versões possuem critérios de admissão e saída? | escolha por preferência do time | catálogo provider/model/version, evaluation binding, fallback e exit strategy |
| runtime e plataforma | existem enforcement, isolamento, resiliência e rollback? | acesso direto a endpoints e configuração por agente | control plane, policy enforcement, budgets, containment e recovery patterns |
| segurança e AgentSecOps | ameaças agentic entram em prevention, detection e response? | SOC vê apenas logs tradicionais | threat model agentic, red teaming, supply-chain controls e incident integration |
| observabilidade e behavioral analytics | é possível reconstruir, detectar desvio e agir? | logs de aplicação sem correlation ou owner action | event envelope, traces, baselines, thresholds, runbooks e feedback loop |
| FinOps | custo é atribuível a agente, tarefa e outcome? | custo por chave ou centro de custo agregado | budgets, unit economics, anomaly response e arquitetura guiada por custo/qualidade |
| value realization | outcomes influenciam funding, expansão e sunset? | contagem de agentes e relatos de benefício | baseline, KPI, attribution caveats e portfolio decisions por evidência |
| assurance e auditabilidade | controls e decisões podem ser testados por challenge apropriado? | evidence preparada manualmente para auditoria | continuous evidence, segregation, sampling, findings e assurance proporcional |
| adoção, suporte e competências | cada papel consegue usar a rota governada corretamente? | treinamento pontual e suporte informal | currículo por papel, champions, support model e feedback incorporado aos standards |

## Crosswalk para maturity e controls

O framework mantém **15 capabilities** para planejamento porque elas podem ter owners, processos e evidências diferentes. O [maturity model](maturity-model.md) agrega essas capacidades em dez dimensões para scoring; agregação de score não funde accountability.

| Capability | Dimensão(ões) do maturity model | Domínios de controls principais |
| --- | --- | --- |
| estratégia e governança | 1. Estratégia, portfólio e valor; 2. Policy, operating model e decision rights | `organization`, `value` |
| estate inventory e registry | 3. Registry, blueprint e lifecycle | `registry` |
| risco e Responsible AI | 7. Risco, Responsible AI e human oversight | `risk`, `responsible-ai` |
| lifecycle e Agent SDLC | 3. Registry, blueprint e lifecycle; 8. Evaluations e release | `lifecycle`, `registry`, `evaluation` |
| identidade e acesso | 4. Identidade e acesso | `identity` |
| dados e conhecimento | 5. Dados e connectors | `data` |
| tools, APIs e MCP | 6. Tools, APIs e MCP | `tools` |
| modelos e provedores | 8. Evaluations e release | `model`, `evaluation` |
| runtime e plataforma | 9. Auditabilidade e operações | `operations`, `security` |
| segurança e AgentSecOps | 6. Tools, APIs e MCP; 9. Auditabilidade e operações | `security`, `tools`, `audit` |
| observabilidade e behavioral analytics | 9. Auditabilidade e operações | `audit`, `operations` |
| FinOps | 1. Estratégia, portfólio e valor; 9. Auditabilidade e operações | `value`, `operations` |
| value realization | 1. Estratégia, portfólio e valor | `value` |
| assurance e auditabilidade | 2, 7, 8 e 9 | `organization`, `audit`, `evaluation`, `risk` |
| adoção, suporte e competências | 10. Adoção, suporte e competência | `adoption` |

Use o crosswalk para navegar, não para declarar equivalência um-para-um. Uma capability pode depender de vários domínios, e um control pode contribuir para mais de uma capability.

## Procedimento

1. **Listar as capacidades** necessárias ao operating model.
2. **Escrever uma frase de outcome** para cada uma. Exemplo: *"toda ação material de agente é atribuível a uma identidade conhecida e autorizada"*.
3. **Definir evidências observáveis do estado atual.** Evite "o controle de acesso é forte". Prefira: *"74% dos T2/T3 usam identidade dedicada; 26% usam chave compartilhada"*.
4. **Atribuir maturidade com base em evidência** e registrar confidence. Evidência fraca produz nota provisória, não nota otimista.
5. **Definir o alvo por horizonte e necessidade de negócio.** Nem toda capacidade precisa do nível máximo; nível 3 costuma bastar no primeiro ano.
6. **Identificar dependências.** Behavioral analytics confiável depende de identidade própria e telemetria consistente — priorizá-la antes disso desperdiça o investimento.
7. **Converter gaps materiais em iniciativas** do roadmap de maturidade.

## Exemplo

| Capability | Estado atual observado | Alvo 12m | Gap concreto | Iniciativa |
|---|---|---|---|---|
| identidade | chaves compartilhadas; owner não rastreável em 30% dos agentes transacionais | 100% de T2/T3 com identidade própria, JML e rotação | atribuição, lifecycle e least privilege insuficientes | padrão de identidade + onboarding + automação de JML |
| tools e MCP | ferramentas embutidas por time, sem catálogo nem classificação de ação | ferramentas críticas registradas, classificadas e mediadas | sem visão da capacidade executável nem do risco por ação | tool registry + broker + autorização por parâmetro |
| observabilidade | logs de aplicação; custo por chave; sem correlação agente-tarefa-ferramenta | schema de telemetria e dashboards por decisão | impossível investigar um agente ou medir custo por resultado | schema + correlation IDs + pipeline |

Repare no primeiro: o gap **não é "comprar IAM"**. É identidade não humana por agente, least privilege, lifecycle de owner, gestão de secrets e auditabilidade. Nenhum produto entrega isso sozinho.

## Perguntas de challenge

Aplique antes de aprovar o alvo:

- o alvo é necessário para o risco e o volume previstos, ou está sendo escolhido por ambição tecnológica?
- existe dependência invisível em outra capacidade que pode bloquear a iniciativa?
- o alvo pode ser demonstrado por evidência objetiva?
- **existe owner capaz de sustentar a capacidade depois que o programa terminar?**

A última derruba mais iniciativas que as outras três somadas.

## Relação com o maturity model

O capability map responde "o que precisamos saber fazer e onde estamos". O [maturity model](maturity-model.md) fornece a escala, as âncoras de confidence e o método de avaliação por evidência. O [roadmap de maturidade](../../examples/target-maturity-roadmap.example.md) converte os gaps em sequência.

Usar o capability map sem o método de assessment produz nota por percepção — que é o antipattern que o maturity model existe para evitar.

## Failure modes

- mapear produtos e chamar de capacidades;
- quebrar capacidades até virarem tarefas, perdendo o nível de decisão;
- alvo máximo em tudo, ignorando dependência e capacidade operacional;
- estado atual descrito por adjetivo em vez de medida;
- ignorar que uma capacidade em nível baixo pode inutilizar outra em nível alto;
- aprovar alvo sem owner que o sustente depois do programa.
