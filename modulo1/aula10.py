lista = ['joao', 'maria', 'helena']
#adiciona item no final da lista
lista.append('joaoa')

#aqui o range me deu o tamanho do inicio ao fim da lista
#o len conta os itens da lista 
#count virara o tamnha da lista em numeros
count = range(len(lista))

#for percorre cada item dentro da minha lista
#nesse caso o indice vai ser um numero pq count é o numero de itens da lista
for indice in count:

    #o indice vai ser numerico começando do 0
    #e vai chamar o item que representa o numero do indice
    listas = lista[indice]

    print(f"indice {indice} => {listas}")
print('\n\n')


"""
Introdução ao desempacotamento + tuples ou tuplas
"""
#aqui p *_ pega o indice e descarta o resto da variavel
#aonde for adicionado o *_ ou o *resto o lugar ficará "vazio" e o item vai para o "comentario"
#tudo adicionado depois vira o resto da variavel
itens, item, *rest = ['item1', 'item 2', 'item3', 'item4']
print(itens)

_, nome2, *resto = ['item1', 'item 2', 'item3', 'item4']
print(nome2)
print(resto)

_, nome2, *_ = ['item1', 'item 2', 'item3', 'item4']
print(nome2 + '\n\n')
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
print(f"{tupla_1} {tupla_1[-1] } . \n")

#enumerate para numerar os itens de uma lista
lista_enumerate = 'joao', 'carla','fagner'   
for enumere in enumerate(lista_enumerate):
    print(enumere)

#ou, Cria uma lista para para o enumerate
outraLista = list(enumerate(lista_enumerate))
print(outraLista)

#ou
outraLista2 = enumerate(lista_enumerate)
for enumere in outraLista2:
    print(enumere)
    
#ou
lista4 = ['joao', 'carla','fagner']  
for item4 in enumerate(lista4):
    for valor4 in item4:
        print(f"\t{valor4}")

listar_carros = ['carro 1', 'carro2', 'carro 3', 'carro 4']
#aqui o for percorrera todos item da minha lista
#crio uma variavel para o for no caso eu crie "carro"
# a variavel carro receberá cada valor decalrado dentro da minha lista
for carro in listar_carros:
    #o carro pega cada valor dentro da minha lista
    print(carro)


#list comprehesion

# Cria uma nova lista 'pares' com números ímpares da lista 'numeros'
# 'numero' é a variável que representa cada elemento da lista 'numeros'
# 'for numero in numeros' itera sobre cada elemento da lista 'numeros'
numeros = [0, 1, 2, 3 ,54 , 98, 3, 6, 854, 74, 35]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

numeros_2 =  [0, 1, 2, 3 ,10 , 19, 3, 6, 7, 2]
quadrados = []

# 'numeros_3' é a variável que representa cada elemento da lista 'numeros_2'
# 'numeros_3 ** 2' eleva ao quadrado o valor de 'numeros_3'
numeros_comprehension = [numeros_3 ** 2 for numeros_3 in numeros_2]
print(numeros_comprehension)

for numeros in numeros_2:
    quadrados.append(numeros ** 2)
print(quadrados)