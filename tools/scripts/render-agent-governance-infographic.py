from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path
import math
import os

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT = REPO_ROOT / 'docs' / 'architecture' / 'diagrams'
W, H = 1800, 2400
BG = '#081421'
SURFACE = '#10243A'
SURFACE_2 = '#132B44'
WHITE = '#F3F7FC'
MUTED = '#A9B8C9'
BLUE = '#59A6FF'
TEAL = '#38D6C8'
ORANGE = '#FFA44D'
RED = '#FF6B6B'
GREEN = '#7EE0A5'
PURPLE = '#B8A4FF'
GRID = '#183049'

def resolve_font(env_var, candidates):
    override = os.environ.get(env_var)
    if override:
        path = Path(override).expanduser()
        if not path.is_file():
            raise FileNotFoundError(f'{env_var} points to a missing font: {path}')
        return str(path)

    for candidate in candidates:
        path = Path(candidate)
        if path.is_file():
            return str(path)

    raise FileNotFoundError(
        f'No compatible font found. Set {env_var} to a TrueType font file.'
    )


REG = resolve_font('AGF_FONT_REGULAR', [
    '/System/Library/Fonts/Supplemental/Arial.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf',
    'C:/Windows/Fonts/arial.ttf',
])
BOLD = resolve_font('AGF_FONT_BOLD', [
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf',
    'C:/Windows/Fonts/arialbd.ttf',
])


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REG, size)

def text_width(draw, text, f):
    box = draw.textbbox((0, 0), text, font=f)
    return box[2] - box[0]

def wrapped_lines(draw, text, f, max_width):
    words = text.split()
    lines, line = [], ''
    for word in words:
        candidate = word if not line else line + ' ' + word
        if text_width(draw, candidate, f) <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

