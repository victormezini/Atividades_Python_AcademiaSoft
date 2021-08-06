import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

x = 10
y = 10
vel_x = 0
vel_y = 0

while True:
    x = x+vel_x
    y = y+vel_y

tela.fill((0, 0, 0))
pygame.draw.rect(250, 250, 200), ((x, y), (100, 50), 0)
pygame.display.update()

for e in pygame.event.get():
    if e.type == pygame.KEDOWN:
        if e.Key == pygame.K_RIGHT:
            vel_x = 1
        elif e.Key == pygame.K_LEFT:
            vel_x = -1
        elif e.Key == pygame.K_UP:
            vel_y = -1
        elif e.Key == pygame.K_DOWN:
            vel_y = 1

    elif e.type == pygame.KEYUP:
        if e.Key == pygame.K_RIGHT:
            vel_x = 0
        elif e.Key == pygame.K_LEFT:
            vel_x = 0
        elif e.Key == pygame.K_UP:
            vel_y = 0
        elif e.Key == pygame.K_DOWN:
            vel_y = 0

        if e.type == pygame.QUIT:
            exit()

