decremente = 10
result_final = 0
result_final_2 = 0

cpf_digitado = input("digite seu CPF sem pontos ou traços: ")
cpf_num = cpf_digitado[:9]

if cpf_num.isdigit():
    for indice, digitos in enumerate(cpf_num):
        result_final += int(digitos) * decremente
        decremente -= 1
    
    result_final = (result_final * 10) % 11
    resultado_final1 = result_final if result_final < 9 else 0

    cpf_num += str(resultado_final1)
    decremente = 11

    for digito_2 in cpf_num:
        result_final_2 += (int(digito_2) * decremente)
        decremente -= 1

    result_final_2 = (result_final_2 * 10) % 11
    resultado_final_2 = result_final_2 if result_final_2 < 9 else 0

    cpf_num += str(result_final_2)
    
    if cpf_num == cpf_digitado:
        print(f"cpf {cpf_num} valido")
    else:
        print(f"""Primeiro digito e o segundo digito deveriam 
ser respectivamente {resultado_final1}{resultado_final_2}""")

else:
    print("Apenas números são permitidos ")
