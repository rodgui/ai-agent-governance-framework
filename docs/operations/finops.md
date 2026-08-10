---
title: FinOps de agentes e unit economics
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - behavioral-analytics.md
  - ../value/README.md
  - ../model-governance/README.md
---

# FinOps de agentes e unit economics

## Objetivo

Sair de "custo por token" para **custo por resultado**, atribuir esse custo a um responsável e detectar desperdício antes que ele vire um problema de orçamento ou um vetor de abuso.

Um modelo mais caro por token pode ser economicamente melhor se reduzir retries e retrabalho humano. A comparação relevante é sempre **custo por tarefa concluída com qualidade preservada**.

## Atribuição

Todo custo material precisa responder a quatro perguntas: **qual agente, qual owner, qual unidade de negócio, qual caso de uso.**

Sem chave de correlação no evento de custo, FinOps enxerga gasto sem contexto e a decisão de portfólio vira opinião.

## Decomposição do custo

Separe as camadas quando forem materiais:

- inferência;
- retrieval e indexação;
- execução de ferramentas e chamadas externas;
- armazenamento e memória;
- observabilidade e retenção de evidência;
- **supervisão e aprovação humana** — frequentemente o maior custo em T3 e sistematicamente esquecido;
- custo de build e teste, separado do custo de produção.

## Unit economics

1. Definir a unidade de resultado do caso: ticket resolvido, fatura processada, documento revisado.
2. Medir custo por unidade **bem-sucedida**, não por execução. Tentativas falhas são custo do sucesso.
3. Comparar contra o baseline do processo anterior, com as limitações declaradas.
4. Incluir o custo humano de revisão quando o desenho exige aprovação.
5. Reavaliar após mudança de versão de modelo — o custo por tarefa pode mudar sem que o preço por token mude.

## Budget, quota e denial-of-wallet

- budget por caso de uso e por tier, não apenas orçamento global;
- quota e circuit breaker por agente, com limite de chamadas, profundidade de cadeia e duração;
- loops e retries descontrolados são simultaneamente problema de custo e sinal de segurança — veja [behavioral analytics](behavioral-analytics.md);
- notificação ao owner antes de enforcement automático;
- exceção de budget com prazo, como qualquer outra exceção.

O ataque de *denial-of-wallet* não derruba o sistema: ele o torna economicamente inviável. Um agente exposto sem quota é uma superfície de custo aberta.

## Alavancas de otimização

Cache · tamanho de contexto e estratégia de recuperação · roteamento entre modelos com equivalência de controles · redução de profundidade de cadeia · reuso de resultados · escolha de ferramenta com menor custo por chamada.

Nenhuma alavanca pode reduzir silenciosamente o nível de assurance. Roteamento por custo segue as regras de [governança de modelos](../model-governance/README.md#fallback-routing-e-equivalência-de-controles).

## Integração com portfólio

O custo total entra na [decisão de portfólio](../value/README.md#value-review): manter, expandir, corrigir, restringir, substituir ou aposentar. Um agente com bom outcome e unit economics ruim é candidato a redesenho, não a expansão.

## Evidências

- modelo de custo com premissas e fontes;
- atribuição por agente, owner, unidade e caso;
- custo por resultado com baseline e limitações;
- budgets, quotas e exceções vigentes;
- anomalias de custo investigadas e desfecho;
- variação de custo após mudança de versão de modelo.

## Métricas

- custo por agente, por sessão e por resultado bem-sucedido;
- variação contra budget por tier e por unidade;
- proporção de custo gasto em execuções que falharam;
- agentes sem budget ou sem quota em produção;
- anomalias de custo por período e tempo até resposta;
- custo de supervisão humana como fração do total em T3;
- concentração de custo por provedor e modelo.

## Failure modes

- comparar apenas preço por token;
- medir custo por execução em vez de por sucesso;
- ignorar o custo de supervisão, suporte e assurance;
- orçamento global sem quota por agente;
- automatizar corte de budget sem notificar o owner;
- otimizar custo trocando modelo sem equivalência de controles;
- tratar pico de custo apenas como tema financeiro quando também é sinal de segurança.

## Decision gate

Nenhum agente entra em produção sem atribuição de custo, budget do caso e quota compatível com o tier. Nenhuma decisão de expandir portfólio é tomada sem custo por resultado medido contra baseline.
