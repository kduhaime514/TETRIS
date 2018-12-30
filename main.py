import pygame
import constant

import sys
sys.path.append('./classes')
from Shape import Shape
from ShapeType import ShapeType
from Grid import Grid

pygame.init()

windowWidth = 500
windowHeight = windowWidth
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(constant.GAME_NAME)

gridLength = round(windowHeight/constant.TOTAL_BLOCKS_Y)

myFont = pygame.font.SysFont("Times New Roman", 12)

dropRate = constant.STARTING_DROP_RATE
clock = 0
tickRate = 100

# TODO - this doesn't belong in main
def blockReachedBottom():
    return False

grid = Grid(gridLength, windowWidth)
# print(grid.getPosition(1,2))

# TODO - clean up
dropShape = Shape(grid, ShapeType.getRandom(), 0, 0)
dropShape2 = Shape(grid, ShapeType.getRandom(), 5, 0)
dropShape3 = Shape(grid, ShapeType.getRandom(), 0, 5)
dropShape4 = Shape(grid, ShapeType.getRandom(), 5, 5)
dropShape5 = Shape(grid, ShapeType.getRandom(), 0, 10)
dropShape6 = Shape(grid, ShapeType.getRandom(), 5, 10)
dropShape7 = Shape(grid, ShapeType.getRandom(), 0, 15)

run = True
while run:
    clock+=tickRate
    pygame.time.delay(tickRate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    grid.draw(window)

    if blockReachedBottom():
        foo = "bar"
        # TODO - lock shape in place, spawn new one
        # dropShapeY=0
    elif not clock%dropRate:
        bar = "baz"
        # TODO increment Y coord of currently dropping shape

    dropShape.draw(window)
    dropShape2.draw(window)
    dropShape3.draw(window)
    dropShape4.draw(window)
    dropShape5.draw(window)
    dropShape6.draw(window)
    dropShape7.draw(window)

    # pygame.draw.rect(window, (255, 0, 0), (dropShapeX, dropShapeY, gridLength, gridLength))

    # debug = myFont.render("playFieldHeight is: " + str(playField.height), 1, (0, 255, 0))
    # window.blit(debug, (200, 200))

    pygame.display.update()

pygame.quit()