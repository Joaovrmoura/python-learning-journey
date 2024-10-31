# groupby - agrupando valores (itertools)
import itertools 
from itertools import *

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

print()
print('Sorted lista nota')
# Ordena a lista de alunos com base na chave 'nota' e armazena em 'alunos_ordenados'.
alunos_ordenados = sorted(alunos, key=lambda nota : nota['nota'])  
# Agrupa os alunos ordenados por suas notas usando 'groupby'.
grupos = groupby(alunos_ordenados, key=ordena)
# Para cada chave (nota) e grupo de alunos, imprime a chave e a lista de alunos daquele grupo.
for chave, grupo in grupos:
    print(f"Grupo - {chave}") 
    # Converte o grupo em uma lista 
    for aluno in grupo:
        print(f"Nome: {aluno['nome']} - Nota: {aluno['nota']}")

print() 

print('Ordenando listas') 
alunos = ['a', 'a', 'a', 'a', 'b', 'c', 'a']
grupos_listas = groupby(sorted(alunos))

for chave, grupos in grupos_listas:
    print(list(grupos))

