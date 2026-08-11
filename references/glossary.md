# Glossário canônico

Este vocabulário reduz ambiguidade entre policy, arquitetura, patterns, controls e engagements. Quando um termo externo tiver definição normativa própria, a definição aplicável ao contexto deve ser registrada no assessment.

## Sistemas, agentes e capacidades

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **AI system** | Sistema que usa modelos ou técnicas de IA para produzir outputs, recommendations, predictions, content ou actions. | Modelo isolado. |
| **Model** | Artefato computacional versionável usado por um AI system. | Aplicação, workflow ou agent completo. |
| **Generative AI** | IA que produz conteúdo novo como texto, imagem, áudio, código ou estrutura. | Toda IA. |
| **Assistant / copilot** | Sistema orientado a apoiar uma pessoa, geralmente por interaction e suggestion. | Agent com capacidade autônoma de ação. |
| **Agent** | AI system que percebe contexto, decide ou planeja passos e usa capacidades para perseguir um objetivo dentro de boundaries. | Chat interface sem ação. |
| **Agentic system** | Sistema cujo comportamento inclui goal pursuit, planning, tool use, memory, delegation ou adaptação com autonomia relevante. | Marketing label “agent”. |
| **Workflow** | Sequência explícita de etapas e decisões; pode ou não usar IA. | Autonomia aberta de agent. |
| **Orchestration** | Coordenação de models, agents, tools, data e workflow states. | Accountability organizacional. |
| **Multi-agent system** | Sistema no qual múltiplos agents coordenam ou delegam trabalho. | Várias prompts executadas independentemente. |
| **Capability** | Ação tecnicamente possível, como observe, create, modify, execute, approve, delete ou delegate. | Use case ou permissão efetiva. |
| **Tool** | Função, API, código ou interface invocável por agent. | Model ou connector de dados. |
| **Connector** | Integração que fornece acesso a fonte, service ou system. | Autorização automática. |
| **MCP** | Model Context Protocol, protocolo para expor context e tools a AI applications. | Control framework. |
| **MCP server** | Componente que oferece resources, prompts ou tools via MCP. | Servidor confiável por default. |
| **Action class** | Categoria de efeito: observe, create, modify, execute, approve, delete ou delegate. | Risk tier completo. |
| **State-changing action** | Ação que cria, modifica, executa, aprova, deleta ou delega algo fora da resposta do model. | Geração de texto sem side effect. |
| **Prohibited use** | Uso que não pode ser autorizado no scope atual. | Exception pendente. |

## Autonomia e humanos

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Autonomy** | Grau de liberdade para escolher passos e executar ações sem decisão humana a cada etapa. | Intelligence ou qualidade. |
| **AI-operated, human-led** | Pessoas definem finalidade, boundaries, authorities e accountability; automação opera dentro deles. | Humans aprovando tudo manualmente. |
| **Human oversight** | Capacidade humana real de compreender, supervisionar, intervir e contestar o sistema. | Checkbox ou presença nominal. |
| **Human-in-the-loop (HITL)** | Decisão humana exigida dentro do fluxo antes de ação definida. | Revisão posterior. |
| **Human-on-the-loop (HOTL)** | Supervisão humana com capacidade de monitorar e intervir durante operação. | Autonomia sem observabilidade. |
| **Human-in-command** | Autoridade humana sobre finalidade, deployment, boundaries e continuidade. | Operação manual. |
| **Meaningful review** | Revisão com contexto, tempo, competência e poder para mudar a decisão. | Rubber stamp. |
| **Contestability** | Mecanismo para questionar, corrigir ou recorrer de output/decision. | Canal de suporte genérico. |

