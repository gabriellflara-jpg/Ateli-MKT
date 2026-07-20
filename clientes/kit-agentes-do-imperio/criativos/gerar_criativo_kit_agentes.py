"""
Criativo de anuncio -- Kit Agentes do Imperio
Formato: feed 1080x1350 (Instagram/Meta Ads)

Como rodar:
    python gerar_criativo_kit_agentes.py

Requisitos:
    pip install Pillow

Fontes: por padrao usa DejaVuSans (empacotada em assets/fonts/, funciona em
qualquer sistema sem instalar nada). Para bater exatamente com a identidade
oficial (Poppins Bold/Regular), baixe as fontes gratuitas em fonts.google.com/specimen/Poppins,
salve como "Poppins-Bold.ttf" e "Poppins-Regular.ttf" dentro de assets/fonts/
e troque os dois caminhos FONT_BOLD / FONT_REG abaixo.
"""
from PIL import Image, ImageDraw, ImageFont
import math
import os

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_BOLD = os.path.join(_SCRIPT_DIR, "assets", "fonts", "DejaVuSans-Bold.ttf")
FONT_REG = os.path.join(_SCRIPT_DIR, "assets", "fonts", "DejaVuSans.ttf")

PRETO = '#0D0D0D'
PRETO_CARD = '#131211'
DOURADO = '#E99A3B'
DOURADO_BTN = '#C57C2E'
BRANCO = '#FEFEFE'
CINZA = '#898989'
CINZA_ESC = '#555550'
PAD = 52


