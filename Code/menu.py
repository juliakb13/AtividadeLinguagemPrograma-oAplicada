import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Code.const import MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./background/nature 3/orig.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer.music.load("./musica_fundo.wav")
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Game da", (255, 235, 59), (288,50)) #texto do titulo
            self.menu_text(50, "Julia", (0, 229, 255), (288, 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], (255,255,255), (288, 200 + 40 * i))

            pygame.display.flip()

        # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

