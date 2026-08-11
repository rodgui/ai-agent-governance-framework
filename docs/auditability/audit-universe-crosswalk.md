---
title: Integração com o audit universe existente
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - README.md
  - evidence-pack-by-tier.md
  - ../../controls/README.md
  - ../governance/operating-model.md
---

# Integração com o audit universe existente

## Objetivo

Responder à pergunta que auditoria interna faz na primeira reunião: **"como estes controles se relacionam com o que eu já testo?"**

Uma organização madura já tem universo de auditoria, ciclo de teste, matriz de controles financeiros e certificações vigentes. Um framework que chega como universo paralelo não é adotado — é tolerado até a próxima reorganização.

Este documento não mapeia control a control contra normas específicas. Ele responde algo mais útil e mais honesto: **onde estes controles se encaixam no que já existe, e o que muda em relação a um controle de TI convencional.**

## O que o catálogo oferece a auditoria

O [control catalog](../../controls/README.md) tem 44 controls, e três campos determinam como auditoria os trata:

| Campo | Valores | O que significa para o teste |
|---|---|---|
| `scope` | 40 `agent`, 4 `organization` | controle de escopo `agent` é testado por amostra de agentes; `organization` é testado uma vez para a entidade |
| `blocking` | 27 bloqueantes | bloqueante impede release quando reprovado — é candidato natural a control chave |
| `automation` | 9 `automated`, 24 `assisted`, 10 `manual`, 1 `mixed` | determina se o teste é de configuração, de amostra ou de processo |
| `verification` | declarado em todos | diz **como** a evidência é obtida, não só que ela existe |

Um control `organization`-scoped nunca é bloqueante por decisão de design ([ADR-0010](../architecture/decisions/0010-structured-governance-contracts-2.0.md)) — falha de governança corporativa não deve travar um release específico; ela dispara remediação no nível certo. Auditoria precisa saber disso antes de desenhar o teste.

## Onde encaixar no universo existente

A recomendação é **não criar um universo novo**. Quase todo control deste framework é uma extensão de um domínio que auditoria já cobre:

| Domínio do framework | Universo em que normalmente encaixa | O que muda em relação ao teste convencional |
|---|---|---|
| registry e ownership | gestão de ativos e CMDB | o ativo tem comportamento próprio e muda sem deploy; inventário exige descoberta contínua, não recertificação anual |
| identidade | IAM e gestão de acessos | a identidade não é de pessoa nem de serviço estático; JML precisa cobrir reatribuição de owner de agente |
| dados | governança de dados e privacidade | a autorização acontece na recuperação, não só na concessão de acesso |
| tools e MCP | gestão de mudanças e integrações | a capacidade de ação pode crescer sem mudança de código, por descoberta de tool |
| modelos e provedores | gestão de fornecedores e terceiros | a versão do fornecedor muda sem aviso e invalida avaliação aceita |
| segurança | segurança da informação | a superfície inclui a instrução, não só a interface |
| evaluations e release | SDLC e gestão de mudanças | o critério de aceite é probabilístico, com threshold e slice, não binário |
| operações e runtime | continuidade e monitoramento | contenção precisa ser exercitada, não documentada |
| Responsible AI e human oversight | conformidade e conduta | frequentemente **não tem** universo prévio — é onde nasce controle novo |
| valor e portfólio | gestão de benefícios | outcome contra baseline, não uso |

Só a linha de Responsible AI costuma exigir universo novo. As demais são extensão de escopo de auditorias que já ocorrem — o que muda a conversa de "crie um programa de auditoria de IA" para "acrescente estas perguntas ao que você já faz".

## Três diferenças que quebram o teste convencional

Vale antecipá-las, porque cada uma já invalidou papel de trabalho em alguma organização.

**1. Evidência tem data de validade curta.** Um control de TI testado em março costuma valer para o ano. Aqui, mudança de versão de modelo, de fonte de dados ou de tool invalida a evidência no dia em que acontece. O teste precisa amarrar a evidência à **versão** do agente, não ao período. O [evidence pack por tier](evidence-pack-by-tier.md) e o release manifest existem para isso.

**2. Amostragem por população homogênea não funciona.** O estate é deliberadamente heterogêneo por tier. Amostrar 25 agentes ao acaso mede quase só T1, porque T1 é a maioria. A amostra precisa ser **estratificada por tier e por admissibilidade**, com cobertura integral dos T3 e T4.

**3. Aprovação não é evidência de controle.** Um release `conditional` aprovado não diz que as condições foram cumpridas — diz que foram impostas. O teste é sobre a **verificação declarada de cada condição**, e é por isso que o contrato de release exige que toda condição traga owner e método de verificação.

## Onde começar um primeiro teste

Sugestão de escopo para o primeiro ciclo, em ordem de retorno:

1. **Completude e ownership do registry** — agente em produção sem business owner nomeado é o achado mais comum e o mais fácil de evidenciar.
2. **Os 27 controls bloqueantes**, verificando se realmente bloqueiam — control bloqueante que nunca reprovou nada merece investigação.
3. **Attestation vencida** em agentes ativos.
4. **Condições de release com prazo expirado** e agentes ainda operando.
5. **Bindings de catálogo** — modelo, fonte ou tool em uso sem entrada aprovada correspondente.

Os itens 4 e 5 são verificáveis por consulta aos records estruturados, sem depender de entrevista. Comece por onde a evidência já é máquina-legível.

## Limites declarados

Este documento **não** é mapeamento control a control contra ISO/IEC 42001, 23894, 42005, SOX ou qualquer norma específica. Os `frameworkMappings` do catálogo declaram alinhamento direcional e dizem isso explicitamente: *"não constitui equivalência, conformidade nem atestação"*. O escopo de cada norma referenciada está em [`references/standards/`](../../references/standards/README.md), com o motivo de não haver mapeamento cláusula a cláusula.

Quem precisar de mapeamento formal precisa adquirir os textos normativos e produzi-lo internamente, com a authority competente. Alinhamento declarado por um framework de referência não substitui essa avaliação.
