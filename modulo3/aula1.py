# Clsses são moldes para criar objetos
# as classes geram objetos (instâncias) que
# podem ter seus próprios atributos e métodos
# os objetos gerados pela classe podem usar seus 
# dados internos para realizar várias ações
# Por convenção, usamos PascalCase para nomes de classes

class Pessoa:
    ...

# Novo objetot ou nova instância da classe
p1 = Pessoa()
# Atributos da classe OU DADOS da classe
p1.nome = 'joao'
p1.sobrenome = 'rodrigues'
# Novo objetot ou nova instância da classe
p2 = Pessoa()
# Atributos da classe OU DADOS da classe
p2.nome = 'mariana'
p2.sobrenome = 'ximenez'

# Acessando ATRIBUTOS
print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)