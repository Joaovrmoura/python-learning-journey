# Exercício: Agrupamento de Alunos por Notas
# Descrição:
# Você tem uma lista de alunos, cada um com um nome e uma nota. O objetivo deste exercício é:

# Criar uma função que receba uma lista de dicionários contendo os alunos e suas notas.
# Ordenar essa lista por notas.
# Agrupar os alunos de acordo com suas notas.
# Exibir os alunos agrupados por nota.

# Instruções:
# Crie uma lista de dicionários chamada alunos com pelo menos 10 a
# lunos, onde cada dicionário contém o nome do aluno e sua nota (que pode ser de A a D).
# Implemente a função agrupa_alunos_por_nota que utiliza sorted e 
# groupby para realizar o agrupamento. Para cada grupo de notas, 
# imprima o cabeçalho "Grupo - [nota]" seguido pela lista de alunos que pertencem a esse grupo.

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
