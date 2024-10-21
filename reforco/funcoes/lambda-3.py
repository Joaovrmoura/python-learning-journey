# Utilize uma função lambda para 
# ordenar a lista de estudantes 
# com base na nota em ordem decrescente.
# Exiba a lista de estudantes ordenados.

estudantes = [
    {'nome': 'João', 'nota': 7.5},
    {'nome': 'Maria', 'nota': 9.0},
    {'nome': 'Ana', 'nota': 8.0},
    {'nome': 'Carlos', 'nota': 6.0}
]

function = (sorted(estudantes, key=lambda notas : notas['nota'], reverse=True))

for chave, valor in enumerate(function):
    print(f"{valor['nome']} Nota: {valor['nota']}")

        