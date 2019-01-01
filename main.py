import pygame
import constant

import sys
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

def spawnNewShape():
    return Shape(grid, ShapeType.getRandom(), 4, 0)
dropShape = spawnNewShape()

dropRate = constant.STARTING_DROP_RATE
clock = 0
tickRate = 100
run = True
while run:
    clock+=tickRate
    pygame.time.delay(tickRate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dropShape.move(Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                dropShape.move(Direction.RIGHT)
    
    # Drop logic
    if not clock%dropRate:
        if not grid.shapeReachedBottom(dropShape):
            dropShape.move(Direction.DOWN)
        else:
            grid.addBlocks(dropShape.blocks)
            dropShape = spawnNewShape()

    grid.draw(window)
    dropShape.draw(window)
    
    # debug = myFont.render("playFieldHeight is: " + str(playField.height), 1, (0, 255, 0))
    # window.blit(debug, (200, 200))

    pygame.display.update()

pygame.quit()