# Standards de referência — escopo e limites de uso

Esta página existe para responder "o que esta norma cobre e como ela se relaciona com o framework" **sem redistribuir texto normativo**.

## O que esta página é e não é

Normas ISO/IEC são obras protegidas e comercializadas. Reproduzir o texto delas — mesmo parcialmente, mesmo em repositório privado — é violação de direito autoral — um problema jurídico maior que a lacuna que ele tentaria resolver.

Portanto, aqui você encontra:

- **descrição de escopo em linguagem própria**, a partir de informação pública dos catálogos oficiais;
- **como cada norma se relaciona** com os domínios e controls deste framework;
- **o que ela exige que este framework não entrega**;
- link oficial para aquisição ou consulta.

E **não** encontra: cláusulas, requisitos literais, tabelas de Anexo, numeração interna ou qualquer trecho do texto normativo.

## Por que não existe mapeamento control a control para ISO

Os 44 controls declaram `frameworkMappings` para NIST AI RMF, EU AI Act, OWASP e MITRE ATLAS — todos públicos e verificáveis. **ISO não está mapeada**, e isso é deliberado: mapear exige o texto, e um número de cláusula produzido de memória ou de fonte secundária seria uma afirmação que o repositório não pode sustentar.

Enquanto o mapeamento não existir, a relação com ISO deve ser comunicada como **alinhamento conceitual**, nunca como rastreabilidade. A diferença importa: alinhamento conceitual diz "pensamos sobre os mesmos problemas"; rastreabilidade diz "este control atende àquele requisito" — e só a segunda sobrevive a uma pergunta de auditoria.

## ISO/IEC 42001:2023 — AI management system

**O que é.** Norma de sistema de gestão para inteligência artificial, na estrutura comum das normas de gestão (a mesma família estrutural de ISO 9001 e 27001). É **certificável** por organismo acreditado.

**O que cobre, em linhas gerais.** Contexto organizacional e partes interessadas; liderança e política de IA; planejamento incluindo tratamento de riscos e objetivos; recursos, competência e conscientização; operação, incluindo avaliação de impacto e gestão do ciclo de vida dos sistemas de IA; avaliação de desempenho e auditoria interna; melhoria contínua. Possui um anexo de controles de referência que a organização seleciona e justifica.

**Relação com este framework.** É a norma mais próxima do que o corpus faz: o [operating model](../../docs/governance/operating-model.md), a [policy modular](../../docs/governance/policy.md), o [control catalog](../../controls/README.md) e o [maturity model](../../docs/guides/maturity-model.md) endereçam o mesmo território.

**O que ela exige e este framework não entrega.** Certificação depende de auditoria por organismo acreditado, com escopo declarado, evidência amostrada e ciclo de manutenção. Este framework **não certifica, não audita e não substitui** esse processo. Adotar a release 1.0 não aproxima nem afasta uma organização de certificação.

Catálogo oficial: <https://www.iso.org/standard/42001>

## ISO/IEC 23894:2023 — gestão de riscos de IA

**O que é.** Documento de **orientação** — não certificável — sobre gestão de riscos aplicada a sistemas de IA, construído sobre a estrutura genérica de gestão de riscos da ISO 31000.

**O que cobre, em linhas gerais.** Como adaptar princípios, estrutura e processo de gestão de riscos ao contexto de IA, com atenção a fontes de risco específicas da tecnologia e ao ciclo de vida do sistema.

**Relação com este framework.** Corresponde ao domínio de [gestão proporcional de riscos](../../docs/risk-management/README.md), incluindo tiering, red flags, residual risk e reavaliação por mudança material.

**Limite.** Sendo orientação, não produz conformidade verificável por si. Citá-la como "aderência" é impreciso — o que existe é convergência de método.

Catálogo oficial: <https://www.iso.org/standard/77304.html>

## ISO/IEC 42005:2025 — AI system impact assessment

**O que é.** Orientação sobre processo e documentação de avaliação de impacto de sistemas de IA sobre indivíduos, grupos e sociedade, ao longo do ciclo de vida.

**O que cobre, em linhas gerais.** Como identificar onde o sistema pode causar dano ou consequência não pretendida; como analisar severidade, probabilidade e natureza do impacto; quando reexecutar a avaliação; e como documentá-la de forma recuperável.

**Relação com este framework.** Corresponde diretamente ao [impact assessment de Responsible AI](../../docs/responsible-ai/README.md#impact-assessment) e ao control `AGF-RAI-001`.

**Limite.** É a norma que este framework mais se beneficiaria de mapear, porque o objeto é quase idêntico. Permanece não mapeada pelo mesmo motivo das demais.

Catálogo oficial: <https://www.iso.org/standard/42005>

## ISO/IEC 22989:2022 — conceitos e terminologia

**O que é.** Vocabulário e conceitos de IA. Útil para alinhar linguagem entre áreas técnicas, jurídicas e de negócio.

**Relação com este framework.** O [glossário canônico](../glossary.md) foi construído para uso operacional e não reproduz a terminologia normativa. Divergências de vocabulário entre os dois são esperadas e devem ser declaradas quando o contexto for regulatório.

Catálogo oficial: <https://www.iso.org/standard/74296.html>

## Como fechar a lacuna

Três caminhos, em ordem de qualidade da evidência resultante:

1. **Adquirir as normas** e mapear cada control ao requisito real. Produz rastreabilidade de primeira mão e é o único caminho que sobrevive a uma auditoria.
2. **Usar mapeamento publicado por terceiro** — a matriz de controles de IA da Cloud Security Alliance, por exemplo, publica seus próprios mapeamentos para normas. Nesse caso o mapeamento é **do terceiro**, deve ser atribuído a ele, e vale como evidência de segunda mão.
3. **Manter a lacuna declarada**, como está hoje, e comunicar alinhamento conceitual em vez de rastreabilidade.

O caminho 3 é honesto e é o estado atual. Ele apenas não é confortável numa conversa comercial — o que é diferente de ser incorreto.

## Fontes públicas já mapeadas

As referências efetivamente usadas nos `frameworkMappings` estão registradas em [fontes](../sources.md), com data de acesso e uso relacionado.
