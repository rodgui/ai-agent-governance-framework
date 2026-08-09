# Scripts

Scripts reproduzíveis usados para validar ou gerar artefatos do repositório.

- `render-agent-governance-infographic.py` — gera `docs/architecture/diagrams/agent-governance-operating-model.png` em 1800 × 2400 px usando Pillow.

## Uso

```bash
python3 -m pip install Pillow
python3 tools/scripts/render-agent-governance-infographic.py
```

O renderer procura Arial, DejaVu Sans ou Liberation Sans em caminhos comuns de macOS, Linux e Windows. Em outro ambiente, informe fontes TrueType explicitamente:

```bash
export AGF_FONT_REGULAR=/path/to/regular.ttf
export AGF_FONT_BOLD=/path/to/bold.ttf
```
