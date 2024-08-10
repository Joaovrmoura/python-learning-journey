#dict dicionários em python
pessoa = {
    'nome' : 'joao',
    'idade' : 21,
    'estado_civil' : 'solteiro',
    'endereco' : [
        {'rua' : 'rua albertina',
        'cep' : 26455030,
        'estado' : 'Rio de janeiro',
        'cidade' : 'japeri'
        }]
}
for indice, chave in pessoa.items():
    print(f'{indice} {chave}')

for chave in pessoa:
    print(f'{chave}, {pessoa[chave]}')

print('\n')

###manipulando chaves e valores em dicionários
pessoas = {}
chave = 'nome :'
pessoas[chave] = 'joao victor'

#deletar chaves
pessoas['sobrenome :'] = 'rodrigues'
pessoas['idade'] = 21
del pessoas['idade'] 
#deletar chaves

#achar chaves em um dicionários
print(pessoas.get('sobrenome', 'não existe'))
#com if else
if pessoas.get('sobrenome') is not None:
    print(pessoas['sobrenome'])
else:
    print("não existe")

print(pessoas[chave])
print(pessoas)

# List método
print(list(pessoas))
#conta o numero de chaves
print(len(pessoas))
#mostra apenas os valores de suas chaves
print(pessoas.values())
#retorna uma lista com tuplas com indices
print(pessoas.items())
#setdefault retorna uma chave ou adiciona caso não exista
print(pessoas.setdefault('idade', 25))
#nesse caso como não existe ele adicionou
print(pessoas)
for indice, chave in pessoas.items():
    print(f"{indice} {chave}")