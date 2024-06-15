contatos = {
    "joao1@gmail.com" : {"nome1": "joao", "telefone" : "769757757", "cep" : "26454541"},
    "joao54@gmail.com" : {"nome": "Victor", "telefone" : "76975757", "cep" : "26454431"},
    "joaao78@gmail.com" : {"nome": "Morcos", "telefone" : "769354474", "cep" : "26474031"},
    "josao178@gmail.com" : {"nome": "claudio", "telefone" : "76454547", "cep" : "22555031"},
    "joao5dsfsd4@gmail.com" : {"nome": "Victsaor", "telsaefone" : "769744757", "cep" : "26456631"},
}

#copy, copiar o dicionario assim criando um novo id
copy = contatos.copy()
#items retorna uma lista uma lista de tuplas
print(f"{contatos.items()} \n")
#método get{} retorna o valor da chave inserida
print(f"{contatos.get("joao1@gmail.com", {})}")
#keys retorna apenas as chaves de um dicionario
print(f"\n {contatos.keys()} \n")
#pop remove e retona o valor removido da chave dentro do argumento
print(f" {contatos.pop("joao1@gmail.com")} \n")
#caso não exista a chave para remoção adicionamos , "não encontrado"
print(f" {contatos.pop("joao1@gmail.com", "não encontrado")} \n")
#popitem remove os itens da lista em ordem começando do primeiro
print(f"{contatos.popitem()} \n")


exemplo_setdefalut = {"joao@gmail.com" : {"Nome" : "joao", "telefone" : "7854656"}}
#setdefault caso o atributo não estiver no dicionário ele adiciona o valor que 
#Você instanciou, caso o contrário retorna o valor do dicionario
exemplo_setdefalut.setdefault("Nome", "joao")
#caso ele não encontre a chave ele adiciona a chave + valor no final da lista
print(exemplo_setdefalut)
#update troca e adiciona itens de um dicionario,
#caso a chave exista e o valor ela troca o valor do dicionario pelo novo valor exemplo
exemplo_setdefalut.update({"joao@gmail.com": {"Nome" : "cilas"}})
print(f"\n {exemplo_setdefalut}")
exemplo_setdefalut.update({"joao@gmail.com": {"telefone" : "745764756"}})
print(f"\n {exemplo_setdefalut}")
#values retorna os dicionarios sem o valor das chaves
print(f" \n {contatos.values()}")
# "in" método para saber se existe determinado valor dentro da chave
#retorna true or false
result = "joao@gmail.com" in exemplo_setdefalut
print(f"\n {result}")
result = "joao@gmail.co" in exemplo_setdefalut
print(result)
#del recebe deleta o objeto que eu quero remover
# dois exemplos de como podemos remover
#aqui removo uma chave dentro de outra 
del contatos[ "joaao78@gmail.com"]["cep"]
print(f"\n {contatos}")
#aqui removo apenas a chave
del contatos[ "joaao78@gmail.com"]
print(f"\n {contatos}")
