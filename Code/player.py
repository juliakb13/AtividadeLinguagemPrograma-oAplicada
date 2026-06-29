import pygame
from .entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vel_y = 0
        self.no_chao = True

    def move(self):

        teclas = pygame.key.get_pressed()
        if (teclas[pygame.K_SPACE] or teclas[pygame.K_UP]) and self.no_chao:
            self.vel_y = -15
            self.no_chao = False


        self.vel_y += 1
        self.rect.y += self.vel_y


        if self.rect.bottom >= 260:
            self.rect.bottom = 260
            self.vel_y = 0
            self.no_chao = True