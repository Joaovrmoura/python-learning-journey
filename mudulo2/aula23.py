from itertools import count

# Cria um iterador infinito que começa em 10 e incrementa de 8 em 8.
c1 = count(start=10, step=8)  
# Cria um objeto `range` que gera números de 10 a 100 (inclusive), com passos de 10.
r1 = range(10, 101, 10)      


# Verifica se `c1` é iterável (contém o método `__iter__`).
print('c1', hasattr(c1, '__iter__'))  
# Verifica se `c1` é um iterador (contém o método `__next__`).
print('c1', hasattr(c1, '__next__')) 
# Verifica se `r1` é iterável (contém o método `__iter__`).
print('r1', hasattr(r1, '__iter__'))
# Verifica se `r1` é um iterador (contém o método `__next__`).  
print('r1', hasattr(r1, '__next__'))  

print()
print('Count')

for n in c1:
    if n > 100:
        break
    print(n)

print()
print('range')
for n in r1:
    print(n)


