# Instruções para agentes de IA

## Objetivo do repositório

Este repositório contém o framework de governança de agentes de IA corporativo — policy, controles, lifecycle e templates.

## Princípios fundamentais

1. Não tratar hipótese como fato.
2. Não tratar resultado experimental como padrão aceito.
3. Nunca alterar silenciosamente uma ADR `Accepted`; criar nova ADR e marcar a anterior como `Superseded`.
4. Priorizar fontes primárias e registrar data de acesso ou revisão quando a informação for temporal.
5. Diferenciar explicitamente evidência, interpretação, recomendação e decisão.
6. Não duplicar conteúdo existente.
7. Usar links relativos entre documentos do repositório.
8. Preservar histórico e rastreabilidade.
9. Preferir alterações pequenas, reversíveis e revisáveis.
10. Declarar limitações, incertezas e horizonte de validade.

## Classificação dos artefatos

| Artefato | Finalidade |
|---|---|
| `docs/governance/` | Policy, operating model, lifecycle, controles |
| `docs/identity/` | Identidade, autenticação e autorização de agentes |
| `docs/tool-governance/` | Aprovação de ferramentas, sandbox e gates |
| `docs/data-access/` | Classificação de dados, DLP e proveniência |
| `docs/risk-management/` | Taxonomia de riscos e blast radius |
| `docs/evaluations/` | Quality gates e avaliação contínua |
| `docs/auditability/` | Logs, trail retention e evidência de conformidade |
| `docs/human-oversight/` | HITL, approval flows e escalonamento |
| `docs/responsible-ai/` | Princípios, controles, safety e monitoring |
| `docs/executive/` | Briefs executivos e comunicação orientada a decisão |
| `schemas/` | Schemas JSON/YAML para catálogo e auto-avaliação |
| `controls/` | Biblioteca de controles mapeando policy para implementações |
| `templates/` | Modelos de auto-avaliação, checklist e sunset |
| `examples/` | Exemplos práticos e case studies |

## Antes de criar ou alterar conteúdo

O agente deve:

1. Ler o README da área de destino.
2. Pesquisar documentos relacionados e possíveis duplicações.
3. Verificar ADRs existentes e possíveis conflitos.
4. Classificar o artefato pelo estágio de maturidade, não apenas pelo assunto.
5. Declarar os arquivos que serão criados ou alterados.
6. Preparar plano quando a mudança envolver mais de três arquivos.
7. Confirmar com o usuário antes de uma reorganização ampla ou migração.

## Regras para ADR

- Criar ADR somente para decisões arquitetonicamente significativas.
- Usar apenas: `Proposed`, `Accepted`, `Rejected`, `Superseded`, `Deprecated`.
- Registrar contexto, forças, alternativas, decisão, justificativa, consequências, riscos, validação e evidências.
- Não apagar ADRs rejeitadas ou substituídas.
- Ao mudar uma decisão aceita: criar nova ADR, atualizar as referências cruzadas e o índice.

## Regras de policy

- O documento principal de policy em `docs/governance/` é o artefato mais sensível.
- Qualquer modificação deve ser revisada antes de merge.
- Alterações de policy devem incluir changelog entry explicando o motivo.
- Versões antigas da policy devem ser preservadas, nunca reescritas.

## Metadados

Quando aplicável, usar front matter com:

- `status`: `draft`, `review`, `stable`, `deprecated` ou `archived`;
- `maturity`: `hypothesis`, `observed`, `validated` ou `adopted`;
- `last_reviewed` e `review_cycle`;
- owners, tags e artefatos relacionados.

Combinações incoerentes, como `status: stable` e `maturity: hypothesis`, devem ser reportadas.

## Qualidade mínima antes de concluir

- verificar links e referências;
- verificar conflitos com ADRs;
- confirmar que conclusões são suportadas pelas evidências;
- declarar limitações e confiança;
- atualizar índices, README, ROADMAP ou CHANGELOG quando aplicável;
- validar nomes, estados e links relativos;
- inspecionar o diff Git;
- executar as verificações disponíveis.