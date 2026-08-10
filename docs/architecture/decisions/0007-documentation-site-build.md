---
title: ADR-0007 — Site de documentação gerado a partir do corpus canônico
status: superseded
owner: Rodrigo Garcia Guimarães
last_reviewed: 2026-08-10
review_cycle: major-change
supersedes: null
superseded_by: 0008-manual-documentation-site-publication.md
related:
  - 0003-single-canonical-source-and-guide-absorption.md
  - ../../handbook/README.md
  - ../../../references/standards/README.md
---

# ADR-0007 — Site de documentação gerado a partir do corpus canônico

> **Superseded:** a [ADR-0008](0008-manual-documentation-site-publication.md) preserva build strict e CI, mas torna publicação opcional e manual, sem prerequisite de GitHub Pages.

## Contexto

A [ADR-0003](0003-single-canonical-source-and-guide-absorption.md) estabeleceu o repositório como fonte única, substituindo um guia em documento único. A decisão foi correta — versionamento, CI e rastreabilidade não existem em um `.docx` — mas cobrou um preço que ficou pendente: **perdeu-se a leitura linear**.

Ninguém abre 122 arquivos. Um executivo, um comprador ou um aluno precisa de uma superfície de leitura contínua, com navegação e busca. O handbook define a ordem editorial, mas hoje é apenas um índice de links dentro do próprio repositório.

Há um obstáculo técnico específico: o conteúdo canônico está distribuído entre `docs/`, `controls/`, `schemas/`, `templates/`, `examples/`, `references/`, `assessments/` e `consulting/`, e os links entre essas pastas são relativos e cruzam fronteiras (`../../controls/README.md`). Qualquer solução que publique apenas uma dessas pastas produz um site com links quebrados.

## Forças e constraints

- o repositório não tinha nenhum sistema de build; adicionar um é peso novo de manutenção;
- reescrever links para acomodar a ferramenta inverteria a relação: o corpus passaria a servir o site;
- o site não pode divergir do repositório — se divergir, volta a existir uma segunda fonte, exatamente o que a ADR-0003 eliminou;
- os diagramas do corpus são mermaid e precisam renderizar;
- as âncoras internas usam acentuação e precisam continuar funcionando nos dois lugares.

## Opções consideradas

### Opção A — Jekyll nativo servindo `docs/`

**Vantagens:** zero dependência, basta ligar nas configurações do repositório.

**Desvantagens:** serve apenas `docs/`. Todo link para `controls/`, `schemas/`, `templates/` e `examples/` quebra. Corrigir exigiria reescrever links ou mover conteúdo — o corpus servindo a ferramenta.

### Opção B — Página única gerada do handbook

**Vantagens:** recupera exatamente a leitura linear perdida; bom para entregar a um cliente.

**Desvantagens:** não resolve navegação nem busca; um documento de 359 mil caracteres não é consultável.

### Opção C — MkDocs Material com staging que preserva a estrutura

**Vantagens:** navegação pela ordem do handbook, busca, mermaid renderizado, tema claro e escuro; e, principalmente, **nenhum link precisa ser reescrito**.

**Desvantagens:** adiciona um build e três dependências ao repositório.

## Decisão

Adotar a opção C.

1. `tools/scripts/build-docs-site.py` monta `site_src/` copiando as pastas canônicas **preservando a hierarquia de diretórios**. Como a estrutura relativa é idêntica à do repositório, os links que cruzam pastas continuam válidos sem qualquer reescrita.
2. O build roda em **modo strict**: link quebrado ou referência inexistente falha a execução.
3. O mesmo build entra no workflow de quality gates. Um pull request que quebre um link não passa — o site deixa de poder divergir do repositório em silêncio.
4. As âncoras usam slugify compatível com o GitHub, preservando acentuação, para que um link funcione igual no repositório e no site.
5. `site_src/` e `site/` são artefatos de build: ignorados no git e excluídos da varredura do validador.
6. A navegação reproduz a ordem do handbook. **O handbook continua sendo a ordem editorial canônica**; a configuração do site a espelha e não a substitui.
7. As dependências ficam fixadas em `requirements-docs.txt`, separadas das de validação.

## Consequências positivas

- o custo declarado da ADR-0003 é pago: leitura contínua sem segunda fonte;
- o site é derivado, nunca mantido em paralelo — é o que a ADR-0003 exige de qualquer publicação;
- link quebrado passa a ser erro de CI, não descoberta do leitor;
- schemas e exemplos são publicados como fonte, permitindo inspecionar o contrato e não apenas sua descrição.

## Consequências negativas

- três dependências novas e um build a manter;
- a ordem de navegação existe em dois lugares — handbook e configuração do site — e pode divergir;
- publicar exige uma configuração no repositório que não está sob controle de versão.

## Riscos e mitigação

| Risco | Mitigação |
|---|---|
| navegação do site divergir do handbook | comentário explícito na configuração declarando o handbook como origem; divergência é revisada junto com mudanças no handbook |
| site publicar conteúdo defasado | build no mesmo workflow de qualidade e publicação disparada por push na branch principal |
| dependência de build quebrar por atualização | versões fixadas em `requirements-docs.txt` |
| leitor confundir site com fonte normativa | o site é gerado do corpus; qualquer divergência é defeito de build, não versão alternativa |

## Configuração externa necessária

A publicação exige que, nas configurações do repositório, **Pages → Build and deployment → Source** esteja definido como **GitHub Actions**. Essa configuração não vive no repositório e precisa ser feita uma vez pelo mantenedor. Enquanto não for, o workflow constrói e falha na publicação — o que é preferível a falhar silenciosamente.

## Critérios de validação

- o build passa em modo strict, sem link quebrado;
- as âncoras acentuadas resolvem no site e no repositório;
- os diagramas mermaid renderizam;
- o validador do repositório não inspeciona artefatos de build;
- a ordem de navegação corresponde ao handbook.

## Evidência da decisão

Decisão tomada por Rodrigo Garcia Guimarães em 2026-08-10, após a release 1.0, para pagar o custo de leitura linear que a adoção do repositório como fonte única havia deixado em aberto.
