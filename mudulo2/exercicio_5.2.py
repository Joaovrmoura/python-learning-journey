import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos_novo_preco = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

ordem_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['nome'], 
    reverse=True
)
ordem_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['preco']
)

print(*produtos_novo_preco, sep='\n')
print()
print(*ordem_nome, sep='\n')
print()
print(*ordem_preco , sep='\n')