"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# Primeira Forma
print()
print("Primeira Forma")
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
def menor_lista(lista1, lista2):
    menor_lista = min(len(lista1), len(lista2));
    return [
        lista1[i] + lista2[i] for i in range(menor_lista)
    ]
print(menor_lista(lista_a, lista_b))

# Segunda Forma
print()
print("Segunda Forma")
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# m = menor_lista(lista_a, lista_b)
# print(m)

soma = [lista_a[i] + lista_b[i] for i in range(min(len(lista_a), len(lista_b)))]
print(soma)


# Terceira forma
print()
print("Terceira forma")
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista = []
for i in range(len(lista_b)):
    lista.append(lista_a[i] + lista_b[i])
print(lista)

# Quarta forma
print()
print(" Quarta forma")
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

# Quinta forma
print()
print(" Quinta forma")
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(list(zip(lista_a, lista_b)))