import pygame
from pygame.locals import *
from sys import exit

# Inicializando o Pygame
pygame.init()

# Definindo a largura e altura da janela
largura = 480
altura = 520

# Criando a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Game Treino')
# Loop principal do jogo
while True:
    for event in pygame.event.get():
        # Fechar a janela quando clicar no "X"
        if event.type == QUIT:
            pygame.quit()
            exit()
    # Atualiza a tela
    pygame.display.update()
