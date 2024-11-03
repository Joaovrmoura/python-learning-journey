# Exercício - sistema de perguntas e respostas
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


cont_acertos = 0
for n in perguntas:
    print(n['Pergunta'])
    for p, pergunta in enumerate(n['Opções']):
        print(f"{p}) {pergunta}")
    resposta = input("Digite a resposta: ")
    
    if resposta.isdigit():
        resposta = int(resposta)
        if 0 <= resposta < len(n['Opções']):
            print("Bobão Não escolheu direito e perdeu uma chance!🤧") 
        else:
            if n['Opções'][resposta] == n['Resposta']:
                print("ACERTOU MIRESAVEL😎")
                cont_acertos += 1
            else:
                print("Burrão Mané🤣")
    else:
         print("Bobão Não escolheu um número e perdeu uma chance!🤧")
            
print(f"Você acertou {cont_acertos} de 3")