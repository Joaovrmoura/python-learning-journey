#dicionario são criados com {} o o dict()
#os itens do dicionário devem ser imutáveis
#como strings e tuplas
#o dicionario recebe a chave "nome"  atribuição ":" depois da chave seu valor "joao"
exemplo_1 = {"nome" : "joao", 'idade' : 24 }
#aqui chamamos a função dict e atribuimos os valores com =
exemplo_2 = dict(nome="joao", idade= 24)
print(exemplo_2)
#para acessar itens adicionamos o nome do dicionário com colchetes
#exemplo
print(exemplo_1["nome"])
#para alterar o item chamamos ele em [] e depois sub-escrevemos com = ""
exemplo_1["idade"] = 25
print(exemplo_1["idade"])

contatos = {
    "joao1@gmail.com" : {"nome": "joao", "telefone" : "769757757", "cep" : "26454541"},
    "joao54@gmail.com" : {"nome": "Victor", "telefone" : "76975757", "cep" : "26454431"},
    "joaao78@gmail.com" : {"nome": "Morcos", "telefone" : "769354474", "cep" : "26474031"},
    "josao178@gmail.com" : {"nome": "claudio", "telefone" : "76454547", "cep" : "22555031"},
}
#para acessar um item dentro de outro utilizamos variável = [chave][chave] que retorna 
# = [valor da chave]
print(contatos["joao54@gmail.com"]["telefone"])
#ao iterar sobre dicionários ele retornará a chave do dicionário
for chave in contatos:
    print(f"{chave} {contatos[chave]}")
    
#outro método
for chaves, valor in contatos.items():
    print(chave, valor)