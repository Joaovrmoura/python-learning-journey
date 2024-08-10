### higher order functions são funções que retornam outras funções 
def saudacao(nome, msg):
    return f'{nome}, {msg}'

def executa(sadacao, *args):
    return sadacao(*args)

print(
    executa(saudacao,'joao', 'Bom dia')
)

###clousure executa uma função dentro de outra
"""deixamos sem os parênteses para deixar a função ser 
executada em outras partes"""

def outraSaudacao(saudacaos, nome):
    def execute(): 
        return f'{saudacaos}, {nome}'
    return execute

s1 = outraSaudacao('boa noite', 'marcelo')
s2 = outraSaudacao('bom dia', 'marcela')

print(s1())
print(s2())

##Outra forma passar o segundo paramentro para a função dentro do escopo
##da função

def outraSaudacao2(saudacaos):
    def execute(nome): 
        return f'{saudacaos}, {nome}'
    return execute

s3 = outraSaudacao2('boa noite')
s4 = outraSaudacao2('bom dia')

for nome in ['joao', 'marcela', 'vitoria']:
    print(s3(nome))
