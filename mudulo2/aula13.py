#Generetor functions funções que pausam ao invés de pausar
#toda função que tem um yield é uma generetor function
def generetor(n=0):
    yield 1 #pausa a função
    print("continua ate o proximo next da função...")
    yield 2
    print("só mais um")
    yield 3
    return 'finalmente acabou'

# Generator tem o método __ITER__ e __NEXT__ dentro dele
#para ele entregar o valor se utiliza o método next()
gen = generetor(n=0)
print(next(gen))
#continua onde parou o primeiro next que foi = yield 1
# vai até o próximo e assim suscetivamente
print(next(gen))
#yiled 2 para yield 3
print(next(gen))
#como ele é iterável podemos utilizar o for
for n in gen:
    print(n)
    
print()
def loop(n=0, maximum=10):
    while True:
        yield n
        n += 1
        
        if n >= maximum:
            return 
loops = loop(maximum=15)
for n in loops:
    print(n)
    
    
    

print()
print()
# podemos utilizar o yield from para escolher onde o proximo yield deve começar
def gen1():
    yield 1
    yield 2
    yield 3
    print('ACABOU O GEN 1')
def gen3():
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN 3')
    # começa o proximo yield da ultima vez que foi iterado
def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU O GEN 2')
g1 = gen2(gen1)
g2 = gen2(gen3)

for n in g1:
    print(n)
for n in g2:
    print(n)

def fib(limite):
    a, b = 0, 1
    while a <= limite:
        yield a
        a,b = b, a + b
        
fibon = fib(10)
for fibo in fibon:
    print(fibo)
    print("acabou fib")