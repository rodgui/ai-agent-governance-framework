# Exemplo — Governance charter e scope statement

> Fictício e sanitizado. Nomes, unidades e limites são ilustrativos.

Demonstra o entregável do gate G0 do [implementation playbook](../docs/guides/framework-implementation-playbook.md). Sem mandato, não se automatiza aprovação nem se promete cobertura.

## Charter

| Seção | Conteúdo |
|---|---|
| **missão** | Estabelecer governança proporcional ao risco para agentes de IA e permitir escala com accountability, segurança e valor demonstrável. |
| **escopo** | Agentes internos e externos em produção e pilotos corporativos. Builders pessoais entram por discovery e recebem a baseline de policy. |
| **authority** | Definir standards; exigir registro; **suspender agentes fora do Minimum Production Bar**; escalar casos de uso restrito. |
| **princípios** | Visibilidade primeiro; identidade primeiro; capacidade explícita; proporcionalidade; policy-as-code onde a policy é estável; governança em runtime; accountability de valor. |
| **fóruns** | Governance Council; Design Authority; review de risco e Responsible AI; operação de segurança; review de valor. |
| **medidas** | Cobertura do inventário; cobertura de ownership; lead time por tier; incidentes; attestation; custo por resultado; valor observado. |

A linha que faz o charter valer alguma coisa é a terceira. **Authority para suspender é o que separa um charter de uma declaração de intenções** — sem ela, o resto é recomendação.

## Scope statement

**Dentro do escopo:** agentes em produção; agentes compartilhados ou de time; agentes que invocam ferramentas corporativas; agentes que usam dados confidenciais ou restritos; SaaS com recursos agentic; servidores MCP usados corporativamente.

**Fora do escopo inicialmente:** protótipos isolados de pesquisa, com dados sintéticos e sem credencial corporativa — sujeitos a discovery e a exceção com prazo.

**Geografias:** todas as unidades. Restrições legais locais **adicionam** controles; nunca removem.

**Ambientes:** desenvolvimento, teste e produção. Produção tem controles mais estritos, mas **desenvolvimento não é isento** de policy de secrets e de dados.

## Por que o "fora do escopo" tem prazo

Escopo inicial reduzido é decisão legítima de sequenciamento. Escopo reduzido **sem prazo** é uma exceção permanente disfarçada — e é exatamente onde o shadow AI se instala, porque a organização declarou que aquele espaço não é observado.

Por isso a exclusão de protótipos vem com duas condições: continuam sujeitos a discovery, e a exclusão expira.

## O que este exemplo não demonstra

- não substitui aprovação pela authority competente da organização;
- os fóruns listados precisam de [terms of reference](../templates/governance-forum-tor.md) próprios para existirem de fato;
- as medidas precisam de definição, owner e threshold antes de irem a um fórum;
- um charter aprovado e nunca exercido não é evidência de mandato — a evidência é a **primeira decisão registrada** que usou a authority.
