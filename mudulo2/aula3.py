def mostrar_args(*args):
    numeros = 0
    for numero in args:
        numeros += numero
    return numeros

executar = mostrar_args(5 , 8 ,20 ,63, 22)
print(executar)

numero = 1, 2, 3, 4 ,5 ,6 ,7 ,8

print(numero)
print(*numero)

print(sum((5 , 8 ,20 ,63, 22)))