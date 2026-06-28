import pygame
from typing import List
from entity import Entity
from entity_factory import EntityFactory


class Level:
    """Represents a game level that owns a list of entities."""

    def __init__(self, window: pygame.Surface, name: str):
        self.window: pygame.Surface = window
        self.name: str = name
        self.entity_list: List[Entity] = []
        self._factory: EntityFactory = EntityFactory()

    def run(self) -> None:
        pass
