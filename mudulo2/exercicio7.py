# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']


def zipper(lista1, lista2):
    max_inter = min(len(lista1), len(lista2))   
    return [
        (lista1[i],lista2[i]) for i in range(max_inter)
    ]

e = zipper(lista1, lista2)
print(e)

from itertools import zip_longest
print()
#jeito mais fácil
print(list(zip(lista1, lista2)))
print()
print(list(zip_longest(lista1, lista2, fillvalue="Sem cidade")))