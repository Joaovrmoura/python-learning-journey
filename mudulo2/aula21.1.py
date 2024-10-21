def decoradora(func):
    print('parou aqui PQ não executei o decorador OU')
    def interna(*args, **kwargs):
        print('Se chegou aqui, executei o decorador que passou a ser minha função interna')
        # result = funcao_substituida(funçao, argumentos da função)
        result = func(*args, **kwargs)
        return result 
    return interna


# assim que utilizamos o decorador o python
# passa a função para dentro da função decoradora
@decoradora  
def soma(x, y):
    return x + y

print(soma(90, 20))

