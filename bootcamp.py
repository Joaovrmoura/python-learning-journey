extrato = 0
listar_depositos = []
listar_saque = []
numero_deposito = 0
LIMITE_DE_SAQUE = 3
while True:
    operacao = input("""
        Digite qual operação deseja realizar 
        [s] Sacar
        [d] Depositar
        [e] Ver extrato
        [x] Para sair
        letra da Operação: """)
    
    if operacao.lower() == 'd': 
        deposito = float(input("""
        Quanto deseja Depositar? """))
        if deposito <= 0:
            print("""
        Deposito minimo de  1 real""")
        else:
            extrato += deposito
            listar_depositos.append(deposito)

    elif operacao.lower() == 's':
        try:
            if extrato >= 0:
                saque = float(input("""
        Quanto deseja sacar? """))
                if LIMITE_DE_SAQUE > 0:
                    LIMITE_DE_SAQUE -= 1 
                    if saque > extrato or saque > 500:
                        print(f"""
        Saque acima do Valor ou
        Saldo insuficiente 
        Seu saldo é: R${extrato}
""")   
                    listar_saque.append(saque)
                    extrato -= saque  
                else:
                    print(f"""
        Limite de saque Estendido""")  
        except:
            print("""
        Digite uma caracter válido """)
    
                
        

    elif operacao.lower() == 'e':
        print("***********EXTRATO BANCÁRIO**********")
        for indice, n in enumerate(listar_depositos):  
            print(f"°{indice+1} deposito: R$ {n:.2f}")   
        for indice, sacado in enumerate(listar_saque):
            print(f"Valor sacado R$ {sacado:.2f}")
        print(f"Saques disponíveis {LIMITE_DE_SAQUE}")
        print(f"Saldo Atual: R$ {extrato:.2f}")
            
    elif operacao.lower() == 'x':
        print(f"{extrato}")
        break

    
            


            
