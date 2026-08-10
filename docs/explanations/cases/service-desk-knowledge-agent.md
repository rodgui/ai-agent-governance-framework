---
title: "Caso de referência — Service Desk Knowledge Agent (T2)"
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - ../../guides/framework-implementation-playbook.md
  - ../../risk-management/minimum-production-bar.md
  - ../../auditability/evidence-pack-by-tier.md
---

# Caso de referência — Service Desk Knowledge Agent (T2)

> Caso fictício e sanitizado. Demonstra o percurso do framework; não representa deployment real, não é aceite de risco e seus thresholds não são recomendação.

## O caso em uma frase

Um agente interno que ajuda analistas de service desk a localizar procedimentos aprovados e preparar rascunhos de resposta — **sem alterar sistema nenhum**.

| | |
|---|---|
| `agentId` | `service-desk-knowledge-agent` |
| criticidade | **T2** |
| admissibilidade | `permitted` |
| capacidades | `observe`, `create` |
| decisão de release | `conditional`, com quatro condições e expiry |

A ausência de capacidade de escrita em sistema é o que mantém o caso em T2. Ela não é uma característica do agente: é **uma condição da aprovação**, e o próprio manifesto registra que qualquer tool que altere estado devolve o caso a G4.

## Por que este caso

T2 é o tier onde a governança realmente começa a custar. Abaixo dele o [fast path](../../risk-management/README.md#fast-path-de-t1) automatiza; acima dele quase tudo é obviamente necessário. T2 é onde alguém precisa julgar quanto é suficiente — e é por isso que ele serve como primeiro caso.

## Percurso pelos gates

Cada gate abaixo segue o [contrato comum](../../guides/framework-implementation-playbook.md): pré-condição, artefatos, authority, critério de saída.

### G0 — Mandato

O programa já tem mandato: charter, escopo e authorities aprovados. O caso entra dentro de uma fronteira existente, não a cria.

**Evidência:** [governance charter](../../../examples/governance-charter.example.md) · [RACI](../../../examples/governance-raci.example.md)

### G1 — Baseline

O agente aparece no estate por **descoberta**, não por autodeclaração. O registry guarda os dois eixos que a ADR-0010 separou: `status: confirmed` e `confidence: high` são coisas diferentes — um agente pode ser confirmado com confiança baixa, e tratá-los como uma escala só esconde exatamente os casos que precisam de atenção.

Dois sinais independentes sustentam a descoberta: control plane e inventário de identidade.

**Evidência:** [registry record](../../../examples/agent-registry.example.json) · [descoberta e forecast](../../registry/discovery-and-forecast.md)

### G2 — Fundações

Aqui o caso ganha identidade, dados e ferramentas — e as três são **vinculadas a catálogo**, não declaradas livremente.

| Fundação | O que ficou decidido |
|---|---|
| identidade | modelo `hybrid`, principal `workload://…`, escopos `knowledge.search` e `draft.create`, token de curta duração |
| dados | uma fonte certificada, `internal`, autorização pré-recuperação |
| tools | duas, ambas `observe`/`create`, nenhuma alterando estado |

O blueprint referencia `catalogEntryId` em modelo, fonte e tool. O CI verifica que cada binding existe no catálogo, que o tier do caso é permitido pela entrada, que os escopos não excedem o autorizado e que a entrada não expirou antes da última revisão. **Blueprint que declara uma tool fora do catálogo não passa** — não por revisão humana, por validação.

**Evidência:** [blueprint](../../../examples/agent-blueprint.example.json) · [arquitetura](../../../examples/architecture.example.md)

### G3 — Operating model

Handoffs e decision rights vêm do programa, não do caso. O que o caso consome é a matriz: quem entrega o quê a quem, com qual evidência.

**Evidência:** [handoff matrix](../../../examples/handoff-matrix.example.md)

### G4 — Controls e assurance

A classificação combina dados internos, ação limitada a rascunho, alcance de uma unidade e alta reversibilidade → **T2**. Nenhum red flag disparou; se algum tivesse disparado, a [tabela de escaladores](../../risk-management/README.md#red-flags-e-escaladores) imporia a criticidade mínima independentemente do score.

Cinco controls foram exigidos, e o residual risk foi aceito **para este escopo e esta data de corte** — não em geral.

**Evidência:** [risk assessment](../../../examples/risk-assessment.example.md) · [evaluation report](../../../examples/evaluation-report.example.md)

### G5 — Release

A decisão foi **`conditional`**, não `approved`. Quatro condições, cada uma com owner e método de verificação declarados:

1. resposta a usuário externo exige revisão humana — verificada por amostragem mensal;
2. dado pessoal e credencial seguem proibidos — verificado por check automatizado no gateway;
3. connector novo ou tool que altere estado retorna a G4/G5 — verificado por diff de blueprint no pipeline;
4. quarentena e rollback exercitados antes de reativação — verificado por registro anexado ao evidence pack.

Expiry em 2026-11-01. Uma condição sem owner, sem método de verificação e sem prazo não é condição: é intenção.

**Evidência:** [release decision](../../../examples/release-decision.example.md) · [manifesto de evidência](../../../examples/release-evidence-manifest.example.json)

### G6 — Operação

O runtime precisa responder a três perguntas antes de a exposição crescer: dá para observar, dá para conter, dá para voltar atrás. O blueprint responde as três — correlação com redação de payload sensível, bloqueio de novas sessões pelo control plane com negação de tools no gateway, e retorno à última versão aprovada.

**Evidência:** [runbook de suporte](../../../examples/support-runbook.example.md) · [SLO](../../../examples/slo.example.md)

### G7 — Valor e lifecycle

Attestation válida até 2026-11-01, sunset previsto para 2027-08-01. O histórico de transição registra a passagem de `approved`/`not-deployed` para `production`/`enabled`, com authority, motivo e evidência — o estágio de lifecycle e o estado operacional são campos distintos, porque um agente aprovado e não implantado é diferente de um agente em produção desabilitado.

**Evidência:** [registry record](../../../examples/agent-registry.example.json) · [lifecycle](../../lifecycle/README.md)

## Cobertura dos domínios

| Domínio | Onde aparece no caso |
|---|---|
| risco | classificação T2, red flags, residual risk aceito com escopo e data de corte |
| identidade | modelo híbrido, escopos mínimos, token curto, segredo fora do prompt |
| dados | fonte única certificada, autorização pré-recuperação, classe `internal` |
| tools | duas tools em catálogo, nenhuma alterando estado, mediação no gateway |
| lifecycle | estágio e estado operacional separados, histórico de transição, attestation com expiry, sunset |
| observabilidade | correlação, redação de payload, quarentena, rollback, kill switch |
| assurance | evaluation report, evidence pack, manifesto verificável por máquina |

## O que a travessia encontrou

Escrever este percurso encontrou **três divergências** que a leitura por domínio não tinha encontrado. Registrá-las é mais útil do que apagá-las.

| Divergência | Como estava | Resolução |
|---|---|---|
| decisão de release | o registro dizia `condition` com quatro condições; o manifesto dizia `approved` sem condição nenhuma | manifesto passa a `conditional`, carregando as quatro condições com owner e verificação |
| contrato de release | o schema exigia `exceptionRefs` num release `conditional` | condição não é exceção — pelo glossário, exceção autoriza desvio de requisito e condição limita o escopo aprovado. O schema passa a exigir `conditions` e `expiresAt` |
| nome da authority | o histórico de transição dizia "Example Release Authority"; decisão e manifesto diziam "Example Design Authority" | normalizado; `Release Authority` é o papel, `Example Design Authority` é o corpo que decide |

A segunda é a mais relevante para quem for adotar o framework: exigir waiver para toda aprovação condicional empurra a organização a registrar exceção falsa, e exceção falsa contamina exatamente a métrica que deveria detectar acúmulo de risco.

## O que este caso não demonstra

Não demonstra eficácia — é fictício. Não cobre T1 nem T3, então não mostra proporcionalidade entre tiers. Não exercita admissibilidade diferente de `permitted`. E nenhum de seus controles foi executado contra um estate real, que é o critério 10 do [checklist de autossuficiência](../../reference/self-sufficiency-checklist.md) e segue aberto.
