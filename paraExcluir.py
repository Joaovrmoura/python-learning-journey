lista = []

while True:

    action = input("[a]adicionar [d]deletear [l] listar: ")
    
    if action == 'a':
        pd = input("adicionar o produto :")
        lista.append(pd)

    elif action == 'd':
        pd = int(input("apagar: "))
        lista.pop(pd)

    elif action == 'l':
        print("Sua lista de produtos")
        for i, p in enumerate(lista):
            print(f"{i}: {p}")
