---
title: Mapeamento de capability para tecnologia
status: maintained
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: quarterly
supersedes: null
related:
  - overview.md
  - principles.md
  - decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md
  - ../guides/capability-map.md
---

# Mapeamento de capability para tecnologia

## Objetivo

Conectar as capacidades exigidas pelo framework aos sistemas que a organização **já tem**, sem transformar o framework em dependência de produto.

Este é o documento que falta entre a arquitetura de referência e a execução: a arquitetura diz qual controle precisa existir e onde; o capability map diz onde a organização está; este mapeamento diz **qual sistema passa a responder por cada função** e quem é a fonte autoritativa de cada atributo.

## Por que o mapeamento é um artefato separado

A [arquitetura de referência](overview.md) e a [policy de governança de agentes](../governance/policy.md) são agnósticas de produto por decisão registrada ([ADR-0002](decisions/0002-modular-policy-vendor-neutrality-and-commercial-boundary.md)). O mapeamento não é: ele nomeia sistemas concretos da organização.

Manter os dois no mesmo documento é o erro que produz frameworks descartáveis. Quando o produto muda — e ele muda —, uma arquitetura contaminada por nomes de produto precisa ser reescrita inteira. Separados, troca-se o mapeamento e a arquitetura permanece.

Por isso este documento descreve o **método** e as categorias de sistema. O mapeamento preenchido é artefato da organização e vive fora deste repositório.

## Método

1. **Comece pela capability e pelo controle, nunca pelo produto.** A frase de partida é "precisamos de registry com owner, tier e lifecycle" — não "precisamos de uma ferramenta de governança de agentes".
2. **Identifique os systems of record existentes que já fornecem parte da função.** Quase nenhuma organização parte do zero: inventário, identidade, risco, integração, telemetria e catálogo de dados normalmente já existem com owner e processo.
3. **Defina contrato de integração e source of truth por atributo.** Não por sistema — por atributo. Owner de negócio pode vir do sistema de RH, tier do registro de risco, estado operacional da plataforma de execução. Duplicar ownership do mesmo atributo em cinco sistemas é como se perde a rastreabilidade.
4. **Só então avalie produtos para os gaps remanescentes.** Um produto pode cobrir várias capabilities; isso é vantagem operacional, não razão para o framework depender do nome dele.
5. **Registre um ADR para toda decisão que cria lock-in, centraliza enforcement ou altera trust boundary.** Essas três são reversíveis apenas com custo alto, e a justificativa precisa sobreviver à saída de quem decidiu.

A ordem importa. Invertida — produto primeiro, capability depois — a organização passa a chamar de governança aquilo que a ferramenta comprada faz.

## Capacidades a mapear

| Capability | Função de controle | Categorias que costumam fornecer | Decidir antes de escolher produto |
|---|---|---|---|
| estate e registry | existência, ownership, tier e estado de cada agente | inventário de configuração, ITSM, GRC, plataforma de execução | quem é source of truth de cada campo e como conflitos são reconciliados |
| identidade não-humana | emissão, escopo, expiry e revogação de identidade própria | IAM e governança de identidade, gestão de segredos | se o agente atua com identidade delegada, própria ou ambas, e como JML se aplica |
| dados certificados | quais fontes podem ser usadas, por quem e com quais restrições | catálogo de dados, prevenção de perda de dados, plataforma de dados | critério de certificação e quem tem autoridade sobre a fonte |
| mediação de ações | autorização por ação e parâmetro antes da execução | gateway de API, camada de integração, broker próprio | quais ações exigem mediação e quais podem permanecer no builder |
| acesso a modelos | roteamento, allowlist, budget, fallback e logging de chamadas | gateway de modelos ou proxy de inferência | combinações modelo/provedor permitidas por classe de dado |
| lifecycle e attestation | transições, dormancy, revalidação e retirada | GRC, ITSM, o próprio registry | o que é mudança material e o que dispara reassessment |
| observabilidade e correlação | reconstruir o que aconteceu, ponta a ponta | plataforma de observabilidade, SIEM | schema de telemetria e chave de correlação comuns |
| custo e unit economics | orçamento, quota e custo por resultado | gestão de custo de nuvem, FinOps | qual é a unidade de resultado antes de medir custo por ela |
| evidência | pacote recuperável, versionado e íntegro por release | GRC, repositório de evidências | retenção por tier e como a integridade é verificada |

Nenhuma linha nomeia produto. A coluna de categorias existe para acelerar o reconhecimento do que já existe na casa, não para sugerir compra.

## Regra do source of truth

Um atributo tem **exatamente um** sistema autoritativo. Os demais consomem e podem exibir, nunca redefinir.

Quando dois sistemas discordam, a divergência é finding — não é resolvida escolhendo o valor mais recente. Reconciliação silenciosa por timestamp destrói a evidência de que houve conflito, que costuma ser o sinal mais útil.

## Quando o mapeamento exige ADR

- a decisão cria dependência difícil de reverter em prazo aceitável;
- o enforcement de um controle passa a existir em um único componente;
- a fronteira de confiança muda, incluindo quem pode emitir identidade ou autorizar ação;
- uma capability passa a depender de um sistema fora do perímetro de assurance da organização.

## Evidências

- mapeamento capability × sistema, com owner e data;
- source of truth declarado por atributo;
- contratos de integração e o que cada um garante;
- ADRs das decisões de lock-in, centralização e trust boundary;
- gaps sem sistema atribuído, com owner e prazo.

## Métricas

- capabilities sem sistema atribuído;
- atributos com mais de um sistema se declarando autoritativo;
- divergências de reconciliação abertas por período;
- decisões de lock-in sem ADR;
- capabilities cobertas por sistema fora do perímetro de assurance.

## Failure modes

- escolher produto antes de definir capability e controle;
- tratar cobertura de produto como cobertura de controle;
- duplicar ownership do mesmo atributo em vários sistemas;
- reconciliar divergência por timestamp e perder o sinal de conflito;
- deixar o mapeamento sem data de revisão e descobrir na auditoria que ele descreve um estado antigo;
- misturar o mapeamento na arquitetura e ter de reescrever a arquitetura quando o produto mudar.

## Decision gate

Uma capability não é declarada implantada sem sistema atribuído, source of truth por atributo e evidência recuperável. Cobertura prometida por roadmap de fornecedor não é cobertura.
