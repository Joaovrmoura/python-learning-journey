lista = ['joao', 'maria', 'helena']
#adiciona item no final da lista
lista.append('joaoa')
#aqui o range me deu o tamanho do inicio ao fim da lista
#o len conta os itens da lista
count = range(len(lista))
#for percorre 
for indice in count:
    #criei uma variavel para receber a lista com o indice pegando o lugar do item
    listas = lista[indice]
    print(f"indice {indice} => {listas}")

"""
Introdução ao desempacotamento + tuples ou tuplas
"""
#aqui p *_ pega o indice e descarta o resto da variavel
#aonde for adicionado o *_ ou o *resto o lugar ficará "vazio" e o item vai para o "comentario"
#tudo adicionado depois vira o resto da variavel
_, nome2, *resto = ['item1', 'item 2', 'item3', 'item4']
print(nome2)
print(resto)
_, nome2, *_ = ['item1', 'item 2', 'item3', 'item4']
print(nome2)

#tuplas são listas nas quais os itens não são alteráveis 
#para criar tuplas retiramos os colchetes [] da lista 
tupla_lista = 'maria', 'jose', 'carlos'
print(tupla_lista)
#Também é possível fazer uma "tuple" virar lista com ""list"
tupla_lista = list(tupla_lista)
print(tupla_lista)
#Também podemos adicionar () ou nome_variavel = tuple(nome_variavel) 
tupla_1 = ['maria', 'jose', 'carlos']
tupla_1 = tuple(tupla_1)
print(f"{tupla_1} {tupla_1[-1]}")


