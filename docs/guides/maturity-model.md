---
title: Maturity model de governança de IA e agentes
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: semiannual
supersedes: null
related:
  - framework-implementation-playbook.md
  - ../../schemas/maturity-assessment.schema.json
  - ../../templates/maturity-assessment-template.md
  - ../../examples/maturity-assessment.example.json
---

# Maturity model de governança de IA e agentes

## Objetivo

Estabelecer baseline, target state e roadmap com evidência. Maturidade mede capacidade organizacional; não mede risco de um agente e não certifica conformidade.

## Níveis

| Nível | Nome | Característica |
|---:|---|---|
| 0 | inexistente | atividade ausente ou desconhecida |
| 1 | ad hoc | depende de pessoas e decisões pontuais |
| 2 | definido | processo, owner e artefatos existem |
| 3 | gerenciado | execução e evidence são consistentes e medidos |
| 4 | adaptativo | controls são integrados, testados e melhorados por sinais |

## Regra de evidência

Um nível só é atribuído quando há evidência suficiente de operação, não apenas documento. Exemplo:

- policy escrita sem aplicação: no máximo nível 1;
- processo definido e usado em parte do escopo: nível 2 com coverage declarado;
- métricas, exceptions e remediação observadas: candidato a nível 3;
- automation testada e mudança baseada em outcomes: candidato a nível 4.

Quando evidência é conflitante, use o menor nível demonstrado e registre nuance.

## Modos de assessment

| Modo | Uso | Limite da conclusão |
|---|---|---|
| `self-assessment` | owners avaliam a própria capacidade | hipótese interna sujeita a challenge |
| `facilitated-assessment` | facilitador aplica o método com os owners | conclusão baseada no escopo e evidence cutoff declarados |
| `peer-review` | função distinta revisa evidências e rationale | challenge interno; não implica independência formal |
| `limited-scope-review` | revisão delimitada de claims e controles selecionados | conclusão somente sobre a amostra; não é audit, certification ou attestation |

O rótulo `independent assessment` não é usado nesta versão. Ele só pode ser adotado quando engagement, conflitos, reporting line, serviços incompatíveis, amostragem e forma da conclusão estiverem definidos e aprovados. Quem desenhou ou implementou o objeto avaliado deve declarar o conflito e não pode emitir conclusão independente sobre o próprio trabalho.

## Evidence register, sampling e rastreabilidade

Cada evidência recebe ID estável, tipo, referência recuperável, data observada, coletor, escopo e limitações; hash SHA-256 é recomendado para snapshots imutáveis. Dimensões apontam para `evidenceRefs`, não para descrições soltas.

O assessment registra população, método de amostragem, tamanho da população e amostra, rationale e limitações. `Coverage` é calculado contra uma base declarada por dimensão; não é um percentual intuitivo. Amostra judgmental pode ser apropriada para risco, mas não deve ser apresentada como estatisticamente representativa.

### Âncoras de confidence

| Confidence | Evidência mínima |
|---|---|
| `low` | fonte única, coverage baixa, conflito não resolvido ou claim não corroborado |
| `medium` | duas formas de evidência ou walkthrough corroborado, com gaps/coverage conhecidos |
| `high` | records e testes corroborados na amostra, coverage defensável e nenhum conflito material em aberto |

`High confidence` não transforma amostra em população nem elimina limitações.

## Rationale, review e comparabilidade

Cada score exige rationale que relacione evidências às âncoras do nível e explique por que o nível seguinte não foi demonstrado. Um reviewer diferente do assessor registra disposition, conflitos verificados e comentários; divergência permanece como `disputed`, não é apagada.

Comparação entre períodos ou unidades só é válida quando method version, scope, evidence cutoff, sampling e coverage são compatíveis. Este modelo não fornece benchmark entre empresas.

## Dimensões

### 1. Estratégia, portfólio e valor

| Nível | Evidência típica |
|---:|---|
| 0 | não há ownership ou baseline |
| 1 | iniciativas aprovadas caso a caso |
| 2 | business case e portfolio review definidos |
| 3 | criação, uso, qualidade e outcome medidos separadamente |
| 4 | funding e sunset mudam com evidence e risco |

### 2. Policy, operating model e decision rights

| Nível | Evidência típica |
|---:|---|
| 0 | decisões informais |
| 1 | council sem authority clara |
| 2 | policy, RACI, gates e exceptions definidos |
| 3 | SLAs, handoffs e segregation medidos |
| 4 | authority e controls evoluem por sinais e assurance |

