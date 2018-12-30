import pygame
import constant

class PlayField:
    def __init__(self, gridLength, windowWidth):
        self.width = constant.TOTAL_BLOCKS_X*gridLength
        self.height = constant.TOTAL_BLOCKS_Y*gridLength
        self.x = 0
        self.y = 0
