import pygame
from entity import Entity


class Background(Entity):
    """Background entity representing the game scenery."""

    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        pass
