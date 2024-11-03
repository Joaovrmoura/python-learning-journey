# 1-Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

# F
# U
# L
# A
# N
# O

# 2-Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

# 3-Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

# FULANO
# FULAN
# FULA
# FUL
# FU
# F

palavra =  'FULANO'
palavra_v = ''
palavra = list(palavra)

for p in range(len(palavra)):
    print(*palavra)
    del palavra[-1]
    


    




