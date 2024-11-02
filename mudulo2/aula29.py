#funções recursivas em python
# Em funções recursivas necessitamos de um caso base
#que pare a execução

def recursiva(inicio=0, fim=4):
    print(inicio, fim)
    if inicio >= fim:
        return fim

    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())


# soma = 0
# n = 5

# for i in range(1, 6):
#     soma += n * n - 1    
#     print(soma)
print()
def factorial(n):
    if n <= 1 or n <= 0:
        return 1
    return n * factorial(n - 1)

n = factorial(5)
print(n)