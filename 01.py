import pygame # a biblioteca de desenvolvimento de jogo
from pygame.locals import * #contem constantes e funções

from sys import exit #importa a função do sistema de tornar o "x" das janelas clicaveis 


pygame.init() #inicializar o pygame
largura = 640
altura = 480
x =  largura/2
y = altura/2

tela = pygame.display.set_mode((largura, altura)) #Definindo as dimensões da janela
pygame.display.set_caption("jogo") #definindo o titulo da janela do jogo
relogio = pygame.time.Clock() #criando um relogio dentro do jogo


while True: #loop principal do jogo
    
    relogio.tick(30) #definindo quanto será a taxa de atualização do jogo
    
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        """
        if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            if event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            if event.key == K_s:
                y += 20
            """



    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20


    if pygame.key.get_pressed()[K_s]:
        y += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    #função para desenhar retangulo

    #rect(aonde vai ser desenhado, (o esquema RPG ), (posição x, posicão y, largura, altura))
    pygame.draw.rect(tela, (255,0,0), (x, y,40,80))
    
#lógica para fazer o retangulo sumir



    pygame.display.update()



