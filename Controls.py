import pygame
import sys
sys.path.append('./classes')
from Direction import Direction

def handleEvents(events, dropShape):
    run = True 

    for event in events:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dropShape.move(Direction.LEFT)
            if event.key == pygame.K_RIGHT:
                dropShape.move(Direction.RIGHT) 
            if event.key == pygame.K_UP:
                dropShape.rotate()
            if event.key == pygame.K_DOWN:
                dropShape.move(Direction.DOWN)

    return run