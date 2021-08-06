import pygame


pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)

tela.set_at((400,300), (255, 255, 0))

pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()