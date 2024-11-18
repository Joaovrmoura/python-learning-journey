# 2-Implemente uma classe chamada “Banco” que represente uma 
# instituição financeira. Essa classe deve conter métodos para 
# cadastrar clientes, abrir contas bancárias e realizar operações 
# como saques, depósitos e transferências.

class Deposito:
    def __init__(self, depositos):
        self.depositos = depositos
    
    def set_dp(self, valor):
        self.depositos = valor
        return self.depositos

class Saque:
    def __init__(self, saques):
        self.saques = saques
        
    def saque(self, valor):
        self.saques = valor
        return self.saques
    
class Extrato:
    def __init__(self):
        self.depositos = []
        self.saques = []
    
    def set_dep(self,valor):
        self.depositos.append(valor)
        print(self.depositos)

    def set_saque(self, valor):
        if sum(self.depositos) > valor:
            self.saques.append(valor)
            print(self.saques)
        else:
            print("Não foi possível sacar")


saq = Saque(20)
dep = Deposito(50)
ext = Extrato()
ext.set_saque(saq.saque(20))
ext.set_saque(saq.saque(40))
ext.set_dep(50)
ext.set_dep(90)
