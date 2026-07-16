# ATELIÊ MKT — GUIA DE USO

## 37 skills · execução + estratégia + design · memória multi-cliente · Claude Cowork / Code / Chat

---

## O QUE É

Sistema de 37 skills de IA que transforma o Claude numa agência de marketing completa —
pensado pra quem atende **vários clientes ao mesmo tempo** (freelancer ou dono de agência).

Organizado no padrão oficial do Claude Code (`.claude/skills/[nome]/SKILL.md`), o que faz
o comando **"Ative o [nome]"** funcionar direto, sem precisar apontar caminho de arquivo.

- **Execução** (22 skills) — o trabalho tático: carrossel (gera PNG pronto, não só texto),
  site/landing page (HTML pronto pra publicar, com design profissional via `ui-ux-pro-max`),
  SEO, Google Meu Negócio, Google Ads, Meta Ads, relatórios, WhatsApp, design, copy.
- **Estratégia** (10 skills) — o diferencial: ofertas (Hormozi), funil de lançamento,
  StoryBrand, vendedor Challenger, negociação, diagnóstico rápido de negócio, precificação.
  Não é só quem executa — é quem também pensa estratégia com o cliente.
- **Sistema** (4 skills) — cuidam da memória: instalam o perfil da agência, criam clientes
  novos, trocam de contexto entre clientes, atualizam informações pontuais.
- **Design** (1 skill) — `ui-ux-pro-max`: banco de 84 estilos visuais, 192 paletas de cor e
  74 combinações de fonte, usado pela skill `criar-site` pra decisões de design mais
  profissionais. Open source (MIT, Next Level Builder/claudekit), licença preservada dentro
  da própria skill.

Cada cliente atendido tem sua própria pasta com perfil, tom de voz e identidade visual —
os agentes puxam isso automaticamente, sem repetir contexto toda entrega.

---

## PASSO 0 — CONFIGURE A MEMÓRIA (obrigatório)

### Forma recomendada — Cowork Project (memória 100% automática)

1. Abra o Claude Desktop → Cowork → Projects → **+**
2. Escolha "Usar uma pasta existente" e selecione a pasta `ATELIE-MKT`
3. No campo **Instruções** do Project, cole:

   ```
   Antes de qualquer tarefa, leia silenciosamente _memoria/perfil-agencia.md e
   _memoria/foco-atual.md. Se a tarefa for sobre um cliente específico, leia também
   clientes/[nome-do-cliente]/_memoria/*.md e identidade/design-guide.md desse cliente.
   Se nenhum cliente foi mencionado e o pedido depende de contexto de cliente, pergunte
   qual antes de gerar a entrega.
   ```

4. Dentro do Project, digite: **"Ative o instalar-memoria"** e responda a entrevista curta
   sobre a agência (nome, serviços, tom de voz).
5. Pra cada cliente novo: **"Ative o novo-cliente"** — ele entrevista sobre o negócio, tom
   e identidade visual do cliente e cria a pasta isolada dele.

### Claude Code (VS Code)

Abra o terminal na pasta `ATELIE-MKT` e rode `claude`. Como as skills estão no padrão
`.claude/skills/`, **"Ative o [nome]" deve funcionar direto**, sem passo extra.

Se por algum motivo não funcionar (versão antiga do Claude Code, ou skill muito nova que
ainda não foi indexada na sessão), use o comando alternativo apontando o caminho exato:
```
Leia o arquivo .claude/skills/[nome]/SKILL.md e siga as instruções dele
```

### Claude Chat (claude.ai)

Instale cada skill em Customize → Skills → Adicionar Skill (zipando a pasta individual de
`.claude/skills/[nome]/`). Sem pasta local vinculada, cole o conteúdo de `_memoria/`
relevante direto na conversa quando for pedir uma entrega.

### Atualizando depois

