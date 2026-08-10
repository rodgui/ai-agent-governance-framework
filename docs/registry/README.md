---
title: Estate, registry, ownership e taxonomia
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - discovery-and-forecast.md
  - ../lifecycle/README.md
  - ../patterns/registry-and-blueprint.md
  - ../../schemas/README.md
  - ../governance/operating-model.md
---

# Estate, registry, ownership e taxonomia

## Objetivo

Criar a fonte corporativa de verdade sobre quais agentes existem, quem responde por cada um e o que cada um pode fazer — em linguagem comum, estável e independente da plataforma onde o agente foi construído.

Sem essa camada, todas as outras falham por falta de sujeito: não há como aplicar tier, evidência, contenção ou sunset a um ativo que a organização não sabe que existe.

## Quatro objetos distintos

| Objeto | Pergunta que responde | Natureza |
|---|---|---|
| **Registry** | qual agente é este, quem responde, qual tier, admissibilidade, stage e operational state? | fonte corporativa de identificação e correlação |
| **Blueprint** | como esta versão deve ser configurada e controlada? | especificação versionada do desired state |
| **Policy/gate** | a configuração e as evidências atendem às regras? | decisão automática ou semiautomática |
| **Runtime/telemetria** | o agente está operando conforme aprovado? | estado observado |

Confundir registry com blueprint produz o antipattern mais comum: um inventário que cresce sem nunca virar controle.

## Taxonomia corporativa

Taxonomia é a linguagem de classificação do estate: características relativamente estáveis que fazem registry, scoring, policies, dashboards e lifecycle usarem os mesmos termos.

**Taxonomia não é risk tier.** Dois agentes podem ser `transactional` e receber tiers diferentes por operarem sobre dados, privilégios ou processos distintos.

| Dimensão | Categorias sugeridas | Por que muda a governança |
|---|---|---|
| origem | citizen, partnered, professional, fornecedor/SaaS | define suporte, SDLC e responsabilidade técnica |
| ownership | pessoal, time, processo de negócio, corporativo | muda attestation, JML, continuidade e retirada |
| alcance | usuário único, time, unidade, corporativo, externo/público | muda blast radius e necessidade de assurance |
| função | informacional, redação, transacional, autônomo | separa conteúdo de efeito colateral |
| autonomia | assistiva, sugestão, execução limitada, planejamento autônomo | direciona oversight, limites e controles de runtime |
| identidade | delegada, própria (NHI), compartilhada (proibida) | define accountability e padrão de autorização |
| dados | público, interno, confidencial, restrito/regulado | aciona controles de dados, privacidade e residency |
| tools | nenhuma, leitura, escrita, execução, privilegiada | direciona mediação, rollback e aprovação humana |
| runtime | SaaS, nuvem, on-premises, edge, híbrido | muda pontos de enforcement e ownership operacional |
| topologia | agente único, multiagente, delegação entre agentes | adiciona trust chain e requisitos de correlação |
| lifecycle | efêmero, do usuário, do time, corporativo | muda retenção, dormancy e sucessão |

Evite taxonomia baseada em produto ("agente da plataforma X"). O produto informa onde o agente foi construído, não o que ele pode fazer — e a taxonomia precisa sobreviver à troca de builder.

### Como implementar

1. Colete amostra representativa incluindo citizen-built, SaaS, custom e ao menos um caso com execução de ferramentas.
2. Escolha **apenas** dimensões que alteram decisão, controle, métrica ou lifecycle. Categoria que não muda nada não deve ser obrigatória.
3. Defina códigos canônicos e descrições inequívocas — "autônomo" precisa de critério operacional, não percepção do builder.
4. Crie regras de normalização por plataforma, mapeando termos nativos para as categorias corporativas.
5. Defina o que é obrigatório por tier e o que pode ser autodescoberto. O fast path de T1 deve minimizar input manual.
6. Classifique 20–30 casos e meça concordância entre avaliadores. Divergência sistemática indica definição fraca, não avaliador fraco.
7. Implemente a taxonomia no registry, no pre-screen, nos dashboards e no blueprint. Taxonomia que vive só em documento não gera governança.

## Registry: capacidades mínimas

O registry não precisa armazenar tudo — pode referenciar sources of truth existentes. O requisito é responder de forma consistente: **qual agente é este, quem responde, qual tier e admissibilidade, qual lifecycle stage e operational state, quais identidades, tools, dados e modelos usa, e quando foi visto pela última vez.**

| Grupo | Campos | Source of truth preferido |
|---|---|---|
| identidade do ativo | `agent_id` imutável, nome, versão, plataforma, ambiente | registry/plataforma |
| ownership | business owner, technical owner, delegado, time/centro de custo | diretório organizacional + registry |
| governança | tier, admissibilidade, score, escaladores, decision/exception refs | sistema de risco |
| dependências | IDs de fontes de dados, tools, servidores MCP, modelos | catálogos + blueprint |
| runtime | ID de identidade, endpoint, perfil de telemetria, `last_seen`, budget | IAM/plataforma/observabilidade |
| lifecycle | stage, operational state, transition history, próxima attestation, dormancy, retirada | serviço de lifecycle |
| valor | ID do caso de uso, KPI, status no portfólio, valor observado | portfólio |

