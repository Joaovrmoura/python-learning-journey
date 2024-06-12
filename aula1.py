#string methods em python
print("Hello world!")
#end adiciona no final sep= separa as strings dentro do print
print(12, 45, 'end=\n', sep=" - - " 'ola munbdo')
print('joao')
#barra de escape mostra a o caracter a seguir
print("joao \"victor\"")
#r exibe a contra barra
print(r"joao \"victor\"")
# int float  e tipo
print(1.1)
print(10)
print(-5)
# int float  e tipo
a = 0
print(type('otavio'))
print(type(a == 90), type(-1.1), type(5))
#true or false
print(10 == 10)
print(10 != 10)
#tipos str, float, bool
print(7 + 7)
#conversão de tipos, coerção
print(float('1'), type('1'))
print(str(1))
print(int('1'), type('1'))
print(int('1') + 9)
print(bool(''), bool('-5'))

#variáveis
nome = 'joao21'
idade = 5 + 5
print(idade + idade,'\n' + nome)

nomes = 'joao'
idades = 25
data_nasimento = 25-10-2000

print(nomes, idades, data_nasimento)

if idades > 18:
    print("é maior de idade")
else:
    print("é menor de idade")

#interpolação 
n = "joao"
idade = "24"
print("sou {} e tenho {} la ele" .format(n, idade))

# declarando variáveis com varias linhas
b = f"""
   sdsadassadasdsad as
   sadas dsadasdasd


   asdadadsfsdfasf
   sdfsdfsfadf
"""
print(b)