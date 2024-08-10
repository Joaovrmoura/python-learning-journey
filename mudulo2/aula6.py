import copy
#deep copy e shallow copy
#Shallow copy cria uma cópia de um dicionário criando um "novo dicionário"
#porém no shallow copy caso existam outras listas dentro dessa lista 
#ela não criara uma nova lista e o valor da lista sempre apontara para lista inicial
#mesmo que alterado

d1 = {
    'c1' : 'lista 1',
    'c2' : 1,
    'c3' : [0, 1, 2]
}

#com o copy.deepcopy (import copy) a lista será copiada de forma profunda
#mesmo que exista outra lista não mudará a lista inicial
d3 = copy.deepcopy(d1)
print(d1)
print(d3)

#aqui as alterações vão ser feitas nos dois dicionarios d1 e d2
d2 = d1
d2['c3'] = [22,23,24]
d2['c1'] = 'margaria'
d2 = d1.copy()
print(d1)
print(d2)

# Aqui caso existam outras listas dentro dessa lista 
#ela não criara uma nova lista e o valor alterado alterará a lista inicial
d2['c1'] = 'joao'
print(d2)
