# Valida e corrige número de telefone.
# Faça um programa que leia um número de telefone,
# e corrija o número no caso deste conter somente 7 dígitos,
# acrescentando o '3' na frente. O usuário pode informar o
# número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

def is_digit(numeros):
    # Remove caracteres não numéricos de uma lista de caracteres
    return [item for item in numeros if item.isdigit()]
    
def format_number(lista):
    if len(lista) == 7:
        print(f"Telefone:", ''.join(lista))
        print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
        lista = ['3'] + lista
        print(f"Telefone corrigido sem formatação: {''.join(lista)}")
    if len(lista) == 8:
        lista.insert(4, '-')
        numero_completo = ''.join(lista)
        print(f"Telefone: {numero_completo}")
    else:
        print('Numero inválido!')


numero = input("Digite o número do telefone: ")
digitos = is_digit(numero)
format = format_number(digitos)
