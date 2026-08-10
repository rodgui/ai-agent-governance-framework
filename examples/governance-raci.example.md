# Exemplo — RACI de governança de agentes

> Fictício e sanitizado. Substitua os papéis pelos equivalentes corporativos antes de usar.

Demonstra o [operating model e decision rights](../docs/governance/operating-model.md). A regra estruturante: **um único `A` por decisão material**. Célula vazia é preferível a inventar participação que não existe.

`R` executa · `A` responde pela decisão · `C` é consultado antes · `I` é informado depois

| Decisão | Business Owner | Technical Owner | Governance Office | Função de controle | Plataforma/Ops | SLA |
|---|---|---|---|---|---|---|
| definir finalidade e outcome | **A** | C | I | | | — |
| classificar risco e rota | C | R | **A** | C | | 2 dias |
| conceder identidade e permissões | I | R | | **A** (Identidade) | R | 3 dias |
| aprovar fonte de dados | C | R | I | **A** (Dados) | | 5 dias |
| aprovar ferramenta ou servidor MCP | I | R | C | **A** (Segurança) | C | 5 dias |
| decisão de publicação | C | C | **A** | C | R | por tier |
| aceitar risco residual | **A** | C | C | C | | — |
| conter ou colocar em quarentena | I | C | I | C | **A** (Run Authority) | imediato |
| reativar após contenção | C | R | I | C | **A** | após regression |
| aprovar exceção | C | I | **A** | C | I | com expiry |
| attestation periódica | **A** | R | I | | I | por tier |
| aposentar | **A** | R | I | | R | 15 dias de grace |

## Leituras que este RACI força

**Contenção não espera comitê.** A Run Authority é `A` em quarentena e o Governance Office é apenas `I`. Se conter exigisse aprovação colegiada, a contenção não existiria na prática.

**Quem constrói não aceita o próprio risco residual.** O Technical Owner é `C`, nunca `A`, em aceitação de risco residual — isso pertence a quem responde pelo impacto no negócio. É o `AGF-ORG-002` aplicado.

**Reativar é mais caro que conter.** Conter tem `A` único e SLA imediato; reativar exige `A` da Run Authority *e* evidência de regressão, com o Technical Owner como `R`.

**Aprovar dados e aprovar ferramentas são authorities diferentes.** Concentrar as duas no mesmo papel é o atalho mais comum e o que mais produz aprovação de conveniência.

## O que este exemplo não demonstra

- não define os papéis corporativos — apenas as funções de decisão;
- SLAs são ilustrativos e devem sair do baseline real de capacidade;
- um RACI não substitui o [contrato de decision gates](../docs/guides/framework-implementation-playbook.md#contrato-comum-dos-decision-gates): ele diz quem decide, não o que a decisão precisa registrar;
- em organizações pequenas, papéis podem se acumular na mesma pessoa — desde que a segregação exigida pelo tier seja preservada e a acumulação seja declarada.