### 3. Registry, blueprint e lifecycle

| Nível | Evidência típica |
|---:|---|
| 0 | inventário desconhecido |
| 1 | planilhas isoladas |
| 2 | schemas, owners e lifecycle comuns |
| 3 | reconciliation, attestation e sunset operacionais |
| 4 | discovery/enforcement integrados e coverage monitorado |

### 4. Identidade e acesso

| Nível | Evidência típica |
|---:|---|
| 0 | credenciais embutidas ou compartilhadas |
| 1 | acesso manual sem attestation |
| 2 | workload identity e permission mapping definidos |
| 3 | JIT/expiry, testes negativos e revogação medidos |
| 4 | policy dinâmica e anomaly response integrada |

### 5. Dados e connectors

| Nível | Evidência típica |
|---:|---|
| 0 | fontes sem owner/classificação |
| 1 | aprovação informal por sistema |
| 2 | data contracts e connector gates definidos |
| 3 | lineage, leakage tests, retention e quality monitorados |
| 4 | enforcement e reavaliação por mudança automatizados |

### 6. Tools, APIs e MCP

| Nível | Evidência típica |
|---:|---|
| 0 | tools descobertas e usadas sem controle |
| 1 | allowlists locais |
| 2 | registry, provenance, scopes e approval definidos |
| 3 | gateway, kill switch e chain monitoring operacionais |
| 4 | policy contextual e threat intelligence realimentam controls |

### 7. Risco, Responsible AI e human oversight

| Nível | Evidência típica |
|---:|---|
| 0 | impacto não avaliado |
| 1 | checklists genéricos |
| 2 | tiering, assessments e oversight definidos |
| 3 | residual risk, slices, contestability e incidents medidos |
| 4 | challenge com segregation testada e controls adaptativos |

### 8. Evaluations e release

| Nível | Evidência típica |
|---:|---|
| 0 | demo substitui teste |
| 1 | testes manuais sem thresholds |
| 2 | evaluation strategy, datasets e gates definidos |
| 3 | regressions, calibration e runtime evals operacionais |
| 4 | promotion/rollback e portfolio decision guiados por evidence |

### 9. Auditabilidade e operações

| Nível | Evidência típica |
|---:|---|
| 0 | ações não atribuíveis |
| 1 | logs fragmentados |
| 2 | event model, runbooks e retention definidos |
| 3 | correlation, containment, drills e attestation medidos |
| 4 | automated response testada e learning loop institucionalizado |

### 10. Adoção, suporte e competência

| Nível | Evidência típica |
|---:|---|
| 0 | usuários sem guidance ou suporte |
| 1 | treinamento pontual |
| 2 | personas, paved road e support tiers definidos |
| 3 | discovery, competence, feedback e support outcomes medidos |
| 4 | experience e controls coevoluem por evidence |

## Scoring

### Score por dimensão

Use 0–4 e registre:

- `score` demonstrado;
- `confidence`: low, medium ou high, com rationale;
- `coverage`: percentual e base de cálculo;
- `evidenceRefs` para o evidence register;
- gaps;
- rationale do score;
- target e prazo;
- owner.

### Score global

A média é apenas resumo visual. Não use para esconder dimensão crítica. Reporte:

- mediana;
- faixa mínimo–máximo;
- dimensões abaixo do target;
- evidence confidence;
- blockers críticos e altos.

Um score alto não reduz o tier de risco de um sistema específico.

## Target state

Não é necessário atingir nível 4 em tudo. Escolha target por:

- risk appetite e obrigações;
- portfólio e criticality;
- dependências;
- capacidade operacional;
- custo e benefit esperado;
- sequence lógica.

Exemplo: tools/MCP e identidade podem exigir target 3 antes de expansão de agentes action-capable, enquanto adoption pode evoluir em paralelo.

## Processo de assessment

1. definir scope, evidence cutoff, assessment mode e stakeholders;
2. declarar população, sampling method, coverage basis e limitações;
3. registrar documentos, systems evidence, entrevistas, walkthroughs e testes no evidence register;
4. testar claims com records e amostras recuperáveis;
5. atribuir score, rationale, confidence e coverage por dimensão;
6. submeter evidências e rationale a reviewer diferente do assessor;
7. registrar `accepted`, `accepted-with-conditions` ou `disputed` sem apagar divergência;
8. priorizar roadmap por severidade, risco e dependência;
9. aprovar target e owners;
10. revisar após mudanças ou no ciclo definido.

## Como executar na prática

