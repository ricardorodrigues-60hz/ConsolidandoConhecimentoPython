dados = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

print(dados) # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

dados = dict(nome='João', idade=30, cidade='São Paulo')

dados['telefone'] = '1234-5678' 
print(dados) # {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'telefone': '1234-5678'}

dados['nome'] # 'João'
dados['idade'] # 30
dados['cidade'] # 'São Paulo'

dados['nome'] = 'Maria'
dados['idade'] = 25
dados['cidade'] = 'Rio de Janeiro'
print(dados) # {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro', 'telefone': '1234-5678'}

