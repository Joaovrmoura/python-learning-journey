# Escreva um programa que leia uma matriz 3x3 e um número. O 
# programa deve multiplicar todos os elementos da matriz por esse número 
# e exibir o resultado.

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        entrada = input(f"Preencha a matriz A[{i}][{j}]: ")
        linha.append(entrada)
    matriz.append(linha)   
    
for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]}\t", end="")
    print()
