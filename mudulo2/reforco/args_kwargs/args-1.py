# Crie uma função chamada produto_numeros que receba um número 
# variável de argumentos usando *args e retorne o produto 
# de todos os números fornecidos (multiplicação de todos
# os argumentos). Se nenhum número for fornecido, a
# função deve retornar 1.

def produto_numeros(*args):
    produto = 1
    for n in args:
        produto *= n
    return produto

print(produto_numeros(5, 25))
print(produto_numeros())