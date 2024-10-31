# Função de fábrica que cria funções (decoradores)
def fabrica_de_funcoes(func):
    # print('parou aqui PQ não executei o decorador OU')
    # Definindo uma função interna que irá substituir a função original
    def copia_funcao(*args, **kwargs):
        # print('Se chegou aqui, executei o decorador que passou a ser minha função interna')
        # A função original (substituída) é chamada com os mesmos argumentos fornecidos
        funcao_copiada = func(*args, **kwargs)
        return funcao_copiada 
    
    return copia_funcao  

# Função de fábrica de decoradores, que retorna o decorador 'fabrica_de_funcoes'
def fabrica_de_decoradores(a, b, c):
    print(a, b, c) 
    return fabrica_de_funcoes  # Retorna a função que irá agir como decorador

# Decorando a função 'soma' com 'fabrica_de_decoradores', passando 1, 2 e 3 como parâmetros
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y  

print(soma(90, 20)) 

#outra forma de fazer MAIS UTILIZADA
print('função 1')
print()
print('função 2')

# Função fábrica de decoradores, que recebe três parâmetros opcionais (a, b, c)
# Esses parâmetros podem ser usados para personalizar o comportamento do decorador, se necessário.
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        # Definindo uma função interna (copia_funcao) que irá substituir a função original (func)
        def copia_funcao(*args, **kwargs):
            # A função decorada é chamada com os argumentos originais
            funcao_copiada = func(*args, **kwargs)
            # O resultado da função original é retornado
            return funcao_copiada
        # irá substituir a função original
        return copia_funcao
    
    return fabrica_de_funcoes


# O decorador funciona normalmente, pois 'fabrica_de_decoradores()' retorna 'fabrica_de_funcoes'
@fabrica_de_decoradores()
def soma(x, y):
    return x + y  

# 'multiplica' é a versão decorada da função lambda, onde o decorador foi aplicado
multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

mult = multiplica(5, 20)
print(mult)  
print(soma(90, 20)) 