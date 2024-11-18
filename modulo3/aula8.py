# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método  de classe
# @staticmethod - método estático (self, cls)

# SELF
   # QUALQUER MÈTOD QUE UTILIZO O SELF, 
   # SE ESTOU USANDO UM MÈTODO DE INSTÂNCIA
   # É UM MéTODO DE INSTÂNCIA

# classmethod 
    # acessa os objetos da classe sem o SELF

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # método para confugurar atributo
    def set_user(self, user):
        self.user = user

    def set_pass(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        conn = cls()
        conn.user = user
        conn.password = password
        return conn
    
    # não tem acesso ao self ou cls
    @staticmethod
    def log(msg):
        print("log:", msg)

c1 = Connection()
c1 = c1.create_with_auth('joao', 123)
Connection.log("Mensagem de log")

print(c1.user)
print(c1.password)

