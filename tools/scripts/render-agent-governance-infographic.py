from __future__ import annotations

import argparse
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO_ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK_OUT = (
    REPO_ROOT / "docs" / "architecture" / "diagrams" / "ai-agent-governance-framework.png"
)
MICROSOFT_OUT = (
    REPO_ROOT
    / "docs"
    / "explanations"
    / "diagrams"
    / "microsoft-customer-zero-agent-governance.png"
)
W, H = 1800, 2400
BG = "#081421"
SURFACE = "#10243A"
SURFACE_2 = "#132B44"
WHITE = "#F3F7FC"
MUTED = "#A9B8C9"
BLUE = "#59A6FF"
TEAL = "#38D6C8"
ORANGE = "#FFA44D"
RED = "#FF6B6B"
GREEN = "#7EE0A5"
PURPLE = "#B8A4FF"
GRID = "#183049"


FONT_DIR = REPO_ROOT / "tools" / "assets" / "fonts"


def resolve_font(env_var: str, default_path: Path) -> str:
    path = Path(os.environ.get(env_var, str(default_path))).expanduser()
    if not path.is_file():
        raise FileNotFoundError(
            f"{env_var} points to a missing font: {path}. "
            "Restore the vendored DejaVu font or set a valid override."
        )
    return str(path)


REG = resolve_font("AGF_FONT_REGULAR", FONT_DIR / "DejaVuSans.ttf")
BOLD = resolve_font("AGF_FONT_BOLD", FONT_DIR / "DejaVuSans-Bold.ttf")


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(BOLD if bold else REG, size)


def text_width(draw: ImageDraw.ImageDraw, text: str, selected_font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=selected_font)
    return int(round(box[2] - box[0]))


