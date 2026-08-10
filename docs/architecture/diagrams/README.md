# Architecture diagrams

## Framework canônico

- [AI Agent Governance Framework](ai-agent-governance-framework.png) — visual vendor-neutral dos cinco planos, decision gates, build/runtime e lifecycle.

O visual principal não contém produtos ou métricas de fornecedor.

## Estudos de caso

Visuais específicos de fornecedor ficam junto ao estudo correspondente. O caso Microsoft está em [`docs/explanations/diagrams/`](../../explanations/diagrams/).

## Reprodução

Ambas as variantes são geradas por [`tools/scripts/render-agent-governance-infographic.py`](../../../tools/scripts/render-agent-governance-infographic.py).

```bash
python3 tools/scripts/render-agent-governance-infographic.py --variant framework
```
