numero = input("Digite um numero: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0 :
        print(f"Voce digitou {numero} ele é par")
    else:
        print(f"Esse número é ímpar")
else:    
    print("Você digitou uma String ou não é um número inteiro ")



hora = input("Digite o horario: ")
try:
    hora = int(hora)
    if hora > 0 and hora < 12:
        print(f"Bom dia são {hora:.2f} ")
    elif hora > 11 and hora <= 17:
        print(f"boa tarde são {hora:.2f}  ")
    elif hora >= 18 and hora <= 23:
        print(f"Boa noite são {hora:.2f} ")
    else:
        print(f"Não digitou uma hora conhecida ")
except:
    print("Não digitou uma hora válida")



nome = input("Digite o seu nome: ")

if len(nome) < 1:
    print("Digite pelo menos uma letra ")
else:
    if len(nome) <= 4 and len(nome) >= 0:
        print(f"Seu nome é {nome} e tem {len(nome)} letras (curto)")
    elif len(nome) >= 5 and len(nome) <= 6:
        print(f"Seu nome é {nome} e tem {len(nome)} letras (medio)")
    elif len(nome) > 6:
        print(f"Seu nome é {nome} e tem {len(nome)} letras(maior)")
    else:
        print("nome inválido")

