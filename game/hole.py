import pygame
from config import hole, color


class Hole(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, position):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with transparent background.
        # This could also be an image loaded from the disk.
        image = pygame.Surface([hole['radius'] * 2, hole['radius'] * 2], pygame.SRCALPHA, 32)
        self.image = image.convert_alpha()

        pygame.draw.circle(self.image, color['black'], (hole['radius'], hole['radius']), hole['radius'])
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.center = position
