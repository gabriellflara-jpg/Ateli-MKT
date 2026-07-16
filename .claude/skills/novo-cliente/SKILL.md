---
name: novo-cliente
description: >
  Cria uma pasta isolada para um cliente novo (copiando o template de clientes/_template/)
  e entrevista sobre o negócio dele, preenchendo perfil-negocio.md, preferencias.md,
  foco-atual.md e identidade/design-guide.md desse cliente. Use SEMPRE que o usuário disser
  "novo cliente", "adicionar cliente", "começar um cliente novo", "/novo-cliente", ou
  "preciso configurar um cliente que acabei de fechar".
---

# /novo-cliente — Onboarding de Cliente Novo

## Passo 1 — Nome da pasta
Pergunte o nome do cliente. Crie a pasta `clientes/[nome-do-cliente]/` copiando a
estrutura de `clientes/_template/` (subpastas `_memoria/` e `identidade/`).

## Passo 2 — Entrevista de negócio
Pergunte: nicho, o que vende, pra quem, ticket médio, concorrentes, fase do negócio,
principal gargalo. Preencha `clientes/[nome-do-cliente]/_memoria/perfil-negocio.md`.

## Passo 3 — Preferências de marca
Pergunte: tom de voz, palavras que usa/evita, referências que gosta, o que já reprovou antes.
Preencha `clientes/[nome-do-cliente]/_memoria/preferencias.md`.

## Passo 4 — Identidade visual
Pergunte: cores (hex se souber), fontes, estilo geral, onde está o logo.
Preencha `clientes/[nome-do-cliente]/identidade/design-guide.md`.

## Passo 5 — Foco atual
Pergunte: qual a primeira entrega, prazo, e a métrica que mais importa agora.
Preencha `clientes/[nome-do-cliente]/_memoria/foco-atual.md`.

## Passo 6 — Confirmação
Resuma em 3 linhas o que foi criado e diga: "a partir de agora, pra trabalhar com esse
cliente é só dizer 'abre o cliente [nome]' antes de pedir qualquer entrega."
