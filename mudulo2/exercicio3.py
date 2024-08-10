# Exercício - sistema de perguntas e respostas
#as perguntas devem ter opções começando do zero
#o usuario deve escolher a resposta certa baseado no indice que contem a resposta
#exemplo
#0) reposta 1
#1) resosta 2
#2) reposta 3 ...
#se acertar retornar acertou || errou se errar
#contar acertos 
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for questions in perguntas:
    print(questions.get('Pergunta'))

    for op, chave in enumerate(questions.get('Opções')):
        print(f'{op}){chave}')

        if questions.get('Resposta') == str(chave):
            resposta_certa = op

    resposta = input("Digite a opção correspondente a reposta certa: ")
    resposta_int = None

    if resposta.isdigit():
        resposta_int = int(resposta)

    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int <= len(questions.get('Opções')):
            if resposta_int == resposta_certa:
                print('Acertou 😎')
            else:
                acertos += 1
                print(f"Resposta errada!🦧")
    else:
         print(f"Digite um numero!🦧")
print(f"Você acertou {acertos} no total de 3 perguntas")









# acertos = 3

# pergunta_1 = perguntas[0]
# pergunta_2 = perguntas[1]
# pergunta_3 = perguntas[2]


# print(f'{pergunta_1.get('Pergunta')} ? ')

# for indice, chave in enumerate(pergunta_1.get('Opções')):
#     print(f'{indice}) {chave}')

# first_question = input(f'resposta ? ')

# if first_question == '2':
#     print(pergunta_1.get('Resposta'))
# else:
#     acertos -= 1
#     print("resposta incorreta")
    

# print(f'{pergunta_2.get('Pergunta')} ? ')

# for indice, chave in enumerate(pergunta_2.get('Opções')):
#     print(f'{indice}) {chave}')

# first_question = input(f'resposta ? ')

# if first_question == '0':
#      print(pergunta_2.get('Resposta'))
# else:
#     acertos -= 1
#     print("resposta incorreta")


# print(f'{pergunta_3.get('Pergunta')} ? ')

# for indice, chave in enumerate(pergunta_3.get('Opções')):
#     print(f'{indice}) {chave}')

# first_question = input(f'resposta ? ')

# if first_question == '1':
#      print(pergunta_3.get('Resposta'))
# else:
#     acertos -= 1
#     print("resposta incorreta")
    
# print(f"Você acertou {acertos} de 3")


 


##for indice, chave in enumerate(pergunta_2.get('Opções')):
    #print(f'{indice}) {chave}')

#for indice, chave in enumerate(pergunta_3.get('Opções')):
    #print(f'{indice}) {chave}')
