import pygame
screen = pygame.display.set_mode((800, 600), 0, 32)

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        self.rect = Rect((100, 100), (50, 50))
        self.velocidade = [0, 0]

    def draw(self, tela):
        pygame.draw.rect(tela, (255, 255, 0), self.rect, 0)

    def update(self, *args):
        super.update(self, *args)
        nova_pos = (self.rect.topleft[0] + self.velocidade[0],
                    self.rect.topleft[1] + self.velocidade[1])
        self.rect.topleft = nova_pos

    def processa_evento(self, e):
        if e.type == pygame.KEYDOWN:

heroi = Personagem()
while True:
    #calcular regras

    #printar

    screen. fill((0, 0, 0))
    heroi.draw(screen)
    pygame.display.update()


    #captura de eventos

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                heroi.velocidade = [1, 0]