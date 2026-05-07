contatos = {
    'guilherme@gmail.com': {
        'nome': 'Guilherme',
        'idade': 30,
        'cidade': 'São Paulo'
    }
}

copia_contatos = contatos.copy()

copia_contatos['guilherme@gmail.com'] = {'nome': 'Gui'}

print(contatos)

print(copia_contatos)