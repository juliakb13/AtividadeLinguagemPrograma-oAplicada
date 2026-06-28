from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    """Abstract base class for all game entities."""

    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        self.name: str = name
        self.surf: pygame.Surface = surf
        self.rect: pygame.Rect = rect

    @abstractmethod
    def move(self) -> None:
        pass
