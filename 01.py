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


    #função para desenhar retangulo

    #rect(aonde vai ser desenhado, (o esquema RPG ), (posição x, posicão y, largura, altura))
    pygame.draw.rect(tela, (255,0,0), (200, 300,40,80))
    #para desenhar circulos se define o raio ali no 40
    pygame.draw.circle(tela, (0,0,255),(300,260),40)

    #para desenhar linha se define a cor, aoonde começa e aonde termina
    pygame.draw.line(tela, (255,255,0), (390,0),(390,600), 5)


    pygame.display.update()



