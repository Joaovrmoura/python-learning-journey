# Exercício 2: Exibição de Informações
# Crie uma função chamada exibir_informacoes
# que aceite um número variável de 
# argumentos nomeados usando **kwargs. 
# A função deve imprimir cada chave e valor
# fornecidos. 
# Teste a função passando diferentes 
# informações como 
# nome, idade e cidade (por exemplo, nome='João', 
# idade=30, cidade='São Paulo')
# e exiba as informações formatadas.

#em funções recebem varios argumentos nomeados
def exibir_informacoes(*args, **kwargs):
    if args:
        print("Obs:", args)
    for chave, valor in kwargs.items():
        print(f"{chave} {valor}")
  
for n in range(2):      
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite o nome da sua cidade: ")
    exibir_informacoes(nome=nome, idade=idade, cidade=cidade)
    