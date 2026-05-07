contatos = {
    'guilherme@gmail.com': {
        'nome': 'Guilherme',
        'idade': 30,
        'cidade': 'São Paulo'
    }
}

contatos["chave_inexistente"] # KeyError: 'chave_inexistente'

contatos.get("chave_inexistente") # None
contatos.get("chave_inexistente", {}) # {}
contatos.get('guilherme@gmail.com', {}) # {'nome': 'Guilherme', 'idade': 30, 'cidade': 'São Paulo'}