#!/usr/bin/env python3
"""
Gera imagens PNG de carrossel (1080x1350, formato Instagram 4:5) a partir de uma lista de slides.

Uso:
    python3 gerar_carrossel.py --config config.json --out ./saida

O config.json deve ter o formato:
{
  "cor_fundo": "#0b0b0d",
  "cor_texto": "#f2f2f2",
  "cor_destaque": "#c9a227",
  "slides": [
    {"texto": "O gancho vai aqui", "tipo": "capa"},
    {"texto": "Primeiro argumento", "tipo": "conteudo"},
    {"texto": "Segue no perfil", "tipo": "cta"}
  ]
}

"tipo" controla o estilo: "capa" (texto grande, centralizado), "conteudo" (texto médio,
numerado), "cta" (texto grande + destaque de cor).
"""
import json
import argparse
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
# Fontes empacotadas dentro da própria skill — funciona em qualquer sistema
# (Windows, Mac, Linux), não depende de fontes instaladas no sistema.
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_BOLD = os.path.join(_SCRIPT_DIR, "..", "assets", "fonts", "DejaVuSans-Bold.ttf")
FONT_REGULAR = os.path.join(_SCRIPT_DIR, "..", "assets", "fonts", "DejaVuSans.ttf")


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_slide(slide, cor_fundo, cor_texto, cor_destaque, slide_num, total):
    img = Image.new("RGB", (W, H), hex_to_rgb(cor_fundo))
    draw = ImageDraw.Draw(img)
    texto = slide.get("texto", "")
    tipo = slide.get("tipo", "conteudo")

    margin = 90
    max_width = W - 2 * margin

    if tipo == "capa":
        font_size = 76
    elif tipo == "cta":
        font_size = 64
    else:
        font_size = 54

    font = ImageFont.truetype(FONT_BOLD, font_size)
    lines = wrap_text(draw, texto, font, max_width)

    line_height = font_size * 1.25
    total_height = line_height * len(lines)
    y = (H - total_height) / 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_w = bbox[2] - bbox[0]
        x = (W - line_w) / 2
        draw.text((x, y), line, font=font, fill=hex_to_rgb(cor_texto))
        y += line_height

    # Barra de destaque no topo
    draw.rectangle([0, 0, W, 10], fill=hex_to_rgb(cor_destaque))

    # Contador de slide (canto inferior direito), exceto capa
    if tipo != "capa":
        small_font = ImageFont.truetype(FONT_REGULAR, 28)
        contador = f"{slide_num}/{total}"
        bbox = draw.textbbox((0, 0), contador, font=small_font)
        cw = bbox[2] - bbox[0]
        draw.text((W - margin - cw, H - 70), contador, font=small_font, fill=hex_to_rgb(cor_destaque))

    return img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    with open(args.config, encoding="utf-8") as f:
        config = json.load(f)

    os.makedirs(args.out, exist_ok=True)
    slides = config["slides"]
    total = len(slides)

    for i, slide in enumerate(slides, start=1):
        img = draw_slide(
            slide,
            config.get("cor_fundo", "#0b0b0d"),
            config.get("cor_texto", "#f2f2f2"),
            config.get("cor_destaque", "#c9a227"),
            i,
            total,
        )
        path = os.path.join(args.out, f"slide_{i:02d}.png")
        img.save(path)
        print(f"Gerado: {path}")


if __name__ == "__main__":
    main()
