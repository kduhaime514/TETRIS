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

    # Returns the position (in pixels) of the provided coordinate
    # Assumes the coordinate plane starts at (0,0), in the upper left of the window
    # Returns the pixel position of the upper left corner of the corresponding grid cell
    def getPosition(self, coord):
        return coord*self.gridLength

    def addBlock(self):
        # TODO
        foo = "bar"

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
                block.draw(window, self, 0, 0)
                y+=1
            y=0
            x+=1

    def __drawBlocks(self, window):
        for block in self.blocks:
            foo = "bar"

    def draw(self, window):
        # Draw white background of play area
        # TODO - probably not needed
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))

        # Draw Grid
        self.__drawGrid(window)
        
        # TODO - draw blocks too!

    