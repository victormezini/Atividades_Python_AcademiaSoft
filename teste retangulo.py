import pygame


pygame.init()

tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.draw.rect(tela, (255, 255, 0), ((260, 200), (200, 100)), 0)
pygame.draw.rect(tela, (255, 255, 0), ((260, 200), (200, 200)), 5)

pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()