#Nesta seção, o código implementa um jogo 
#de adivinhação onde o usuário tenta adivinhar uma palavra secreta.
# O código solicita repetidamente que o usuário insira uma letra 
# e verifica se essa letra está na palavra secreta.
# O usuário tem um número limitado de tentativas para adivinhar 
# a palavra secreta.
# Se o usuário adivinhar corretamente a palavra,o jogo é encerrado 
# e uma mensagem de vitória é exibida.



palavra_secreta = "feijoada"
chances = len(palavra_secreta)
letra_adivinhada = ""

while chances > 1:
    letra = input("Digite a letra e adivinhe a palavra: ")
    print(chances)
    
    for n in range(len(palavra_secreta)):
        if letra in palavra_secreta[n]:
            letra_adivinhada += palavra_secreta[n]
            print(letra_adivinhada)
        else:
            letra_adivinhada += "#"
    print(letra_adivinhada)
    chances -= 1
    
print("voce não ganhou")