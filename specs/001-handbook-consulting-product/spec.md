---
title: Productização do framework como handbook e oferta de consultoria
status: approved
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-09
review_cycle: major-change
supersedes: null
related:
  - ../../docs/architecture/decisions/0001-canonical-modular-framework-and-vendor-mappings.md
  - plan.md
  - tasks.md
  - validation.md
---

# Especificação: framework canônico, handbook e oferta de consultoria

## Problema

O repositório possui uma Policy v1 adotada, uma arquitetura inicial e um estudo de caso Microsoft bem fundamentado, mas ainda não constitui um produto de conhecimento completo. Domínios importantes são placeholders, os artefatos operacionais não possuem schemas verificáveis e o visual principal pode ser confundido com uma arquitetura dependente de fornecedor.

## Objetivo

Transformar o repositório em uma fonte canônica capaz de sustentar simultaneamente:

1. referência técnica de governança de IA e agentes;
2. guia prático de implantação organizacional;
3. arquitetura editorial preparada para uma futura publicação executiva ou ebook;
4. catálogo de design patterns e antipatterns;
5. método e toolkit para uma oferta profissional de consultoria.

## Não objetivos

- executar ou simular piloto organizacional;
- declarar que a Policy v2 foi adotada;
- modificar silenciosamente a Policy v1;
- prometer ROI, redução de incidentes, conformidade ou certificação sem evidência;
- criar dependência obrigatória de Microsoft Agent 365 ou de qualquer fornecedor;
- gerar nesta etapa PDF, EPUB, manifesto ou pipeline de publicação;
- duplicar manualmente o conteúdo do handbook em uma segunda fonte editorial;
- incluir dados, resultados ou cases de clientes inexistentes.

## Público

- conselho, executivos e sponsors;
- CISO, DPO, jurídico, compliance e Responsible AI;
- arquitetura, plataforma, identidade, dados e segurança;
- product owners, makers e equipes de engenharia;
- operações, auditoria e assurance;
- consultores e líderes de transformação.

## Princípios editoriais

1. **Fonte única:** documentos modulares são canônicos; futuras publicações serão derivadas.
2. **Núcleo neutro:** fornecedores aparecem apenas em mappings e estudos de caso.
3. **Fluxo orientado a evidência:** documents, patterns, controls e schemas sustentam futuras publicações sem criar cópias editoriais.
4. **Normativo explícito:** policy adotada é separada de guidance e backlog.
5. **Governança proporcional:** controles variam por risco, alcance, autonomia, criticidade, reversibilidade, dados e capacidade de ação.
6. **Evidência antes de afirmação:** benefícios esperados, hipóteses e resultados comprovados permanecem separados.
7. **Build time e runtime:** controles preventivos não substituem observabilidade, contenção e resposta.
8. **AI-operated, human-led:** automação não remove decision rights nem accountability humana.
9. **Ferramentas verificáveis:** schemas, exemplos e geração de visuais são testados automaticamente.

## Requisitos funcionais

### RF-01 — Arquitetura da informação

O índice deve oferecer jornadas por persona e por objetivo, sem transformar o README em um documento monolítico.

### RF-02 — Framework canônico

O handbook deve cobrir fundamentos, operating model, ciclo de vida, risco, identidade, dados, ferramentas/MCP, Responsible AI, supervisão humana, avaliações, auditabilidade, operações e valor.

### RF-03 — Método de implantação

O playbook deve usar fases, decision gates, entregáveis e critérios de saída. Não pode depender de piloto para ser compreendido ou aplicado.

### RF-04 — Design patterns

Cada pattern deve declarar intent, problema, contexto, forças, solução, participantes, fluxo, controles, evidências, métricas, consequências, limitações, antipatterns, exemplo neutro, mappings e fontes.

### RF-05 — Toolkit operacional

O repositório deve fornecer schemas e exemplos válidos para registry, agent blueprint, control catalog e maturity assessment.

### RF-06 — Oferta de consultoria

O modelo comercial deve derivar do método e declarar problema, escopo, pré-requisitos, atividades, entregáveis, participantes, critérios de aceite, dependências, exclusões, riscos e métricas, sem alegações não comprovadas.

### RF-07 — Separação visual

O README e a arquitetura principal devem usar um visual neutro. O visual Microsoft deve permanecer identificado como estudo institucional de Customer Zero.

### RF-08 — Prontidão editorial

Uma ordem linear de leitura deve organizar os documentos canônicos e preservar a possibilidade de gerar uma publicação futura. Gerar PDF ou EPUB não faz parte desta etapa.

### RF-09 — Quality gates

CI deve validar Markdown, links locais, schemas, exemplos, geração determinística de visuais e consistência dos artefatos gerados.

## Requisitos de qualidade

- português como idioma canônico desta edição;
- terminologia controlada por glossário;
- links relativos válidos;
- zero secrets, tokens ou paths pessoais;
- diagrams e outputs reproduzíveis;
- documentos com owner, status, revisão e relações quando aplicável;
- fontes primárias registradas e limitações epistemológicas explícitas.

## Critérios de aceite

1. Policy v1 mantém blob idêntico à `origin/main`.
2. O visual neutro é o único visual de framework exposto no README.
3. O estudo Microsoft e seu visual são rotulados como caso de estudo.
4. O índice oferece jornadas para pelo menos seis personas.
5. O playbook cobre diagnóstico, fundações, operating model, controles, onboarding por risco, operação, assurance e melhoria contínua.
6. O catálogo contém pelo menos oito patterns completos e antipatterns relacionados.
7. Quatro schemas JSON possuem exemplos que validam.
8. O maturity model possui dimensões, níveis, scoring e critérios de evidência.
9. A oferta de consultoria contém pacotes e critérios de aceite sem prometer resultados não demonstrados.
10. Markdown, links, schemas e scripts passam nas validações locais.
11. CI executa gates reproduzíveis no GitHub.
12. O PR permanece aberto até revisão final; merge não é automático.

## Decisão e autorização

A especificação foi aprovada pela instrução explícita do owner em 2026-08-09 para realizar os ajustes, exceto piloto, com objetivo de produzir uma bíblia, guia, ebook, catálogo de patterns e base de consultoria.
