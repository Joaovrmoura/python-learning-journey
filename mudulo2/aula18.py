#singleton só pode existir uma instancia de algo no 
# programa
#Após carregar um módulo no python, não é pssível recarregalo
#diversas vezes, o python reconhece o módulo
#caso queira recarregar algum módulo
from sys import path

#Módulos em python são chamados de packages=pastas
#para importar algo do package Exemplo:
#from PASTA.(NOME_DO_SCRIPT.PY) import (FUNÇÂO"NESSE CASO")
from aula18_package.modulo import soma_do_modulo

import aula18_package
from aula18_package.modulo import *


print(*path, sep='\n')
print()
print(soma_do_modulo(5, 8))


# import importlib
# import aula18_modulo
# for i in range(2):
#importlib.(nomedoModulo) = recarega o módulo a cada laço de rep
#     importlib.reload(aula18_modulo)
#     print(i)
# print('Fim')


from aula18_package.modulo_b import fala_oi

fala_oi()
print(variavel)
print(string)