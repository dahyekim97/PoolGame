import pygame
import config

class Hole(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with transparent background.
       # This could also be an image loaded from the disk.
       image = pygame.Surface([config.hole.Diameter, config.hole.Diameter], pygame.SRCALPHA, 32)
       self.image = image.convert_alpha()

       pygame.draw.circle(self.image, (0, 0, 0),
                          (config.hole.Radius, config.hole.Radius), config.hole.Radius, 0)
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.center = position


def init(self):
    self.holes = pygame.sprite.Group()
    self.allSprites = pygame.sprite.OrderedUpdates()


def initializeHoles(self):
    horizontalPosition = config.hole.InitialHorizontalPosition
    for i in range(0, 3):
        # middle hole is in different position from other two holes in the same row
        # when i == 1 it is middle hole
        topHolesPosition = (config.hole.TopPosition, config.hole.TopPosition - 10)[i == 1]
        bottomHolesPosition = (config.hole.BottomPosition, config.hole.BottomPosition + 10)[i == 1]
        self.holes.add(Hole((horizontalPosition, topHolesPosition)))
        self.holes.add(Hole((horizontalPosition, bottomHolesPosition)))
        horizontalPosition += int(config.table.Width / 2)
    self.tableSprites.add(self.holes)



def createTable(game):
    initializeHoles(game)
    game.tableSprites.draw(game.screen)

