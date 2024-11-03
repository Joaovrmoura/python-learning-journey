# Exercício 2:
# Filtragem com List Comprehension
# Dada uma lista de dicionários 
# representando produtos, onde cada 
# dicionário possui as chaves 
# 'nome' e 'preco', crie uma 
# nova lista que contenha 
# apenas os produtos cujo preço é 
# maior que 15. Utilize list comprehension 
# para isso. Quais seriam os passos 
# para implementar essa filtragem?

produtos = [
    {'nome': 'Produto A', 'preco': 10},
    {'nome': 'Produto B', 'preco': 25},
    {'nome': 'Produto C', 'preco': 15},
    {'nome': 'Produto D', 'preco': 30},
    {'nome': 'Produto E', 'preco': 5}
]

nome_produtos = [#primeira regra###
    {'nome': produto['nome'], 'preco':produto['preco']} 
    #segunda "regra"(pode executar a primeira)
    for produto in produtos 
    #terceira regra executa a primeira
    if produto['preco'] > 15]

for produto in nome_produtos:
    print(f"{produto['nome']} preço: {produto['preco']}")
        