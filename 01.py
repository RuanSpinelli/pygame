import pygame # a biblioteca de desenvolvimento de jogo
from pygame.locals import * #contem constantes e funções

from sys import exit #importa a função do sistema de tornar o "x" das janelas clicaveis 


pygame.init() #inicializar o pygame
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura)) #Definindo as dimensões da janela
pygame.display.set_caption("jogo") #definindo o titulo da janela do jogo



while True: #loop principal do jogo

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.display.update()



