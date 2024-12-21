import pygame # a biblioteca de desenvolvimento de jogo
from pygame.locals import * #contem constantes e funções
from random import randint



pygame.init() #inicializar o pygame


#iniciando a música de fundo e determinando que ela tocara em loop infinito
pygame.mixer.init()

musica_fundo = "Cyberpunk_Moonlight_Sonata.mp3" #variavel que guarda o arquivo da musica principal


som_colisao = pygame.mixer.Sound("smw_coin.wav")  # Colocando o som de colisão em uma variavel


pygame.mixer.music.load(musica_fundo) # método para carregar a música
pygame.mixer_music.play(loops=-1) #definindo que a música tocará infinitamente
pygame.mixer.music.set_volume(0.02) #definindo o volume da musica de fundo


#definindo a largura e altura da janela
largura = 640
altura = 480




#definindo o ponto aonde o jogador irá iniciar
x_cobra =  largura/2
y_cobra = altura/2

velocidade = 10

x_controle = velocidade 
y_controle = 0


x_maca = randint(40, 600)
y_maca = randint(50, 430)


pontos = 0 
fonte = pygame.font.SysFont('inkfree', 40, False, False)


#Definindo as dimensões da janela
tela = pygame.display.set_mode((largura, altura))


#definindo o titulo da janela do jogo
pygame.display.set_caption("jogo") 


#criando um relogio dentro do jogo
relogio = pygame.time.Clock() 

morreu = False


running = True #uma variavel que recebe um boolian "true" para fazer o loop principal do jogo

lista_cobra = []
comprimento_inicial = 3

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:

        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20,20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos= 3
    comprimento_inicial = 3
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)    
    y_maca = randint(50,430)
    morreu = False


while running: #loop principal do jogo
    
    relogio.tick(30) #definindo quanto será a taxa de atualização do jogo
    
    
    
    
    #pintando a tela de preto
    tela.fill((255,255,255))

    mensagem = f"pontos: {pontos}"
    texto_formatado = fonte.render(mensagem, False, (0,0,0))


    #checando se o usuário clicou no X pra fechar a janela
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == KEYDOWN:
            
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
                
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0    
            

            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0

            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade 
                    x_controle = 0


    x_cobra += x_controle
    y_cobra += y_controle

    """
    #checando se o jogador precionou as teclas para se mover
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
        
    if pygame.key.get_pressed()[K_d]:
        x_cobra += 20
        
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20
        
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20
    """
    
        


    
    #função para desenhar retangulo
    #rect(aonde vai ser desenhado, (o esquema RGB ), (posição x, posicão y, largura, altura))
    
    #criando o retangulo do jogador
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra,20,20))
    
    #criando um retangulo azul para o jogador coletar
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca, 20, 20))
    
    #checa se os retangulos estão colidindo
    
    if cobra.colliderect(maca):
        x_maca , y_maca = randint(40, 600), randint(50, 430) 
        pontos += 1
        som_colisao.play()
        comprimento_inicial += 1


    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)


    
    lista_cobra.append(lista_cabeca)


    #condicional para checar se a cabeça da cobra toca na propria cabeça
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont("arial", 20, True, True)
        mensagem = f"""game over! Pressione a tecla "R". Pontos = {pontos}"""

        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()


        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)               
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


    if x_cobra > largura:
        x_cobra = 0
    
    if x_cobra < 0:
        x_cobra = largura

    if y_cobra < 0:
        y_cobra = altura

    if y_cobra > altura:
        y_cobra = 0




    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]


    aumenta_cobra(lista_cobra)



    #escreve o texto na tela
    tela.blit(texto_formatado, (450, 40))
    
    
    #atualizar todo o conteúdo que há na tela
    pygame.display.update()

