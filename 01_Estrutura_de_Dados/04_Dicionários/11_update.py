contatos = {
    'guilherme@gmail.com': {
        'nome': 'Guilherme',
        'idade': 30,
        'cidade': 'São Paulo'
    }
}

contatos.update({'guilherme@gmail.com': {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}})
contatos # {'guilherme@gmail.com': {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'}}

contatos.update({'giovana@gmail.com': {'nome': 'Giovana', 'idade': 25, 'cidade': 'Rio de Janeiro'}})
contatos # {'guilherme@gmail.com': {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'},
         #  'giovana@gmail.com': {'nome': 'Giovana', 'idade': 25, 'cidade': 'Rio de Janeiro'}}