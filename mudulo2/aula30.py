"""# Caminho de arquivos em python
# utilize barras invertidas duplas
# para caminhos dentro do windows
# para aqrquivos em python temos os seguintes
# modos
# r (leitura), w (escrita), x(para criação)
# a (escrever ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# métodos úteis 
# write, read (escrever, ler)
# writeline (escrever várias linhas)
# seek (mover o cursor)
# readline (ler linha)
# readlines (ler linhas)
# """


caminho_arquivo = r'C:\\Users\\joaov\Desktop\\tutorial-py\\'

# qunado o arquivo não existe e preciso criar, uso 
# algum modo de
# escrita 'w', 'a' 'x'
caminho_arquivo += 'python-curso.txt'


#sempre feche os arquivos

# 1-Método de abertura e fechamento
# abre o arquivo, recebe a ação que vc quer fazer 
# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# utilizamos o withopen para abrir e fechar o arquivo
# pois sempre devemos fechar os arquivos evitar erros

# 2 - Método de abertura e fechamento "automático"
# Com o + ao lado do w+ = Escrita com possibilidade 
# de leitura :

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    # Writelines é um iterável que escreve dentro
    # do arquivo, aonde as linhas são passados dentrp
    # de tuplas
    arquivo.writelines(
        ('Linha 3\n', 'linha 4\n')
    )
    arquivo.seek(0, 0)
    print('Lendo...')
    #lê apenas 1 linha por vez
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print()
    print('Readlines')
    arquivo.seek(0, 0)
    # Readlines é um iterável que pode ser lido em um for
    for linha in arquivo.readlines():
        print(linha.strip())
print()

print('#' * 10)
with open(caminho_arquivo, 'r') as arquivo:
    # ler o arquivo no terminal
    print(arquivo.read())

