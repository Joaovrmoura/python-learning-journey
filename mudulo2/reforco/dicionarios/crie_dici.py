lista = []
for n in range(3):
    linha = []
    for n in range(1):
        dicionario = {}
        nome = input(f"Nome do item {n + 1} do dicionario: ")
        valor = input(f"Valor do item {n + 1} do dicionario: " )
        taxa = input(f"Taxa de entrga do item  {n + 1} do dicionario: ")
        dicionario.update(nome=nome, valor=valor, taxa=taxa)
        
    lista.append(dicionario)
    
for indice, itens in enumerate(lista):
    print(f"Nome {itens['nome']}: Valor: {itens['valor']} Taxa: {itens['taxa']}")
            