lista = [
    {'nome':'joao', 'sobrenome' : 'rodrigues'},
    {'nome':'victor', 'sobrenome' : 'moura'},
    {'nome':'george', 'sobrenome' : 'mirante'},
    {'nome':'rodrigo', 'sobrenome' : 'silva'},
]

#Função lambda em python, é uma função que deve ser escrita em uma única linha de código
#São funções anônimas que devem ser contidas em uma única expressão

#função escrita normalmente
def exibir(lista):
    for item in lista:
        print(item)

def ordena(item):
    return item['nome']

lista.sort(key=ordena)
exibir(lista)
print()

#Aqui função com lambda
#o lambda é o equivalente a def o return ja recebe o item direto 
lista.sort(key=lambda item : item['sobrenome'])
exibir(lista)
print()

#com sorted
l1 = (sorted(lista, key=lambda item : item['nome']))
exibir(l1)