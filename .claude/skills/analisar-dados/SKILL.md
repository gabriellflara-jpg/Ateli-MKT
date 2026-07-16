---
name: analisar-dados
description: >
  Lê uma planilha ou arquivo de dados (CSV, XLSX, PDF com tabelas) e devolve um resumo
  executivo com os números que mais importam, tendências e alertas. Use SEMPRE que o
  usuário subir uma planilha e pedir análise, disser "analisa esses dados", "resume essa
  planilha", "o que esses números mostram", ou pedir insight sobre um export qualquer.
---

> 🧠 **Memória:** leia `_memoria/perfil-agencia.md` e, se um cliente estiver aberto, `clientes/[nome-do-cliente]/_memoria/foco-atual.md` — isso ajuda a saber qual métrica importa mais pra essa análise agora.

# Analisar Dados

## Passo 1 — Entender o arquivo
Abra o arquivo (use ferramentas de código quando necessário — pandas para CSV/XLSX, extração
de tabela para PDF). Identifique: período coberto, colunas disponíveis, granularidade
(diário, semanal, por campanha, por cliente).

## Passo 2 — Resumo executivo (sempre primeiro)
3-5 linhas, sem jargão técnico, respondendo: o que aconteceu, o número mais importante,
se está melhor ou pior que o período anterior (se der pra comparar).

## Passo 3 — Detalhamento
- Principais métricas em tabela curta
- 1-2 tendências relevantes (queda, crescimento, sazonalidade)
- Outliers — algo fora do padrão que merece atenção

## Passo 4 — Alertas e recomendação
Se algo indicar problema real (queda brusca, métrica zerada, gasto sem retorno), destaque
isso no topo da resposta, não no fim. Termine com 1-2 ações recomendadas, não uma lista
longa — a prioridade real, não tudo que poderia ser feito.

## Regra
Nunca invente número que não está na planilha. Se um dado necessário não existir no arquivo,
diga isso explicitamente em vez de estimar.
