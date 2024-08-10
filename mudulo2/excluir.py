alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
cont = 0

while cont != 1:
    try:
        numero_letra = int(input("Digite o numero referente a letra do dicionario: "))
    except:
        print("digite um numero válido")
    
    if numero_letra < 1 or numero_letra > 26:
        print("numero invalido o numero deve ser maior que 1 e menor que 26")
    else:
        cont = 1
        
for chave in range(numero_letra):
    letra = alfabeto[chave]

print(letra)