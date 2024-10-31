#Métodos mais utilizados em python

# Funções de Manipulação de Strings
# ================================
print("texto".capitalize())          # Primeiro caractere maiúsculo.
print("TEXTO".casefold())            # Converte para minúsculas.
print("texto".center(10, '-'))       # Centraliza com largura e preenchimento.
print("texto".count('t'))            # Conta ocorrências de um caractere.
print("texto".find('e'))             # Retorna índice de primeira ocorrência.
print("texto".upper())               # Converte para maiúsculas.
print(" texto ".strip())             # Remove espaços em branco ao redor.
print("texto".replace("e", "a"))     # Substitui caracteres.
print("texto123".isalnum())          # Retorna True se todos os caracteres são alfanuméricos.
print("texto".isalpha())             # Retorna True se todos os caracteres são letras.
print("1234".isdigit())              # Retorna True se todos os caracteres são dígitos.
print("texto".isidentifier())        # Retorna True se for um identificador válido em Python.
print("Texto".istitle())             # Retorna True se cada palavra começa com maiúscula.
print("texto".isupper())             # Retorna True se todos os caracteres são maiúsculos.
print("texto\noutra".splitlines())   # Divide a string por quebras de linha, retorna lista.
print("texto".startswith("te"))      # Retorna True se a string começa com o prefixo dado.
print("texto".endswith("to"))        # Retorna True se a string termina com o sufixo dado.
print("texto".ljust(10, '-'))        # Justifica à esquerda com largura e preenchimento.
print("texto".rjust(10, '-'))        # Justifica à direita com largura e preenchimento.
print("Texto".swapcase())            # Troca maiúsculas para minúsculas e vice-versa.
print("palavra".partition("a"))      # Divide a string na primeira ocorrência do separador.
print("palavra".rpartition("a"))     # Divide a string na última ocorrência do separador.
print("Texto com quebra".split())    # Divide a string em uma lista usando espaço como separador.
print("Texto com quebra".rsplit())   # Divide a string em uma lista a partir da direita.
print("esquerda direita centro".expandtabs(4))  # Expande tabulações para espaços.

# ================================
# Funções para Manipulação de Listas
# ================================
lista = [1, 2, 3]
lista.append(4)                     # Adiciona item ao final da lista.
lista.clear()                       # Remove todos os elementos.
print(lista.copy())                 # Cópia rasa da lista.
print(lista.count(2))               # Conta quantas vezes um item aparece.
lista.extend([5, 6])                # Adiciona elementos do iterável.
print(lista.index(3))               # Índice da primeira ocorrência.
lista.insert(0, 10)                 # Insere item em posição específica.
print(lista.pop())                  # Remove e retorna o último item.
lista.remove(10)                    # Remove a primeira ocorrência.
lista.sort()                        # Ordena a lista.
lista.reverse()                     # Inverte a lista.


# ================================
# Funções para Trabalhar com Iteráveis
# ================================
print(all([True, True, False]))     # True se todos os itens forem True.
print(any([False, False, True]))    # True se algum item for True.
print(enumerate("abc"))             # Índice e valor como tupla.
print(filter(lambda x: x > 1, [1, 2, 3]))  # Filtra valores maiores que 1.
print(map(lambda x: x * 2, [1, 2, 3]))     # Aplica função em cada elemento.
print(sum([1, 2, 3]))               # Soma todos os elementos.
print(zip([1, 2], ['a', 'b']))      # Combina itens de iteráveis.
print(sorted([3, 1, 2]))            # Retorna lista ordenada.


# ================================
# Funções para Manipulação de Dicionários
# ================================
dicionario = {"a": 1, "b": 2}
print(dicionario.keys())            # Retorna todas as chaves.
print(dicionario.values())          # Retorna todos os valores.
print(dicionario.items())           # Retorna pares (chave, valor).
print(dicionario.get("a"))          # Retorna valor da chave especificada.
dicionario.update({"c": 3})         # Atualiza o dicionário com outro dicionário.
dicionario.pop("b")                 # Remove e retorna valor da chave.
dicionario.clear()                  # Remove todos os itens.


# ================================
# Funções para Manipulação de Conjuntos
# ================================
conjunto = {1, 2, 3}
conjunto.add(4)                     # Adiciona item ao conjunto.
conjunto.discard(1)                 # Remove item, se existir.
print(conjunto.union({5, 6}))       # União de conjuntos.
print(conjunto.intersection({2, 3}))# Interseção de conjuntos.
print(conjunto.difference({2}))     # Diferença entre conjuntos.
print(conjunto.isdisjoint({10}))    # Verifica se não há itens comuns.



# ================================
# Funções de Ajuda e Informação
# ================================
help(print)                         # Documentação do objeto fornecido.
dir(lista)                          # Lista atributos e métodos do objeto.
type(123)                           # Retorna o tipo do objeto.
id(lista)                           # Retorna o identificador na memória.
isinstance(123, int)                # Verifica se objeto é de tipo específico.
callable(print)                     # Verifica se objeto pode ser chamado.


# ================================
# Funções para Manipulação de Objetos e Atributos
# ================================
obj = type('Objeto', (), {'atributo': 10})  # Cria um objeto com um atributo "atributo"

print(hasattr(obj, 'atributo'))     # Verifica se o objeto possui o atributo especificado.
print(getattr(obj, 'atributo'))     # Obtém o valor do atributo, se ele existir.
setattr(obj, 'novo_atributo', 20)   # Define um novo atributo com o valor especificado.
print(vars(obj))                    # Retorna um dicionário dos atributos do objeto.
print(delattr(obj, 'atributo'))     # Deleta o atributo do objeto, se ele existir.



# ================================
# Funções para Objetos e Atributos
# ================================
class Teste:
    atributo = 10

obj = Teste()
print(hasattr(obj, 'atributo'))     # Verifica se objeto tem atributo.
print(getattr(obj, 'atributo'))     # Obtém o valor de um atributo.
setattr(obj, 'novo_atributo', 20)   # Define valor de novo atributo.
print(vars(obj))                    # Retorna o __dict__ de um objeto.

# ================================
# Funções para Trabalhar com Números Aleatórios
# ================================
import random
print(random.randint(1, 10))        # Número aleatório entre 1 e 10.
print(random.choice([1, 2, 3]))     # Escolhe um item aleatório.

# ================================
# Funções Lambda e Map
# ================================
dobrar = lambda x: x * 2
print(dobrar(5))                    # Aplica função lambda.
print(list(map(dobrar, [1, 2, 3]))) # Aplica lambda em lista.

# ================================
# Funções Filter e Reduce
# ================================
print(list(filter(lambda x: x > 1, [0, 1, 2, 3])))  # Filtra valores maiores que 1.
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3]))       # Soma todos os itens.