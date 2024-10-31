#funções recursivas em python
def recursiva(n):
    total = 0
    if n > 0:
        total = recursiva(n - 1) * recursiva(n)
    return total

n = recursiva(5)
print(n)

def recurviva2(inicio=0, fim=10):
    inicio += 1
    return recursiva(inicio, fim)

recurviva2()