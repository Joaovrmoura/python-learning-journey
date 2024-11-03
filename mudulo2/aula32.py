#problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1= adiciona_clientes('joao')
adiciona_clientes('victor', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('maria')
adiciona_clientes('vitoria', cliente2)
print(cliente2)