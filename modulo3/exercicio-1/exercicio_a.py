import json

CAMINHO = 'exe_1.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('joao victor', 24)
p2 = Pessoa('luanainha', 36)
p3 = Pessoa('mariana', 15)
lista = [vars(p1), vars(p2), vars(p3)]

def salvar():
    with open(CAMINHO, 'w', encoding='UTF8') as arq:
        json.dump(lista, arq, indent=2)
# Só executa a função se o módulo for o 
# principal = "__MAIN__"
# UM MÒDULO È CONSIDERADO __MAIN__ QUANDO
# È EXECUTADO DIRETAMENTE
if __name__ == '__main__':
    print('Olá, eu sou o __MAIN__')
    salvar()