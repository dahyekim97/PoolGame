import pygame
import sys
import config
import table

class Game:
    def __init__(self):
        global clock
        pygame.init()
        self.screen = pygame.display.set_mode((config.screen.Width, config.screen.Height))

        pygame.display.set_caption('LET\'S PLAY POOL!')
        clock = pygame.time.Clock()
        self.holes = pygame.sprite.Group()
        self.tableSprites = pygame.sprite.OrderedUpdates()
        tableImage = pygame.image.load("table.jpg")
        tableImage = pygame.transform.scale(tableImage, (config.screen.Width, config.screen.Height))
        self.background = tableImage
        self.screen.blit(self.background, (0, 0))

def init():
    global game
    game = Game()


def run():
    global screen, clock, game

    onGame = False
    # table = pygame.Rect(tableLeft, tableTop, tableWidth, tableHeight)

    while not onGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

        table.createTable(game)
        pygame.display.update()

    pygame.quit()

init()
run()
