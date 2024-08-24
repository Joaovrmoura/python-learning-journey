#set em python, não garante a ordem dos elementos dentro dele
# set são iteraveis e podem receber valores de varios tipos separador por virgulas
#porém não recebem valores mutaveis dentro deles listas dicionarios e set
#set não possui índexes

s1 = {1, 2, 3}
s2 = {2, 3, 4}
# Operadores para o set # (union) | unir dois itens
s3 = s1 | s2
print(s3)
# intersection & retorno os itens presente em ambas as listas
s3 = s1 & s2
print(s3)
# Sinal '-'(sinal de menos) retorna a diferença presente(que só existe) no item da esquerda
s3 = s1 - s2
print(s3)
#Sinal ^ retorna a diferença presente nos dois itens(os itens do primeiro que não tem no segundo e vice-versa)
s3 = s1 ^ s2
print(s3)
print('\n')


#set vazio
s1 = set()
#set com dados
s1 = {'joao', 1, 2, 3}
#utilidade remover valores duplicados-
l1 = {1,2,3,3,3,2,3,1,2}
print(l1)
#podemos usar in not in e for para buscar algo dentro de set
# metodo add
l2 = set()
l2.add('joao')
#podemos também utilizar o update como em dicionarios
#aqui enviamos uma tupla, pois strings são 'fatiadas'
l2.update(("victor", 21))
#discard discarta o valor passado como parâmentro para função
l2.discard(21)
print(l2, '\n')

#exemplos de uso de set
letras = set()

while True:
    digito = input("Digite uma letra: ")
    letras.add(digito.lower())
    if 'l' in letras:
        print("Você ganhou!")
        break
    