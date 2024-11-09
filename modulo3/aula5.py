# Atributos de classes em python
# permite usar o atributo em qualquer 
# lugar  do escopo 

class Pessoa:
    # para todas as instancias
    # fica disponível e vai ter o mesmo valor

    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual

    def get_ano_nacimento(self):
        # Posso acessar com o self.variavel ou 
        # NOME_DA_CLASSE.variavel
        return Pessoa.ano_atual - self.idade 
    
# A VARIAVEL SEMPRE VAI UTILIZAR O SELF DENTRO DA INSTÂNCIA
# QUANDO CHAMAMOS O SELF E UMA VAIRAVEL DE FORA DO ESCOPO 
# DA FUNCAO
   
# Posso acessar a variavel da classe do lado de fora
print(Pessoa.ano_atual)
p1 = Pessoa('luana', 24)
print(p1.get_ano_nacimento())
# altera o valor da variavel para todas as instancias
Pessoa.ano_atual = 1
print(p1.get_ano_nacimento())