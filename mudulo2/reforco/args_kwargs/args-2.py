# Exercício 2: Filtrando Argumentos com *args
# Crie uma função chamada filtrar_strings que receba vários
# argumentos com *args e retorne uma lista contendo 
# apenas os argumentos que são do tipo str.

# filtrar_strings(1, 'olá', 2.5, 'Python', [3, 4], 'mundo')  
# Saída: ['olá', 'Python', 'mundo']

def filtrar_strings(*args):
    lista = []
    for n in args:
        if isinstance(n, str):
            lista.append(n)
    return lista

print(filtrar_strings(1, 'olá', 2.5, 'Python', [3, 4], 'mundo'))     