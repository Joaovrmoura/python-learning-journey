# raise - Lançamento de exceções (erros)
def divide(n, d):
    # Não faça isso! Isso vai suprimir o erro, pois você 
    # está apenas printando a mensagem
    # O raise sem argumentos dentro do except relança a
    # mesma exceção que foi capturada
    try:
        return n / d
    except ZeroDivisionError:
        print('__relancei___')
        # O raise relança a exceção original, mantendo a 
        # mensagem e a pilha de execução

# Aqui, como d é 0, ocorrerá uma ZeroDivisionError, 
# mas ela será relançada pelo raise dentro do except
print(divide(8, 0))

print()

def nao_aceito_zero(b):
    # Melhor abordagem: Se o divisor for 0, você lança
    # explicitamente uma exceção com uma mensagem customizada.
    if b == 0:
        raise ZeroDivisionError('tentando dividir por zero') 
        # Aqui, o raise lança uma exceção do tipo 
        # ZeroDivisionError com uma mensagem específica
    #é uma boa adicionar um True caso ela retorn algo
    return True
    
def divide2(a, b):
    # Chama a função para verificar se o divisor é 
    # zero antes de tentar a divisão
    nao_aceito_zero(b)
    # Se b for diferente de 0, a divisão acontece 
    # normalmente
    return a / b

print(divide2(8, 0))
print()
print()

def erro_no_tipo(n, d):
    if not isinstance(n, (float, int)):
        raise TypeError(f"{n} deve ser int ou float")
    if not isinstance(d, (float, int)):
        raise TypeError(f"{d} deve ser int ou float")
    # Neste caso, caso o tipo seja diferente, o programa lançará 
    # a exceção personalizada antes de tentar dividir
    return n / d

def simplificando_a_funcao_acima(n):
    tipo = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float ' 
                         f'você envio tipo {tipo.__name__}')
        #tipo.__name__ retorna o tipo da variavel caso caia na exceção 
    return True
def erro_no_tipo_simplificado(n, d):
    simplificando_a_funcao_acima(n)
    simplificando_a_funcao_acima(d)
    
print(erro_no_tipo_simplificado(7, 's'))