Sempre que algo mudar, é só pedir: `"atualiza meu foco atual: [nova prioridade]"` ou
`"atualiza a identidade visual do cliente [nome]: cor primária é [hex]"` — não precisa
refazer a entrevista inteira.

---

## COMO ATIVAR OS AGENTES

`"Abre o cliente [nome]"` (sempre primeiro, se a entrega for pra um cliente) + o pedido.

Exemplos:
- "Abre o cliente Studio Bella. Cria um carrossel de 6 slides sobre limpeza de pele"
- "Abre o cliente Studio Bella. Cria uma landing page de captura de leads"
- "Ativa o tráfego pago Sobral e estrutura uma campanha de leads com R$50/dia"
- "Gera o relatório de Meta Ads dessa semana" + anexar export
- "Ativa o diagnóstico rápido pro Studio Bella"
- "Ativa o estrategista de ofertas Hormozi — o cliente quer lançar um pacote novo"

Com a memória ativa, você não precisa repetir quem é o cliente, tom de voz ou cores —
o agente já sabe.

---

## PROMPTS PRONTOS POR SERVIÇO

### Redes Sociais
```
Abre o cliente [nome]. Ativa o estrategista de conteúdo e monta um calendário
editorial de [X] posts pro mês de [mês].
```
```
Cria um carrossel de 8 slides sobre [tema], com CTA pra [comentar / salvar / clicar
no link da bio].
```
```
Cria um roteiro de Reel de 30 segundos sobre [tema], com gancho forte nos primeiros
3 segundos.
```

### Sites e Landing Pages
```
Abre o cliente [nome]. Cria uma landing page de captura de leads pro
[produto/serviço], com formulário de nome/telefone/email.
```
```
Cria uma página de vendas pro [produto], com headline, benefícios, prova social e CTA.
```

### Tráfego Pago
```
Abre o cliente [nome]. Ativa o tráfego pago Sobral e estrutura uma campanha de
[objetivo] com orçamento de R$ [valor]/dia.
```
```
Gera o relatório de Meta Ads dessa semana. [anexar export]
```
```
Ativa o Google Ads análise e diagnostica por que essa campanha não está performando.
[anexar export ou descrever números]
```

### SEO e Google Meu Negócio
```
Abre o cliente [nome]. Ativa o SEO completo e roda o diagnóstico das 8 frentes.
```
```
Ativa o Google Meu Negócio e roda o checklist de otimização do perfil.
```
```
Responde essa avaliação do Google: "[colar o texto]"
```

### WhatsApp
```
Abre o cliente [nome]. Ativa o WhatsApp atendimento e cria um script de resposta
pra quando um lead pergunta sobre [produto/serviço].
```
```
Ativa os disparos de WhatsApp e monta uma campanha de reativação pra contatos que
não compram há [X] dias.
```

### Branding e Copy
```
Abre o cliente [nome]. Ativa o design de marca e ajuda a definir posicionamento e
tom de voz do zero.
```
```
Ativa o copywriter BR e escreve uma página de vendas pro [produto/serviço].
```

### Consultoria Estratégica (upsell de ticket alto)
```
Abre o cliente [nome]. Ativa o diagnóstico rápido e mapeia o principal gargalo
dele em 10 perguntas.
```
```
Ativa o estrategista de ofertas Hormozi e ajuda a estruturar uma oferta
irresistível pro [produto/pacote].
```
```
Ativa o plano de ação e transforma esse diagnóstico num plano de 90 dias.
```

---

## RESUMO DE TODAS AS SKILLS

### Execução — 22 skills

