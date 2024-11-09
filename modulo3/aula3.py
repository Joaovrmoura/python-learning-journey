# métodos em instâncias de classes em Python
# hard coded = Algo que foi escrito diretamente dentro do
# código

# Uma Classe pode gerar vários objetos
# Em uma classe os dados são salvos nas instâncias (objetos)
# Na classe o self é a própria Instância

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')
        
fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('celata')
print(celta.nome)
celta.acelerar()

# classes tem escopo 
print()
class Animal:
    def __init__(self, nome):
        self.nome = nome
        valor = 'variavel'
        print(valor)
    def acao(self, comendo):
        try:
            return f'O {self.nome} está comendo {comendo}'
        except ValueError as ve:
            print(f'{ve.__class__.__name__} erro de tipo')

leao = Animal('leao')
print(leao.nome)
print(leao.acao('12asd3'))