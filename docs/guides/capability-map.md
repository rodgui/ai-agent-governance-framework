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
|---|---|---|---|
| estratégia e governança | existe mandato, escopo e decisão clara? | política genérica de IA, sem charter de agentes | charter aprovado, fóruns, decision rights, processo de exceção |
| estate e registry | sabemos quais agentes existem e quem responde? | planilhas por plataforma | discovery contínuo + registry corporativo reconciliável |
| risco e Responsible AI | risco e impacto roteiam controles? | mesma review para todos os casos | tiers, escaladores e impact assessment por gatilho |
| lifecycle | estados e mudanças estão definidos? | publicação ad hoc | state machine, gates, attestation e retirada |
| identidade e acesso | cada ação é atribuível? | chaves e contas de serviço compartilhadas | identidade própria por agente e delegação quando aplicável |
| dados e conhecimento | as fontes são classificadas e certificadas? | recuperação sobre qualquer pasta autorizada | catálogo de fontes certificadas com critérios AI-ready |
| tools e MCP | as ações são catalogadas e mediadas? | ferramentas embutidas por time | registry de tools, mediação e classificação por ação |
| modelos e provedores | há critérios de admissão e saída? | escolha por preferência do time | catálogo de combinações aprovadas com restrições |
| runtime e plataforma | existe ponto de enforcement? | acesso direto aos endpoints | gateway ou broker com policy aplicada |
| segurança | há threat model e resposta específicos? | operação de segurança vê apenas logs tradicionais | cenários de ameaça agentic, detecção e contenção |
| observabilidade e valor | dá para investigar e medir? | logs de aplicação e custo por chave | telemetria correlacionada e custo por resultado |
| adoção e competência | as pessoas conseguem executar? | treinamento pontual | currículo por papel e caminho governado mais fácil que o desvio |

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
