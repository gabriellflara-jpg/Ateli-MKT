---
name: criar-site
description: >
  Cria sites e landing pages completas em HTML/CSS/JS, prontos pra publicar (Netlify,
  Hostinger, Vercel), no padrão de identidade visual do cliente. Use SEMPRE que o usuário
  pedir "cria um site", "landing page", "página de vendas em HTML", "site pro cliente",
  "preciso de uma página pra receber tráfego pago", ou qualquer entrega que precise virar
  um site publicável, não só texto.
---

> 🧠 **Memória:** se for site de um CLIENTE, leia `clientes/[nome-do-cliente]/_memoria/*.md` e `identidade/design-guide.md` desse cliente. Se for site da PRÓPRIA agência, leia `_memoria/perfil-agencia.md` e `_memoria/identidade-visual-agencia.md`. Se não estiver claro, pergunte antes de criar — cores, fontes e copy dependem disso.

# Criar Site

Gera site real (arquivo HTML/CSS/JS), não protótipo — o cliente recebe algo que já pode
subir no ar.

## Passo 1 — Entender o objetivo
Pergunte (se não estiver claro): que tipo de página é essa — site institucional, landing
page de captura (leads), página de vendas de produto/serviço, ou link na bio.
Pergunte também: vai receber tráfego pago? Isso muda a estrutura (página de vendas de
tráfego pago precisa ser mais direta, sem menu de navegação que tira o visitante do funil).

## Passo 2 — Estrutura por tipo

**Landing page de captura (leads):**
Headline → subheadline → formulário/CTA acima da dobra → 3 benefícios → prova social →
CTA final. Sem menu, sem links de saída.

**Página de vendas:**
Headline com a promessa → agitação do problema → apresentação da solução → como funciona →
prova social/depoimentos → oferta e preço → garantia → FAQ → CTA final repetido.

**Site institucional:**
Header com menu → hero com proposta de valor → sobre → serviços → prova social → contato/CTA
→ footer.

## Passo 3 — Gerar o código
Use a skill `frontend-design` (se disponível no ambiente) pra decisões de tipografia, cores
e espaçamento — não usar template genérico. Aplique as cores e fontes do
`identidade/design-guide.md` do cliente. HTML + CSS (+ JS mínimo se precisar de formulário
ou menu mobile) em um único arquivo ou pasta simples, sem dependências pesadas.

Sempre responsivo (mobile-first) — mais da metade do tráfego de anúncio é mobile.

## Passo 4 — Entrega
Salve o arquivo pronto (ex: `index.html`) e informe que pra publicar é só:
- Arrastar a pasta pro Netlify Drop (netlify.com/drop), ou
- Subir via FTP/gerenciador de arquivos na Hostinger, ou
- Conectar o repositório no Vercel

Não tente publicar automaticamente — apenas entregue o arquivo pronto pra ela subir.

## Regra
Nunca invente depoimento, número ou prova social que o cliente não forneceu. Se faltar
conteúdo real (depoimentos, fotos, textos institucionais), deixe marcado como
`[INSERIR: depoimento do cliente X]` em vez de inventar.
