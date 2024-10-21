novela = 0
print('valor' if False else 'outrovalor')

condicao = 10 == 10
variavel = 'valor' if condicao else 'Outro valor'
print(variavel)

digito = 10
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('valor ' if True else 'outro valor')