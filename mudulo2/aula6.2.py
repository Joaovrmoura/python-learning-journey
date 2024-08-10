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

#adiciona itens ao dicionario
print(pessoa.update(email='joao@'))
#adicionar tuplas
tupla = ('nome', 'novo valor'),
#ou com tuplas dentro de tuplas
tuplas = (('nome', 'valor_novo'), ('idade', 23))
listas = (['nome', 'valor_novo'], ['idade', 23])
print(pessoa.update(tuplas))
print(pessoa.update(listas))
print(pessoa)



print(pessoa.get('email', 'não retornou nada'))
print(pessoa.setdefault('email'))
#apaga o item adicionado
print(pessoa.pop('email'))
print(pessoa.setdefault('email'))
#pop item apaga o ultimo item do dicionario
print(pessoa.popitem())