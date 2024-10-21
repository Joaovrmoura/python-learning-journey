
piramedes = int(input("digite o numero de linhas da piramede "))
n = '#'
for piramede in range(piramedes):
    print(n)
    n += '#'
    
#iteradores
#iteravel
##texto = iter('joao')
texto = 'joao'
#iterador
iterator = iter(texto)
##print(texto.__next__())
##print(texto.__next__())
##print(next(texto))

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break
for letra in texto:
    print(letra)

for i in range(12):
    if i == 2:
        print('i = 2 pula')
        continue
    if i == 8:
        print('i = 8 pula')
        continue
    