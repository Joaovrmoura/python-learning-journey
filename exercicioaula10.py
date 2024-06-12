
lista = []

while True:
    
    adicionar_item = input("[a]adicionar [d]deletar [l]listar: ")

    if adicionar_item == 'a':
        item_lista = input("listar item ")
        lista.append(item_lista)
    
    elif adicionar_item == 'l':
        if len(lista) <= 0:
            print("nada para listar")
        for indice, item in enumerate(lista):
            print(f"{indice}: {item}")

    elif adicionar_item == 'd':
        try:
            indice_item = input("item para apagar da lista ")
            indice_item = int(indice_item)
            if indice_item < 0 or len(lista) <= 0:
                print("item não existe ")
            else:
                del lista[indice_item]
        except:
            print("digite um numero válido ")
    elif adicionar_item == 's':
        break
    else:
        print("Digite uma letra válida ")




