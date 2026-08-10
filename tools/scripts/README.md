# Scripts

Scripts reproduzíveis usados para validar ou gerar artefatos do repositório.

## Infográficos

`render-agent-governance-infographic.py` gera duas variantes em 1800 × 2400 px:

- `framework` → `docs/architecture/diagrams/ai-agent-governance-framework.png`;
- `microsoft` → `docs/explanations/diagrams/microsoft-customer-zero-agent-governance.png`.

```bash
python3 tools/scripts/render-agent-governance-infographic.py
python3 tools/scripts/render-agent-governance-infographic.py --variant framework
python3 tools/scripts/render-agent-governance-infographic.py --variant microsoft
python3 tools/scripts/render-agent-governance-infographic.py --output-dir /tmp/agf-render
```

Sem `--variant`, ambas são geradas. `--output-dir` escreve as duas imagens com os nomes canônicos em um diretório alternativo; o CI usa essa opção para comparar pixels sem alterar o working tree. O renderer usa as fontes DejaVu Sans versionadas em `tools/assets/fonts/`, com a respectiva `LICENSE_DEJAVU`, para produzir o mesmo layout em macOS, Linux e Windows. Overrides explícitos continuam disponíveis para desenvolvimento, mas alteram o hash do output:

```bash
export AGF_FONT_REGULAR=/path/to/regular.ttf
export AGF_FONT_BOLD=/path/to/bold.ttf
```

## Validação

`validate-repository.py` executa gates de estrutura, links Markdown, paths em `related:` do front matter, referências em JSON (inclusive fragmentos), schemas, negative schema guardrails, invariantes entre records, examples, controls, assets e segurança básica. Também protege os boundaries de produto: consultoria somente em `consulting/`, três pacotes compostos exatamente pelos nove módulos, nomes de fornecedores restritos a fontes, casos, assessments e mappings permitidos e ausência de rótulos da Policy v1 nos templates canônicos. A detecção de fornecedores cobre variações de caixa sem tratar palavras comuns em português como produtos. Os casos negativos incluem evidence IDs inexistentes, assessor/reviewer coincidentes, sampling inválido, attestation vencida no `lastReviewed`, catálogo sem data de revisão, records de produção sem evidência, tools state-changing com enforcement incompleto e entradas malformadas que devem produzir findings em vez de exceptions.

```bash
uv run --with-requirements requirements-ci.txt python3 tools/scripts/validate-repository.py
uv run --with-requirements requirements-ci.txt python3 -m unittest tools/scripts/test_validate_repository.py
```

Os scripts nunca devem materializar secrets, credenciais ou paths pessoais nos artefatos.
