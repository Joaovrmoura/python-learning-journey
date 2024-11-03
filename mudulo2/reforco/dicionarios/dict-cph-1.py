# Utilize Dictionary Comprehension 
# para criar um novo dicionário 
# contendo apenas os produtos da 
# categoria "Eletrônico", onde as 
# chaves são os nomes e os valores 
# são os preços.
# Exiba o dicionário resultante.

produtos = [
    {'nome': 'Produto A', 'preco': 30, 'categoria': 'Eletrônico'},
    {'nome': 'Produto B', 'preco': 20, 'categoria': 'Roupas'},
    {'nome': 'Produto C', 'preco': 50, 'categoria': 'Eletrônico'},
    {'nome': 'Produto D', 'preco': 15, 'categoria': 'Alimentos'}
]

lista = [{produto['nome'],produto['preco']} 
        for produto in produtos 
        if produto['categoria'] == 'Eletrônico']

print(lista)
