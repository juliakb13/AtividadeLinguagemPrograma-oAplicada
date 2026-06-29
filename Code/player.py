import pygame
from .entity import Entity


class Player(Entity):
    """Player entity controlled by the user."""

    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        pass