## Ownership e decision rights

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Accountability** | Obrigação de responder por decisão, resultado e correção. Não é transferida ao agent. | Execução de tarefa. |
| **Sponsor** | Autoridade executiva sobre mandato, appetite, funding e material trade-offs. | Project manager. |
| **Governance Owner** | Owner do framework, control catalog, forums, exceptions e improvement. | Dono de todos os agents. |
| **Business Owner** | Responsável por finalidade, uso permitido, outcomes e continuidade do agent. | Usuário frequente. |
| **Technical Owner** | Responsável por arquitetura, change, evaluations e technical remediation. | Fornecedor da plataforma. |
| **Design Authority** | Autoridade sobre admissibilidade pré-release e conditions. | Run Authority. |
| **Run Authority** | Autoridade operacional para contain, quarantine, rollback, reactivate ou retire. | Service desk sem authority. |
| **Domain Owner** | Owner de control especializado como identity, data, security, privacy ou RAI. | Governance Owner. |
| **Decision right** | Papel com autoridade explícita para uma decisão definida. | RACI genérico sem poder decisório. |
| **Risk appetite** | Quantidade e tipo de risco que authority aceita perseguir ou reter. | Risk tier. |
| **Risk acceptance** | Decisão explícita de aceitar residual risk por prazo e scope. | Ausência de mitigação. |

## Inventário, arquitetura e lifecycle

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Registry** | Registro operacional de existência, ownership, status, tier, platform e evidence links. | Blueprint completo. |
| **Inventory** | Observação agregada de assets descobertos; pode conter duplicidade e baixa confiança. | Registry reconciliado. |
| **Blueprint** | Especificação versionada de arquitetura, models, data, identity, tools, boundaries e runtime. | Linha no registry. |
| **Source of truth** | Sistema reconhecido como autoridade para determinado campo/decision. | Único banco para todos os domínios. |
| **Reconciliation** | Processo de comparar sources, resolver conflitos e manter provenance. | Sobrescrever tudo pelo source mais recente. |
| **Lifecycle** | Discover, register, assess, approve, release, operate, change, attest, sunset e archive. | SDLC apenas. |
| **Attestation** | Declaração periódica, por authority, de que owner, purpose, controls e evidence permanecem válidos. | Avaliação inicial. |
| **Sunset** | Retirada planejada com revocation, retention, dependency e communication. | Desligamento sem cleanup. |
| **Material change** | Mudança que pode alterar tier, admissibilidade, controls, evaluation ou approval. | Toda alteração cosmética. |
| **Dormancy** | Ausência de uso relevante por período definido, que dispara revisão de continuidade. | Falha técnica ou indisponibilidade. |
| **Dormancy threshold** | Período calibrado por tipo de agente a partir do qual a dormência é tratada. Threshold único para todo o estate produz falso positivo em agente sazonal. | Timeout de sessão. |
| **Grace period** | Prazo entre o trigger de retirada e a revogação efetiva, para dependentes reagirem. | Adiamento indefinido. |
| **Joiner/mover/leaver (JML)** | Processo que reatribui ou revoga ownership e acessos quando a pessoa responsável entra, muda de função ou sai. | Offboarding apenas de credencial humana. |
| **Evidence cutoff** | Data até a qual evidências foram consideradas em assessment ou decisão. | Data de publicação. |

