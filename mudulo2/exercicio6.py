# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y
 
def multiplica(x, y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

# o numero que vc passar tem que retornar numero_passado + numero_passado passado
soma_com_cinco = criar_funcao(soma, 5)
# o numero que vc passar tem que retornar numero_passado * numero_passado passado
multiplica_por_dez = criar_funcao(multiplica, 10)
