import pygame
import constant
from Block import Block
from ShapeType import ShapeType
from Grid import Grid

class Shape():
    def __init__(self, grid, shapeType, xCoord, yCoord):
        self.grid = grid

        if(shapeType == ShapeType.LINE):
            block1 = Block(self.grid.gridLength, 0, 0, (66, 134, 244))
            block2 = Block(self.grid.gridLength, 1, 0, (66, 134, 244))
            block3 = Block(self.grid.gridLength, 2, 0, (66, 134, 244))
            block4 = Block(self.grid.gridLength, 3, 0, (66, 134, 244))
        elif(shapeType == ShapeType.SQUARE):
            block1 = Block(self.grid.gridLength, 0, 0, (244, 223, 66))
            block2 = Block(self.grid.gridLength, 1, 0, (244, 223, 66))
            block3 = Block(self.grid.gridLength, 0, 1, (244, 223, 66))
            block4 = Block(self.grid.gridLength, 1, 1, (244, 223, 66))
        elif(shapeType == ShapeType.CORNER):
            block1 = Block(self.grid.gridLength, 0, 0, (0, 33, 255))
            block2 = Block(self.grid.gridLength, 1, 0, (0, 33, 255))
            block3 = Block(self.grid.gridLength, 0, 1, (0, 33, 255))
            block4 = Block(self.grid.gridLength, 0, 2, (0, 33, 255))
        elif(shapeType == ShapeType.CORNER_MIRROR):
            block1 = Block(self.grid.gridLength, 0, 0, (255, 114, 0))
            block2 = Block(self.grid.gridLength, 1, 0, (255, 114, 0))
            block3 = Block(self.grid.gridLength, 1, 1, (255, 114, 0))
            block4 = Block(self.grid.gridLength, 1, 2, (255, 114, 0))
        elif(shapeType == ShapeType.STEP):
            block1 = Block(self.grid.gridLength, 1, 0, (9, 198, 25))
            block2 = Block(self.grid.gridLength, 2, 0, (9, 198, 25))
            block3 = Block(self.grid.gridLength, 0, 1, (9, 198, 25))
            block4 = Block(self.grid.gridLength, 1, 1, (9, 198, 25))
        elif(shapeType == ShapeType.STEP_MIRROR):
            block1 = Block(self.grid.gridLength, 0, 0, (255, 0, 25))
            block2 = Block(self.grid.gridLength, 1, 0, (255, 0, 25))
            block3 = Block(self.grid.gridLength, 1, 1, (255, 0, 25))
            block4 = Block(self.grid.gridLength, 2, 1, (255, 0, 25))
        elif(shapeType == ShapeType.TRIANGLE):
            block1 = Block(self.grid.gridLength, 1, 0, (114, 0, 255))
            block2 = Block(self.grid.gridLength, 0, 1, (114, 0, 255))
            block3 = Block(self.grid.gridLength, 1, 1, (114, 0, 255))
            block4 = Block(self.grid.gridLength, 2, 1, (114, 0, 255))
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.blocks = [block1, block2, block3, block4]
        
    def draw(self, window):
        shapeXPosition = self.grid.getPosition(self.xCoord)
        shapeYPosition = self.grid.getPosition(self.yCoord)

        for block in self.blocks:
            block.draw(window, self.grid, shapeXPosition, shapeYPosition)