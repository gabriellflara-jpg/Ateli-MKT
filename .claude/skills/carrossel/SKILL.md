---
name: carrossel
description: >
  Cria carrosséis para Instagram/LinkedIn — texto de cada slide, legenda e especificação
  visual (cores, fontes, layout) no padrão de identidade do cliente aberto na sessão.
  Use SEMPRE que o usuário pedir "carrossel", "post em carrossel", "sequência de slides",
  "cria um carrossel sobre [tema]", ou pedir conteúdo em formato de múltiplos slides
  para redes sociais.
---

> 🧠 **Memória:** se for conteúdo de um CLIENTE, leia `clientes/[nome-do-cliente]/_memoria/*.md` e `identidade/design-guide.md` desse cliente. Se for conteúdo da PRÓPRIA agência (ex: Instagram da agência), leia `_memoria/identidade-visual-agencia.md`. Se não estiver claro se é cliente ou agência, pergunte antes de gerar — nunca assuma identidade visual.

# Carrossel

## Passo 1 — Confirmar cliente e tema
Se não houver cliente aberto na sessão, pergunte qual cliente é essa entrega antes de continuar.
Confirme o tema e o objetivo do carrossel (educar, vender, gerar prova social, etc).

## Passo 2 — Estruturar os slides
Formato padrão de 6 a 10 slides:
1. **Capa** — gancho forte, a promessa do carrossel em uma frase
2. **Slides 2 a N-1** — um argumento/passo por slide, frase curta + 1 ideia de apoio
3. **Penúltimo** — resumo ou virada
4. **Último** — CTA claro (comentar, salvar, seguir, clicar no link)

Cada slide deve ter no máximo ~25 palavras. Se passar disso, corte.

## Passo 0 — Checagem antes de rodar (primeira vez)

Antes de rodar o script pela primeira vez nesta máquina, confirme que o Python e a
biblioteca Pillow estão disponíveis:

```
python --version
```
(no Windows costuma ser `python`, não `python3` — se `python` não for reconhecido, tenta
`python3` ou `py`)

Se der erro de "Pillow não encontrado" ao rodar o script, instale com:
```
pip install Pillow
```

## Passo 3 — Gerar as imagens PNG de verdade

Esta skill gera o carrossel pronto em PNG (1080×1350, formato 4:5 do Instagram), não só o
texto. Use o script `scripts/gerar_carrossel.py`:

1. Pegue as cores de `identidade/design-guide.md` do cliente (cor primária, secundária, fundo).
   Se o cliente não tiver cores definidas, use o padrão dark/gold (`#0b0b0d` fundo,
   `#f2f2f2` texto, `#c9a227` destaque) e avise que está usando o padrão.
2. Monte um `config.json` com os slides, no formato:
   ```json
   {
     "cor_fundo": "#0b0b0d",
     "cor_texto": "#f2f2f2",
     "cor_destaque": "#c9a227",
     "slides": [
       {"texto": "Gancho da capa", "tipo": "capa"},
       {"texto": "Primeiro argumento", "tipo": "conteudo"},
       {"texto": "CTA final", "tipo": "cta"}
     ]
   }
   ```
3. Rode: `python3 scripts/gerar_carrossel.py --config config.json --out ./saida-[cliente]-[tema]`
   (no Windows, se `python3` não funcionar, tenta `python scripts/gerar_carrossel.py ...`)
4. Isso gera um PNG por slide, numerado (`slide_01.png`, `slide_02.png`...), prontos pra
   fazer upload direto no Instagram, sem precisar do Canva.

Se o cliente quiser um layout mais elaborado (com foto, ícones, camadas), avise que o script
atual cobre texto + cor sólida — layouts com imagem de fundo exigem evolução do script, e
pergunte se quer que você faça isso agora.

## Passo 4 — Legenda
Escreva a legenda do post separadamente, coerente com os slides, no tom de voz do cliente,
com CTA e até 3-5 hashtags relevantes ao nicho (nada de hashtag genérica tipo #marketing).

## Entrega
Organize a saída em blocos por slide (Slide 1, Slide 2...) seguidos da legenda, prontos
pra copiar.
