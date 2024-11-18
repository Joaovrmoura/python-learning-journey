# Criar uma função que receba uma lista de dicionários contendo os alunos e suas notas.
# Ordenar essa lista por notas.
# Agrupar os alunos de acordo com suas notas.
# Exibir os alunos agrupados por nota.

# Instruções:
# Crie uma lista de dicionários chamada alunos com pelo menos 10 a
# lunos, onde cada dicionário contém o nome do aluno e sua nota 
# (que pode ser de A a D).
# Implemente a função agrupa_alunos_por_nota que utiliza sorted e 
# groupby para realizar o agrupamento. Para cada grupo de notas, 
# imprima o cabeçalho "Grupo - [nota]" seguido pela lista de alunos 
# que pertencem a esse grupo.


import itertools 
from itertools import groupby

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

def notas(aluno):
    return aluno['nota']

agrupar = sorted(alunos, key=lambda nota : nota['nota'])
agruparA = groupby(agrupar, key=notas)

for chave, grupos in agruparA:
   for aluno in grupos:
        print(f'Grupo - [{aluno['nota']}] aluno - {aluno['nome']}')


# Exercício 2: Exibição de Informações
# Crie uma função chamada exibir_informacoes
# que aceite um número variável de 
# argumentos nomeados usando **kwargs. 
# A função deve imprimir cada chave e valor
# fornecidos. 
# Teste a função passando diferentes 
# informações como 
# nome, idade e cidade (por exemplo, nome='João', 
# idade=30, cidade='São Paulo')
# e exiba as informações formatadas.

#em funções recebem varios argumentos nomeados


def argumentos_nomeados(**kwargs):
       for chave, valor in kwargs.items():
           print(chave, valor)

for n in range(1):
    nomes = input("Digite seu nome: ")
    idade =  input("Digite sua idade: ")
    cidades =  input("Digite sua cidade: ")
    argumentos_nomeados(nome=nomes, idade=idade, cidade=cidades)