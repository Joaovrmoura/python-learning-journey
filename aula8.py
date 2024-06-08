#listas python = array
lista = [123, True, 'joao, 1.5',[], 300 , 500]
string = 'ABCDE'
lista_2 = [50, 60, 70, 80, 90]
 
#podemos acessar os items da lista
print(lista[-1])
print(lista[-2])
#deletar o item da lista -del-
del lista[2]
#adicionar item no final da lista
lista.append(50)
#remove o ultimo item adionado por ultimo no código 
#ou caso vc adicione o indice a remover, ele será removido
lista.pop()

print(lista)