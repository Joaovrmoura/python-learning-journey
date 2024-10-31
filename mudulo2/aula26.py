#map partials and Generator type
# é uma função que recebe outra função, que pode receber um ou mais
# argumentos

# cria uma função e preenchendo um ou mais parâmetros da função original
# exemplo: 
# def soma(a, b): a * b
# função com partial:
# nova_func = partial(parametro_da_funcao_original, valor_do_parametro)
from functools import partial
#Retorna o tipo se é generetor o iterator
#todo generator é um iterator, mas nem todo iterator e um generator
from types import GeneratorType

def print_p(iterators):
    print(*list(iterators), sep='\n')
    print()

def aumenta_preco(valor, percente):
    return round(valor * percente, 2)

aumenta_dez_percent = partial(
    aumenta_preco, 
    percente=1.1
)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# np = [
#     {**p, 'preco' : aumenta_dez_percent(p['preco'])} for p in produtos
# ]
#map faz a mesma coisa que o comentário acima, porém mapeando os dados
def muda_preco_proutos(produto):
    return {
        **produto, 
        'preco' : aumenta_dez_percent(produto['preco'])
    }

np = list(map(
    muda_preco_proutos, 
    produtos
))

lista = [
    1, 2, 3, 4
]


print('LISTA COM listar = list(map(lambda x : x * 3, lista))')
listar = list(map(lambda x : x * 3, lista))
print(listar)


print()
print(np)

print()
print('Lista: filtro = list(filter(lambda preco : preco["preco"] > 30, produtos))')
filtro = list(filter(lambda preco : preco['preco'] > 30, produtos))
print_p(filtro)
print()

print(hasattr(np, '__iter__'))
print(hasattr(np, '__next__'))
print(isinstance(np, GeneratorType))