# Módulo json em python
import json

pessoas = {
  "nome": "Luiz Otávio 2",
  "sobrenome": "Miranda",
  "enderecos": [
    {"rua": "R1","numero": 32},
    {"rua": "R2","numero": 55}
  ],
  "altura": 1.8,
  "numeros_preferidos": (2,4,6,8,10),
  "dev": True, "nada": None
}

#json não suporta métodos funções ou classes
with open('aula31.json', 'w', encoding='utf8') as js:
    # dump "joga" os dados json para outro lugar ou arquivo
    json.dump(pessoas, js,
        # identação do json, para melhor view
        indent=2)

with open('aula31.json', 'r', encoding='utf8') as arquivo:
    #carrega os dados json 
    pessoa = json.load(arquivo)
    # print(pessoa)