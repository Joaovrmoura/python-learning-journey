# Exercício 1: Quadrado de Números
# Crie uma lista de números inteiros 
# de 1 a 10.
# Utilize uma função lambda para criar 
# uma nova lista que contenha o quadrado 
# de cada número da lista original.
# Exiba a nova lista com os quadrados.


crie_a_lista = [numeros for numeros in range(1, 11)]
print(crie_a_lista)
function1 = list(map(lambda x : x * 2, crie_a_lista))

print(function1)
# for n in crie_a_lista:
#     print(function1(n))