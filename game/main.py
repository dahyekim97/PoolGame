import pygame
import sys
import config

def init():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((config.screen.Width, config.screen.Height))
    pygame.display.set_caption('LET\'S PLAY POOL!')
    clock = pygame.time.Clock()


def drawHoles():
    horizontalPosition = config.hole.InitialHorizontalPosition

    for i in range(0, 3):
        # middle whole is in different position from other two holes in the same row
        topHolesPosition = (config.hole.TopPosition, config.hole.TopPosition - 10)[i == 1]
        bottomHolesPosition = (config.hole.BottomPosition, config.hole.BottomPosition + 10)[i == 1]
        pygame.draw.circle(screen, config.color.BLACK, (horizontalPosition, topHolesPosition), config.hole.Radius)
        pygame.draw.circle(screen, config.color.BLACK, (horizontalPosition, bottomHolesPosition), config.hole.Radius)
        horizontalPosition += (int)(config.table.Width / 2)


def run():
    global screen, clock

    onGame = False
    # table = pygame.Rect(tableLeft, tableTop, tableWidth, tableHeight)

    while not onGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(config.color.WHITE)

        tableImage = pygame.image.load("table.jpg")
        tableImage = pygame.transform.scale(tableImage, (config.screen.Width, config.screen.Height))
        tableImageRect = tableImage.get_rect()
        screen.blit(tableImage, tableImageRect)
        pygame.display.flip()

        drawHoles()

        # pygame.draw.rect(screen, tableColor, table)
        # pygame.draw.rect(screen, frameColor, table, tableFrameThickness)

        pygame.display.update()

    pygame.quit()


init()
run()
