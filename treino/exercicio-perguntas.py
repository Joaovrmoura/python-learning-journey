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
acertos = 0


for n, value in enumerate(perguntas):
    todas_perguntas = perguntas[n]
    pergunta = todas_perguntas['Pergunta']
    op = todas_perguntas['Opções']
    qtd_op = len(op)
    r = todas_perguntas['Resposta']
    r = int(r)
    
    print(pergunta)
    for chave, valor in enumerate(op):
        print(f"{chave}) {valor}")
        valor = int(valor)
        if valor == r:
            resposta_correta = chave         
    escolha = input("Digite a resposta: ") 
    escolha_int = None
    
    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int <= 4:
            if escolha_int == resposta_correta:
                acertos += 1
                print("Acertou miserável😎")
            else:
                print("Você é um lixo🤮 PFVR NÂO Tente Novamente")
        else:    
            print(f"Você perdeu a perunta pois digitou {escolha} que é uma opção inválida!") 
    else:
        print(f"Você perdeu a perunta pois digitou {escolha} que é uma opção inválida!")   
        
print(f"Você acertou: {acertos} de 3")
    


