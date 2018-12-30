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
