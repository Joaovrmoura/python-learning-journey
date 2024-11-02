# Variáveis globais e escopo de funções
# variaveis só podem ser alteradas dentro da sua própria função
#caso seja criada dentro de uma função uma variavel com mesmo nome de outra do lado de fora,
#ela "vira" outra variavel diferente 
# e só pode ser alterada dentro da função 

x = 285

def valor():

    x = 20

    def outro_valor():
        x = 50
        y = 32
        print(x, y)

    print(x)

    outro_valor()


#É impossível acessar funções que estão dentro de outras
valor()
print(x)


#retorno das funções 
# a palavra RETURN que é utilizada somente em métodos ou funções 
# para o script e retorno o valor da função
# utilizamos o return para receber valores em variáveis pois
# funções dentro do python sem return devolvem o valor None


def mostrar_return():
    b = 50
    return b
  
exemplo = 5 * mostrar_return()

print(exemplo)

# *args em python permite que uma função receba um numero indeterminado de valores
# no final da execuão *args retorna um tupla

def mostrar_args(*args):
    numeros = 0
    for numero in args:
        numeros += numero
    print(numeros)

mostrar_args(1,2,3,4,5,6)

# jogando em uma variável
def mostrar_args2(*args):
    numeros = 0
    for numero in args:
        numeros += numero
    return numeros

total = mostrar_args2(1,2,3,4,5,6)
print(f"\n{total} com a função return")

