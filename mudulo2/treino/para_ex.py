import json


CAMINHO_ARQUIVO = 'text.json'

def print_l(lista):
    for i, indice in enumerate(lista):
        print(indice)

def desfazer(lista_tarefas, lista_removidos):
    if not lista_tarefas:
        return 
    item = lista_tarefas.pop()
    lista_removidos.append(item)
    print_l(lista_removidos)

def adicionar(lista_tarefas, acao):
    if not acao.split():
        print('Escreva algo')
    else:
        lista_tarefas.append(acao)
        print_l(lista_tarefas) 

def refazer(lista_tarefas, lista_removidos):
    if not lista_removidos:
        return 
    item = lista_removidos.pop()
    lista_tarefas.append(item)
    print_l(lista_tarefas)

def json_carregar(lista):
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arq:
        json.dump(lista, arq, indent=2)

def json_ler(caminho, lista):
    with open(caminho, 'r', encoding='utf8') as arq2:
        dados = json.load(arq2)
        for n in dados:
            print(n)

def op():
    lista_tarefas = []
    lista_removidos = []
    while True:
        acao = input("Digite uma tarefa: ")
        tarefas = {
            'listar' : lambda : print_l(lista_tarefas),
            'desfazer' : lambda : desfazer(lista_tarefas, lista_removidos),
            'refazer' : lambda : refazer(lista_tarefas, lista_removidos),
            'add' : lambda : adicionar(lista_tarefas, acao)
        }
        fazer = tarefas.get(acao) if tarefas.get(acao) is not None else tarefas['add']
        fazer()

        json_carregar(lista_tarefas)

        print("Com json: ")
        json_ler(CAMINHO_ARQUIVO, lista_tarefas)
        print("===")

        if acao == 'x':
            break


print()

class Animal:
    def __init__(self, nome, acao):
        self.nome = nome
        self.acao = acao

    def oque_ele_faz(self):
        return f'O {self.nome} {self.acao}'

leao = Animal('leao', 'rugi')
acao = Animal('leao', 'rugi')
lobo = Animal('lobo','uiva')

print(lobo.nome)
print(lobo.oque_ele_faz())
print(leao.oque_ele_faz())