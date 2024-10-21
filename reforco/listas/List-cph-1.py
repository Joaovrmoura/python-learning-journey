# Exercício 1: 
# List Comprehension Simples
# Crie uma lista que contém os 
# quadrados dos números pares de 0 a 20 
# usando list comprehension. 
# Como você faria isso e
# qual seria a saída esperada?

#numero x 2 aqui(for range até 20) SE numero for par executa o numero x 2
lista_num = [numeros * numeros for numeros in range(21) if numeros %2 == 0]
print(lista_num)