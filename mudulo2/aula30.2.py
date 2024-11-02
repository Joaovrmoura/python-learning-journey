import os

caminho_arquivo = r'C:\\Users\\joaov\Desktop\\tutorial-py\\'
# escrita 'w', 'a' 'x'
caminho_arquivo += 'python-curso.txt'

# with open(caminho_arquivo, 'w+') as arquivo:

# A difirença entre o w e o a,
# o w Apaga os arquivos, e escrever 
# caso vc tenha pedido isso
# o A não apaga, ele começa a escrever da última
# linha caso tehna algo escrito

# encoding WTF-8 permite ler assentos e caracteres especiais
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    arquivo.writelines(
        ('Linha 3\n', 'linha 4\n')
    )
#biblioteca os
# apaga os arquivos

os.unlink(caminho_arquivo)
os.remove(caminho_arquivo)
# Renomeia o arquivo
os.rename(caminho_arquivo, 'Novo-nome.txt')