def wrapped_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    selected_font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = word if not line else f"{line} {word}"
        if text_width(draw, candidate, selected_font) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    selected_font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    spacing: int = 8,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = wrapped_lines(draw, text, selected_font, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while text_width(draw, f"{last}…", selected_font) > max_width and last:
            last = last[:-1]
        lines[-1] = f"{last.rstrip()}…"
    line_height = int(round(selected_font.size + spacing))
    for line in lines:
        draw.text((x, y), line, font=selected_font, fill=fill)
        y += line_height
    return int(round(y))


def pill(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fill: str,
    text_fill: str = BG,
    pad_x: int = 16,
    pad_y: int = 8,
    selected_font: ImageFont.FreeTypeFont | None = None,
) -> int:
    selected_font = selected_font or font(20, True)
    x, y = xy
    width = text_width(draw, text, selected_font)
    height = int(round(selected_font.size + pad_y * 2))
    draw.rounded_rectangle(
        (x, y, x + width + pad_x * 2, y + height),
        radius=height // 2,
        fill=fill,
    )
    draw.text((x + pad_x, y + pad_y - 1), text, font=selected_font, fill=text_fill)
    return x + width + pad_x * 2


def card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: str = SURFACE,
    outline: str | None = None,
    radius: int = 24,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(
        box,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width if outline else 1,
    )


def section_label(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    number: str,
    title: str,
    accent: str,
) -> None:
    draw.text((x, y), number, font=font(20, True), fill=accent)
    draw.text((x + 46, y - 2), title.upper(), font=font(20, True), fill=MUTED)


def line_icon(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    kind: str,
    color: str,
) -> None:
    if kind == "registry":
        draw.rounded_rectangle((x + 8, y + 4, x + 52, y + 62), radius=6, outline=color, width=4)
        draw.line((x + 18, y + 18, x + 42, y + 18), fill=color, width=4)
        draw.line((x + 18, y + 31, x + 42, y + 31), fill=color, width=4)
        draw.line((x + 18, y + 44, x + 35, y + 44), fill=color, width=4)
    elif kind == "controls":
        draw.line((x + 8, y + 18, x + 52, y + 18), fill=color, width=4)
        draw.line((x + 8, y + 34, x + 52, y + 34), fill=color, width=4)
        draw.line((x + 8, y + 50, x + 52, y + 50), fill=color, width=4)
        for cx, cy in [(25, 18), (43, 34), (20, 50)]:
            draw.ellipse((x + cx - 6, y + cy - 6, x + cx + 6, y + cy + 6), fill=BG, outline=color, width=3)
    elif kind == "lifecycle":
        draw.arc((x + 3, y + 7, x + 58, y + 62), 35, 205, fill=color, width=4)
        draw.polygon([(x + 8, y + 22), (x + 2, y + 10), (x + 20, y + 14)], fill=color)
        draw.arc((x + 3, y + 7, x + 58, y + 62), 215, 385, fill=color, width=4)
        draw.polygon([(x + 51, y + 46), (x + 59, y + 58), (x + 39, y + 54)], fill=color)
    elif kind == "risk":
        draw.polygon([(x + 31, y + 3), (x + 60, y + 60), (x + 2, y + 60)], outline=color)
        draw.line((x + 31, y + 21, x + 31, y + 42), fill=color, width=5)
        draw.ellipse((x + 28, y + 49, x + 34, y + 55), fill=color)
    elif kind == "automation":
        draw.rectangle((x + 8, y + 10, x + 48, y + 51), outline=color, width=4)
        draw.line((x + 28, y + 51, x + 28, y + 64), fill=color, width=4)
        draw.line((x + 18, y + 64, x + 38, y + 64), fill=color, width=4)
        draw.line((x + 48, y + 29, x + 61, y + 29), fill=color, width=4)
        draw.polygon([(x + 57, y + 21), (x + 67, y + 29), (x + 57, y + 37)], fill=color)


def arrow(
    draw: ImageDraw.ImageDraw,
    start: tuple[int, int],
    end: tuple[int, int],
    color: str,
    width: int = 5,
) -> None:
    draw.line((start[0], start[1], end[0], end[1]), fill=color, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    length = 18
    first = angle + math.pi - 0.55
    second = angle + math.pi + 0.55
    p1 = (end[0] + length * math.cos(first), end[1] + length * math.sin(first))
    p2 = (end[0] + length * math.cos(second), end[1] + length * math.sin(second))
    draw.polygon([end, p1, p2], fill=color)


def content_for(variant: str) -> dict:
    if variant == "framework":
        return {
            "output": FRAMEWORK_OUT,
            "pill": "FRAMEWORK VENDOR-NEUTRAL  •  POLICY  •  PATTERNS  •  EVIDENCE",
            "title": "AI Agent Governance",
            "subtitle": "Operating model para governança em escala",
            "subtitle_size": 42,
            "tagline": "Estratégia + control plane + assurance + adoção + runtime",
            "tagline_size": 29,
            "note": "Fonte canônica modular: policy, 10 patterns, 38 controls, schemas e playbooks",
            "metrics": [
                ("5 planos", "conectados do mandato ao runtime", BLUE),
                ("38", "controls em 13 domínios verificáveis", TEAL),
            ],
            "thesis_left": "Governar não é centralizar;",
            "thesis_right": "é atribuir decisão, evidência e ação.",
            "thesis_note": "AI-operated • human-led  +  autonomia proporcional ao risco",
            "section1": "Cinco planos conectados",
            "pillars": [
                ("01", "Estratégia + valor", "Mandato, portfólio, baseline e outcomes.", "lifecycle", BLUE),
                ("02", "Control plane", "Registry, blueprint, identidade e lifecycle.", "registry", TEAL),
                ("03", "Assurance plane", "Risco, RAI, privacy, security e evals.", "risk", ORANGE),
                ("04", "Adoção + suporte", "Paved road, discovery, enablement e feedback.", "automation", GREEN),
                ("05", "Runtime + melhoria", "Sinais, contenção, attestation e valor.", "controls", PURPLE),
            ],
            "roles": [
                ("Business owners + sponsor", "finalidade • value • accountability", BLUE),
                ("Data / identity / platform", "contratos • acesso • enforcement", PURPLE),
                ("Security / Privacy / RAI", "impacto • risco • assurance", ORANGE),
                ("Builders / support / run", "release • operação • contenção", GREEN),
            ],
            "roles_footer": "decision rights  •  handoffs explícitos  •  humans accountable",
            "registry_title": "REGISTRY + BLUEPRINT",
            "registry_line1": "Visibilidade + arquitetura",
            "registry_line2": "para decidir e operar.",
            "chips": ["owner", "data", "tools", "risk", "evidence", "sunset"],
            "registry_note": "Blueprint = models • identity • permissions • boundaries • runtime",
            "gates_label": "Decision gates antes e depois do release",
            "gates_title": "TIERING + ASSURANCE",
            "signals": [
                ("risco / alcance", RED),
                ("dados / identidade", BLUE),
                ("evals / evidências", GREEN),
                ("autoridade humana", ORANGE),
            ],
            "release_actions": "aprovar • condicionar • bloquear • publicar",
            "gate_footer": "policy no design  +  controls na execução",
            "runtime_title": "BUILD TIME + RUNTIME",
            "build_items": "blueprint • data • identity • tests",
            "runtime_items": "signals • policy • quarantine • recovery",
            "runtime_note": "Contexto comum; ownership e remediação permanecem no domínio certo.",
            "lifecycle_label": "Lifecycle: confiança construída continuamente",
            "steps": [("1", "estratégia"), ("2", "registrar"), ("3", "avaliar"), ("4", "publicar"), ("5", "operar"), ("6", "attestar")],
            "lifecycle_note": "proporcional  •  federado  •  human-led  •  verificável",
            "footer_left": "Referências: NIST • ISO • OECD • EU AI Act • OWASP • MITRE",
            "footer_right": "policy • patterns • controls • evidence",
        }

    if variant == "microsoft":
        return {
            "output": MICROSOFT_OUT,
            "pill": "CASO DE ESTUDO  •  MICROSOFT CUSTOMER ZERO  •  2025–2026",
            "title": "Agent 365",
            "subtitle": "Governança de agentes em escala",
            "subtitle_size": 54,
            "tagline": "Control plane + Responsible AI + adoção  →  confiança  →  valor em escala",
            "tagline_size": 26,
            "note": "Escala reportada: >100 mil (2025) → >500 mil (2026) — escopos não diretamente comparáveis",
            "metrics": [
                (">500 mil", "agentes com visibilidade (2026)", BLUE),
                (">80", "projetos de IA em andamento (Microsoft Digital)", TEAL),
            ],
            "thesis_left": "Governar não é centralizar;",
            "thesis_right": "é conectar controle, avaliação e ação.",
            "thesis_note": "AI-operated • human-led  +  autonomia proporcional ao risco",
            "section1": "Cinco capacidades observadas",
            "pillars": [
                ("01", "Registry + blueprint", "Visibilidade, identidade, ownership e lifecycle.", "registry", BLUE),
                ("02", "AI-ready data + identidade", "Data mesh, labels, DLP e conectores.", "controls", TEAL),
                ("03", "Risco + Responsible AI", "Matriz proporcional, impacto e release.", "risk", ORANGE),
                ("04", "Adoção + suporte", "Coortes, champions, enablement e self-service.", "automation", GREEN),
                ("05", "Telemetria + valor", "Uso, impacto, remediação e attestation.", "lifecycle", PURPLE),
            ],
            "roles": [
                ("AI admins", "inventário • uso • lifecycle", BLUE),
                ("Data / identity / platform", "AI-ready • acesso • metadata", PURPLE),
                ("Security / Privacy / RAI", "risco • dados • release", ORANGE),
                ("Adoption / support", "coortes • champions • enablement", GREEN),
            ],
            "roles_footer": "mesma visão  •  handoffs explícitos  •  humano no controle",
            "registry_title": "REGISTRY + BLUEPRINT",
            "registry_line1": "Visibilidade + especificação",
            "registry_line2": "para decidir e publicar.",
            "chips": ["owner", "data", "scope", "policy", "value", "attest"],
            "registry_note": "Blueprint = identity • capabilities • constraints • data • lifecycle",
            "gates_label": "Gates antes e depois do release",
            "gates_title": "RISK MATRIX + ASSESSMENT",
            "signals": [
                ("risco / alcance", RED),
                ("AI-ready data", BLUE),
                ("mitigadores", GREEN),
                ("revisão humana", ORANGE),
            ],
            "release_actions": "aprovar • iterar • bloquear • publicar",
            "gate_footer": "processo no design  +  ferramenta para executar",
            "runtime_title": "DADOS + MCP + RUNTIME",
            "build_items": "labels • gateway • isolamento • blueprint",
            "runtime_items": "telemetria • acesso • quarentena • remediação",
            "runtime_note": "Centralizar contexto; remediar no domínio certo — identidade, dados, segurança e plataforma.",
            "lifecycle_label": "Lifecycle: confiança construída continuamente",
            "steps": [("1", "estratégia"), ("2", "avaliar"), ("3", "publicar"), ("4", "adotar"), ("5", "medir"), ("6", "attestar")],
            "lifecycle_note": "proporcional  •  embutido  •  human-led  •  iterativo",
            "footer_left": "Fontes: 5 artigos Microsoft Inside Track • 2025–2026",
            "footer_right": "relato institucional • não é auditoria independente",
        }

    raise ValueError(f"Unknown variant: {variant}")


def make_image(variant: str, output_dir: Path | None = None) -> Path:
    content = content_for(variant)
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)

    for x in range(0, W, 60):
        draw.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H, 60):
        draw.line((0, y, W, y), fill=GRID, width=1)
    for x, y, radius, color in [
        (1600, 160, 300, BLUE),
        (1450, 1050, 250, TEAL),
        (200, 2050, 260, PURPLE),
    ]:
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        rgb = tuple(int(color[index : index + 2], 16) for index in (1, 3, 5))
        glow_draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill=rgb + (30,),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(90))
        image = Image.alpha_composite(image.convert("RGBA"), glow).convert("RGB")
        draw = ImageDraw.Draw(image)

    x0 = 80
    pill(draw, (x0, 72), content["pill"], BLUE, BG, selected_font=font(19, True))
    draw.text((x0, 150), content["title"], font=font(82, True), fill=BLUE)
    draw.text(
        (x0, 250),
        content["subtitle"],
        font=font(content["subtitle_size"], True),
        fill=WHITE,
    )
    tagline_end = draw_wrapped(
        draw,
        (x0, 330),
        content["tagline"],
        font(content["tagline_size"]),
        MUTED,
        1050,
        spacing=5,
        max_lines=2,
    )
    draw.text((x0, tagline_end + 4), content["note"], font=font(18), fill=MUTED)

    metric_boxes = [(1190, 116, 1715, 270), (1190, 292, 1715, 440)]
    for (big, label, accent), box in zip(content["metrics"], metric_boxes):
        card(draw, box, fill=SURFACE_2, outline=accent, radius=22, width=2)
        draw.text((box[0] + 35, box[1] + 24), big, font=font(58, True), fill=WHITE)
        draw_wrapped(draw, (box[0] + 35, box[1] + 98), label, font(20), MUTED, 455, spacing=3, max_lines=2)

    card(draw, (80, 470, 1720, 650), fill=SURFACE, outline=TEAL, radius=25, width=3)
    draw.rectangle((80, 470, 96, 650), fill=TEAL)
    draw.text((130, 495), "A TESE", font=font(20, True), fill=TEAL)
    draw_wrapped(
        draw,
        (130, 535),
        f"{content['thesis_left']} {content['thesis_right']}",
        font(35, True),
        WHITE,
        1510,
        spacing=5,
        max_lines=2,
    )
    draw.text((130, 598), content["thesis_note"], font=font(22), fill=MUTED)

    section_label(draw, 80, 700, "01", content["section1"], BLUE)
    card_width, card_height = 540, 200
    positions = [(80, 750), (630, 750), (1180, 750), (355, 970), (905, 970)]
    for (number, title, description, icon, accent), (cx, cy) in zip(content["pillars"], positions):
        card(
            draw,
            (cx, cy, cx + card_width, cy + card_height),
            fill=SURFACE,
            outline=accent,
            radius=22,
            width=2,
        )
        draw.text((cx + 25, cy + 20), number, font=font(20, True), fill=accent)
        line_icon(draw, cx + card_width - 84, cy + 20, icon, accent)
        draw.text((cx + 25, cy + 62), title, font=font(29, True), fill=WHITE)
        draw_wrapped(
            draw,
            (cx + 25, cy + 110),
            description,
            font(22),
            MUTED,
            card_width - 50,
            spacing=4,
            max_lines=2,
        )

    section_label(draw, 80, 1220, "02", "Operating model: papéis e accountability", TEAL)
    card(draw, (80, 1270, 935, 1650), fill=SURFACE, outline=TEAL, radius=24, width=2)
    draw.text((115, 1305), "PAPÉIS E HANDOFFS", font=font(19, True), fill=TEAL)
    role_y = 1355
    for role, description, accent in content["roles"]:
        draw.ellipse((120, role_y + 7, 136, role_y + 23), fill=accent)
        draw.text((155, role_y), role, font=font(24, True), fill=WHITE)
        draw.text((155, role_y + 34), description, font=font(20), fill=MUTED)
        role_y += 64
    draw.text((115, 1620), content["roles_footer"], font=font(19, True), fill=TEAL)

    card(draw, (965, 1270, 1720, 1650), fill=SURFACE, outline=BLUE, radius=24, width=2)
    draw.text((1000, 1305), content["registry_title"], font=font(19, True), fill=BLUE)
    draw.text((1000, 1350), content["registry_line1"], font=font(31, True), fill=WHITE)
    draw.text((1000, 1390), content["registry_line2"], font=font(31, True), fill=WHITE)
    chip_x, chip_y = 1000, 1460
    for label in content["chips"]:
        chip_font = font(19, True)
        chip_width = text_width(draw, label, chip_font) + 28
        if chip_x + chip_width > 1650:
            chip_x = 1000
            chip_y += 52
        draw.rounded_rectangle((chip_x, chip_y, chip_x + chip_width, chip_y + 36), radius=18, fill=BLUE)
        draw.text((chip_x + 14, chip_y + 6), label, font=chip_font, fill=BG)
        chip_x += chip_width + 10
    draw_wrapped(draw, (1000, 1565), content["registry_note"], font(20), MUTED, 670, spacing=4, max_lines=2)

    section_label(draw, 80, 1695, "03", content["gates_label"], ORANGE)
    card(draw, (80, 1745, 935, 2040), fill=SURFACE, outline=ORANGE, radius=24, width=2)
    draw.text((115, 1780), content["gates_title"], font=font(19, True), fill=ORANGE)
    signal_y = 1830
    for label, accent in content["signals"]:
        draw.ellipse((120, signal_y + 7, 136, signal_y + 23), fill=accent)
        draw.text((155, signal_y), label, font=font(24, True), fill=WHITE)
        signal_y += 44
    arrow(draw, (520, 1880), (770, 1880), ORANGE, 5)
    draw.text((610, 1810), "release", font=font(20, True), fill=ORANGE)
    draw_wrapped(draw, (560, 1920), content["release_actions"], font(22), MUTED, 325, spacing=4, max_lines=2)
    draw.text((115, 1995), content["gate_footer"], font=font(20, True), fill=ORANGE)

    card(draw, (965, 1745, 1720, 2040), fill=SURFACE, outline=RED, radius=24, width=2)
    draw.text((1000, 1780), content["runtime_title"], font=font(19, True), fill=RED)
    draw.rounded_rectangle((1000, 1830, 1330, 1940), radius=18, fill="#1B3048", outline=ORANGE, width=2)
    draw.text((1025, 1847), "DESIGN / BUILD", font=font(18, True), fill=ORANGE)
    draw_wrapped(draw, (1025, 1880), content["build_items"], font(18), MUTED, 280, spacing=3, max_lines=2)
    draw.rounded_rectangle((1355, 1830, 1685, 1940), radius=18, fill="#1B3048", outline=RED, width=2)
    draw.text((1380, 1847), "RUNTIME", font=font(18, True), fill=RED)
    draw_wrapped(draw, (1380, 1880), content["runtime_items"], font(18), MUTED, 280, spacing=3, max_lines=2)
    draw_wrapped(draw, (1000, 1970), content["runtime_note"], font(20), WHITE, 680, spacing=4, max_lines=2)

    section_label(draw, 80, 2090, "04", content["lifecycle_label"], PURPLE)
    card(draw, (80, 2140, 1720, 2310), fill=SURFACE_2, outline=PURPLE, radius=24, width=2)
    step_x = 125
    for index, (number, label) in enumerate(content["steps"]):
        draw.ellipse((step_x, 2180, step_x + 55, 2235), fill=PURPLE)
        draw.text((step_x + 19, 2190), number, font=font(22, True), fill=BG)
        draw.text((step_x - 10, 2248), label, font=font(19, True), fill=WHITE)
        if index < len(content["steps"]) - 1:
            arrow(draw, (step_x + 70, 2208), (step_x + 170, 2208), PURPLE, 4)
        step_x += 270
    draw.text((125, 2282), content["lifecycle_note"], font=font(20, True), fill=MUTED)

    draw.line((80, 2330, 1720, 2330), fill=GRID, width=2)
    draw.text((80, 2350), content["footer_left"], font=font(18), fill=MUTED)
    draw.text((1050, 2350), content["footer_right"], font=font(18), fill=MUTED)

    default_output = Path(content["output"])
    output = output_dir / default_output.name if output_dir else default_output
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG", optimize=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Render framework and case-study infographics.")
    parser.add_argument(
        "--variant",
        choices=["all", "framework", "microsoft"],
        default="all",
        help="Infographic variant to render (default: all).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Optional directory for generated files; tracked outputs remain untouched.",
    )
    args = parser.parse_args()
    variants = ["framework", "microsoft"] if args.variant == "all" else [args.variant]
    for variant in variants:
        print(make_image(variant, args.output_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
