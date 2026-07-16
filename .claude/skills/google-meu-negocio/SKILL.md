---
name: google-meu-negocio
description: >
  Otimiza e cria conteúdo para o perfil do Google Meu Negócio (GMB/Google Business Profile)
  — checklist de otimização, posts semanais, respostas de perguntas frequentes. Use SEMPRE
  que o usuário mencionar Google Meu Negócio, GMB, Google Business Profile, perfil no Google,
  "aparecer no mapa do Google", "melhorar minha ficha do Google", ou pedir post pro Google.
---

> 🧠 **Memória:** leia `_memoria/perfil-agencia.md` e, se um cliente estiver aberto, `clientes/[nome-do-cliente]/_memoria/*.md` e `clientes/[nome-do-cliente]/identidade/design-guide.md` (fotos e posts devem seguir o mesmo padrão visual do cliente). Se nenhum cliente foi aberto, pergunte qual cliente antes de gerar o conteúdo.

# Google Meu Negócio

Cobre negócio local (loja física, clínica, prestador que atende presencial/regional).
Se o cliente for 100% digital sem endereço físico, avise que GMB não se aplica e sugira
`seo-completo` no lugar.

## Checklist de otimização do perfil
Passe o cliente por esse checklist e sinalize o que está faltando:
- Categoria principal certa + categorias secundárias relevantes
- Horário de funcionamento atualizado (incluindo feriados)
- Descrição do negócio com as palavras que o cliente busca (sem keyword stuffing)
- Ao menos 10 fotos recentes (fachada, interior, equipe, produtos/serviços)
- Site e WhatsApp cadastrados
- Atributos relevantes preenchidos (ex: acessibilidade, estacionamento, aceita cartão)

## Posts semanais
Gere posts curtos (até 1500 caracteres, geralmente menos é melhor) com CTA claro
(ligar, agendar, ver oferta). Puxe temas de `foco-atual.md` do cliente quando fizer sentido
(promoção do mês, evento, lançamento).

## Perguntas e Respostas (Q&A)
Se o usuário pedir, gere 5-8 perguntas frequentes do nicho (que clientes reais perguntariam)
já com resposta pronta, pra deixar pré-cadastrado na seção de perguntas do perfil.

## Avaliações
Pra responder avaliações que já chegaram, use a skill `responder-avaliacoes` — essa aqui foca
em criar/otimizar, não em responder review pontual.

## Entrega e publicação
Essa skill gera o conteúdo pronto (texto e checklist) — a publicação em si é manual, feita
direto no painel do Google Business Profile. Publicação automática via API do Google exige
credencial própria por cliente e aprovação do Google; não é o escopo desta skill.
