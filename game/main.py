import sys

import pygame

from table import Table
from config import screen

class Game:
    def __init__(self):
        global clock
        pygame.init()
        self.screen = pygame.display.set_mode((screen['width'], screen['height']))
        pygame.display.set_caption('LET\'S PLAY POOL!')
        clock = pygame.time.Clock()
        table_image = pygame.image.load("table.jpg")
        table_image = pygame.transform.scale(table_image, (screen['width'], screen['height']))
        self.background = table_image
        self.screen.blit(self.background, (0, 0))

        on_game = True
        # table = pygame.Rect(tableLeft, tableTop, tableWidth, tableHeight)

        table = Table(self)

        while on_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

            pygame.display.update()

        pygame.quit()



game = Game()

