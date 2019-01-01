import pygame
import constant
from Block import Block
from ShapeType import ShapeType
from Direction import Direction
from Grid import Grid

class Shape():
    def __init__(self, grid, shapeType, xOffset, yOffset):
        self.grid = grid

        if(shapeType == ShapeType.LINE):
            block1 = Block(self.grid.gridLength, xOffset + 0, yOffset + 0, (66, 134, 244))
            block2 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (66, 134, 244))
            block3 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (66, 134, 244))
            block4 = Block(self.grid.gridLength, xOffset + 3, yOffset + 0, (66, 134, 244))
        elif(shapeType == ShapeType.SQUARE):
            block1 = Block(self.grid.gridLength, xOffset + 0, yOffset + 0, (244, 223, 66))
            block2 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (244, 223, 66))
            block3 = Block(self.grid.gridLength, xOffset + 0, yOffset + 1, (244, 223, 66))
            block4 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (244, 223, 66))
        elif(shapeType == ShapeType.CORNER):
            block1 = Block(self.grid.gridLength, xOffset + 0, yOffset + 0, (0, 33, 255))
            block2 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (0, 33, 255))
            block3 = Block(self.grid.gridLength, xOffset + 0, yOffset + 1, (0, 33, 255))
            block4 = Block(self.grid.gridLength, xOffset + 0, yOffset + 2, (0, 33, 255))
        elif(shapeType == ShapeType.CORNER_MIRROR):
            block1 = Block(self.grid.gridLength, xOffset + 0, yOffset + 0, (255, 114, 0))
            block2 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (255, 114, 0))
            block3 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (255, 114, 0))
            block4 = Block(self.grid.gridLength, xOffset + 1, yOffset + 2, (255, 114, 0))
        elif(shapeType == ShapeType.STEP):
            block1 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (9, 198, 25))
            block2 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (9, 198, 25))
            block3 = Block(self.grid.gridLength, xOffset + 0, yOffset + 1, (9, 198, 25))
            block4 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (9, 198, 25))
        elif(shapeType == ShapeType.STEP_MIRROR):
            block1 = Block(self.grid.gridLength, xOffset + 0, yOffset + 0, (255, 0, 25))
            block2 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (255, 0, 25))
            block3 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (255, 0, 25))
            block4 = Block(self.grid.gridLength, xOffset + 2, yOffset + 1, (255, 0, 25))
        elif(shapeType == ShapeType.TRIANGLE):
            block1 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (114, 0, 255))
            block2 = Block(self.grid.gridLength, xOffset + 0, yOffset + 1, (114, 0, 255))
            block3 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (114, 0, 255))
            block4 = Block(self.grid.gridLength, xOffset + 2, yOffset + 1, (114, 0, 255))
        self.blocks = [block1, block2, block3, block4]

    def rotate(self):
        # TODO 
        foo = "bar"

    def move(self, direction):
        if (direction == Direction.DOWN):
            # TODO - handle actual drop mechanics
            for block in self.blocks:
                block.yCoord += 1
        elif (direction == Direction.LEFT):
            for block in self.blocks:
                block.xCoord -= 1
        elif (direction == Direction.RIGHT):
            for block in self.blocks:
                block.xCoord += 1

    def draw(self, window):
        for block in self.blocks:
            block.draw(window, self.grid)