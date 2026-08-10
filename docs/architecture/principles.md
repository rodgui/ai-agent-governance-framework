---
title: "Princípios arquiteturais de governança de agentes"
status: maintained
maturity: validated
last_reviewed: 2026-08-10
review_cycle: 180d
owners: [rodgui]
tags: [architecture, principles, agent-governance]
---

# Princípios arquiteturais de governança de agentes

Princípios só têm valor se alterarem decisões. Um princípio que nunca reprovou uma proposta é um slogan.

Por isso cada princípio abaixo carrega três coisas: a **pergunta de decisão** que ele faz, a **aplicação prática** que dele decorre e o **antipattern** que ele existe para evitar. Um princípio que não consegue preencher as três colunas não deveria estar nesta lista.

## Os princípios

1. **Visibility first:** não se governa o que não se consegue descobrir e registrar.
2. **Identity first:** toda ação relevante é atribuível a um usuário, agente ou workload identificado.
3. **Explicit capability:** acesso de leitura não implica direito de escrita; possuir uma ferramenta não autoriza qualquer parâmetro.
4. **Proportional by risk:** controles aumentam com alcance, dados, capacidade de ação, autonomia e irreversibilidade.
5. **Embedded by default:** guidance, limites, identidade, logging e policy entram nas ferramentas e pipelines.
6. **Human-led:** pessoas definem direção, aprovam exceções e permanecem accountable.
7. **Observable and remediable:** autonomia relevante exige telemetria, quarantine, rollback e sunset.
8. **Federated with common controls:** domínios mantêm ownership; padrões comuns preservam interoperabilidade e confiança.
9. **Evidence before automation:** decisões e exceções precisam de evidência antes de virar policy-as-code.
10. **Lifecycle-aware:** criação, mudança, attestation, transferência e decommissioning fazem parte do mesmo sistema.
11. **Platform-agnostic:** policy e control objectives são comuns; implementação varia por plataforma.
12. **Value-linked:** criação e uso só importam quando conectados a qualidade, risco, experiência e resultado.
13. **Iterative:** arquitetura, controles e classificação de risco evoluem com tecnologia, regulação e evidência operacional.

## Como cada princípio decide

| Princípio | Pergunta de decisão | Aplicação prática | Antipattern |
|---|---|---|---|
| Visibility first | consigo identificar o agente, o owner e a plataforma? | agente desconhecido é descoberto e classificado antes de receber enforcement progressivo | bloquear tudo antes de ter inventário, criando incentivo para shadow AI |
| Identity first | quem ou o que executou esta ação? | cada execução relevante carrega identidade do ator e contexto de autorização | uma chave de API compartilhada entre vários agentes |
| Explicit capability | a autorização considera a ação **e** os parâmetros? | uma ferramenta de atualização pode editar descrição sem poder alterar prioridade crítica | autorizar uma API inteira porque uma operação era necessária |
| Proportional by risk | o esforço de controle corresponde ao impacto real? | T1 somente leitura recebe policy gate; T3 financeiro recebe assessment, oversight e assurance ampliado | o mesmo formulário e o mesmo comitê para todos |
| Embedded by default | o caminho governado é mais fácil que contorná-lo? | limites, identidade e logging vêm no template, não no manual | publicar guidance e esperar adesão voluntária |
| Human-led | quem responde por esta decisão, nominalmente? | aceitação de risco residual pertence a quem responde pelo impacto | tratar revisão humana como carimbo de um resultado já pronto |
| Observable and remediable | como detectamos desvio depois da aprovação? | telemetria, budget, baseline de comportamento, quarentena e reassessment | tratar a aprovação inicial como garantia permanente |
| Federated with common controls | esta decisão pertence a qual authority de domínio? | identidade, dados e segurança mantêm suas competências sob padrões comuns | um time de governança que absorve o ownership dos demais |
| Evidence before automation | temos dado confiável para automatizar esta decisão? | automatizar primeiro a preparação da evidência; a decisão só com policy estável | policy-as-code sobre um campo que ninguém reconcilia |
| Lifecycle-aware | o que acontece quando o owner sai ou o uso desaparece? | cada agente nasce com owner, reavaliação, attestation e critério de retirada | agente publicado que mantém acessos e custo sem dono |
| Platform-agnostic | esta regra sobrevive à troca de fornecedor? | a policy define capability e evidência; o adapter varia | escrever o controle em termos de um produto |
| Value-linked | que outcome justifica custo e risco? | portfolio review retira agentes sem adoção ou benefício | medir sucesso pelo número de agentes publicados |
| Iterative | o que aprendemos que muda esta regra? | thresholds e classificação revisados com evidência de operação | congelar a matriz de risco depois do primeiro release |

## Como validar os princípios

Princípio ambíguo produz interpretação local, e interpretação local produz divergência que só aparece em auditoria.

1. Selecione dez cenários reais ou plausíveis — incluindo ao menos um caso financeiro, um somente leitura, um com ferramenta privilegiada e um agente de terceiro embarcado em SaaS.
2. Peça a **três grupos diferentes** que apliquem os princípios sem consultar o autor. Compare as decisões.
3. Divergência alta indica princípio ambíguo, não grupo despreparado.
4. Transforme divergência recorrente em regra mais concreta, standard ou decision tree. **Princípio não deve carregar detalhe que pertence a um standard.**
5. Revalide anualmente, ou quando surgir nova classe de risco — novos protocolos de descoberta de ferramentas, delegação entre agentes ou aumento material de autonomia.

Registre o resultado do teste: cenários usados, divergências encontradas e o que foi refinado em consequência. Sem esse registro, a próxima revisão recomeça do zero.

## Tensões que os princípios não resolvem sozinhos

Alguns princípios se opõem em casos concretos, e é aí que a authority decide:

- **Visibility first × Embedded by default** — enforcement antes do inventário empurra a criação para fora do radar. A sequência correta é descobrir, classificar e só então restringir progressivamente.
- **Proportional by risk × Federated with common controls** — proporcionalidade pede caminhos diferentes; federação pede padrão comum. O padrão comum é o *mínimo*, não o uniforme.
- **Evidence before automation × Value-linked** — esperar evidência perfeita custa valor; automatizar cedo custa confiança. O gargalo manual medido é o que decide qual custo é maior.

Quando dois princípios colidem, a decisão é registrada com rationale — não resolvida por preferência de quem estava na sala.

## Relação com a policy

Esses princípios integram a [policy modular](../governance/policy.md). Sua adoção e alteração exigem revisão formal, decision authority e release versionada; mappings de plataforma não podem redefini-los.
