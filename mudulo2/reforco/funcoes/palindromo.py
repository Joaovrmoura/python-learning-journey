# 2. Função para Verificar Palíndromo
# Escreva uma função chamada eh_palindromo que receba uma string e verifique se ela é um palíndromo
# (lê-se da mesma forma de trás para frente, ignorando espaços e letras maiúsculas/minúsculas).

def eh_palindromo(palavra):
    if palavra.isdigit():
        print('Saporra é número')
    else:
        palavra_limpa = ','.join(palavra.split()).lower()
        palavra_invertida = palavra_limpa[::-1]

        if palavra_limpa == palavra_invertida:
            return True
        else:
            return False

palavra = input("Digite a palavra e verifique se é palindromo: ")
palavra_limpa = ''.join(palavra.split()).lower()
print(palavra_limpa)
print()
if eh_palindromo(palavra):
    print('Saporra é palindromo!')
else:
    print(f"saporra aqui não é palindromo=> {palavra}" )
