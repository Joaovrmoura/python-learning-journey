decremente = 10
result_final = 0
while True:

    cpf_num = input("digite seu CPF sem pontos ou traços: ")
    
    if len(cpf_num) > 9:
        print("Seu cpf deve ter apenas 9 digitos")

    elif cpf_num.isdigit():
        for indice, digitos in enumerate(cpf_num):
            digitos = int(digitos)
            n = digitos * decremente
            result_final += n
            decremente -= 1
        result_final = (result_final * 10) % 11
        resultado_final = print(result_final if result_final < 9 else 0)
    else:
        print("Apenas números são permitidos ")
