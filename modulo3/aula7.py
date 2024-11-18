#métodos de classe + factories 
# são métodos onde o "Self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmtro, receberemos a própria classe.add()


# @classmethod
    # Transforma o método comum em um
    # método de classe com esse decorator;
    # utilizadno isso, posso usar esse método 
    # sem o self, porém, 
    # sempre devo utilizar o parâmetro cls no método
    # impossivel utilizar o self

# @classmethod
    # permite usar o "molde" class
    # sem usar as instancias da class o self 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('hey')
    
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
   
    @classmethod
    def sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa('Joao', 24)
p2 = Pessoa.criar_com_50_anos('helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

