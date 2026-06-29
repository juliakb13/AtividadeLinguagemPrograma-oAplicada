import pygame
from .entity import Entity
from .player import Player
from .enemy import Enemy
from .background import Background


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (576, 0)))

                return list_bg

            case 'Player':
                return Player('boneco1', (80, 210))
                #                         ↑ nome do arquivo    ↑ posição inicial


            case 'Obstacle':
                return Enemy('obstaculo', (576, 210))
                #                          ↑ nome do arquivo   ↑ começa fora da tela à direita

