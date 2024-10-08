#ainda sobre a função lamda
def multiplicador(num_multiplcador):
    def multiplica(numero):
        return numero * num_multiplcador
    return multiplica

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y
#diferentes formas de executar uma função
print(
    executa(
        lambda x, y: x + y, 2, 3
    ),
    executa(soma, 5, 2)
)
# desempacotamento e empacotamento de dicionários
a, b = 1,2
b, a = a, b
#troca do valor de variável sem terceira variável
print(a, b)
pessoa = {
    'nome':'joao',
    'sobrenome': 'rodirgues',
}
a, b = pessoa.values()
print(a, b)
print()
# a, b = pessoa.items()
# print(a, b)
#desempacotando o dicionário
dados = {
    'cpf': 42454,
    'idade': '22',
}
#para criar juntar um dicionario dentro do outro podemos utilizar '**'dentro de um terceiro
#dicionario
terceiro = {**pessoa, **dados}
print(terceiro)
print()

(a1, a2), b = pessoa.items()
print(a1, a2)
print(b)
print()

#Kwargs serve para o empacotamento de dicionarios
#em funções recebem varios argumentos nomeados
def mostrar_dicionarios(*args, **kwargs):
#caso use algum argumento não nomeado(args) deve ser utilizado o args para especificar
    print('não nomeados', args)
    for chave, valor in kwargs.items():
        print(chave, valor)
#valor não nomeado 13,2 - nomeados 'joao', 'qlqr'
mostrar_dicionarios(13, 2, nome='joao', qlqr=123)
print()
#com um dicionario inteiro
mostrar_dicionarios(terceiro)