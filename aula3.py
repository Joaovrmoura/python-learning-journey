#try -> tentar executar o código 
#except -> ocorreu algum erro ao tentar executar
print(123)
print(456)
numero = input('dobrar o numero ')

try:
    numerofloat = int(numero)
    print(f"o dobro de {numero} é {numerofloat * 2}")
except:
    print("not a number ")

