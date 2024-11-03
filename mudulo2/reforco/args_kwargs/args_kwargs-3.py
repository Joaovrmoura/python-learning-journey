# Exercício 3: Combinação d *args e **kwargs
# Crie uma função chamada descrever_pessoa
# que aceite um número variável de atributos
# (como nome, idade e ocupação) usando *args
# e informações adicionais sobre a 
# pessoa (como cidade e estado) 
# usando **kwargs. 
# A função deve exibir uma descrição 
# completa da pessoa.
# Teste a função passando uma 
# lista de atributos como 
# ('João', 30, 'Engenheiro') e informações
# adicionais como cidade='São Paulo',
# estado='SP' e mostre a descrição 
# formatada.

def descrever_pessoa(*args, **kwargs):
    print("Sobre:")
    for n in args:
        print(n)
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

nome = input("Digite seu nome: ")
idade = input("Digite sua Idade: ")
ocupacao = input("Digite sua Ocupção: ")
estado = input("Digite seu Estado: ")
cidade = input("Digite sua Cidade: ")

descrever_pessoa(nome, idade, ocupacao, cidade=cidade, estado=estado)