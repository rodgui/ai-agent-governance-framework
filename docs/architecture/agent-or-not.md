---
title: Decisão arquitetural — agente é o mecanismo certo?
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - overview.md
  - principles.md
  - ../risk-management/README.md
  - ../../templates/use-case-intake.md
---

# Decisão arquitetural — agente é o mecanismo certo?

## Objetivo

O primeiro gate não é "qual plataforma usar". É **"precisamos mesmo de um agente?"**.

Comportamento agentic aumenta variabilidade, custo de observabilidade e superfície de risco. Deve existir uma razão explícita para introduzir autonomia ou raciocínio probabilístico — e essa razão precisa estar registrada, não pressuposta.

Processos determinísticos, estáveis e integralmente especificáveis costumam ser melhor atendidos por workflow, automação tradicional ou uma chamada de API.

## Árvore de decisão

Percorra na ordem. Cada resposta muda o que precisa ser desenhado, não apenas o que precisa ser aprovado.

**1. O problema exige interpretação de linguagem, contexto variável, planejamento ou seleção dinâmica de ferramentas?**
Se não — prefira solução determinística e **registre a alternativa escolhida**. Essa é uma decisão arquitetural legítima, não uma desistência.

**2. A saída é apenas conteúdo ou pode gerar ação?**
Ação introduz exigências de autorização, rollback, trilha de auditoria e lifecycle que conteúdo não tem.

**3. A ação é reversível?**
Irreversível ou material eleva o controle: avalie aprovação humana, step-up e circuit breaker antes de decidir a plataforma.

**4. O agente acessará dados classificados?**
Confirme que a fonte está certificada ou registre a remediação **antes** do go-live, conforme o [gate de dados](../data-access/README.md).

**5. Opera com usuário presente ou de forma autônoma?**
Isso decide identidade delegada versus [identidade própria](../identity/README.md) — e não pode ser decidido depois.

**6. Há ferramentas, APIs ou servidores MCP?**
Classifique **cada ação**. O tier do agente não substitui a classificação da ferramenta.

**7. O uso afeta pessoas, direitos, oportunidades, segurança física, processo regulado ou comunicação pública?**
Aciona o impact trigger screen e, quando aplicável, o [impact assessment](../responsible-ai/README.md#impact-assessment).

**8. Onde cada controle vai residir?**
Management plane, gateway de runtime, broker de ferramentas, IAM, plataforma de dados, aplicação ou processo humano. **Não concentre controle no prompt** — prompt é instrução, não enforcement.

## Exemplos de decisão

| Caso | Decisão arquitetural | Por quê |
|---|---|---|
| assistente de conhecimento | recuperação somente leitura, identidade delegada, fontes certificadas, sem ferramenta de escrita | o valor vem de interpretação e recuperação; ação transacional seria risco sem benefício |
| agente de service desk | identidade própria, catálogo de ferramentas para criar e atualizar chamados, rollback e telemetria | há escrita reversível e operação multiusuário; a atribuição precisa sobreviver à ausência do usuário |
| agente de contas a pagar | identidade própria, broker de ferramentas, serviço de aprovação para pagamento, segregação de funções | o escalador financeiro impede execução autônoma irrestrita |
| agente de operações de produção | control plane de runtime, mediação de ferramenta privilegiada, remediações pré-aprovadas, circuit breaker | **a ferramenta é mais crítica que o modelo**; o comando precisa ser autorizado fora do modelo |

O último caso é o mais instrutivo: quando a ferramenta é privilegiada, a discussão sobre qual modelo usar é secundária. O controle está na autorização da ação, não na qualidade do raciocínio.

## Onde registrar

A decisão vai no [intake do caso de uso](../../templates/use-case-intake.md) e, quando arquiteturalmente relevante, num [ADR](../../templates/adr-template.md).

Se a resposta for "não precisamos de agente", **registre assim mesmo**. Decisão de não construir é a mais barata do portfólio e a que menos costuma ser documentada — o que faz a mesma discussão voltar seis meses depois.

## Definition of done

- a opção agentic foi comparada com alternativas determinísticas, e a comparação está registrada;
- modo de identidade, fontes de dados, ferramentas, nível de autonomia, oversight humano e controles de runtime estão explícitos;
- está declarado **onde cada policy será aplicada e onde a evidência será coletada**;
- as mudanças materiais que exigem reavaliação foram definidas **antes** do desenvolvimento começar.

## Failure modes

- começar pela plataforma e derivar o desenho dela;
- tratar "é IA" como justificativa em vez de decisão;
- classificar o agente e esquecer de classificar cada ferramenta;
- deixar o controle no prompt porque é o lugar mais fácil de escrever;
- decidir identidade depois do build, quando trocar custa reescrita;
- não registrar a decisão de **não** usar agente.
