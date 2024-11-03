# Exercício 3: 
# Aninhamento de List Comprehension
# Crie uma lista de listas utilizando 
# list comprehension, onde a lista 
# externa deve conter três listas, e 
# cada lista interna deve conter os 
# números de 0 a 4. Como você 
# estruturaria essa lista e qual 
# seria a saída esperada?

# Executa a primeira regra depois faz oque a segunda pede
lista_aninhada = [[n for n in range(5)] for x in range(3)]
print(lista_aninhada)