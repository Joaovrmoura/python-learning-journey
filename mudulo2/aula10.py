#list comprehension é uma forma rápida de criar listas 
# a partir de iteráveis
# aqui uma lista criada "normamente"
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

#aqui o list comprehension
#cria um for dentro da lista
#primeira variável serve como parâmentro para o loop do for
lista = [numero for numero in range(10)]
print(f'{lista} list comprehension')

#essa variavel numero é o equivalente a primeira linha que fica embaixo do for
lista = [numero * numero for numero in range(10)]
print(f'{lista}aqui com multiplicador')
print()

#Mapeamento de dados em list comprehesion
lista2 = [
    {'nome': 'p1', 'preco': 5},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 40},
]
#aqui estou criando um novo dicinário para cada item da lista

novo_produto = [{'nome': produto['nome'],'preco': produto['preco']} for produto in lista2]
print(novo_produto)
print()

#aqui posso alterar o valor de qualquer item da lista desempacotnado-a
#estou alterando o valor da chave preço
novo_produto = [{**produto,'preco': produto['preco'] * 1.05} for produto in lista2]
print(novo_produto)
print()

#também podemos usar condicionar dentro do list comprehension depois do "parâmetro do for"
#o if aumenta o valor da chave preço caso o preço do produto for maior ou = a 20
novo_produto = [
    {**produto,'preco': produto['preco'] * 1.05} 
    if produto['preco'] >= 20 else {**produto}
    for produto in lista2 
    ]
print(novo_produto)
print()

#####################################################################################

#módulo que importa um print mais compreensivo
import pprint

def p(v):
    return pprint.pprint(v, sort_dicts=False, width=35)

#list comprehension filter
# utlizamos o if depois do for para filtrar determinada informação

lista = [n for n in range(10) if n < 5]
p(lista)
print()

novo_produto = [
    {**produto,'preco': produto['preco'] * 1.05} 
    if produto['preco'] >= 20 else {**produto}
    for produto in lista2 
    if produto['preco'] > 20
    ]
#quando utilizamos o filter(depois do for) não podemos utilizar o else 
p(novo_produto)
print()

# For dentro de for em list comprehension
lista = [(n, x) for n in range(3) for x in range(3)]
print(lista)
print()
#podemos gerar uma nova list comprehesion dentro de outra list comprehesion
lista = [[x for x in range(3)] for n in range(3)]
print(lista)

novo_produto = [{**produto,'preco': produto['preco'] * 1.05} for produto in lista2]
print(novo_produto)
print()
