frase = 'ola mundo fsdfwgukrhyg2ghrjg sjfsdfgefwsg'

i = 0
letra_repetida = 0
letra_result = ''

while i < len(frase):
    letra_atual = frase[i] 
    cont_letra = frase.count(letra_atual)
    
    if cont_letra > letra_repetida:
        letra_repetida = cont_letra
        letra_result = letra_atual
    i += 1
print(f" apareceu mais vezes foi {letra_atual}")
   