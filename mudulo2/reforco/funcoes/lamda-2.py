# Exercício 2: Filtrar Números Pares
# Crie uma lista de números inteiros, 
# incluindo alguns números pares e 
# ímpares (por exemplo, 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).
# Utilize uma função lambda junto 
# com filter() para criar uma nova 
# lista contendo apenas os números pares.
# Exiba a lista de números pares.

lista = [numeros for numeros in range(1, 11)]

function1 = list(filter(lambda x : x % 2 == 1, lista))
print(function1)

