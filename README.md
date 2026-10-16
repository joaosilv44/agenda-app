### Teste de exclusão de local

Foi realizada uma tentativa de excluir, pelo Django Admin, um local que possuía eventos associados. A exclusão foi impedida pelo Django, preservando o local e os eventos vinculados.

Essa regra é implementada pelo parâmetro `on_delete=models.PROTECT` no relacionamento `ForeignKey` entre `Evento` e `Local`. O `PROTECT` impede a exclusão do objeto referenciado enquanto existirem objetos dependentes, evitando que eventos fiquem sem o local obrigatório.

**Resultado esperado:** o local não é excluído enquanto houver eventos associados a ele.