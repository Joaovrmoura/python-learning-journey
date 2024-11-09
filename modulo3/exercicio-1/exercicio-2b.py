import json
from exercicio_a import CAMINHO, Pessoa

with open(CAMINHO, 'r', encoding='UTF8') as arq:
    dados = json.load(arq)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)

print()
# ou    
for n in dados:
   print(f"{n['nome']} {n['idade']}")
