from abc import ABC, abstractmethod
import pygame


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name #salvar os bichinhos na pasta ./background/nature 1
        self.surf = pygame.image.load('./background/nature 1/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self,):
        pass
