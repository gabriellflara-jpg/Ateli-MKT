---
name: atualizar-memoria
description: >
  Atualiza um campo específico da memória (da agência ou de um cliente) sem refazer a
  entrevista inteira. Use quando o usuário disser "atualiza meu foco atual", "atualiza a
  prioridade do cliente [nome]", "muda a identidade visual do [nome]", ou qualquer pedido
  pontual de mudança em memória já existente.
---

# /atualizar-memoria — Atualização Pontual

1. Identifique se é sobre a agência (`_memoria/`) ou sobre um cliente (`clientes/[nome]/_memoria/`).
2. Identifique qual arquivo e qual campo mudar.
3. Edite só o campo pedido, mantendo o resto do arquivo intacto.
4. Atualize a linha "_Última atualização: —_" com a data de hoje.
5. Confirme em uma linha o que mudou.
