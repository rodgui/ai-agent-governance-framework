# Template — Autoavaliação de agente de IA

Preencha antes de solicitar aprovação de design, release ou mudança material. Respostas sem evidência devem ser marcadas como `missing`, não presumidas como atendidas.

## 1. Identificação e finalidade

- Agent ID:
- Nome:
- Versão do blueprint:
- Business owner:
- Technical owner:
- Finalidade autorizada:
- Usuários e regiões:
- Outcome esperado e métrica:
- Usos explicitamente proibidos:

## 2. Alcance, dados e impacto

- Processos ou direitos afetados:
- Sistemas e integrações:
- Categorias e classificação dos dados:
- Origem, qualidade e retenção dos dados:
- População e volume estimados:
- Impactos sobre pessoas, finanças, operações e reputação:
- Tier de risco proposto e rationale:

## 3. Autonomia, tools e autoridade

Para cada tool ou ação, registre capability, scopes, condição de uso, reversibilidade, approval mode e enforcement técnico.

| Tool/ação | Capability | State-changing | Scopes | Reversível | Aprovação | Gateway/controle |
|---|---|---|---|---|---|---|
| | | | | | | |

- Decision rights aplicáveis:
- Human accountability boundary:
- Segregation of duties:
- Kill switch, quarantine e rollback:
- Ações que o agente não pode executar:

## 4. Controls e evidências

| Control ID | Implementação | Owner | Evidência | Status |
|---|---|---|---|---|
| | | | | `missing` |

- Evidence package:
- Exceptions abertas, owner e expiry:
- Riscos residuais e autoridade de aceitação:

## 5. Evaluation e release

- Testes funcionais e de integração:
- Prompt injection e conteúdo adversarial:
- Exfiltração, acesso indevido e isolamento:
- Qualidade, safety, fairness e human oversight aplicáveis:
- Tool-use, autorização e ações inesperadas:
- Cenários de falha, rollback e recuperação:
- Release evidence e disposition:

## 6. Operação e lifecycle

- Logs, métricas, alertas e retenção:
- Thresholds de containment:
- Incident owner e escalation path:
- Frequência de review e attestation:
- Critérios de suspensão, reativação e sunset:

## 7. Disposition

- Gate solicitado:
- Decisão: `approved` / `conditional` / `rejected` / `expired`
- Decision authority:
- Condições e prazo:
- Evidence refs:

Use a [policy de governança de agentes](../docs/governance/policy.md), o [operating model](../docs/governance/operating-model.md), o [playbook](../docs/guides/framework-implementation-playbook.md) e os [schemas](../schemas/README.md) como referências correntes.
