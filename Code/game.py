import pygame
from typing import List
from menu import Menu
from level import Level


class Game:
    """
    Central game controller.

    Owns exactly one Menu and one-or-more Levels.
    """

    def __init__(self, window: pygame.Surface):
        self.window: pygame.Surface = window
        self.menu: Menu = Menu(window)          # composition 1-to-1
        self.levels: List[Level] = []           # composition 1-to-1..*

    def run(self) -> None:
        pass
