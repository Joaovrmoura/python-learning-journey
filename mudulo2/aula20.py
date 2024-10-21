def fora(x):
    # A variável 'a' é uma variável livre, 
    # pois não está definida dentro da função 'dentro'
    # Ela é atribuída ao valor de 'x'
    a = x
    # Função interna, que acessa a 
    # variável 'a' do escopo da função 'fora'
    def dentro():
        #locals mostra a variavel dentro da funçao
        print(locals())
        print(dentro.__code__.co_freevars)
        # Retorna o valor de 'a', que é 
        # "lembrado" mesmo após a execução da função 'fora'
        return a
    # Retorna a função 'dentro', criando um fechamento (closure)
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())  
print(dentro2())  # Saída: 20

print()


# NONLOCAL
# com o nonlocal o python busca o valor da variavel
# no escopo acima onde a variavel esta definida
def concatenar(string_inicial):
    # para dizer que a variavel não é local e poder "utilizala"
    # em outros escopos mais internos utilizamos nonlocal
    valor_final = string_inicial
    def interna(valor_a_concatenar):
        # agora podemos reescrever valores
        # de fora do escopo da função
        nonlocal valor_final
        # UnboundLocalError só podemos ler valores fora do escopo
        # da função, não podemos altrar seu valor
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
