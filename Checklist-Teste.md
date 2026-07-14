# CHECKLIST DE TESTE — ATELIÊ MKT

Rodem isso juntos, na ordem, antes de usar com cliente real. Cada passo tem o que fazer e
o que confirmar. Se algum passo falhar, param ali e me chamam antes de seguir.

---

## PARTE 1 — Instalação

**1.1** Descompactar o zip e abrir a pasta `ATELIE-MKT`.
☐ Confirma que existem as pastas: `_memoria`, `_sistema`, `clientes`, `execucao`, `estrategia`

**1.2** Escolher o ambiente (recomendo começar pelo Cowork, é o mais visual):
- Cowork → Projects → **+** → "Usar uma pasta existente" → selecionar `ATELIE-MKT`
☐ Confirma que o Project abriu e mostra a pasta certa

**1.3** Colar nas Instruções do Project:
```
Antes de qualquer tarefa, leia silenciosamente _memoria/perfil-agencia.md e
_memoria/foco-atual.md. Se a tarefa for sobre um cliente específico, leia também
clientes/[nome-do-cliente]/_memoria/*.md e identidade/design-guide.md desse cliente.
Se nenhum cliente foi mencionado e o pedido depende de contexto de cliente, pergunte
qual antes de gerar a entrega.
```
☐ Confirma que salvou

---

## PARTE 2 — Memória da agência

**2.1** Digite: `Ative o instalar-memoria`
☐ Confirma que ele começou a entrevistar (nome, marca, serviços, tom de voz)

**2.2** Responda a entrevista com dados reais dela (não precisa ser perfeito, dá pra editar depois).

**2.3** Depois de terminar, digite: `Abre o arquivo _memoria/perfil-agencia.md`
☐ Confirma que os campos foram preenchidos com o que ela respondeu (não ficou em branco)

**Se falhar aqui:** o problema é a skill não estar sendo reconhecida ou não estar
escrevendo no arquivo — me chama com o print do que aconteceu.

---

## PARTE 3 — Cliente de teste (usar dados fictícios, não um cliente real ainda)

**3.1** Digite: `Ative o novo-cliente` e responda com um negócio fictício, ex:
"Studio Bella, clínica de estética, São Paulo, ticket médio R$300, cores rosa e dourado"

**3.2** Depois de terminar, digite: `Abre o cliente Studio Bella`
☐ Confirma que ele diz algo como "Contexto do Studio Bella carregado"

**3.3** Digite: `Que cores e fontes o Studio Bella usa?`
☐ Confirma que ele responde com as cores/fontes que vocês acabaram de cadastrar
   (isso prova que a memória de cliente está funcionando de verdade)

---

## PARTE 4 — Testar uma entrega de execução

**4.1** Com o Studio Bella ainda aberto, digite:
`Cria um carrossel de 4 slides sobre os benefícios da limpeza de pele`

☐ Confirma que ele gera o texto dos 4 slides
☐ Confirma que ele tenta gerar os PNGs (pode pedir pra rodar o script — deixem ele rodar)
☐ Abre os PNGs gerados — confirma que as cores batem com o que foi cadastrado no cliente

**Se o script der erro:** me manda a mensagem de erro exata, eu ajusto.

**4.2** Digite: `Gera um relatório de Meta Ads` e cole ou anexe uma planilha/print de
exemplo de qualquer campanha (pode ser fake, só pra testar o formato)
☐ Confirma que ele devolve um relatório estruturado, não só texto solto

---

## PARTE 5 — Testar uma entrega de estratégia

**5.1** Digite: `Ativa o diagnóstico rápido pro Studio Bella`
☐ Confirma que ele faz as perguntas de diagnóstico, não só devolve um texto genérico

---

## PARTE 6 — Trocar de cliente (testar isolamento)

**6.1** Digite: `Ative o novo-cliente` de novo, com um segundo negócio fictício diferente
(cores e tom bem diferentes do primeiro, tipo um negócio B2B sério vs o Studio Bella jovem)

**6.2** Digite: `Abre o cliente [segundo nome]`

**6.3** Peça outro carrossel.
☐ Confirma que as cores/tom saíram diferentes do Studio Bella — isso prova que não está
   misturando memória de um cliente com o outro (o erro mais perigoso do sistema)

---

## SE TUDO PASSOU

Está pronto pra primeiro cliente real. Recomendo o primeiro cliente real ser um caso simples
(cliente já ativo, dados fáceis de levantar) antes de um caso complexo.

## SE ALGO FALHOU

Anota exatamente em qual passo (ex: "3.3") e o que aconteceu de diferente do esperado —
manda pra mim que eu ajusto a skill específica, sem precisar refazer tudo.
