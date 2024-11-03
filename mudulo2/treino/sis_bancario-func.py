#sistema bancário crud
def is_digit(numero):
    if numero.isdigit():
        numero = int(numero)
        return numero
    else:
        return 'Operação inválida'

def extrato_deposito(lista):
    print('Lista de depositos: ')
    for i, item in enumerate(lista):
        print(f"{i + 1}º deposito: {item}")
        

def extrato_saque(lista):
    print('Lista de saques: ')
    for i, item in enumerate(lista):
        print(f"{i + 1}º Saques: {item}")

def op():
    lista_saque = []
    lista_deposito = []
    cont_saques = 0
    soma_dep = 0
    while True:
        op = input("""Digite a operação desejada:
[d]Depositar [s]Sacar [e]Extrato or [x]Sair: """)
        if op == 'x':
            break

        if op == 'd':
            depositar = input("Qual valor deseja depositar: ")
            depositos = is_digit(depositar)
        if depositos != False:
            lista_deposito.append(depositos)
            soma_dep += depositos

        if op == 's':
            cont_saques += 1
            if cont_saques <= 3:
                sacar = input("Qual valor deseja sacar: ")
                saque = is_digit(sacar)
                lista_saque.append(-saque)
                if saque > soma_dep:
                    print('Não tem saldo suficiente')
            else:
                print('Atingiu quantidade máxima de saques')      

        if op == 'e':
            if len(lista_deposito) > 0:
                extrato(lista_deposito)
            if len(lista_saque) > 0:
                extrato(lista_saque)

op()