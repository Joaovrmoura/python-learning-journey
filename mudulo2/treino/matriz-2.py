# matriz 8x8 composta por números binários (0 ou 1):
# O programa deve solicitar ao usuário que preencha uma matriz
# com números 0 ou 1, garantindo que os VV
# valores inseridos sejam apenas 0 ou 1. VV

# o programa deve contar quantos números 0 estão presentes. VV
# Determine a quantidade de 1s na segunda coluna:  vv
# Conte os 1s da diagonal principal:  vv
# Conte os 0s na diagonal secundária: vv
# Calcule os percentuais de 0s e 1s: VV

import decimal
TAM = 3
#preenchi a matriz v
def PreencherMatriz():
    matriz = []
    while len(matriz) < TAM:
        for i in range(TAM):
            linha = []
            for j in range(TAM):
                while True:
                    numero = input(f"Preencha a matriz: item nº[{i + 1}][{j + 1}]: ")
                    if numero.isdigit():
                        numero_int = int(numero)
                        if 0 <= numero_int <= 1:
                            linha.append(numero_int)
                            break
                        else:
                            print("Digite apenas números entre 0 e 1")
                    else:
                        print("Digite um número inteiro")           
            matriz.append(linha)  
    return matriz

# Contei os zeros da matriz v
def cont_zero(matriz):
    nums_zero = 0
    for linha in matriz:
        for item in linha:
            if item == 0:
                nums_zero += 1
    return nums_zero


# quantidade de 1s na segunda coluna: 
def cont_1s_coluna_2(matriz):
    cont_1s = 0
    for i, vetores in enumerate(matriz):
        cont_1s += matriz[i][1]
    return cont_1s
        
        
            
# Conte os 1s da diagonal principal:     
def cont_1s_dp(matriz):
    cont_1s = 0
    for i, vetores in enumerate(matriz):
        cont_1s += matriz[i][i]
    return cont_1s
 
 
# Conte os 0s na diagonal secundária:
def cont_0s_ds(matriz):
    cont_zeros = 0
    for i, j in enumerate(matriz):
        if matriz[i][TAM - 1 - i] == 0:
            cont_zeros += 1
    return cont_zeros


#Fiz o percentual             
def percentual(numero):
    media = (numero/(TAM * TAM)) * 100
    return media

#Fiz o percentual 
def contagem(matriz):
    cont_zeros = 0
    cont_uns = 0
    for linha in matriz:
        for item in linha:
            if item == 1:
                cont_uns += 1  
            if item == 0:
                cont_zeros += 1             
    return percentual(cont_uns), percentual(cont_zeros)


# print    
def exibirMatriz(matriz):
    print("Matriz 3x3:")
    for n in matriz:
        print(*n)
       
matriz = PreencherMatriz()
print()   
exibirMatriz(matriz)
print()   
percentual_1, percentual_2 = contagem(matriz)
print(f"Quantidade de Zeros da matriz: {cont_zero(matriz)}")
print(f"Quantidade de 1s da Segunda Coluna: {cont_1s_coluna_2(matriz)}")
print(f"Quantidade de 1s da Diagonal Principal: {cont_1s_dp(matriz)}")
print(f"Quantidade de os da Diagonal Secundária: {cont_0s_ds(matriz)}")
print(f"Percentual: Número Um: {percentual_1:.2f}% / Número zero: {percentual_2:.2f}%")



    

