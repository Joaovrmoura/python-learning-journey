#Funções em python recebem parâmetros
#cada parâmetro deve recebe seu valor na chamada da função
def Printar(a, b, c):
    print("ola")
    print("mundo") 
    print("ola mundo")

Printar(1, 2, 3)

#aqui o parâmetro funciona como uma variável
#quando eu não passo um valor ao chamar a função ele retorna o valor
#que passei dentro do parâmetro
def nomear(nome= "sem nome"):
    print(f"ola, {nome}")
# sem parâmetro
nomear()
#com parâmetro
nomear("mundo")

def soma(x, y):
    print(x + y)

print(soma(5, 10))
soma(5, 10)
#quando chamamos uma função todos os parâmetros tem que ser declarados "usados"
#dentro dos parênteses
#após nomear uma funçao fora da declaração inicial caso mude o valor da variavel
#todos os valores seguintes devem ser alterados por convênção
