# Exercício - Salvar Lista de tarefas com desfazer e refazer
# em um arquivo json
import json

def print_l(lista):
    if not lista:
        print('Nehuma tarefa para listar')
        return
    print()
    print('Tarefas: ')
    for i, item in enumerate(lista):
        print(f"\t{item}")
    print()
   

def add(lista, tarefa):
    if not tarefa.split():
        print('Digite um Tarefa')
        return
    else:
        lista.append(tarefa)
        print_l(lista)

def desfazer(lista, desfazer):
    if not lista:
        print('Nada para Desfazer')
        return
    if len(lista) > 0: 
        desfeito = lista.pop()
        desfazer.append(desfeito)

def refazer(lista, refazer):
    if not refazer:
        print("Nada para Refazer")
        return
    if len(refazer) > 0:
        removido = refazer.pop(0)
        lista.append(removido)
        print_l(lista)

CAMINHO_ARQ = 'exercicio9.json'

def ler(lista, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arq2:
            dados = json.load(arq2) 
    except FileNotFoundError:
        print('Arquivo Não existe')
        salvar()
    return dados

def salvar(caminho, lista):
    with open(caminho, 'w', encoding='UTF8') as arq:
        json.dump(lista, arq, indent=2)

lista_original = ler([], CAMINHO_ARQ)
lista_removidos = []

while True:
    action = input("""Comandos: Listar, Desfazer, Refazer
Digite uma tarefa ou comando: """).lower()
    
    # Transformou o if em um dicionario
    comandos = {
        'listar' : lambda : print_l(lista_original),
        'desfazer' : lambda: desfazer(lista_original, lista_removidos),
        'refazer' : lambda : refazer(lista_original, lista_removidos),
        'adicionar' : lambda : add(lista_original, action)
    }
    
    fazer = comandos.get(action) if comandos.get(action) is not None else comandos['adicionar']
    fazer()
    
    salvar(CAMINHO_ARQ, lista_original)

    if action == 'x':
        break