### Obrigatoriedade por tier

| Campo | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| owner | obrigatório | dual (business + technical) | dual + delegado | sponsor executivo + owners accountable |
| tier e admissibilidade | ambos obrigatórios | ambos obrigatórios | ambos + reassessment | ambos + authority compatível; exceção somente se `restricted` |
| dados e tools | lista | lista + classificação | lista + constraints + evidência | constraints e lineage críticos completos |
| identidade | definida | identidade própria | identidade própria + policy reforçada | identidade dedicada, isolamento e dual control onde aplicável |
| observabilidade | padrão | completa | completa + baseline de comportamento | monitoramento e containment reforçados |
| attestation | periódica | periódica | frequente ou orientada a evento | orientada a evento e executive review |

O fast path de T1 existe para reduzir input manual em alto volume, **não** para dispensar registro: descoberta, owner, logging e fontes aprovadas continuam obrigatórios.

## Regras de qualidade que geram finding

O registry só é controle quando detecta continuamente que deixou de representar a realidade. O objetivo não é ter uma lista perfeita.

- owner inexistente ou inativo;
- tier ausente ou expirado após mudança material;
- `last_seen` incompatível com o estado de lifecycle;
- ferramenta ou fonte de dados referenciada que não existe no catálogo;
- agente em produção sem perfil de telemetria ou sem kill switch quando exigido;
- attestation vencida;
- identidade compartilhada entre múltiplos agentes T2/T3 sem exceção aprovada;
- agente descoberto sem owner — recebe status `unmanaged` e entra em remediação.

## Blueprint machine-readable

O blueprint é o contrato entre design, desenvolvimento, governança, CI/CD e runtime. Machine-readable significa que os campos relevantes podem ser interpretados por automação para gerar policy checks, verificar o baseline do tier e comparar drift entre configuração aprovada e runtime.

Isso não exige que toda a governança esteja em YAML: decisões narrativas, impact assessments e risk acceptance continuam como evidências **referenciadas** pelo blueprint. Os contratos canônicos são o [Agent Registry 2.0](../../schemas/agent-registry.schema.json) e o [Agent Blueprint 2.0](../../schemas/agent-blueprint.schema.json).

### Como implementar

1. Defina primeiro o contrato lógico e apenas os campos que têm consumidor real. Schema grande sem consumidor é dívida.
2. Use formato versionável com validação por schema; campos críticos com enum, formato e obrigatoriedade por tier.
3. Associe o blueprint a `agent_id` + versão. Alterar o blueprint não pode sobrescrever silenciosamente a evidência de releases anteriores.
4. Valide em build/release: IDs de fontes, tools e modelos precisam existir em catálogos aprovados; tier e padrão de identidade precisam ser coerentes.
5. Use o blueprint para gerar ou verificar configuração: policy bindings, budgets, perfil de telemetria, allowlist de tools e cadência de attestation.
6. Compare desired state com runtime observado. Drift material produz finding e, se altera risco, reassessment.
7. Comece com dois ou três patterns (T1 somente leitura, T2 transacional, T3 alto impacto) e evolua o schema só quando houver caso real.

## Artefatos

- Agent Registry Data Standard: campos, tipos, obrigatoriedade por tier, sources of truth e quality checks;
- [Agent Registry schema](../../schemas/agent-registry.schema.json) e [exemplo estruturado](../../examples/agent-registry.example.json);
- [Agent Blueprint schema](../../schemas/agent-blueprint.schema.json) e [exemplo estruturado](../../examples/agent-blueprint.example.json);
- Agent Taxonomy & Metadata Dictionary;
- [template de registry](../../templates/agent-registry-template.md) e [template de blueprint](../../templates/agent-blueprint-template.md);
- [descoberta contínua e forecast do estate](discovery-and-forecast.md).

## Evidências

- registro autoritativo com owners, tier e estado por agente;
- histórico de reconciliação entre registry e plataformas de origem;
- findings de qualidade abertos e remediados;
- blueprint versionado por release, com evidence refs;
- relatórios de drift entre desired state e runtime;
- decisões de exceção para identidade compartilhada.

## Métricas

- agentes descobertos sem owner (`unmanaged`) e tempo até remediação;
- cobertura do registry contra fontes de descoberta independentes;
- campos obrigatórios vazios por tier;
- referências quebradas para tools, dados e modelos;
- drift material entre blueprint e runtime;
- duplicidade e sobreposição de capability no estate;
- tempo entre criação do agente e registro.

## Failure modes

- registry como planilha mestre que ninguém reconcilia;
- taxonomia derivada de produto em vez de comportamento;
- inventário completo sem quality rules — lista bonita, controle zero;
- blueprint gigante sem consumidor automatizado;
- agente pessoal compartilhado que permanece "pessoal" no registro;
- tratar descoberta como projeto de inventário pontual;
- sobrescrever o blueprint aprovado ao publicar uma nova versão.

## Decision gate

Nenhum agente é construído em ambiente compartilhado ou publicado sem `agent_id`, owner, tier e admissibilidade registrados. Nenhum agente permanece em produção sem stage/operational state coerentes ou com quality finding crítico aberto no registry.
