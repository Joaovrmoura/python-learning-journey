# Implemente um programa em Python que armazene informações
# de 5 municípios. Cada município deve ser representado por um dicionário com as 
# seguintes chaves: "municipio" e "populacao". O programa deve:

# Permitir que o usuário insira o nome de 5 municípios e suas respectivas populações.
# Calcular e exibir a média populacional entre os municípios.
# Determinar e exibir o município com maior população e o município com menor população.
# Ao final, exibir o nome e a população de todos os municípios cadastrados.


lista_municipios = []
i = 0
soma = 0
menor_p = -1
maior_p = 0
for lista in range(3):
    adicionar = input("Digite o nome do {}º municipio: ".format(lista + 1))
    populacao = int(input("População do estado: "))

    municipios = {'nome': adicionar, 'populacao': populacao}
    
    lista_municipios.append(municipios)
    
    soma += municipios['populacao']
    
    if municipios['populacao'] > maior_p:
        maior_p = municipios['populacao']
    if menor_p == -1 or municipios['populacao'] < menor_p :
        menor_p = municipios['populacao']
        
media = soma / 5 

for i, valor in enumerate(lista_municipios):
    print(f"Município de {valor['nome']} Populção: {valor['populacao']}")

print(f"A media populacional do municipios: {media}")
print(f"Municipio com a maior população: {maior_p}")
print(f"Municipio com a menor população: {menor_p}")
print()

