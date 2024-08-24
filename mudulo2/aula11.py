#Dictionary comprehension e Set Comprehension

produto = {
    'nome' : 'joao',
    'idade' : 21,
    'formacao' : 'ens. medio'
}

#Dictionary comprehension
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'idade'
}

lista = [
    ('a', 'b'),
    ('c', 'd'),
    ('h', 'j')
]
print(dict(lista))
print(dc)

lista2 = ['a', 22, True, {22}, ['arroz', 'feijao'], {'joao' : 8}, (8, 2)]

for item in lista2:
    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set))

    if isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    if isinstance(item, str):
        print('STR')
        print(item.upper(), isinstance(item, str))


print()
print()
print()

# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy'if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))