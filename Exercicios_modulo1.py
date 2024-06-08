#variáveis
nome = 'joao21'
idade = 5 + 5
print(idade + idade,'\n' + nome)

nomes = 'joao'
idades = 25
data_nasimento = 25-10-2000

print(nomes, idades, data_nasimento)

if idades > 18:
    print("é maior de idade")
else:
    print("é menor de idade")


 
# Exercício
# Nesta seção, o usuário é solicitado a inserir seu nome e idade.
# O código verifica se ambos os campos foram preenchidos e se a idade é um número.
# Em seguida, são realizadas diversas operações com o nome inserido pelo usuário, 
# incluindo inversão, contagem de letras, etc.

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade:
    print('Não digitou nada')
else:
    if idade.isnumeric: 
        print(f'Seu nome é {nome}')
        print(f'Seu nome invertido é {nome[::-1]}')

        if ' ' in nome:
            print(f'seu nome {nome} tem espaços')
        else:
            print(f'seu nome {nome} não contém tem espaços')

        print(f'seu nome tem', len(nome), 'letras')
        print(f'seu nome {nome}, a primeira letra é {nome[0]}')
        print(f'seu nome {nome}, e a ultima letra é {nome[-1:]}')
    else:
        print("Digite um número na idade ")



nome = input("digite seu nome : ")
cont = 0
novo_nome = ''
while cont < len(nome):
    letra = '*' + nome[cont] + ''
    novo_nome += letra
    cont += 1
novo_nome += '*'
print(novo_nome)






while True:
    
    try:
        num_1 = input("digite um numero ")
        num_2 = input("digite outro numero ")
        num_1 = float(num_1)
        num_2 = float(num_2)

        operador = input("digite o sinal de operação ")
        operador_pass = '*-+/'

        if operador in operador_pass and len(operador) < 2:
            if operador == '/':            
                print( num_1 / num_2)
            elif operador == '-': 
                print(num_1 - num_2)
            elif operador == '+':
                print(num_1 + num_2)
            elif operador == '*':
                print(num_1 * num_2)
    except Exception as error:
        print(error)
#startswitch pega a primerira letra e retorno se ela for igual = Boolean true
    sair = input("Quer sair [s] ou [n] ? ").lower().startswith('s')
    if sair is True:
        break
     


#Nesta seção, o código implementa um jogo 
#de adivinhação onde o usuário tenta adivinhar uma palavra secreta.
# O código solicita repetidamente que o usuário insira uma letra 
# e verifica se essa letra está na palavra secreta.
# O usuário tem um número limitado de tentativas para adivinhar a palavra secreta.
# Se o usuário adivinhar corretamente a palavra, o jogo é encerrado 
# e uma mensagem de vitória é exibida.

palavra_secreta = 'bolo'
letras_acertadas = ''
chance = 0

while chance < 5:
    chance += 1
    letra_digitada = input("digite uma letra e tente advinhar a palavra ")
    
    if len(letra_digitada) < 1:       
        print("digite apenas uma letra ")
        continue
    #for percorre cada item dentro do objeto
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_inteira = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_inteira += letra_secreta
    else:
        palavra_inteira +='*'
    print(palavra_inteira)

    if palavra_inteira == palavra_secreta:
        print("voce ganhou")
        break
    
   