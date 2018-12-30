import pygame
import constant

class Block():
    def __init__(self, gridLength, xCoord, yCoord, color):
        self.width = gridLength
        self.height = gridLength
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.gridPos = (0, 0)
        self.color = color

    def draw(self, window, grid, xOffset, yOffset):
        blockXPosition = grid.getPosition(self.xCoord)
        blockYPosition = grid.getPosition(self.yCoord)    

        # border
        pygame.draw.rect(window, (0, 0, 0), (xOffset + blockXPosition, yOffset + blockYPosition, self.width, self.height))

        # inner square
        innerSquare = (xOffset + blockXPosition + constant.BORDER_WIDTH, yOffset + blockYPosition + constant.BORDER_WIDTH, self.width - 2*constant.BORDER_WIDTH, self.height - 2*constant.BORDER_WIDTH)
        pygame.draw.rect(window, self.color, innerSquare)