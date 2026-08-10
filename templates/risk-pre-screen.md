# Template — Risk pre-screen de agente

Questionário objetivo aplicado no intake, antes do scoring completo. Serve para **roteamento rápido** e para acionar escaladores e impact assessment.

O pre-screen **não substitui** a avaliação de risco. Ele decide qual rota o caso segue e o que precisa ser aprofundado. Consulte [gestão proporcional de riscos](../docs/risk-management/README.md) e o [Minimum Production Bar](../docs/risk-management/minimum-production-bar.md).

## Identificação

- Agent ID:
- Nome:
- Business owner:
- Technical owner:
- Caso de uso e processo afetado:
- Data do pre-screen:
- Responsável pelo preenchimento:
- Versão do modelo de risco aplicada:

## Questionário

Responda `sim`, `não` ou `não sei`. **`Não sei` não é `não`** — é um gap que precisa de owner e prazo antes da classificação final.

| # | Pergunta | Resposta | Evidência ou observação |
|---:|---|---|---|
| 1 | O agente acessará dados confidenciais ou restritos? | | |
| 2 | O agente executará ações de escrita? | | |
| 3 | Alguma ação é irreversível ou materialmente relevante? | | |
| 4 | Fará comunicação externa sem revisão humana? | | |
| 5 | Usará privilégio elevado ou administrativo? | | |
| 6 | Pode afetar emprego, crédito, elegibilidade ou acesso a serviço de pessoas? | | |
| 7 | Atua em processo safety-critical ou de tecnologia operacional? | | |
| 8 | Acessará a internet ou ferramentas externas de forma dinâmica? | | |
| 9 | Executará código ou comandos? | | |
| 10 | Manipulará identidade, permissão ou secrets? | | |
| 11 | Envolverá múltiplos agentes ou delegação em cadeia? | | |
| 12 | Continuará executando sem usuário presente? | | |
| 13 | Usará memória persistente? | | |
| 14 | Terá alcance corporativo ou público? | | |
| 15 | Existe rollback ou kill switch testável? | | |

## Leitura do resultado

- **Qualquer `sim` nas perguntas 3, 5, 6, 7, 9, 10** aciona escalador e retira o caso do fast path, independentemente do score.
- **Qualquer `sim` na pergunta 6** aciona o impact trigger screen de Responsible AI, mesmo em caso tecnicamente simples.
- **`Não` na pergunta 15**, combinado com `sim` em 2 ou 3, é bloqueador: capacidade de ação sem contenção testável não vai a produção.
- **`Não sei` em qualquer item** impede a conclusão da classificação. Registre owner e prazo.

## Encaminhamento

- Tier proposto: `T1 fast path` / `T1` / `T2` / `T3` / `T4`
- Admissibilidade preliminar: `permitted` / `conditional` / `restricted` / `prohibited`
- Rationale e authority necessárias para admissibilidade:
- Escaladores acionados:
- Impact assessment requerido: `sim` / `não`
- Domain reviews acionadas:
- Gaps com owner e prazo:
- Rationale da rota:

O pre-screen é evidência: registre-o com data, responsável e versão do modelo de risco. A classificação e a admissibilidade finais, com suas authorities, são registradas conforme o [contrato de decision gates](../docs/guides/framework-implementation-playbook.md#contrato-comum-dos-decision-gates).
