# Exemplo — Certified Source Catalog e Data Remediation Backlog

> Fictício e sanitizado. Nomes, sistemas e prazos são ilustrativos e não representam cliente real.

Demonstra o [gate de dados AI-ready](../docs/patterns/ai-ready-data-gate.md) e o domínio de [dados, acesso e provenance](../docs/data-access/README.md): uma fonte só pode ser usada por um agente depois de certificada, e o que não passa vira backlog com owner e prazo — não some do mapa.

## Critérios de certificação

Uma fonte é `certified` quando todos os requisitos passam com evidência recuperável.

| Requisito | Critério de aprovação | Evidência esperada |
|---|---|---|
| owner | data owner e steward registrados e ativos | registro no catálogo |
| classificação | rótulo atual e regra explícita de uso por IA | label + política aplicável |
| acesso | least privilege e higiene de grupos verificadas | relatório de revisão de ACL |
| qualidade | checks adequados ao caso de uso, não genéricos | painel de qualidade |
| atualidade | cadência de refresh e SLA conhecidos | `last_refresh` + SLA |
| proveniência | origem e transformações rastreáveis | metadados de lineage |
| segurança | controles de envenenamento, injeção e secrets quando aplicável | resultados de scan e teste |
| recertificação | data de revisão e gatilho definidos | data de revisão no catálogo |

`Conditional` significa que a fonte é utilizável com restrição declarada. `Not ready` significa que nenhum agente pode usá-la — e não que o assunto está encerrado.

## Certified Source Catalog

| Source ID | Nome | Classificação | Status | Tiers permitidos | Restrições | Próxima revisão |
|---|---|---|---|---|---|---|
| `KB-HR-001` | Políticas de RH | interno | `certified` | T1–T2 | apenas usuários internos | 2026-11-01 |
| `KB-IT-001` | Base de procedimentos de TI | interno | `certified` | T1–T2 | somente leitura | 2026-11-15 |
| `CMDB-READ` | Visão de configuração | interno | `certified` | T1–T3 | somente leitura; identidade própria do agente | 2026-10-30 |
| `ERP-AP-READ` | Visão de faturas a pagar | confidencial | `conditional` | T2–T3 | somente leitura; identidade própria; sem exportação | 2026-10-15 |
| `LEGACY-SHARE-9` | Compartilhamento legado | desconhecida | `not-ready` | nenhum | limpeza de permissões pendente | — |

Repare em `LEGACY-SHARE-9`: classificação **desconhecida** não é o mesmo que baixa sensibilidade. Enquanto não houver owner e classificação, nenhum tier pode consumi-la.

## Data Remediation Backlog

O que reprova na certificação não desaparece: entra aqui com gap, risco, ação, owner e prazo.

| Fonte | Gap | Risco | Ação | Owner | Prazo |
|---|---|---|---|---|---|
| `LEGACY-SHARE-9` | ACLs amplas e owner desconhecido | alto | atribuir owner, revisar ACL, classificar | Domínio de Dados A | 30 dias |
| `KB-IT-001` | 20% dos documentos sem data de revisão | médio | completar metadados e revisar conteúdo | Operações | 60 dias |
| `ERP-AP-READ` | lineage parcial nas transformações | médio | mapear pipeline e registrar proveniência | Plataforma de Dados | 45 dias |

## O que este exemplo não demonstra

- não define thresholds de qualidade — eles dependem do caso de uso;
- não substitui avaliação de privacidade ou obrigação setorial sobre as fontes;
- `certified` não é permanente: é válido até a data de revisão ou até um gatilho de mudança material;
- a ausência de fonte `not-ready` em produção não prova que não existe acesso paralelo fora do catálogo — isso é medido por descoberta, não por este registro.
