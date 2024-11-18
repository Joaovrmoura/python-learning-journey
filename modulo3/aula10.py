# @property + @setter - getter e settter 
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# podemos configurar os valores com o setter

 # _variavel = não pode utilizar atributo fora da classe
        # ele está protegido pela classe
""" self._cor = self.cor_tintacor"""

class Caneta:
    def __init__(self, cor):
        # isso é igual a private/protected
        self.cor = cor
        self._cor_tampa = None
       
    # MÉTODOS NÃO SALVAM VALORES
    @property
    def cor(self):
        print('Estou no GETTER')
        return self._cor
    
    # é um método que tem que receber um valor
    @cor.setter
    def cor(self, valor):
        print('Estou no SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Marrom')
caneta.cor_tampa = 'vermelho'
caneta.cor = 'Rosa'
print(caneta.cor)
print(caneta.cor_tampa)