def f(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()


def tw(draw, text, fo):
    bb = draw.textbbox((0, 0), text, font=fo)
    return bb[2] - bb[0]


def th(draw, text, fo):
    bb = draw.textbbox((0, 0), text, font=fo)
    return bb[3] - bb[1]


def cx(draw, text, y, fo, color, W=1080):
    x = (W - tw(draw, text, fo)) // 2
    draw.text((x, y), text, font=fo, fill=color)


def inline_text(draw, parts, y, W=1080):
    total_w = sum(tw(draw, t, fo) for t, c, fo in parts)
    sx = (W - total_w) // 2
    for text, color, fo in parts:
        draw.text((sx, y), text, font=fo, fill=color)
        sx += tw(draw, text, fo)


def draw_sunburst_icon(draw, x, y, size=38, color_fill=DOURADO, color_bg=PRETO):
    draw.ellipse([x, y, x + size, y + size], fill=color_fill)
    cx_i, cy_i = x + size // 2, y + size // 2
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        r1, r2 = int(size * 0.35), int(size * 0.58)
        draw.line([
            cx_i + int(r1 * math.cos(rad)), cy_i + int(r1 * math.sin(rad)),
            cx_i + int(r2 * math.cos(rad)), cy_i + int(r2 * math.sin(rad))
        ], fill=color_fill, width=3)
    inner = int(size * 0.22)
    draw.ellipse([cx_i - inner, cy_i - inner, cx_i + inner, cy_i + inner], fill=color_bg)


def draw_badge(draw, text, ix, iy, icon_size=38):
    draw_sunburst_icon(draw, ix, iy, icon_size)
    badge_font = f(FONT_BOLD, 20)
    btw = tw(draw, text, badge_font)
    bx = ix + icon_size + 12
    by = iy + 3
    draw.rounded_rectangle([bx, by, bx + btw + 28, by + 32],
                            radius=16, fill=PRETO, outline=DOURADO, width=1)
    draw.text((bx + 14, by + 7), text, font=badge_font, fill=DOURADO)


def draw_warm_glow(draw, W, H, cx_g=None, cy_g=None):
    if cx_g is None:
        cx_g = W // 2
    if cy_g is None:
        cy_g = int(H * 0.35)
    radius = int(W * 0.65)
    for r in range(radius, 0, -2):
        ratio = (1 - r / radius) ** 1.8
        try:
            draw.ellipse(
                [cx_g - r, cy_g - int(r * 0.55), cx_g + r, cy_g + int(r * 0.55)],
                fill=(int(10 + ratio * 52), int(8 + ratio * 28), int(5 + ratio * 8))
            )
        except Exception:
            pass


def draw_product_card(draw, x, y, w, h, icon_x, icon_y, name, subtitle, icon_size=32):
    draw.rounded_rectangle([x, y, x + w, y + h],
                            radius=16, fill=PRETO_CARD, outline='#252320', width=1)
    draw_sunburst_icon(draw, icon_x, icon_y, icon_size)
    draw.text((icon_x + icon_size + 14, y + 14), name, font=f(FONT_BOLD, 28), fill=BRANCO)
    draw.text((icon_x + icon_size + 14, y + 50), subtitle, font=f(FONT_REG, 19), fill=CINZA)


def draw_price(draw, x, y_old, y_new, old_price, new_price):
    old_f = f(FONT_REG, 42)
    pre_f = f(FONT_REG, 42)
    real_f = f(FONT_BOLD, 106)
    pre_t = "Por apenas "

    draw.text((x, y_old), old_price, font=old_f, fill=CINZA_ESC)
    line_y = y_old + th(draw, old_price, old_f) // 2 + 4
    draw.line([x, line_y, x + tw(draw, old_price, old_f), line_y], fill=CINZA_ESC, width=2)

    draw.text((x, y_new), pre_t, font=pre_f, fill=BRANCO)
    draw.text((x + tw(draw, pre_t, pre_f), y_new - 30), new_price, font=real_f, fill=DOURADO)


def draw_cta_button(draw, x1, y, x2, h, text):
    draw.rounded_rectangle([x1, y, x2, y + h], radius=14, fill=DOURADO_BTN)
    btn_f = f(FONT_BOLD, 34)
    cx(draw, text, y + 24, btn_f, PRETO)


def draw_footer(draw, y, items, W=1080):
    ft_bold = f(FONT_BOLD, 25)
    ft_reg = f(FONT_REG, 25)
    sep = " . "

    parts = []
    for i, (text, color) in enumerate(items):
        parts.append((text, color, ft_bold if i == 0 else ft_reg))
        if i < len(items) - 1:
            parts.append((sep, '#252320', ft_reg))

    total = sum(tw(draw, t, fo) for t, c, fo in parts)
    sx = (W - total) // 2
    for t, c, fo in parts:
        draw.text((sx, y), t, font=fo, fill=c)
        sx += tw(draw, t, fo)


def gerar_criativo(
    badge_text,
    headline_1_branco, headline_1_dourado,
    headline_2_dourado, headline_2_branco,
    sub_partes,
    impacto_numero,
    impacto_label,
    impacto_sub1,
    impacto_sub2,
    card_nome,
    card_sub,
    preco_de,
    preco_por,
    cta_texto,
    footer_items,
    output_path,
    W=1080, H=1350
):
    img = Image.new('RGB', (W, H), PRETO)
    draw = ImageDraw.Draw(img)

    draw_warm_glow(draw, W, H)
    draw_badge(draw, badge_text, PAD, 44)

    h1 = f(FONT_BOLD, 90)
    h2 = f(FONT_BOLD, 88)
    y_h = 115
    p1a, p1b = headline_1_branco, headline_1_dourado
    w1a, w1b = tw(draw, p1a, h1), tw(draw, p1b, h1)
    x1s = (W - w1a - w1b) // 2
    draw.text((x1s, y_h), p1a, font=h1, fill=BRANCO)
    draw.text((x1s + w1a, y_h), p1b, font=h1, fill=DOURADO)

    y_h2 = y_h + 104
    p2a, p2b = headline_2_dourado, headline_2_branco
    w2a, w2b = tw(draw, p2a, h2), tw(draw, p2b, h2)
    x2s = (W - w2a - w2b) // 2
    draw.text((x2s, y_h2), p2a, font=h2, fill=DOURADO)
    draw.text((x2s + w2a, y_h2), p2b, font=h2, fill=BRANCO)

    y_s = y_h2 + 110
    sub_parts_render = []
    for text, cor in sub_partes:
        is_key = cor == DOURADO
        sub_parts_render.append((text, cor, f(FONT_BOLD if is_key else FONT_REG, 32)))
    inline_text(draw, sub_parts_render, y_s)

    y_imp = y_s + 100
    big_f = f(FONT_BOLD, 142)
    lab_f = f(FONT_BOLD, 36)
    sub_f = f(FONT_REG, 28)
    big_w = tw(draw, impacto_numero, big_f)
    draw.text((PAD, y_imp - 10), impacto_numero, font=big_f, fill=DOURADO)
    side_x = PAD + big_w + 22
    draw.text((side_x, y_imp + 28), impacto_label, font=lab_f, fill=BRANCO)
    draw.text((side_x, y_imp + 72), impacto_sub1, font=sub_f, fill=CINZA)
    draw.text((side_x, y_imp + 106), impacto_sub2, font=sub_f, fill=CINZA)

    y_card = y_imp + 172
    draw_product_card(draw, PAD, y_card, 520, 86, PAD + 18, y_card + 18, card_nome, card_sub)

    y_pr = y_card + 86 + 55
    draw_price(draw, PAD, y_pr, y_pr + 54, preco_de, preco_por)

    y_btn = y_pr + 54 + 116
    draw_cta_button(draw, PAD, y_btn, W - PAD, 86, cta_texto)

    draw_footer(draw, y_btn + 86 + 36, footer_items)

    img.save(output_path)
    print(f"Criativo salvo: {output_path}")
    return output_path


if __name__ == "__main__":
    output = os.path.join(_SCRIPT_DIR, "criativo-kit-agentes-r67.png")
    gerar_criativo(
        badge_text="KIT AGENTES DO IMPÉRIO",
        headline_1_branco="Seu ",
        headline_1_dourado="consultor de IA.",
        headline_2_dourado="62 especialistas",
        headline_2_branco=" no Cowork.",
        sub_partes=[
            ("Vendas, ", CINZA),
            ("tráfego, ", DOURADO),
            ("copy, ", DOURADO),
            ("negócios ", DOURADO),
            ("e ", CINZA),
            ("estratégia", DOURADO),
            (" — no Claude que você já usa.", CINZA),
        ],
        impacto_numero="30 dias",
        impacto_label="de resultado",
        impacto_sub1="com 30 missões",
        impacto_sub2="guiadas",
        card_nome="Kit Agentes do Império",
        card_sub="62 agentes · 11 esquadrões · Claude Cowork",
        preco_de="De R$ 197",
        preco_por="R$ 67",
        cta_texto="Quero meu acesso por R$ 67  ›",
        footer_items=[
            ("🛡 Garantia de 7 dias", DOURADO),
            ("Acesso imediato", CINZA),
            ("62 especialistas únicos", CINZA),
        ],
        output_path=output,
    )
