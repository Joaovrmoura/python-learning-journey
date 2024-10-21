# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from exercicio5_package import produtos
import copy

def showItems(lista):
    for chave, valor in enumerate(lista):
        print(f"Nome do Produto: {valor['nome']} Preco:{valor['preco']:0.02f}")
    
def CopiarLista(lista):
    copia = copy.deepcopy(lista)
    return copia

def novoValor(lista):
    lista_nova = [{'nome': produto['nome'], 'preco': produto['preco'] * 1.1} 
    for produto in CopiarLista(lista)]
    return showItems(lista_nova)


ordem_preco = CopiarLista(produtos)

produto_ordenado_nome = (sorted(CopiarLista(produtos), key=lambda item : item['nome'], reverse=True))
ordem_preco.sort(key=lambda produto : produto['preco'])

print('Lista Original')
showItems(produtos)
print()
print('Produtos 10% mais caros')
novoValor(produtos)
print()
print('Produtos Ordenados por Nome')
showItems(produto_ordenado_nome)
print()
print('Produtos Ordenados por Preço')
showItems(ordem_preco)
print()
print(__name__)

# print(showItems(produto_ordenado_nome))











