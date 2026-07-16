---
name: abrir-cliente
description: >
  Carrega o contexto de um cliente específico antes de uma sessão de trabalho — lê
  perfil-negocio.md, preferencias.md, foco-atual.md e identidade/design-guide.md da pasta
  desse cliente. Use SEMPRE que o usuário disser "abre o cliente [nome]", "trabalhar no
  cliente [nome]", "muda pro cliente [nome]", ou mencionar um cliente pelo nome no início
  de um pedido.
---

# /abrir-cliente — Trocar de Contexto

1. Identifique o nome do cliente mencionado.
2. Leia `clientes/[nome-do-cliente]/_memoria/perfil-negocio.md`, `preferencias.md`,
   `foco-atual.md` e `identidade/design-guide.md`.
3. Se a pasta não existir, avise e sugira rodar `/novo-cliente` primeiro — não invente dados.
4. Confirme em uma linha: "Contexto do [cliente] carregado." e siga com o pedido original
   do usuário já aplicando esse contexto.
5. Esse contexto vale só para os próximos pedidos até o usuário abrir outro cliente ou
   encerrar a sessão — não misture com o cliente anterior.
