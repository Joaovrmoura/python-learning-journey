#continue quebra o laço e retorna o laço sem o valor do atribuido a parada
cont = 0

while cont <= 20:
    cont += 1
    if cont == 6:
        continue
    print(cont)

    if cont == 10:
        break

#deve ter uma questão dessa na prova
linhaq = 5
colunaq = 5

linha = 0
while linha <= linhaq:
    coluna = 1
    if coluna <= colunaq:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1



#while, enquanto for verdadeira executa, break encerra o laço de repetição
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    if nome == 'sair':
        break
print("acabou")

contador = 0

while contador < 5:
    contador += 1
    print(contador)