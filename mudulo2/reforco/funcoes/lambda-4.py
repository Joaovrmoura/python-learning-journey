# Utilize uma função lambda com filter()
# para criar uma nova lista que contenha 
# apenas os produtos cujo preço é menor 
# que 20. Exiba a lista filtrada 
# com os produtos.

produtos = [
    {'nome': 'Produto A', 'preco': 25.50},
    {'nome': 'Produto B', 'preco': 15.00},
    {'nome': 'Produto C', 'preco': 30.00},
    {'nome': 'Produto D', 'preco': 10.00}
]

def listar(lista):
    for chave, valor in enumerate(lista):
        print(f"Nome: {valor['nome']} Preço: {valor['preco']}")
        
function = list(filter(lambda preco : preco['preco'] < 20, produtos))
listar(function)
