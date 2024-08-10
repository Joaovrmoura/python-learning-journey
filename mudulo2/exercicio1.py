def receberNum(*args):
    num = 1
    for n in args:
        num *= n
    return num

executar = receberNum(1,2,3,4,5)

print(executar)

def parOuImpar(num1):
    if num1 %2 == 0: 
        return print(f"O numero {num1} é par") 
    
    return print("Esse numero é ímpar")
     

numero = int(input("digite um numero: "))
showNumber = parOuImpar(numero)
print(showNumber)