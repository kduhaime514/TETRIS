import pygame
import constant

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

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))

        # TODO - draw grid?
        x = 0
        y = 0

        while x < constant.TOTAL_BLOCKS_X:
            while y < constant.TOTAL_BLOCKS_Y:
                pygame.draw.rect(window, (0, 0, 0), (self.getPosition(x), self.getPosition(y), self.gridLength, self.gridLength))

                # TODO - duplicated code. these could techncially be repeated "white" blocks to form the grid
                innerSquare = (self.getPosition(x) + constant.BORDER_WIDTH, self.getPosition(y) + constant.BORDER_WIDTH, self.gridLength - 2*constant.BORDER_WIDTH, self.gridLength - 2*constant.BORDER_WIDTH)
                pygame.draw.rect(window, (255, 255, 255), innerSquare)
                y+=1
            y=0
            x+=1

        # TODO - draw blocks too!