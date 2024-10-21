import random

for _ in range(20):
    cpf_validado = ''
    for i in range(9):
        cpf_validado += str(random.randint(0, 9))


    cpf_num = cpf_validado[:9]

    decremente = 10
    result_final = 0
    for indice, digitos in enumerate(cpf_num):
        result_final += int(digitos) * decremente
        decremente -= 1
    
    result_final = (result_final * 10) % 11
    resultado_final1 = result_final if result_final < 9 else 0
    cpf_num += str(resultado_final1)

    result_final_2 = 0
    decremente = 11
    for digito_2 in cpf_num:
        result_final_2 += (int(digito_2) * decremente)
        decremente -= 1

    result_final_2 = (result_final_2 * 10) % 11
    resultado_final_2 = result_final_2 if result_final_2 < 9 else 0
    cpf_num += str(result_final_2)

    print(cpf_num)
    