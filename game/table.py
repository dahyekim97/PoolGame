import pygame
from config import screen, table, hole
from hole import Hole


class Table:

    def __init__(self, game):
        self.game = game

        self.holes = pygame.sprite.Group()
        self.tableSprites = pygame.sprite.OrderedUpdates()

        self.initialize_holes()
        self.tableSprites.draw(self.game.screen)

    def initialize_holes(self):
        horizontal_position = table['margin']
        for i in range(0, 3):
            # middle hole is in different position from other two holes in the same row
            # when i == 1 it is middle hole
            top_hole = table['margin']
            bottom_hole = screen['height'] - table['margin']
            top_holes_position = (top_hole, top_hole - 10)[i == 1]
            bottom_holes_position = (bottom_hole, bottom_hole + 10)[i == 1]

            self.holes.add(Hole((horizontal_position, top_holes_position)))
            self.holes.add(Hole((horizontal_position, bottom_holes_position)))

            horizontal_position += int(table['width'] / 2)
        self.tableSprites.add(self.holes)

