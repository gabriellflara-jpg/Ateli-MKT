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
**Antes de decidir cores/fontes/layout, consulte a skill `ui-ux-pro-max`** (banco de 84
estilos visuais, 192 paletas de cor e 74 combinações de fonte) pra escolher uma direção de
design coerente com o nicho do cliente — em vez de decidir cor/fonte "no chute" toda vez.
Combine a recomendação dela com as cores/fontes já definidas no
`identidade/design-guide.md` do cliente (se o cliente já tiver identidade definida, ela tem
prioridade; o banco de estilos entra pra decisões que a identidade não cobriu, tipo
composição de layout e hierarquia visual).

Use também a skill `frontend-design` (se disponível no ambiente) pra decisões finas de
espaçamento. HTML + CSS (+ JS mínimo se precisar de formulário ou menu mobile) em um único
arquivo ou pasta simples, sem dependências pesadas.

Sempre responsivo (mobile-first) — mais da metade do tráfego de anúncio é mobile.

**REGRA CRÍTICA — NUNCA cole o código HTML na conversa.** O usuário deste sistema pode não
saber ler código, e uma tela cheia de tags HTML não serve pra ele avaliar o site. O código
vai DIRETO pro arquivo, nunca aparece como texto na resposta.

## Passo 4 — Publicar como Artifact (preferencial) ou salvar local (alternativa)

**Se estiver rodando no Claude Code** (não no Cowork ou Chat): tente publicar o site como
um Artifact — isso gera um link visual tipo `claude.ai/code/artifact/...` que abre sozinho
no navegador, exatamente como um site pronto, sem mostrar código nenhum. É a experiência
que o usuário espera ver.

Esse recurso pede confirmação antes de publicar (normal, é assim que funciona) — aceite.

**Se o Claude Code responder que não consegue publicar** (o plano Team/Enterprise é exigido
pra esse recurso — no plano Pro pode não estar disponível), caia automaticamente pro plano B:

1. Salve o arquivo numa pasta clara: `saida-[cliente]-site/index.html`
2. Abra o arquivo automaticamente no navegador padrão pra o usuário ver o resultado visual
   na hora, sem precisar saber onde o arquivo está:
   - Windows: rode no terminal `start saida-[cliente]-site/index.html`
   - Mac: rode `open saida-[cliente]-site/index.html`
   - Linux: rode `xdg-open saida-[cliente]-site/index.html`
3. Se mesmo assim falhar, informe em português simples onde está o arquivo e como abrir
   manualmente (ex: "abre a pasta X, dá dois cliques no arquivo index.html") — nunca deixe
   a única saída ser "aqui está o código".

**No Cowork ou Claude Chat:** não existe esse recurso de Artifact do Claude Code — use
direto o plano B (salvar e orientar a abrir/publicar).

## Passo 5 — Explicar como publicar (linguagem simples, sem jargão técnico)
Depois que o usuário já viu o site visualmente, explica como publicar de verdade — sempre
em passos numerados, nunca assumindo conhecimento técnico:
1. Vai em netlify.com/drop
2. Arrasta a pasta inteira (a que tem o `index.html` dentro) pra área que aparece na tela
3. Em poucos segundos aparece um link — esse link já é o site no ar, pronto pra mandar pro cliente

Não tente publicar automaticamente — apenas entregue o arquivo pronto e o passo a passo.

## Regra
Nunca invente depoimento, número ou prova social que o cliente não forneceu. Se faltar
conteúdo real (depoimentos, fotos, textos institucionais), deixe marcado como
`[INSERIR: depoimento do cliente X]` em vez de inventar.