## Risco, controles e assurance

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Risk** | Efeito da incerteza sobre objetivos, pessoas, direitos, sistemas ou organização. | Finding confirmado. |
| **Impact** | Magnitude da consequência se evento ocorrer. | Likelihood. |
| **Likelihood** | Possibilidade estimada de ocorrência nas condições avaliadas. | Frequência histórica isolada. |
| **Residual risk** | Risco remanescente após controls e mitigations. | Risco inicial. |
| **Risk tier** | Classe de governança que determina rigor mínimo por criticidade; neste framework T1–T4. | Admissibilidade ou score de maturidade. |
| **Admissibilidade** | Dimensão que responde se e sob quais condições um uso pode operar: `permitted`, `conditional`, `restricted` ou `prohibited`. Independente do tier ([ADR-0009](../docs/architecture/decisions/0009-risk-tier-and-admissibility.md)). | Risk tier. Um T1 pode ser proibido; um T4 pode ser admitido. |
| **Red flag** | Condição que impede fast path e eleva a criticidade mínima independentemente do score. | Falha automaticamente comprovada. |
| **Escalador** | Red flag registrado na norma com criticidade mínima e efeito declarados. A lista normativa prevalece sobre o instrumento que a coleta. | Pergunta de questionário. |
| **Fast path** | Rota automatizada de T1: elimina revisão manual caso a caso, não os controles nem a evidência. | Isenção de governança. |
| **Minimum Production Bar (MPB)** | Piso de controles que precisam ser verdadeiros para um agente entrar **e permanecer** em produção, por tier. | Teto de controles ou gate de release completo. |
| **Blast radius** | Extensão potencial do efeito por usuários, dados, sistemas, regiões e dependências. | Número de usuários apenas. |
| **Reversibility** | Capacidade de desfazer efeito com custo, prazo e integridade aceitáveis. | Existência nominal de rollback. |
| **Policy** | Regra normativa aprovada com authority e enforcement expectation. | Guidance. |
| **Policy corporativa de IA** | Instrumento que a organização já aprovou para toda a IA — princípios, obrigações mínimas, usos proibidos e conformidade regulatória. Quando existe, prevalece. | A policy de governança de agentes. |
| **Policy de governança de agentes** | A camada normativa deste framework: como um agente é construído, aprovado, operado e retirado. Executa a policy corporativa no escopo de agentes; não a substitui. | Instrumento aprovado da organização, enquanto ela não o adotar. |
| **Standard** | Requirement obrigatório que especifica como satisfazer policy. | Referência externa sem adoção. |
| **Guidance** | Recomendação adaptável que não muda policy. | Requirement adotado. |
| **Procedure** | Passos operacionais para executar tarefa ou control. | Control objective. |
| **Control objective** | Resultado de risco/governança que precisa ser alcançado. | Implementação específica. |
| **Control** | Medida preventiva, detective, responsive ou corrective para alcançar objective. | Documento que afirma intenção. |
| **Compensating control** | Control alternativo que reduz risco quando requirement primário não é viável. | Waiver sem mitigação. |
| **Exception** | Desvio temporário aprovado, com rationale, owner, compensating controls e expiry. | Nova regra permanente. |
| **Assurance** | Atividade que aumenta confiança de que requirements e controls são adequados e eficazes. | Operação do control pelo owner. |
| **Independent assurance** | Assurance com independência suficiente do owner e implementer. | Self-assessment. |
| **Control plane** | Camada de inventory, identity, configuration, policy decision, lifecycle e administrative action. | Governança completa. |
| **Assurance plane** | Camada de risk, security, privacy, RAI, evaluations e independent challenge. | Control plane. |
| **Build time** | Design, build, assessment, evaluation e release antes da operação. | Runtime. |
| **Runtime** | Período em que o sistema opera com usuários, data e tools reais. | Test environment. |
| **Decision gate** | Ponto em que authority decide avançar, condicionar, bloquear, conter ou encerrar com evidence. | Reunião sem output. |
| **Evidence package** | Conjunto versionado de artifacts, test results, approvals e limitations para uma decisão. | Pasta de documentos sem manifesto. |
| **System evidence** | Evidência extraída de logs, configs, tests, APIs ou records operacionais. | Afirmação em workshop. |

