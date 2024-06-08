#append - adicionar item ao final
#insert- adiciona um item no indeice escolhido
#del apaga o indice
#clear limpa a lista
#extend - estende a lista
# + - concatena listas 
lista= [10, 20 ,30 , 40]
lista.append('joao')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(100, 5)

lista_b = [1, 2 , 3]
lista_c = lista + lista_b
lista.extend(lista_b)
print(lista)
print(lista_c)