Maturity assessment **não é pesquisa de percepção**. Responde duas perguntas: qual capacidade existe de fato e quão repetível ela é. Nota alta sem evidência é hipótese, não resultado.

### Preparação

1. **Congelar escopo, unidades, geografias e data de corte.** Se o assessment cobre uma unidade, a nota não se estende à empresa.
2. **Congelar a lista de capacidades e suas descrições operacionais.** Mudar critério durante as entrevistas torna as notas incomparáveis.
3. **Escrever critérios específicos por nível e por dimensão**, antes de olhar evidência. Exemplo de nível 3 para registry: cobertura acima de 90%, owner obrigatório, quality rules ativas e remediação medida.
4. **Montar a evidence request list antes das entrevistas** — não durante.

### Evidence request list

Pedir o artefato certo separa avaliação de conversa. Cada linha declara o que a evidência comprova **e o sinal de que ela foi fabricada para o assessment**.

| Capacidade | Evidência solicitada | O que comprova | Sinal de alerta |
|---|---|---|---|
| registry | export dos últimos 90 dias com owners, tier e `last_seen` | cobertura e qualidade reais | planilha criada para o assessment |
| identidade | identidades não humanas, idade de credencial, owners e permissões | identidade dedicada e lifecycle | secret compartilhado sem owner |
| lifecycle | tickets de publicação, suspensão, attestation e retirada | processo repetível | documento existe, nenhum caso executado |
| observabilidade | dashboard, amostra de trace e correlação de incidente | rastreabilidade ponta a ponta | logs sem identificador de agente ou tarefa |

### Entrevistas

Por domínio, com **dois a quatro papéis — não apenas o líder**. Compare o discurso com a evidência operacional. Divergência entre o que o líder descreve e o que o operador executa é achado, não ruído.

### Workshop de scoring

De 60 a 90 minutos por conjunto de capacidades relacionadas.

Sequência: apresentar a definição do nível → mostrar a evidência → pedir que o owner proponha a nota → desafiar com os critérios → registrar rationale.

**Não vote.** Maturidade não é consenso político, é aderência a critério observável. Sem evidência suficiente, use a nota mais conservadora e marque confidence `low` — nunca a nota otimista com ressalva verbal.

### Findings que orientam ação

`M1` sozinho não orienta nada. O finding precisa ser uma condição observável.

> **Identidade e acesso — nível 1, confidence `high`.** 18 de 27 agentes transacionais usam credencial compartilhada; não há processo de JML; quatro identidades de serviço sem owner ativo. Alvo proposto: nível 3 em 12 meses. Prioridade: identidade própria para T2/T3 e reatribuição automática por evento de owner.

### Dependências quebradas

Uma capacidade pode parecer nível 3 isoladamente e ser inutilizável em escala por depender de outra em nível 0. Registre essas dependências — elas mudam a ordem do roadmap mais que a severidade individual.

### Playback e aprovação

Faça playback com os stakeholders e **aceite contestação apenas com nova evidência**. Aprove baseline, data de corte, confidence e o backlog de evidências pendentes. Sem baseline aprovada, a próxima medição não é comparável.

### Definition of done

- cada nota tem critério, evidência e rationale;
- confidence está registrado e não é escondido pela nota;
- gaps são condições observáveis, não rótulos genéricos;
- dependências quebradas e riscos imediatos estão identificados;
- a baseline foi aprovada e pode ser repetida com o mesmo método.

## Entregáveis

- assessment JSON validado;
- evidence register e sampling statement;
- reviewer disposition e conflitos declarados;
- heatmap com confidence;
- narrative de current state;
- top gaps e dependencies;
- target state;
- roadmap 90 dias e 6–12 meses;
- executive decision memo.

## Reassessment

Reexecute o assessment completo pelo menos anualmente, ou após transformação material. Use os **mesmos critérios** e preserve a baseline anterior — mudar o método invalida a comparação, que é o único produto de uma segunda medição.

Para capacidades em evolução rápida, um mini-assessment trimestral baseado em evidência é suficiente.

**Não eleve a maturidade porque uma ferramenta foi adquirida.** Exija cobertura, processo, métrica e operação sustentada. Ferramenta comprada e não operada move o nível para baixo, não para cima: adiciona superfície sem adicionar capacidade.

## Antipatterns

- score por opinião sem evidence;
- média global como “nota de compliance”;
- target 4 para todos os domínios;
- comparar empresas sem contexto;
- vender assessment como certificação;
- melhorar documento sem melhorar operação;
- ocultar low coverage com precisão numérica.
