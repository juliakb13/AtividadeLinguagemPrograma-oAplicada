import pygame
from typing import List
from Code.entity import Entity
from Code.entity_factory import EntityFactory

class Level:

    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

        # background
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        # boneco e obstáculo
        self.player = EntityFactory.get_entity('Player')
        self.obstacle = EntityFactory.get_entity('Obstacle')

        self.entity_list.append(self.player)
        self.entity_list.append(self.obstacle)

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # fecha o jogo se apertar X
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            # se o boneco tocar no obstáculo, volta ao menu
            if self.player.rect.colliderect(self.obstacle.rect):
                return 'GAME_OVER'

            pygame.display.flip()
            clock.tick(60)
