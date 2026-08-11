#!/usr/bin/env python3
"""Monta os entregáveis em DOCX a partir do corpus canônico.

Três documentos, um corpus. O repositório continua sendo a fonte; estes arquivos são
derivados e descartáveis — nada é editado aqui e depois trazido de volta.

O que a conversão precisa resolver, e que um `pandoc` direto não resolve:

- **links não existem no papel.** Referência interna vira texto simples; o leitor de um
  documento impresso não clica. Link externo permanece, porque ali a URL é o conteúdo.
- **mermaid não renderiza em DOCX.** O bloco vira uma nota de figura em vez de despejar
  código-fonte de diagrama no meio do texto.
- **front matter YAML** é metadado de repositório, não de publicação.
- **cada documento-fonte vira um capítulo**, então a hierarquia de títulos precisa ser
  normalizada para que o sumário do Word tenha um nível só de capítulo.

Uso:
    python3 tools/scripts/build-docx.py [executive|guide|reference|all]
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "dist"

DISCLAIMER = """
> **O que este documento é e o que não é.** Framework de referência vendor-neutral para
> governar sistemas de IA e agentes. Os controles declaram evidência e modo de verificação,
> e os casos apresentados são **fictícios e sanitizados**: demonstram coerência do método,
> não eficácia comprovada. Nenhum controle deste material foi exercitado contra um estate
> real. Tiers, thresholds e prazos são ilustrativos e **precisam ser recalibrados** com os
> dados da organização que o adotar.
>
> Se a organização já possui uma policy corporativa de IA, **ela prevalece**. Este material
> é a camada de execução para agentes, não substituto de instrumento normativo aprovado.
>
> A adoção de uma release versiona esta baseline; não constitui certificação, auditoria
> independente nem declaração de conformidade por nenhuma organização.
"""

# Cada entrega: título, subtítulo e a sequência de documentos-fonte.
# A ordem do guia é a do método, não a dos domínios — é o que separa guia de referência.
DELIVERABLES: dict[str, dict] = {
    "executive": {
        "title": "Governança de Agentes de IA",
        "subtitle": "Brief executivo — o que decidir antes de escalar",
        "output": "AI-Agent-Governance-Executive-Brief.docx",
        "sources": [
            "docs/executive/governing-agents-at-scale.md",
            "docs/fundamentals/README.md",
            "docs/architecture/overview.md",
            "docs/governance/operating-model.md",
            "docs/explanations/cases/benefits-eligibility-triage.md",
        ],
    },
    "guide": {
        "title": "Governança de Agentes de IA",
        "subtitle": "Guia de implantação — do mandato ao runtime",
        "output": "AI-Agent-Governance-Guia-de-Implantacao.docx",
        "sources": [
            # mandato e método
            "docs/start-here.md",
            "docs/guides/framework-implementation-playbook.md",
            "docs/governance/policy.md",
            # baseline
            "docs/guides/capability-map.md",
            "docs/guides/maturity-model.md",
            # risco e decisão
            "docs/risk-management/README.md",
            "docs/risk-management/minimum-production-bar.md",
            "docs/governance/operating-model.md",
            # fundações
            "docs/registry/README.md",
            "docs/identity/README.md",
            "docs/data-access/README.md",
            "docs/tool-governance/README.md",
            "docs/model-governance/README.md",
            "docs/architecture/capability-to-technology.md",
            # assurance
            "docs/security/README.md",
            "docs/responsible-ai/README.md",
            "docs/human-oversight/README.md",
            "docs/evaluations/README.md",
            "docs/auditability/evidence-pack-by-tier.md",
            "docs/auditability/audit-universe-crosswalk.md",
            # runtime e valor
            "docs/operations/README.md",
            "docs/lifecycle/README.md",
            "docs/value/README.md",
            "docs/adoption/README.md",
            # casos e toolkit
            "docs/explanations/cases/meeting-notes-summarizer.md",
            "docs/explanations/cases/service-desk-knowledge-agent.md",
            "docs/explanations/cases/benefits-eligibility-triage.md",
            "docs/reference/artifact-catalog.md",
            "templates/ai-vendor-contract-clauses.md",
        ],
    },
}

FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", flags=re.S)
MERMAID_RE = re.compile(r"```mermaid\r?\n.*?```", flags=re.S)
# [texto](destino) onde destino não é http/mailto — no papel o link não existe
INTERNAL_LINK_RE = re.compile(r"\[([^\]]+)\]\((?!https?://|mailto:)[^)]+\)")
BADGE_RE = re.compile(r"^!\[[^\]]*\]\([^)]*\)\s*$", flags=re.M)


def handbook_sources() -> list[str]:
    """A referência completa segue a ordem editorial do handbook, sem duplicá-la."""
    text = (ROOT / "docs/handbook/README.md").read_text(encoding="utf-8")
    seen: list[str] = []
    for match in re.finditer(r"^\s*(?:\d+\.|\s+-)\s+\[[^\]]+\]\(([^)]+\.md)\)", text, flags=re.M):
        target = (ROOT / "docs/handbook" / match.group(1)).resolve()
        try:
            rel = str(target.relative_to(ROOT))
        except ValueError:
            continue
        if target.exists() and rel not in seen:
            seen.append(rel)
    return seen


def clean(markdown: str) -> str:
    markdown = FRONTMATTER_RE.sub("", markdown)
    markdown = BADGE_RE.sub("", markdown)
    markdown = MERMAID_RE.sub(
        "> *[Diagrama disponível na versão on-line do framework.]*", markdown
    )
    markdown = INTERNAL_LINK_RE.sub(r"\1", markdown)
    return markdown.strip()


def demote(markdown: str) -> str:
    """Cada documento-fonte é um capítulo: seu H1 permanece H1 e o resto desce um nível."""
    lines = []
    for line in markdown.splitlines():
        match = re.match(r"^(#{2,6})\s", line)
        if match and len(match.group(1)) < 6:
            line = "#" + line
        lines.append(line)
    return "\n".join(lines)


# O writer DOCX do pandoc não conhece \newpage — isso é LaTeX e sairia como texto
# literal. Quebra de página em DOCX é OpenXML bruto.
PAGE_BREAK = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'


def assemble(spec: dict) -> str:
    # Título e subtítulo entram por --metadata; o bloco `% título` do pandoc só é lido
    # nos formatos markdown clássicos e vazaria como texto em gfm.
    parts = [DISCLAIMER.strip(), ""]
    for rel in spec["sources"]:
        path = ROOT / rel
        if not path.exists():
            print(f"  aviso: fonte ausente, ignorada: {rel}", file=sys.stderr)
            continue
        parts.append(PAGE_BREAK)
        parts.append(demote(clean(path.read_text(encoding="utf-8"))))
    return "\n\n".join(parts)


def build(name: str, spec: dict) -> Path:
    OUT.mkdir(exist_ok=True)
    md_path = OUT / f"{name}.md"
    md_path.write_text(assemble(spec), encoding="utf-8")
    docx_path = OUT / spec["output"]
    subprocess.run(
        [
            "pandoc", str(md_path),
            "-f", "gfm+definition_lists+raw_attribute",
            "-o", str(docx_path),
            "--toc", "--toc-depth=2",
            "--metadata", f"title={spec['title']}",
            "--metadata", f"subtitle={spec['subtitle']}",
        ],
        check=True,
    )
    chars = len(md_path.read_text(encoding="utf-8"))
    print(f"  {spec['output']}  ({len(spec['sources'])} capítulos, {chars:,} chars)")
    return docx_path


def main() -> int:
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    specs = dict(DELIVERABLES)
    specs["reference"] = {
        "title": "Governança de Agentes de IA",
        "subtitle": "Referência completa — framework, controles e toolkit",
        "output": "AI-Agent-Governance-Referencia-Completa.docx",
        "sources": handbook_sources(),
    }
    targets = specs if which == "all" else {which: specs[which]}
    for name, spec in targets.items():
        print(f"gerando {name}...")
        build(name, spec)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
