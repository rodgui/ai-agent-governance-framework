# Exemplo — Autoavaliação de agente de IA

Exemplo fictício e sanitizado. Não contém dados reais nem representa aprovação de produção.

## 1. Identificação e finalidade

- Agent ID: `AGENT-EXAMPLE-001`
- Nome: Assistente de triagem interna
- Versão do blueprint: `1.2.0`
- Business owner: Operations Director
- Technical owner: AI Platform Lead
- Finalidade autorizada: classificar solicitações internas e preparar uma resposta para revisão humana
- Usuários e regiões: equipe interna, uma região
- Outcome esperado: reduzir tempo de triagem sem delegar decisão final
- Uso proibido: aprovar solicitações, alterar registros ou enviar comunicação externa

## 2. Alcance, dados e impacto

- Dados: texto de solicitações internas com classificação `internal`
- Sistemas: fila de atendimento em ambiente de teste
- População estimada: 500 solicitações por mês
- Tier proposto: `T2`
- Rationale: alcance limitado e sem ação externa, mas com possível impacto operacional

## 3. Autonomia, tools e autoridade

| Tool/ação | Capability | State-changing | Scopes | Reversível | Aprovação | Gateway/controle |
|---|---|---|---|---|---|---|
| consultar fila | read | não | solicitações atribuídas | sim | automatizada | gateway de leitura |
| preparar rascunho | create | sim | resposta transitória | sim | revisão humana | workspace isolado |

- Human accountability boundary: o agente prepara; o analista decide e envia.
- Segregation of duties: o technical owner não aprova a finalidade nem aceita risco residual.
- Containment: bloquear tools e colocar o agente em quarantine.

## 4. Controls e evidências

| Control ID | Implementação | Owner | Evidência | Status |
|---|---|---|---|---|
| AGF-ORG-001 | owners e finalidade registrados | Business owner | `EV-001` | `passed` |
| AGF-TOL-001 | allowlist e scopes no gateway | Technical owner | `EV-002` | `passed` |
| AGF-EVL-001 | suíte de evaluation versionada | Evaluation owner | `EV-003` | `conditional` |

- Gap: teste de recuperação ainda incompleto.
- Condição: concluir `EV-004` antes do release.

## 5. Evaluation e release

- Prompt injection: aprovado nos casos definidos.
- Exfiltração: aprovado para os scopes testados.
- Tool-use: agente não envia nem altera registros.
- Release disposition: `conditional`.

## 6. Operação e lifecycle

- Logs: prompts, tool calls, decisões humanas e outcomes.
- Alertas: acesso negado, repetição anômala e queda de qualidade.
- Review: trimestral ou após mudança material.
- Sunset: remover integrações, revogar identidade e preservar evidências requeridas.

Este exemplo usa a [policy de governança de agentes](../docs/governance/policy.md) e não substitui evidência, review ou aprovação formal.
