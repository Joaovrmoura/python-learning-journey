# Exercício
# Nesta seção, o usuário é solicitado a inserir seu nome e idade.
# O código verifica se ambos os campos foram preenchidos e se a idade é um número.
# Em seguida, são realizadas diversas operações com o nome inserido pelo usuário, 
# incluindo inversão, contagem de letras, etc.

nome_r = []
nome = input("Digite a porra do nome: ")
idade = input("Insira a porra da idade: ")
idade = int(idade)
nome_r.append(nome)

if isinstance(idade, int):
    print("é numerico")


for indice, letras in enumerate(nome_r):
    print(letras[indice])

print(f"{"nome invertido", nome[::-1]}")  
print(nome)
print(idade)