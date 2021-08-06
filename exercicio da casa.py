import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

#tela.set_at((400,300), (255, 255, 0))
pygame.draw.line(tela, (255, 255, 0), (400,100), (500, 160), 3)
pygame.draw.line(tela, (255, 255, 0), (500,160), (300, 160), 3)
pygame.draw.line(tela, (255, 255, 0), (300,160), (400, 100), 3)
pygame.draw.line(tela, (255, 255, 0), (500, 160), (500, 340), 3)
pygame.draw.line(tela, (255, 255, 0), (500, 340), (300, 340), 3)
pygame.draw.line(tela, (255, 255, 0), (300, 340), (300, 160), 3)

pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()      