# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

# @property 
    # se e eu precisar mudar o nome do atributo
    # evita que se use o atributo direto/Protege o atributo
    
class Caneta1:
    def __init__(self, cor):
        self.cor_tinta = cor

    # método que se comporta como atributo
    @property
    def cor(self):
        print('Posso executar ações')
        return self.cor_tinta
    
    # fora da classe se parece com um atributo
    # (mesmo sendo método)
    @property
    def cor_tampa(self):
        return 123546
    
canetas = Caneta1('Azul')
print(canetas.cor)
print(canetas.cor_tampa)
print()

###########################################

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # GETTER - atributo protegido / 
    # evita quebrar código cliente
    def get_cor(self):
        #Com o getter posso executar algo 
        # aqui antes do atributo
        print("Posso executar ações")
        return self.cor_tinta
    
# Código cliente
caneta = Caneta('azul')
print(caneta.get_cor())
print(caneta.get_cor())
