#dir hasattr getattr em python
# pegar um método do python com um nome 
# atribuido fora da variavel

"""A função hasattr() no Python é usada para verificar se um objeto
possui um atributo específico. Essa verificação é útil em situações 
onde não temos certeza se determinado objeto possui uma função ou 
atributo, permitindo que o código trate casos específicos de acordo 
com a presença ou ausência desse atributo.
"""
nome = 'joaoola'
metodo = 'lower'

if hasattr(nome, metodo):
    print('existe método')
    print(getattr(nome, metodo)())
else:
    print('Não existe o método')

#Generator expression, iterables iterators em python
itarable = ['eu', 'tenho', '__iter__']

iterator = itarable.__iter__() #__iter__ e __next__


print()
print('Trecho fora do curso')

class Carro:
    def dirigir(self):
        print("O carro está em movimento.")
carro = Carro()

if hasattr(carro, 'dirigir'):
    carro.dirigir()

def processar(obj):
    if hasattr(obj, 'iniciar'):
        obj.iniciar()
    else:
        print("Método 'iniciar' não encontrado.")

# Suponha que temos uma lista de objetos variados
objetos = [Carro(), str(), int()]

for objeto in objetos:
    processar(objeto)

