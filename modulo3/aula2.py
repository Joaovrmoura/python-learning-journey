# Self referencia ao objeto que está sendo criado
# Método init inicia os métodos da class

class Pessoa:
    # O método __init__ é um método especial chamado 
    # automaticamente quando uma nova instância da classe é criada.
    # Ele inicializa o objeto com os atributos fornecidos.
    def __init__(self, nome, sobrenome):
        # 'self' é uma referência ao próprio objeto que está sendo 
        # criado. Com 'self', acessamos os atributos e métodos da instância.
        # Aqui, estamos criando dois atributos: 'nome' e 'sobrenome'.
        self.nome = nome
        self.sobrenome = sobrenome
    
# Criamos uma instância da classe Pessoa, chamada 'p1'.
# Passamos os valores 'joao' e 'Rodrigues' 
# como argumentos para o nome e sobrenome.
p1 = Pessoa('joao', 'Rodrigues')

# atributos 'nome' e 
# 'sobrenome' da instância 'p1'.
print(p1.nome, p1.sobrenome)
