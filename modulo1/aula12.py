#split join com list e str
#split divide uma string
#join - une uma string

frase = '       olha so que, coisa interessante     '
listar_frases_fixed = frase.split(',')

listar = []
for i, frase in enumerate(listar_frases_fixed):
    listar.append(listar_frases_fixed[i].strip())
    #strip remove os espaços da lista
print(listar_frases_fixed)
print(listar)
#deve ser criada uma string vazia 
frases_unidas = ', '.join(listar)
print(frases_unidas)

listaCarros = [
    ['pegeout', 'camaro'],
    ['carro2', 'carro4'],
    ['carro3', 'carro4', 'carro5', 'carro6', 'carro7']
]
print(*listaCarros, end='\n')
for carro in listaCarros:
    #o segundo for acessa cada item dentro do primeiro for
    for modelo in carro:
        print(modelo)

print(listaCarros[0][1])
print(listaCarros[2][2])
print(listaCarros[2][3])

#DESENPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕEs
string = 'ABCD'
lista = ['maria ', 'helena', 1, 2, 3, 'eduarda']
tupla = 'Python', 'é', 'legal' 
a, b, *_, c = lista
lista2 = ['maria ', 'helena', 1, 2, 3, 'eduarda']
for nome in lista2:
    print(nome)
print(*lista2)
print(*tupla)
print(a, c)

