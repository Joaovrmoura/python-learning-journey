#set não existe ordem
#O set retorna os valores sem repetiçao
numeros = set([1,2,3,4])
print(numeros)
#podemos trnasformar set em listas
numeros = list(numeros)
print(numeros)
letras = set("abacaxi")
print(letras)
carros = set(("palio","celta","gol", "celta"))
print(carros)
#métodos da classe set
conjunto_a = set([1, 2, 3])
conjunto_b = set([2, 3, 4])
#union para unir conjuntos
print(conjunto_a.union(conjunto_b))
#interseção de deconjuntos com intersection
print(conjunto_a.intersection(conjunto_b))
#diferença, com difference
#pega a diferença que não
#exite entre um conjunto e outro
print(conjunto_a.difference(conjunto_b))
print(conjunto_a.symmetric_difference(conjunto_b))
#issubset se os elementos de um conjunto estão
#dentro de outro então é True
print(conjunto_a.issubset(conjunto_b))
#ou isspuerset se os elemntos do primeiro 
# estiverem fora do sengundo = False
print(conjunto_a.issuperset(conjunto_b))
#isdisjoint verifica se existe interseção
#entre os elementos se existir retona false
print(conjunto_a.isdisjoint(conjunto_b))


#aqui os nomes das funções são
# auto explicativas 
conjunto_b.add()#só adiciona itens inexistentes
conjunto_b.clear()
conjunto_b.copy()
# DISCARD só discarta oque estiver dentro 
#do conjunto
conjunto_b.discard(2)
# POP mesma lógica list, porém
#remove o primeiro valor em diante
conjunto_b.pop()
# REMOVE aqui devemos passar 
#o valor a ser removido
conjunto_b.remove()
#podemos utilizar o in
print(1 in conjunto_a)
0 in conjunto_a