| Skill | O que faz |
|---|---|
| carrossel | Cria carrosséis com imagem PNG pronta, no padrão visual do cliente |
| criar-site | Gera sites/landing pages em HTML prontos pra publicar, com design via ui-ux-pro-max |
| estrategista-conteudo | Calendário editorial, pilares de conteúdo, frequência |
| roteirista-reels | Roteiros de Reels/Shorts/TikTok com gancho de abertura |
| trafego-pago-sobral | Estrutura campanhas de Meta/Google Ads (método Pedro Sobral) |
| criativo-anuncio | Copy de anúncios pagos (Meta, Google, TikTok) |
| google-ads-copy | Copy completa pra Google Ads |
| google-ads-analise | Diagnóstico de campanhas Google Ads com baixa performance |
| google-ads-relatorio | Relatório executivo de performance do Google Ads |
| relatorio-ads-meta | Relatório executivo de performance do Meta Ads, com alertas |
| seo-completo | Diagnóstico e plano de SEO em 8 frentes, incluindo SEO pra IA |
| seo-landing-page | SEO e copy focado em landing pages que convertem |
| google-meu-negocio | Checklist de otimização, posts e perguntas/respostas do perfil Google |
| responder-avaliacoes | Respostas humanas pra avaliações (Google, redes sociais) |
| analisar-dados | Lê planilhas/CSV e devolve resumo executivo com alertas |
| whatsapp-atendimento | Scripts e protocolos de atendimento via WhatsApp |
| whatsapp-chatbot | Fluxos automáticos de conversa e qualificação no WhatsApp |
| whatsapp-disparos | Campanhas de disparo em massa e reativação no WhatsApp |
| design-marca | Posicionamento, tom de voz e personalidade da marca |
| design-briefing | Briefing completo pra repassar a um designer |
| copywriter-br | Copy e persuasão pro mercado brasileiro |
| email-marketing | Sequências de email marketing: boas-vindas, nutrição, vendas |

### Estratégia — 10 skills

| Skill | O que faz |
|---|---|
| diagnostico-rapido | Mapeia o gargalo principal de um negócio em 10 perguntas |
| estrategista-ofertas-hormozi | Ofertas irresistíveis baseadas em "$100M Offers" |
| funil-lancamento | Funis de lançamento (semente, interno, externo) pro mercado BR |
| negociador-estrategico | Negociação baseada no método Chris Voss |
| plano-de-acao | Plano de 90 dias a partir de um diagnóstico |
| precificacao-estrategica | Avalia e reestrutura preços com base em valor percebido |
| qualificador-leads | Critérios e scripts pra separar lead bom de lead ruim |
| seth-godin | Diferenciação e marketing de permissão |
| storybrand-miller | Clareza de mensagem de marca (framework StoryBrand) |
| vendedor-challenger | Modelo de vendas B2B pra ciclos longos |

### Sistema — 4 skills (memória)

| Skill | O que faz |
|---|---|
| instalar-memoria | Entrevista sobre a agência, preenche a memória de nível agência |
| novo-cliente | Cria a pasta de um cliente novo com perfil, preferências e identidade visual |
| abrir-cliente | Carrega o contexto de um cliente antes de trabalhar nele |
| atualizar-memoria | Atualiza um campo pontual sem refazer a entrevista inteira |

### Design — 1 skill (terceiros, MIT)

| Skill | O que faz |
|---|---|
| ui-ux-pro-max | Banco de 84 estilos, 192 paletas de cor, 74 combinações de fonte — consultado pela skill `criar-site` |

---

## ESTRUTURA DE PASTAS

```
ATELIE-MKT/
  .claude/skills/          → as 37 skills, padrão oficial do Claude Code
  _memoria/                → quem é a agência (dela)
  clientes/
    _template/              → nunca editar, é o molde
    [cada cliente real]/     → criado automaticamente por /novo-cliente
```

---

## O QUE AINDA NÃO TEM (fases futuras)

- Publicação automática (Instagram, Facebook, Google Meu Negócio) via API — decisão
  consciente, gera tudo pronto e a publicação é manual
- Layout de carrossel com foto de fundo/camadas (hoje cobre texto + cor sólida)
- Skill de "criar skill sob demanda"

---

Dúvidas? Rode primeiro o `Checklist-Teste.md` com dados fictícios antes de usar com
cliente real.
