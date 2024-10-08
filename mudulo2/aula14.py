#try, except, else e finally
# try tenta executar o código, caso encontre algum 
# erro na sitanxe
# pula imediatamente para excecao
# em python exeções são classes chamadas de exceptions
# a = 18
# b = 0
# c = a / b
# no except podemos passar a exceção que desejamos tratar
print("PARTE 1")
try:
    a = 18
    b = 0
    c = a / b
#podemos tratar duas exceções ao mesmo tempo Exemplo:
except(TypeError, IndexError):
    print('TypeError + IndexError')
#erro da divisão por zero
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
#erro de declarção e nome de uma variável
except NameError:
    print("Name b não está definido(NameError)")
#Classe Exeption contendo erros de tipo
except TypeError:
    print("TypeError")
#Classe Exeption contém o erro de todas as classes
#Porém não identifica o erro!
except Exception:
    print('ERRO DESCONHECIDO(Exception)')


# PARTE DOIS DA AULA
#para identificarmos o erro de exceção podemos atribui-lo
#a uma variável com "as" = eliás
print()
print()
print("PARTE 2")
try:
    x = 16
    b = 0
    print('LINHA 1'[1000])
#aqui temos a classe
except(TypeError, IndexError) as error:
   print('msg de erro:', error)
   #pegando o nome da classe atribuida ao erro
#aqui temos a instancia da classe!
   print('Nome', error.__class__.__name__)

print()
print()
print("PARTE 3")
#AULA PARTE 2
#usar Finally quando não queremos tratar exceções 
# é um bloco que sempre será executado no try except
try:
    print("Abrir o arquivo")
    8/0
except ZeroDivisionError:
    print("dividiu zero")
# finally permite executar o arquivo mesmo ocorrendo algum erro
finally:
    print('Fechar arquivo')
    
