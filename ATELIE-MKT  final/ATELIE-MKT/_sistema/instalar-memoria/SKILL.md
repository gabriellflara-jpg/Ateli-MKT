---
name: instalar-memoria
description: >
  Instala a memória da agência — entrevista sobre quem ELA é como prestadora de serviço
  (não sobre um cliente específico) e preenche _memoria/perfil-agencia.md e _memoria/foco-atual.md.
  Use SEMPRE na primeira instalação do sistema, quando disser "instalar memória",
  "configurar minha agência", "/instalar-memoria", ou "como o sistema aprende quem eu sou".
---

# /instalar-memoria — Memória da Agência

Entrevista curta e natural (não formulário) sobre a pessoa que USA o sistema — a prestadora
de serviço, não um cliente dela.

## Pergunte, em blocos

1. Nome, marca, posicionamento em uma frase
2. Quais serviços oferece e ticket médio
3. Quantos clientes atende hoje
4. Tom de voz dela (como fala com clientes, não o tom de cada cliente)

Preencha `_memoria/perfil-agencia.md` com essas respostas.

Depois pergunte a prioridade do mês e o que está travado — preencha `_memoria/foco-atual.md`.

## Identidade visual da própria agência (opcional, mas recomendado)

Pergunte se ela quer registrar a identidade visual da própria agência (cores, fontes, logo,
estilo) — isso é usado quando o material é da agência mesma (post institucional, proposta
comercial), não de um cliente. Se sim, preencha `_memoria/identidade-visual-agencia.md`.
Se ela preferir pular essa parte agora, tudo bem — pode ser preenchido depois com
`/atualizar-memoria`.

## Diferença importante

Essa memória é sobre a AGÊNCIA. A memória de cada CLIENTE fica em `clientes/[nome-do-cliente]/_memoria/`,
preenchida pela skill `novo-cliente`. Nunca misture as duas.

## Instruções de Project (avise o usuário)

Se estiver usando Cowork Project, oriente a colar isso nas Instruções do Project:

```
Antes de qualquer tarefa, leia silenciosamente _memoria/perfil-agencia.md e
_memoria/foco-atual.md. Se a tarefa for sobre um cliente específico, leia também
clientes/[nome-do-cliente]/_memoria/*.md e clientes/[nome-do-cliente]/identidade/design-guide.md.
Aplique tudo isso na resposta sem citar os arquivos.
```
