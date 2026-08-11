# Template — Cláusulas mínimas de contrato com fornecedor de IA

Checklist de exigências contratuais para provedores de modelo, plataforma de agentes, tool ou MCP server. Serve para **compras e jurídico traduzirem em contrato o que a governança decidiu** em [model governance](../docs/model-governance/README.md) e [tool governance](../docs/tool-governance/README.md).

> Este template **não é aconselhamento jurídico**. Cada cláusula precisa ser redigida pelo jurídico da organização, conforme a jurisdição, o setor e o poder de negociação. O que está aqui é o conjunto de assuntos que não pode ficar de fora — a redação é da sua casa.

## Como usar

1. Classifique o fornecedor pela **maior criticidade** que ele vai suportar. Um fornecedor que atende T3 precisa das cláusulas de T3, mesmo que comece em T1.
2. Marque cada cláusula como obrigatória, negociável ou não aplicável, **com rationale**.
3. O que o fornecedor recusar vira **risco declarado**, com compensating control e authority — não some da conversa.
4. Registre o resultado no [catálogo de modelos e provedores](../docs/model-governance/README.md) ou no registro de tools, conforme o caso.

## Identificação

- Fornecedor e produto:
- Papel no estate: modelo · plataforma · tool/MCP · integrador
- Maior tier que vai suportar: `T1` / `T2` / `T3` / `T4`
- Classes de dados envolvidas:
- Regiões de processamento e armazenamento:
- Owner do contrato / owner técnico:
- Data da avaliação:

## Cláusulas por assunto

### 1. Uso de dados

| # | Exigência | Por que importa | Mínimo por tier |
|---|---|---|---|
| 1.1 | dados do cliente **não são usados para treinar** modelos do fornecedor ou de terceiros, nem para melhoria de serviço, sem consentimento específico e revogável | é o item que mais frequentemente vem permissivo por default e o mais difícil de reverter depois | T1+ |
| 1.2 | subprocessadores nomeados, com aviso prévio e direito de objeção a novos | sem isso o dado circula por cadeia desconhecida | T2+ |
| 1.3 | região de processamento e de armazenamento definidas contratualmente, incluindo failover | região de contingência costuma ser o furo | T2+ |
| 1.4 | retenção máxima de prompts, outputs e logs, com exclusão verificável | "retemos por período razoável" não é cláusula | T2+ |
| 1.5 | proibição de uso de dado do cliente para benchmark, marketing ou caso de estudo sem aprovação escrita | aparece como cortesia comercial e vaza escopo | T3+ |

### 2. Modelo, versão e mudança

| # | Exigência | Por que importa | Mínimo por tier |
|---|---|---|---|
| 2.1 | identificação de **modelo e versão**, com pinning disponível | sem versão fixa, não existe avaliação válida | T2+ |
| 2.2 | aviso prévio mínimo de mudança de versão, depreciação ou alteração de comportamento, com janela declarada | mudança silenciosa invalida evidência já aceita | T2+ |
| 2.3 | direito de permanecer na versão anterior durante a janela de reavaliação | aviso sem direito de permanência é aviso inútil | T3+ |
| 2.4 | descrição das mudanças que afetam comportamento, não apenas o número da versão | "melhorias de qualidade" não permite decidir se reavalia | T3+ |

### 3. Auditoria e evidência

| # | Exigência | Por que importa | Mínimo por tier |
|---|---|---|---|
| 3.1 | relatórios de certificação vigentes e escopo declarado | o escopo importa mais que o selo | T1+ |
| 3.2 | direito de auditoria — direta, por terceiro independente ou por relatório equivalente | sem alguma forma, a asseguração é declaratória | T3+ |
| 3.3 | acesso a logs suficientes para investigar incidente do lado do cliente | investigar sem log do fornecedor é reconstruir por dedução | T2+ |
| 3.4 | cooperação em investigação regulatória e prazo de resposta | o prazo do regulador não espera o SLA comercial | T3+ |

### 4. Segurança e incidentes

| # | Exigência | Por que importa | Mínimo por tier |
|---|---|---|---|
| 4.1 | notificação de incidente com prazo em horas, não "sem demora indevida" | prazo vago é prazo do fornecedor | T2+ |
| 4.2 | notificação também de incidente **em subprocessador** | a cadeia é onde o incidente costuma nascer | T2+ |
| 4.3 | isolamento de tenant e de dados declarado, com controles de segregação | multi-tenant sem segregação declarada é risco não avaliado | T3+ |
| 4.4 | teste de segurança periódico e correção de vulnerabilidade com SLA por severidade | sem SLA, a correção compete com o roadmap comercial | T3+ |

### 5. Continuidade e saída

| # | Exigência | Por que importa | Mínimo por tier |
|---|---|---|---|
| 5.1 | portabilidade de configuração, prompts, avaliações e logs em formato utilizável | exportar em PDF não é portabilidade | T2+ |
| 5.2 | prazo de transição assistida em caso de rescisão ou descontinuação | o pior momento para migrar é o momento em que se é obrigado a migrar | T3+ |
| 5.3 | exclusão verificável dos dados ao término, com atestado | "excluímos conforme política interna" não é verificável | T2+ |
| 5.4 | continuidade em caso de aquisição, mudança de controle ou fim de vida do produto | a cláusula que ninguém lê até precisar | T3+ |

### 6. Responsabilidade e conformidade

| # | Exigência | Por que importa | Mínimo por tier |
|---|---|---|---|
| 6.1 | responsabilidade por violação de propriedade intelectual em output gerado | é o item em que a alocação de risco varia mais entre fornecedores | T2+ |
| 6.2 | declaração de conformidade aplicável e compromisso de manutenção | conformidade na assinatura não é conformidade na renovação | T3+ |
| 6.3 | limitação de responsabilidade proporcional ao dano possível, não ao valor do contrato | contrato barato não significa dano barato | T3+ |
| 6.4 | direito de suspender o uso sem penalidade quando um control obrigatório deixa de ser satisfeito | é o que torna a suspensão por condição violada executável | T3+ |

## Resultado da avaliação

| Cláusula | Estado | Rationale | Compensating control | Owner | Revisão |
|---|---|---|---|---|---|
|  | aceita / negociada / recusada / não aplicável |  |  |  |  |

**Recusas materiais** viram entrada no risk register com residual risk declarado e authority compatível com o tier — não observação em ata.

## Antipatterns

- aceitar "conforme política do fornecedor" como cláusula, quando a política pode mudar unilateralmente;
- negociar apenas preço e SLA de disponibilidade, deixando uso de dados e mudança de versão no default;
- avaliar o fornecedor uma vez e nunca reabrir, mesmo após mudança de versão ou aquisição;
- tratar certificação como equivalente a auditoria, sem ler o escopo;
- aceitar prazo de notificação de incidente sem número.

## Relação com o resto do framework

Este template é o **instrumento contratual** de decisões tomadas em outro lugar. O critério de entrada de um modelo ou tool no catálogo está em [model governance](../docs/model-governance/README.md) e [tool governance](../docs/tool-governance/README.md); a exigência por tier está no [Minimum Production Bar](../docs/risk-management/minimum-production-bar.md); e a saída do fornecedor pertence ao [lifecycle](../docs/lifecycle/README.md).

Um fornecedor aprovado no catálogo e sem contrato compatível é gap de controle, não pendência administrativa.
