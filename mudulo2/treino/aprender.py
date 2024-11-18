from itertools import groupby, combinations
import random
import json

linguagens = ['python', 'javascript', 'typeScript', 'java', 'Golang', 'php']
frameworks = ['laravel', 'flask', 'django', 'React', 'FastApi', 'Spring bot']

CAMINHO = 'aprenda.json'

if __name__ == '__main__':
    lista = []
    rand_l = random.sample(linguagens, 3)
    for n in rand_l:
        lista.append('linguagem - ' + n)

    rand_f = random.sample(frameworks, 3)
    for f in rand_f:
        lista.append('Framework - ' + f)

    with open(CAMINHO, 'w', encoding='UTF8') as arq:
        json.dump(lista, arq, indent=2)
    