preco = 1500
nome = 'abacate'
#interpolação
resumo_produto = '%s tem o preco de %.2f' % (nome, preco)
print(resumo_produto)

variavel = 'ABC'
print(f'{variavel:>4}')
print(f'{variavel:e^20}')
print(f'{1000.55554151651:.2f}')
print(f'{1000.55554151651:0=+10,.1f}')

#FATIAMENTO DE STRINGS
liste = ['o', 'la', 'mundo', 'ola', 'joao', 'carlos']
#[:2] pulando o valor 0 a lista começara 1 e listar tudo dentro do valor do indice
print(f'{liste[:4]} eee')
# [inicia do indice digitado : e não mostra o próximo indice]
print(f'{liste[2:3]} jj')
#pega toda a lista
print(f'{liste[::]} toda lista')
#inicia do zero e só pega 3 elementos e lista pega 0 e 2 no exemplo [0:3:2]
print(f'{liste[0:4:3]}')



var = "ola mundo"
#inverte a lista
print(f'{var[::-1]}')
#contar número de strings
print(len(var))

#exercicio
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if not nome or not idade:
    print('Não digitou nada')
else:
    if idade.isnumeric: 
        print(f'Seu nome é {nome}')
        print(f'Seu nome invertido é {nome[::-1]}')

        if ' ' in nome:
            print(f'seu nome {nome} tem espaços')
        else:
            print(f'seu nome {nome} não contém tem espaços')

        print(f'seu nome tem', len(nome), 'letras')
        print(f'seu nome {nome}, a primeira letra é {nome[0]}')
        print(f'seu nome {nome}, e a ultima letra é {nome[-1:]}')
    else:
        print("Digite um número na idade ")
    