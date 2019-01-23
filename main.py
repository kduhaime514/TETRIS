import pygame
import constant

import sys
import controls
import shapeGenerator
sys.path.append('./classes')
from Shape import Shape
from ShapeType import ShapeType
from Direction import Direction
from Grid import Grid

pygame.init()

# WINDOW SETUP
windowWidth = 500
windowHeight = windowWidth
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(constant.GAME_NAME)

myFont = pygame.font.SysFont("Times New Roman", 12)

gridLength = round(windowHeight/constant.TOTAL_BLOCKS_Y)
grid = Grid(gridLength, windowWidth)

# def spawnNewShape():
#     if constant.TEST_ROTATE_MODE:
#         return Shape(grid, ShapeType(constant.TEST_ROTATE_MODE_SHAPE), 3, 8)
#     else:
#         return Shape(grid, ShapeType.getRandom())
dropShape = shapeGenerator.spawnNewShape(grid)

dropRate = constant.STARTING_DROP_RATE
clock = 0
tickRate = 100
run = True
while run:
    clock+=tickRate
    pygame.time.delay(tickRate)

    run = controls.handleEvents(pygame.event.get(), dropShape)
    
    # Drop logic
    if not clock%dropRate:
        if not grid.shapeReachedBottom(dropShape):
            # if not constant.TEST_ROTATE_MODE:
            dropShape.move(Direction.DOWN)
        else:
            grid.addBlocks(dropShape.blocks)
            dropShape = shapeGenerator.spawnNewShape(grid)
            run = not grid.gameOver(dropShape)

    grid.draw(window)
    dropShape.draw(window)
    
    # debug = myFont.render("playFieldHeight is: " + str(playField.height), 1, (0, 255, 0))
    # window.blit(debug, (200, 200))

    pygame.display.update()

pygame.quit()