#faça uma entrada de dados aonde o usuario adicionara itens a uma lista
#os itens devem ter cada um seu indice começando do 0
#o usuario poderá apagar e listar os itens e voltar a adicionar de forma dinâmica
lista = []

while True:
    acao = input("Escolha uma ação [d]deletar [a]adicionar [l]listar itens ou [x] para sair: ").lower()
    print(acao)
    if acao == "a":
        adicionar = input("Adicione um item a lista: ")
        lista.append(adicionar)
    
    if acao == "d":
        for i, item in enumerate(lista):
            print(f"{i}): {item}")
        deletar = input("Qual desses itens deseja deletar? apague o item de acordo com o indice: ")  
        int_deletar = None
        if deletar.isdigit():
            int_deletar = int(deletar)
            if int_deletar is not None:
                del lista[int_deletar]
                print("Nova lista")
                for i, item in enumerate(lista):
                    print(f"{i}): {item}")
        else:
            print("Digite um numero válido")
            
    if acao == "l":
        for i, item in enumerate(lista):
            print(f"{i}): {item}")
            
    if acao == "x":
        break
    # for i, item in enumerate(lista):
    #     print(i, item)