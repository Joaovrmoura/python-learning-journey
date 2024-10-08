#módulos em python 
#formas de importar o python 
# modulo inteiro = apenas import + nome_do_modulo
#suas vantagens de se utilizar são que os nomes de variávies
#estão asegurados pelo nome do modulo EXEMPLO:
#variavel platform

import sys

platform = 'MINHA VARIÀVEL'
print(sys.platform)
print(platform)

print()
# Dos Módulos podemos importar apenas "partes" que queremos usar
# como no exemplo acima caso queira importar apenas o platfrom
# o código fica from nome_do modulo import objeto1, objeto2
#desvantegem - voce pode acabar subescrevendo 
# vantegem - nomes pequenos
# algum objeto do módulo 
#EXEMPLO:
from sys import platform, exit

platform = "ola mundo"
#aqui o objeto foi subscrevido
print(platform)

print()
#alias 1- apelido para o módulo nome_modulo as apelido
#Exemplo:
import sys as s
print(s.platform)
print(s.exit)

print()
#alias 2 - from nome_modulo import objeto as apelido
#dando apelido ao objeto importado do módulo
#vantegens - voce pode reservar nomes no código para os módulos
#desvantegens - os nomes podem ficar fora do padrão e vc pode 
# se perder
#exemplo:
from sys import platform as pf, exit as ex
print(pf)

#má prática importar tudo do módulo from modulo import *
# vantegens - importa tudo de um módulo
# desvantagens - importa tudo de um módulo
#exemplo:
from sys import *
#agora todas os nomes dos objetos estão disponíveis 
# vc pode acabar utilizando o nome de um sem querer



