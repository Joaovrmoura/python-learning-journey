def parOuImpar(num1):
    if num1 %2 == 0: 
        return print(f"O numero {num1} é par") 
    return print("Esse numero é ímpar")
     

numero = int(input("digite um numero: "))
showNumber = parOuImpar(numero)
print(showNumber)