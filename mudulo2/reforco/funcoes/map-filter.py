# Crie uma nova função aumenta_vinte_percent usando partial para 
# aumentar o preço dos produtos em 20%. Aplique essa função e 
# exiba a lista de produtos com os preços atualizados.

# Defina uma função muda_nome_produtos que adiciona "Novo " antes do 
# nome de cada produto. Utilize map para aplicar essa função a cada produto, 
# criando uma lista novos_nomes_produtos com os nomes atualizados.

# Utilize filter para selecionar apenas os produtos que tenham um preço 
# menor que 50. Exiba a lista resultante.

# Crie uma função eh_generator que verifica se um objeto é um generator, 
# retornando True se for e False caso contrário. Teste eh_generator com 
# a lista produtos e com um generator criado por você.

# Com map, crie uma nova lista precos_dobrados que contenha o 
# dobro do preço de cada produto da lista produtos. 
# Exiba a lista precos_dobrados no final.

# utilize list, map, filter e as 
# bibliotecas 
# copia função e vc pode preencher quantos parametros quiser!


from functools import partial
# Retorna o tipo se é generetor o iterator
from types import GeneratorType

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def print_p(produto):
    for n, item in enumerate(produto):
        print(item)


# 1 #######################################################################

def aumenta_prec(valor, percent):
    return round(valor * percent)


def aumenta_10_percent(func, x):
    p1 = 1.1
    def aninhada(p1):
        return func(p1 * x)
    return aninhada

def mudar_prec(produto): 
    return {
        **produto, 'preco' : aumenta_10_percent(produto['preco'])
    }
    
mudar_prec_map = map(
    mudar_prec, 
    produtos
)

print_p(mudar_prec_map)
print()

# 2 ##############################################################################

def muda_nome_produtos(produto):
    return {
        **produto, 'nome' : 'Novo ' + produto['nome']
    }

mudar_n = map( 
        muda_nome_produtos, 
        produtos
    )

print_p(mudar_n)


# 3 ##############################################################################

def filtra(prduto):
    return prduto['preco']
    
filtar_menor = list(filter(
    lambda p : filtra(p) > 50,
    produtos
))
print()
print_p(filtar_menor)


# 4 ##############################################################################