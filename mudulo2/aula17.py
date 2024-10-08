#modulos em python 
# o primeiro módulo executandi chama-se __main__
#podemos importar outro módulo inteiro ou partes
#o python conhce a pasta onde o __main__ está e 
# as pastas abaixo dele
#ele não reconhece pastas e módulos acima do __main__ padrão
#O python reconhece todos os módulos e pacotes nos mesmos
#caminhos de sys.path
#pastas são chamadas de pacotes

import sys
try:
    sys.path.append('\home')
except ModuleNotFoundError as me:
    print('name_error', me.__class__.__name__)
try:
    import modulo_python
    sys.path.append(r'C:\arquivos-c')
except ModuleNotFoundError as me:
    #aqui capturamos o nome da class atribuida a exceção
    print(me.__class__.__name__)
 
# Aqui, exibimos o nome do módulo que está sendo executado
# '__name__' é uma variável especial que contém o 
# nome do módulo atual Quando um arquivo é executado
# diretamente, seu __name__ é '__main__'    
print('Este módulo chama(aula17)', __name__)
print(*sys.path, sep='\n')

print()
print()

#importando variáveis do módulo 
#modulo inteiro, a ordem que as variáveis foram criadas
# faz diferença
import aula17_modulo
print(aula17_modulo.variavel_modulo)
#importando função(modulo inteiro)
print('função importada: ',aula17_modulo.soma(5,8))
print()


#importando parte do módulo(objeto)
from aula17_modulo import variavel_modulo
print(variavel_modulo)

print()
#importando parte do objeto com alias(apelido)
from aula17_modulo import variavel_modulo as vm, soma
print(vm)
#importando uma função com aliás
print(soma(5, 8))
