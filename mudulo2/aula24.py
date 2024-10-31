# Importa as funções combinations e permutations da biblioteca itertools
from itertools import combinations, permutations, product  

def print_iter(iterator):
    for i, item in enumerate(iterator):  
        print(item)  
    print()  

pessoas = [
    'joao', 'joana', 'mateus', 'luiza'
]
camisetas = [
    ['preta', 'branca'], 
    ['masculino', 'feminino','unisex'],
    ['p', 'm', 'g'],
]


# Gera combinações de 2 pessoas na lista `pessoas`, sem considerar a ordem.
print_iter(combinations(pessoas, 2))  

# Gera permutações de 2 pessoas na lista `pessoas`, considerando a ordem.
print_iter(permutations(pessoas, 2))  

# Gera todas as combinações possíveis.
print_iter(product(*camisetas))  

print()