def draw_wrapped(draw, xy, text, f, fill, max_width, spacing=8, max_lines=None):
    x, y = xy
    lines = wrapped_lines(draw, text, f, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while text_width(draw, last + '…', f) > max_width and last:
            last = last[:-1]
        lines[-1] = last.rstrip() + '…'
    line_h = f.size + spacing
    for line in lines:
        draw.text((x, y), line, font=f, fill=fill)
        y += line_h
    return y

def pill(draw, xy, text, fill, text_fill=BG, pad_x=16, pad_y=8, f=None):
    f = f or font(20, True)
    x, y = xy
    tw = text_width(draw, text, f)
    h = f.size + pad_y * 2
    draw.rounded_rectangle((x, y, x + tw + pad_x * 2, y + h), radius=h//2, fill=fill)
    draw.text((x + pad_x, y + pad_y - 1), text, font=f, fill=text_fill)
    return x + tw + pad_x * 2

def card(draw, box, fill=SURFACE, outline=None, radius=24, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width if outline else 1)

def section_label(draw, x, y, number, title, accent):
    draw.text((x, y), number, font=font(20, True), fill=accent)
    draw.text((x + 46, y - 2), title.upper(), font=font(20, True), fill=MUTED)

def line_icon(draw, x, y, kind, color):
    # Minimal geometric icons, designed to remain readable at Telegram scale.
    if kind == 'registry':
        draw.rounded_rectangle((x+8, y+4, x+52, y+62), radius=6, outline=color, width=4)
        draw.line((x+18, y+18, x+42, y+18), fill=color, width=4)
        draw.line((x+18, y+31, x+42, y+31), fill=color, width=4)
        draw.line((x+18, y+44, x+35, y+44), fill=color, width=4)
    elif kind == 'controls':
        draw.line((x+8, y+18, x+52, y+18), fill=color, width=4)
        draw.line((x+8, y+34, x+52, y+34), fill=color, width=4)
        draw.line((x+8, y+50, x+52, y+50), fill=color, width=4)
        for cx, cy in [(25,18), (43,34), (20,50)]:
            draw.ellipse((x+cx-6, y+cy-6, x+cx+6, y+cy+6), fill=BG, outline=color, width=3)
    elif kind == 'lifecycle':
        draw.arc((x+3, y+7, x+58, y+62), 35, 205, fill=color, width=4)
        draw.polygon([(x+8,y+22),(x+2,y+10),(x+20,y+14)], fill=color)
        draw.arc((x+3, y+7, x+58, y+62), 215, 385, fill=color, width=4)
        draw.polygon([(x+51,y+46),(x+59,y+58),(x+39,y+54)], fill=color)
    elif kind == 'risk':
        draw.polygon([(x+31,y+3),(x+60,y+60),(x+2,y+60)], outline=color, fill=None)
        draw.line((x+31,y+21,x+31,y+42), fill=color, width=5)
        draw.ellipse((x+28,y+49,x+34,y+55), fill=color)
    elif kind == 'automation':
        draw.rectangle((x+8,y+10,x+48,y+51), outline=color, width=4)
        draw.line((x+28,y+51,x+28,y+64), fill=color, width=4)
        draw.line((x+18,y+64,x+38,y+64), fill=color, width=4)
        draw.line((x+48,y+29,x+61,y+29), fill=color, width=4)
        draw.polygon([(x+57,y+21),(x+67,y+29),(x+57,y+37)], fill=color)


def arrow(draw, start, end, color, width=5):
    draw.line((start[0], start[1], end[0], end[1]), fill=color, width=width)
    angle = math.atan2(end[1]-start[1], end[0]-start[0])
    length = 18
    a1 = angle + math.pi - 0.55
    a2 = angle + math.pi + 0.55
    p1 = (end[0] + length*math.cos(a1), end[1] + length*math.sin(a1))
    p2 = (end[0] + length*math.cos(a2), end[1] + length*math.sin(a2))
    draw.polygon([end, p1, p2], fill=color)

def make_image():
    img = Image.new('RGB', (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Blueprint grid
    for x in range(0, W, 60):
        draw.line((x, 0, x, H), fill=GRID, width=1)
    for y in range(0, H, 60):
        draw.line((0, y, W, y), fill=GRID, width=1)
    for x, y, r, c in [(1600, 160, 300, BLUE), (1450, 1050, 250, TEAL), (200, 2050, 260, PURPLE)]:
        glow = Image.new('RGBA', (W, H), (0,0,0,0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse((x-r, y-r, x+r, y+r), fill=tuple(int(c[i:i+2],16) for i in (1,3,5))+(30,))
        glow = glow.filter(ImageFilter.GaussianBlur(90))
        img = Image.alpha_composite(img.convert('RGBA'), glow).convert('RGB')
        draw = ImageDraw.Draw(img)

    # Header
    x0 = 80
    pill(draw, (x0, 72), 'SÍNTESE DE 5 ARTIGOS  •  MICROSOFT DIGITAL  •  2025–2026', BLUE, BG, f=font(19, True))
    draw.text((x0, 150), 'Agent 365', font=font(88, True), fill=BLUE)
    draw.text((x0, 250), 'Governança de agentes em escala', font=font(58, True), fill=WHITE)
    draw_wrapped(draw, (x0, 330), 'Control plane + Responsible AI + adoção  →  confiança  →  valor em escala', font(29), MUTED, 980, spacing=7)
    draw.text((x0, 385), 'Escala reportada: >100 mil (2025) → >500 mil (2026) — escopos não diretamente comparáveis', font=font(18), fill=MUTED)

    # Metrics
    card(draw, (1190, 116, 1715, 270), fill=SURFACE_2, outline=BLUE, radius=22, width=2)
    draw.text((1225, 140), '>500 mil', font=font(60, True), fill=WHITE)
    draw.text((1225, 214), 'agentes com visibilidade (2026)', font=font(21), fill=MUTED)
    card(draw, (1190, 292, 1715, 418), fill=SURFACE_2, outline=TEAL, radius=22, width=2)
    draw.text((1225, 310), '>80', font=font(60, True), fill=WHITE)
    draw.text((1225, 384), 'projetos de IA em andamento (Microsoft Digital)', font=font(21), fill=MUTED)

    # Thesis
    card(draw, (80, 470, 1720, 650), fill=SURFACE, outline=TEAL, radius=25, width=3)
    draw.rectangle((80, 470, 96, 650), fill=TEAL)
    draw.text((130, 495), 'A TESE', font=font(20, True), fill=TEAL)
    draw.text((130, 535), 'Governar não é centralizar;', font=font(37, True), fill=WHITE)
    draw.text((650, 535), 'é conectar controle, avaliação e ação.', font=font(37, True), fill=WHITE)
    draw.text((130, 598), 'AI-operated • human-led  +  autonomia proporcional ao risco', font=font(22), fill=MUTED)

    # Five pillars
    section_label(draw, 80, 700, '01', 'Cinco capacidades para escalar agentes', BLUE)
    pillar_data = [
        ('01', 'Registry + blueprint', 'Visibilidade, identidade, ownership e lifecycle.', 'registry', BLUE),
        ('02', 'AI-ready data + identidade', 'Data mesh, labels, DLP e conectores.', 'controls', TEAL),
        ('03', 'Risco + Responsible AI', 'Matriz proporcional, impacto e release.', 'risk', ORANGE),
        ('04', 'Adoção + suporte', 'Coortes, champions, enablement e self-service.', 'automation', GREEN),
        ('05', 'Telemetria + valor', 'Uso, impacto, remediação e attestation.', 'lifecycle', PURPLE),
    ]
    card_w, card_h = 540, 200
    positions = [(80, 750), (630, 750), (1180, 750), (355, 970), (905, 970)]
    for (num, title, desc, icon, accent), (cx, cy) in zip(pillar_data, positions):
        card(draw, (cx, cy, cx+card_w, cy+card_h), fill=SURFACE, outline=accent, radius=22, width=2)
        draw.text((cx+25, cy+20), num, font=font(20, True), fill=accent)
        line_icon(draw, cx+card_w-84, cy+20, icon, accent)
        draw.text((cx+25, cy+62), title, font=font(29, True), fill=WHITE)
        draw_wrapped(draw, (cx+25, cy+110), desc, font(22), MUTED, card_w-50, spacing=4, max_lines=2)

    # Roles card
    section_label(draw, 80, 1220, '02', 'Operating model: papéis e accountability', TEAL)
    card(draw, (80, 1270, 935, 1650), fill=SURFACE, outline=TEAL, radius=24, width=2)
    draw.text((115, 1305), 'PAPÉIS E HANDOFFS', font=font(19, True), fill=TEAL)
    roles = [
        ('AI admins', 'inventário • uso • lifecycle', BLUE),
        ('Data / identity / platform', 'AI-ready • acesso • metadata', PURPLE),
        ('Security / Privacy / RAI', 'risco • dados • release', ORANGE),
        ('Adoption / support', 'coortes • champions • enablement', GREEN),
    ]
    ry = 1355
    for role, desc, accent in roles:
        draw.ellipse((120, ry+7, 136, ry+23), fill=accent)
        draw.text((155, ry), role, font=font(25, True), fill=WHITE)
        draw.text((155, ry+35), desc, font=font(21), fill=MUTED)
        ry += 66
    draw.text((115, 1610), 'mesma visão  •  handoffs explícitos  •  humano no controle', font=font(20, True), fill=TEAL)

    # Registry card
    card(draw, (965, 1270, 1720, 1650), fill=SURFACE, outline=BLUE, radius=24, width=2)
    draw.text((1000, 1305), 'REGISTRY + BLUEPRINT', font=font(19, True), fill=BLUE)
    draw.text((1000, 1350), 'Visibilidade + especificação', font=font(31, True), fill=WHITE)
    draw.text((1000, 1390), 'para decidir e publicar.', font=font(31, True), fill=WHITE)
    chips = ['owner', 'data', 'scope', 'policy', 'value', 'attest']
    cx, cy = 1000, 1460
    for label in chips:
        f = font(19, True)
        tw = text_width(draw, label, f) + 28
        if cx + tw > 1650:
            cx = 1000
            cy += 52
        draw.rounded_rectangle((cx, cy, cx+tw, cy+36), radius=18, fill=BLUE)
        draw.text((cx+14, cy+6), label, font=f, fill=BG)
        cx += tw + 10
    draw_wrapped(draw, (1000, 1565), 'Blueprint = identity • capabilities • constraints • data • lifecycle', font(20), MUTED, 670, spacing=4, max_lines=2)

    # Observability card
    section_label(draw, 80, 1695, '03', 'Gates antes e depois do release', ORANGE)
    card(draw, (80, 1745, 935, 2040), fill=SURFACE, outline=ORANGE, radius=24, width=2)
    draw.text((115, 1780), 'RISK MATRIX + ASSESSMENT', font=font(19, True), fill=ORANGE)
    signals = [('risco / alcance', RED), ('AI-ready data', BLUE), ('mitigadores', GREEN), ('revisão humana', ORANGE)]
    sy = 1830
    for label, accent in signals:
        draw.ellipse((120, sy+7, 136, sy+23), fill=accent)
        draw.text((155, sy), label, font=font(24, True), fill=WHITE)
        sy += 44
    arrow(draw, (520, 1880), (770, 1880), ORANGE, 5)
    draw.text((610, 1810), 'release', font=font(20, True), fill=ORANGE)
    draw_wrapped(draw, (560, 1920), 'aprovar • iterar • bloquear • publicar', font(22), MUTED, 325, spacing=4, max_lines=2)
    draw.text((115, 1995), 'processo no design  +  ferramenta para executar', font=font(20, True), fill=ORANGE)

    # Security card
    card(draw, (965, 1745, 1720, 2040), fill=SURFACE, outline=RED, radius=24, width=2)
    draw.text((1000, 1780), 'DADOS + MCP + RUNTIME', font=font(19, True), fill=RED)
    # Build lane
    draw.rounded_rectangle((1000, 1830, 1330, 1940), radius=18, fill='#1B3048', outline=ORANGE, width=2)
    draw.text((1025, 1847), 'DESIGN / BUILD', font=font(18, True), fill=ORANGE)
    draw_wrapped(draw, (1025, 1880), 'labels • gateway • isolamento • blueprint', font(18), MUTED, 280, spacing=3, max_lines=2)
    # Runtime lane
    draw.rounded_rectangle((1355, 1830, 1685, 1940), radius=18, fill='#1B3048', outline=RED, width=2)
    draw.text((1380, 1847), 'RUNTIME', font=font(18, True), fill=RED)
    draw_wrapped(draw, (1380, 1880), 'telemetria • acesso • quarentena • remediação', font(18), MUTED, 280, spacing=3, max_lines=2)
    draw_wrapped(draw, (1000, 1970), 'Centralizar contexto; remediar no domínio certo — Entra, Purview, Defender e plataforma.', font(20), WHITE, 680, spacing=4, max_lines=2)

    # Loop
    section_label(draw, 80, 2090, '04', 'Lifecycle: confiança construída continuamente', PURPLE)
    card(draw, (80, 2140, 1720, 2310), fill=SURFACE_2, outline=PURPLE, radius=24, width=2)
    steps = [('1', 'estratégia'), ('2', 'avaliar'), ('3', 'publicar'), ('4', 'adotar'), ('5', 'medir'), ('6', 'attestar')]
    sx = 125
    for i, (num, label) in enumerate(steps):
        draw.ellipse((sx, 2180, sx+55, 2235), fill=PURPLE)
        draw.text((sx+19, 2190), num, font=font(22, True), fill=BG)
        draw.text((sx-10, 2248), label, font=font(19, True), fill=WHITE)
        if i < len(steps)-1:
            arrow(draw, (sx+70, 2208), (sx+170, 2208), PURPLE, 4)
        sx += 270
    draw.text((125, 2282), 'proporcional  •  embutido  •  human-led  •  iterativo', font=font(20, True), fill=MUTED)

    # Footer
    draw.line((80, 2330, 1720, 2330), fill=GRID, width=2)
    draw.text((80, 2350), 'Fontes: 5 artigos Microsoft Inside Track • 2025–2026', font=font(18), fill=MUTED)
    draw.text((1040, 2350), 'governança • adoção • dados • valor', font=font(18), fill=MUTED)

    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / 'agent-governance-operating-model.png'
    img.save(out, format='PNG', optimize=True)
    return out

if __name__ == '__main__':
    print(make_image())
