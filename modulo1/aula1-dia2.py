#operadores aritiméticos python
multiplicação = 10 * 10
divisao = 10 / 2
soma = 5 + 5
subtracao = 8 - 5
divisão_inteira = 10 // 2
exponenciacao = 2 ** 10
resto_divisao = 25 % 5
print(f" {divisao} \n {soma}\n {subtracao}\n {divisão_inteira}\n {exponenciacao}\n {resto_divisao}\n")


a = input("Digite um valor: ")
b = input("DIGITE outro valor")

if a > b:
    print(f"{a=} é maior que {b=}")
else:
    print(f"{b} é maior que {a}")
    
#concatenação
concatenacao = 'joao' + ' ' 'joao'
joao_vezes = 'joao' * 2
print(concatenacao, joao_vezes)

altura = float(input("Digite sua altura  "))
peso = float(input("digite seu peso  "))
imc = peso / (altura * altura)
#Casas decimais se utiliza :.2f: "2 = numero de casas"
print(f"\n Seu Imc é de {imc:.2f}")

a = 'A'
b = 'B'
c = 1.1
#cria um metodo dentro de um objeto
#formato = 'a={1}' .format(a, b, c)
#print(formato)

entrada = input("voce quer entrar ou sair? ")

if entrada == "sair":
    print("voce saiu")
elif entrada == "entrar":
    print("entrou")
else:
    print("inválido")
