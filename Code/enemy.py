import pygame
from entity import Entity


class Enemy(Entity):
    """Enemy entity controlled by the game."""

    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        pass
