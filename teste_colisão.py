import pygame

def overlapping(minA, maxA, minB, maxB):
    return minB <= maxA and minA <= maxB

def rect_colide( rectA, rectB ):
    aLeft = rectA.x
    aRight = rectA.x + rectA.w
    aTop = rectA.y
    aBotton = rectA.y + rectA.h
    bLeft = rectB.x
    bRight = rectB.x + rectB.w
    bTop = rectB.y
    bBotton = rectB.y + rectB.h
    collideX = overlapping(aLeft, aRight, bLeft,bRight)
    collideY = overlapping(aTop, aBotton, bTop, bBotton)
    return collideX and collideY

screen = pygame.display.set_mode((800, 600), 0, 32)
x = 10
y = 10
vel_x = 0
vel_y = 0
cor = (0, 0, 255)
while True:
    #calcular regras
    x = x + vel_x
    y = y + vel_y

    ra = pygame.Rect(((x, y), (100, 50)))
    rb = pygame.Rect(((350, 275), (100, 50)))
    if rect_colide(ra, rb):
        cor = (255, 255, 0)
    else:
        cor = (0, 0, 255)

    #printar
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), ra, 0)
    pygame.draw.rect(screen, cor, rb, 0)
    pygame.display.update()

    #captura de eventos
    for e in pygame.event.get():
       # print(e)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                vel_x = 1
            elif e.key == pygame.K_LEFT:
                vel_x = -1
            elif e.key == pygame.K_UP:
                vel_y = -1
            elif e.key == pygame.K_DOWN:
                vel_y = 1

        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                vel_x = 0
            elif e.key == pygame.K_LEFT:
                vel_x =0
            elif e.key == pygame.K_UP:
                vel_y = 0
            elif e.key == pygame.K_DOWN:
                vel_y= 0

        if e.type == pygame.QUIT:
             exit()