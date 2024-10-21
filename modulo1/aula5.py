nome = input("digite seu nome : ")
cont = 0
novo_nome = ''
while cont < len(nome):
    letra = '*' + nome[cont] + ''
    novo_nome += letra
    cont += 1
novo_nome += '*'
print(novo_nome)

while True:
    
    try:
        num_1 = input("digite um numero ")
        num_2 = input("digite outro numero ")
        num_1 = float(num_1)
        num_2 = float(num_2)

        operador = input("digite o sinal de operação ")
        operador_pass = '*-+/'

        if operador in operador_pass and len(operador) < 2:
            if operador == '/':            
                print( num_1 / num_2)
            elif operador == '-': 
                print(num_1 - num_2)
            elif operador == '+':
                print(num_1 + num_2)
            elif operador == '*':
                print(num_1 * num_2)
    except Exception as error:
        print(error)
#startswitch pega a primerira letra e retorno se ela for igual = Boolean true
    sair = input("Quer sair [s] ou [n] ? ").lower().startswith('s')
    if sair is True:
        break
     

   

         
