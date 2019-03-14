import pygame
import sys

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# screen constants
screenWidth = 1000
screenHeight = 500

# table constants
tableWidth = 900
tableHeight = 400
tableLeft = 50
tableTop = 50
tableColor = (18, 104, 54)
tableFrameThickness = 30
frameColor = (107, 75, 59)

# hole constants
holeRadius = 20
holeTopPosition = 50
holeBottomPosition = screenHeight - 50
initialHorizontalPosition = 50

# 16 balls initial position
balls = [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]


def init():
    global screen, clock
    pygame.init()
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption('LET\'S PLAY POOL!')
    clock = pygame.time.Clock()


def drawHoles():
    horizontalPosition = initialHorizontalPosition

    for i in range(0, 3):
        topHolesPosition = (holeTopPosition, holeTopPosition - 10)[i == 1]
        bottomHolesPosition = (holeBottomPosition, holeBottomPosition + 10)[i == 1]
        pygame.draw.circle(screen, BLACK, (horizontalPosition, topHolesPosition), holeRadius)
        pygame.draw.circle(screen, BLACK, (horizontalPosition, bottomHolesPosition), holeRadius)
        horizontalPosition += (int)(tableWidth / 2)


def run():
    global screen, clock

    onGame = False
    # table = pygame.Rect(tableLeft, tableTop, tableWidth, tableHeight)

    while not onGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        tableImage = pygame.image.load("table.jpg")
        tableImage = pygame.transform.scale(tableImage, (screenWidth, screenHeight))
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
