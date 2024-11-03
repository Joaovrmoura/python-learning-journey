# Crie um script no qual um grupo de alunos devera apresentar, cada um, 
# o tema de um capítulo de um livro, este capitulo possuí 5 temas 
# e o numero de páginas por tema é: 
# tema 3.1 = 8, tema 3.2 = 4, tema 3.3 = 15, tema 3.4 = 2, tema 3.5 = 3 
# o grupo de alunos possui 5 integrantes e para divisão algum aluno 
# poderá ficar com um tema a mais na apresentação, 
# porém cada aluno deverá ter no máximo
# 8 páginas no total para apresentação do tema, e no minimo 2.
# Embaralhe os temas para o grupo mantendo a regra está regra!

import random 
import itertools
from itertools import groupby, permutations

temas_pessoas = [
   {'nome': 'joao', 'tema': '3.3', 'pag' : 15},
   {'nome': 'larissa', 'tema': '3.5', 'pag' : 3},
   {'nome': 'thalis', 'tema': '3.2', 'pag' : 4},
   {'nome': 'cristiano', 'tema': '3.1', 'pag' : 8},
   {'nome': 'davi', 'tema': '3.4', 'pag' : 2}
]



def print_t(lista):
    for i, item in enumerate(lista):
        print(item, sep='\n')
   
def ordena(grupo):
    return grupo['pag']

def aumenta_porcentagem(valor, percent):
    return round(valor * percent, 2)

p = groupby(sorted(temas_pessoas, key=ordena))

new_t = [
    {**pag,'pag': aumenta_porcentagem(pag['pag'], 1.1) } 
    for pag in temas_pessoas
]

print_t(new_t)
print()
print_t(p)