# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual

    def get_ano_nacimento(self):
        return Pessoa.ano_atual - self.idade 

p1 = Pessoa('luana', 24)

# Passando o dicionário como parâmetro para a classe
dados = {'nome': 'ruan', 'idade': 15}
p2 = Pessoa(**dados)
print(vars(p2))

# __dict__ guarda as vaariaveis do meu objeto em dicionario
# pode ser alterada reescrita ou lida com dict methods
p1.__dict__['idade'] = 39
del p1.__dict__['idade'] 
# Adicionando novamente
p1.__dict__['idade'] = 39
print(p1.__dict__)
# funciona da mesma forma que o dict, porém apenas para
# ler os dados "EU ACHO"
print(vars(p1))


