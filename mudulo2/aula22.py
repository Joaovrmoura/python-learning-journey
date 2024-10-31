def parametros_decorador(nome):
    def decorador(func):
        print('decorador:', nome)
        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res}, {nome}'
            return final
        return sua_nova_funcao
    return decorador

#Ordem de execução dos decoradores em python "DE BAIXO PARA CIMA!"
@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y  

s = soma(5, 984)
print(s)