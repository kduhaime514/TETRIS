import pygame
import constant
from Block import Block

class Grid():
    def __init__(self, gridLength, windowWidth):
        self.width = constant.TOTAL_BLOCKS_X*gridLength
        self.height = constant.TOTAL_BLOCKS_Y*gridLength
        self.x = 0
        self.y = 0
        self.blocks = []
        self.gridLength = gridLength

    def shapeReachedBottom(self, shape):
        for fallingBlock in shape.blocks:
            if fallingBlock.yCoord + 1 == constant.TOTAL_BLOCKS_Y:
                return True
            for stationaryBlock in self.blocks:
                if stationaryBlock.xCoord == fallingBlock.xCoord and stationaryBlock.yCoord == fallingBlock.yCoord + 1:
                    return True
        
        return False

    # Returns the position (in pixels) of the provided coordinate
    # Assumes the coordinate plane starts at (0,0), in the upper left of the window
    # Returns the pixel position of the upper left corner of the corresponding grid cell
    def getPosition(self, coord):
        return coord*self.gridLength

    def addBlocks(self, blocks):
        self.blocks.extend(blocks)

    def clearRow(self, y):
        # TODO
        bar = "baz"

    def __drawGrid(self, window):
        # TODO - might be a performance hit to redraw this every frame. Really only need to redraw when something changes
        x = 0
        y = 0
        while x < constant.TOTAL_BLOCKS_X:
            while y < constant.TOTAL_BLOCKS_Y:
                block = Block(self.gridLength, x, y, (255, 255, 255))
                block.draw(window, self)
                y+=1
            y=0
            x+=1

    def __drawBlocks(self, window):
        for block in self.blocks:
            block.draw(window, self)

    def draw(self, window):
        self.__drawGrid(window)
        self.__drawBlocks(window)

    