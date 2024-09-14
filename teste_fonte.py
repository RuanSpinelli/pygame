# Para ver as fontes disponiveis na maquina

import pygame

pygame.init()

# Obtenha a lista de fontes disponíveis
fonts = pygame.font.get_fonts()

# Organize a lista em ordem alfabética
fonts_sorted = sorted(fonts)

# Exiba cada fonte em uma nova linha
for font in fonts_sorted:
    print(font)
