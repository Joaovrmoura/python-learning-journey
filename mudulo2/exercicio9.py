# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os

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


lista_original = []
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

    if action == 'x':
        break

    # if action == 'clear':
    #     os.system('clear')
    #     continue

    # if action == 'listar':
    #     print_l(lista_original)
            
    # elif action == 'desfazer':
    #     desfazer(lista_original, lista_removidos)

    # elif action == 'refazer':
    #     refazer(lista_original, lista_removidos)
    # else:
    #     add(lista_original, action)