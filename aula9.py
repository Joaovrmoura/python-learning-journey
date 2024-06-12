#clear limpa a lista
# + - concatena listas 
lista = [10, 20 ,30 , 40]
#copia a lista criando uma nova com os mesmos dados da copiada
lista_copiada = lista.copy()
#adiciona um elemento no final da lista
lista.append('joao')
#reverse, inverte a lista. "fica de trás para frente"
lista.reverse()
#mostra a posição do item dentro da lista ou "lugar representado por numero"
lista.index(20)
#remove o ultimo item da lista ou o indice caso digitado dentro dela
nome = lista.pop()
#del apaga o indice
del lista[-1]



#lista 2
lista2 = ['joao', 'maria', 'jose']
#remove usado para remover um item pelo nome,
# remove o item apenas 1 vez na primeira aparição
lista2.remove('jose')
#insert- adiciona um item no indeice escolhido 
#lista.insert(aqui a posição que deseja adicionar o iteem, aqui o item)
lista2.insert(2, 5)
#count conta quantas vezes um elemto aparecel no minha lista
lista2.count("joao")
#concatenação de listas
lista_c = lista + lista2
#extend - estende a lista
lista.extend(lista2)

# lista para função sort()
lista_sort = ['ola', 'mundo', 'joao', '24anos', 'japeri']
#vai embaralhar os itens da minha lista
lista_sort.sort()
#sort reverse, inverte a ordem da lista sort()
lista_sort.sort(reverse=True)
#lista com a função anônima lambda
lista_lambda = ['ola', 'mundo', 'joao', '24anosss', 'japeri']
#Essa funçao pega o x =(variavel) para receber o tamanho de cada item e 
# listar em ordem crescente
lista_lambda.sort(key=lambda x: len(x))
#ou utilizar como uma função com o sorted()
sorted(lista_lambda, key=lambda x: len(x))
#função reversa na função lambda
lista_lambda = ['ola', 'mundo', 'joao', '24anosss', 'japeri']
#inverte a oordem da lista para ordem decrescente
lista_lambda.sort(key=lambda x: len(x), reverse=True)
#ou utilizar como uma função com o sorted()
sorted(lista_lambda,key=lambda x: len(x), reverse=True)

print(lista_sort)
print(lista_lambda)
print(lista)
print(lista2)
print(lista_c)
