import pygame

from Code.const import MENU_OPTION
from Code.level import Level
from Code.menu import Menu



class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level 1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()
            else:
                pass



