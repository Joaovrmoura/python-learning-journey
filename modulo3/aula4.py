# Nossas instâncias podem guardar estados
class Camera:
    def __init__(self, nome, filmando=None):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar')
            return
        print(f'{self.nome} está filmando...')

    def parar_ilmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return

        print(f'{self.nome} Está parando de filmar...')
        self.filmando = False


c1 = Camera('Cannon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_ilmar()
c1.filmar()
print()
c2.parar_ilmar()
c2.filmar()
c2.filmar()
c1.fotografar()
c2.parar_ilmar()
c1.fotografar()
