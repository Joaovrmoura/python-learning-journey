# extrato: Armazena o saldo total da conta.
# listar_depositos: Lista que armazena todos os depósitos feitos.
# listar_saque: Lista que armazena todos os saques realizados.
# numero_deposito: (não utilizado no código) provavelmente deveria contar
# o número de depósitos, mas não está sendo utilizado.
# LIMITE_DE_SAQUE: Define o limite de saques por dia (3 saques).

# Operação 'Depositar' (d):

# O usuário insere um valor a ser depositado.
# Se o valor for maior que 0, ele é adicionado ao extrato, e o depósito é registrado na lista listar_depositos.
# Se o valor for 0 ou negativo, uma mensagem é exibida dizendo que o depósito mínimo é de 1 real.

# Operação 'Sacar' (s):
# O usuário insere o valor que deseja sacar.
# O código verifica:
# Se o valor do saque não ultrapassa o saldo disponível (extrato) ou o limite de saque de R$ 500.
# Se o usuário ainda não ultrapassou o limite de 3 saques diários (LIMITE_DE_SAQUE).

# Se o saque não for válido (por saldo insuficiente ou valor acima do limite), uma mensagem de erro é exibida.
# Operação 'Extrato' (e):

# Exibe um resumo das transações:
# Lista os depósitos registrados.
# Lista os valores sacados.
# Exibe o saldo atual e o número de saques restantes.
# Operação 'Sair' (x):

listar_deposito = []
listar_saque = []
saldo = 0
limite_saque = 1

while True:
    op = input("""Digite a operação que deseja:
               
[d]depositar [s]sacar [e]ver extrat ou [x]sair: """)
    if op == "d":
        try:
            depositos = int(input("Digite o valor que deseja depositar: "))
        except:
            print("Digite um numero ou valor válido!")
            continue
        
        if depositos <= 0:
            print("Erro no deposito: valor minimo de 1 real ")
        else:
            listar_deposito.append(depositos)
            saldo += depositos
        
    if op == "s":
        saque = int(input("Digite o valor que deseja Sacar: "))
        
        if saque > 500:
            print("limite de 500 reais para saques!")
        else:
            if saque > saldo:
                print(f"Você tentou sacar: {saque} porém seu saldo é de: {saldo}")
            elif saque < 0:
                print("O saque minimo de 1 real!")
            else:
                if limite_saque == 3:
                    print("Você atingiu o limite diário de Saques!")
                else:
                    print(f"Saque nº {limite_saque} de 3 disponíveis")
                    listar_saque.append(saque)
                    saldo -= saque
                    limite_saque += 1
        
    if op == "e":
        print("Depositos")
        for indice, valores in enumerate(listar_deposito):
            print(f"{indice + 1}º deposito:{listar_deposito[indice]}")
            
        print()  
        print("Saques")
        for indice, valores in enumerate(listar_saque):
            print(f"{indice + 1}º Saque:{listar_saque[indice]}")
            
        print()
        print(f"Seu saldo Atual: {saldo}")

    if op == "x":
        break
print("Operação encerrada")