## Identidade, dados e memória

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Workload identity** | Identidade própria e gerenciada para service, workload ou agent. | Credencial humana compartilhada. |
| **Non-human identity** | Categoria que abrange service accounts, workload identities e agentes; governada por lifecycle próprio, não pelo de pessoas. | Conta de serviço legada sem owner. |
| **Step-up** | Exigência de autenticação ou autorização adicional no momento de uma ação de maior impacto. | Login inicial mais forte. |
| **Prompt injection** | Instrução hostil embutida em conteúdo processado pelo agente, que tenta redirecionar comportamento ou extrair dados. | Erro de prompt do usuário. |
| **Delegated access** | Acesso em nome do usuário, limitado por seus direitos e contexto. | Privilege próprio do agent. |
| **Least privilege** | Menor permission, scope e duração necessários para finalidade aprovada. | Read-only por default em todos os casos. |
| **Data contract** | Acordo versionado de source, purpose, classification, quality, access, retention e owner. | Connector config. |
| **AI-ready data** | Dados avaliados como adequados ao uso definido, com quality, classification, ownership e provenance suficientes. | Dados “limpos” universalmente. |
| **Provenance** | Origem, transformations, versions e chain of custody de dado/output/evidence. | Link para source apenas. |
| **Memory** | Estado persistente ou semipersistente usado pelo agent entre interactions ou steps. | Context window temporária. |
| **Retention** | Prazo e condições para manter dado, log, memory ou evidence. | Backup indefinido. |
| **Right-to-delete mechanism** | Processo capaz de localizar e remover dados aplicáveis inclusive em memory e derived stores. | Delete na interface apenas. |

## Evaluation, operação e valor

| Termo | Definição neste framework | Não confundir com |
|---|---|---|
| **Evaluation** | Teste estruturado de comportamento, qualidade, safety, security ou operação. | Demo. |
| **Metric** | Medida definida com unidade, população e método. | Objective. |
| **Threshold** | Limite que dispara decisão, alert ou action. | Resultado desejado sem critério. |
| **Benchmark** | Conjunto e método padronizados para comparação. | Teste suficiente para contexto específico. |
| **Red teaming** | Teste adversarial para descobrir failure modes e control gaps. | Garantia de segurança. |
| **Regression** | Degradação em cenário anteriormente aceitável. | Drift necessariamente. |
| **Drift** | Mudança relevante em inputs, behavior, performance ou environment ao longo do tempo. | Toda variação. |
| **Observability** | Capacidade de inferir estado e comportamento a partir de signals suficientes. | Logging sem ação. |
| **Telemetry** | Dados de execução, uso, quality, policy, cost e action. | Evidência de valor por si só. |
| **SLO** | Objetivo mensurável de serviço/qualidade para um período. | SLA contratual. |
| **Containment** | Ação para limitar blast radius preservando investigação e recovery. | Remediação definitiva. |
| **Quarantine** | Estado controlado que restringe operação ou acesso até decisão. | Delete. |
| **Kill switch** | Mecanismo testado para interromper capability, tool ou agent. | Botão documentado sem authority. |
| **Circuit breaker** | Corte automático acionado por threshold, sem esperar decisão humana. | Kill switch, que é acionado por authority. |
| **Behavioral baseline** | Padrão de comportamento observado e aceito de um agente, contra o qual desvios são medidos. | Resultado de eval pré-release. |
| **Denial-of-wallet** | Exaustão de orçamento por consumo legítimo em aparência, sem indisponibilidade técnica. | Denial-of-service. |
| **Unit economics** | Custo por resultado útil, não por token ou execução. | Custo total de plataforma. |
| **Rollback** | Retorno verificável a versão/estado conhecido. | Restart. |
| **Reactivation** | Retorno autorizado após evidence de correção e readiness. | Remover alerta. |
| **Adoption** | Uso sustentado por personas/escopos definidos. | Número de agents criados. |
| **Discovery** | Usuário encontra opção existente adequada antes de criar outra. | Inventory técnico. |
| **Quality** | Grau em que outputs/actions atendem critérios do contexto. | Satisfação apenas. |
| **Baseline** | Medida anterior ou contrafactual explícito usado para comparação. | Target. |
| **Outcome** | Mudança observável em processo, pessoa, risco ou negócio. | Output do agent. |
| **Value evidence** | Conjunto de baseline, adoption, quality, risk, cost e outcome com limitações declaradas. | ROI inferido de uso. |

## Regra de terminologia

Se um novo documento usar sinônimo ou definição incompatível, ele deve:

1. referenciar a definição canônica;
2. explicar a diferença de contexto;
3. propor alteração do glossary se a diferença for permanente.
