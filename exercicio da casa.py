import pygame

# inicializa o Pygame
pygame.init()

# cria a janela
tela = pygame.display.set_mode((800, 600), 0, 32)

# desenha o hexágono
pontos = [(400, 100), (500, 160), (500, 340), (400, 400), (300, 340), (300, 160)]
pygame.draw.polygon(tela, (255, 255, 0), pontos, 3)

# atualiza a tela
pygame.display.update()

# loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
