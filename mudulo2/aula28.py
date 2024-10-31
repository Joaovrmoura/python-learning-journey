#Reduce em python - faz a redução de um iterável em um
#  único valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#se eu quiser saber o total dos produtos 
# a função reduce precisa de um valor acumulador
def funcao_do_reduce(acumulador, produto):
    print(acumulador)
    return acumulador + produto['preco'] 

#acumlador, o reduce intera sobre cada item do dicionário
total = reduce(
    funcao_do_reduce, 
    produtos, 
    #valor inicial na primeira execução
    0
)
total2 = reduce(
    lambda ac, p : ac + p['preco'], 
    produtos, 
    0
)
print()
print(f'Total com função: {total:.2f}')

print()
print(f'Total com função lamda: {total2:.2f}')