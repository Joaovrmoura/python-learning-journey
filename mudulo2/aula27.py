# filter em python
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#Isso é a mesma coisa que 
np = list(filter(
        lambda preco : preco['preco'] > 50,
        produtos
        )
    )

#ISSO
np_cph = [
    {**p, 'preco': p['preco']} 
    for p in produtos
    if p['preco'] > 100
]

print(*list(np_cph))
print(np)
