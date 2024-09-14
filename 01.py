import pygame # a biblioteca de desenvolvimento de jogo
from pygame.locals import * #contem constantes e funções
from random import randint

from sys import exit #importa a função do sistema de tornar o "x" das janelas clicaveis 


pygame.init() #inicializar o pygame

#definindo a largura e altura da janela
largura = 640
altura = 480

#definindo o ponto aonde o jogador irá iniciar
x =  largura/2
y = altura/2


x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0 
fonte = pygame.font.SysFont('inkfree', 40, False, False)


#Definindo as dimensões da janela
tela = pygame.display.set_mode((largura, altura))

#definindo o titulo da janela do jogo
pygame.display.set_caption("jogo") 

#criando um relogio dentro do jogo
relogio = pygame.time.Clock() 


while True: #loop principal do jogo
    
    relogio.tick(30) #definindo quanto será a taxa de atualização do jogo
    #pintando a tela de preto
    tela.fill((0,0,0))

    mensagem = f"pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, False, (255,255,255))


    #checando se o usuário clicou no X pra fechar a janela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        #ao colocar o checador de teclas dentro do for acima, o retango só dará pequeno "passos"
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


    #checando se o jogador precionou as teclas para se mover
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
    
    #criando o retangulo do jogador
    rect_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y,80,80))
    
    #criando um retangulo azul para o jogador coletar
    rect_azul = pygame.draw.rect(tela, (0,0,255), (x_azul, y_azul, 40, 50))
    
    #checa se os retangulos estão colidindo
    
    if rect_vermelho.colliderect(rect_azul):
        x_azul , y_azul = randint(40, 600), randint(50, 430) 
        pontos += 1



    tela.blit(texto_formatado, (450, 40))
    #atualizar todo o conteúdo que há na tela
    pygame.display.update()

