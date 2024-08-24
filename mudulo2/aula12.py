#dir hasattr getattr em python
#pegar um método do python com um nome atribuido fora da variavel

nome = 'joaoola'
metodo = 'strip'

if hasattr(nome, metodo):
    print('existe método')
    print(getattr(nome, metodo)())
else:
    print('Não existe o método')

#Generator expression, iterables iterators em python
itarable = ['eu', 'tenho', '__iter__']

iterator = itarable.__iter__() #__iter__ e __next__