#calculos com números flutuantes
#quando necessitamos de fazer um calculo extremamente preciso utilizamos o import decimal

import decimal

num_1 = decimal.Decimal('0.1')
num_2 = decimal.Decimal('0.7')
resul = num_1 + num_2
print(resul)
print(f"{resul:.2f}")
print(round(resul))

n = "joao"
idade = "24"
print("sou {} e tenho {} la ele" .format(n, idade))

b = f"""
   sdsadassadasdsad as
   sadas dsadasdasd


   asdadadsfsdfasf
   sdfsdfsfadf
"""
print(b)