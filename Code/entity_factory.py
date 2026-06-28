import pygame
from entity import Entity
from player import Player
from enemy import Enemy
from background import Background


class EntityFactory:
    """Factory responsible for creating game entities by type."""

    def get_entity(self, entity_type: str) -> Entity:
        """
        Creates and returns an Entity based on the given type string.

        :param entity_type: One of 'player', 'enemy', or 'background'.
        :return: An instance of the corresponding Entity subclass.
        :raises ValueError: If entity_type is not recognised.
        """
        surf = pygame.Surface((0, 0))
        rect = surf.get_rect()

        if entity_type == "player":
            return Player(name="Player", surf=surf, rect=rect)
        elif entity_type == "enemy":
            return Enemy(name="Enemy", surf=surf, rect=rect)
        elif entity_type == "background":
            return Background(name="Background", surf=surf, rect=rect)
        else:
            raise ValueError(f"Unknown entity type: '{entity_type}'")
