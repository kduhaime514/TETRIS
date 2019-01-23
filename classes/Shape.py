import pygame
import constant
from Block import Block
from ShapeType import ShapeType
from Direction import Direction
from Grid import Grid
from Rotation import Rotation

class Shape():
    def __init__(self, grid, shapeType, xOffset = constant.SPAWN_X, yOffset = -1):
        self.grid = grid
        self.shapeType = shapeType
        self.rotation = Rotation.NORTH

        if (shapeType != ShapeType.LINE):
            # TODO - won't need any of the below when we create super classes
            if (shapeType == ShapeType.SQUARE):
                block1 = Block(self.grid.gridLength, xOffset + 1, yOffset - 1, (244, 223, 66))
                block2 = Block(self.grid.gridLength, xOffset + 2, yOffset - 1, (244, 223, 66))
                block3 = Block(self.grid.gridLength, xOffset + 1, yOffset, (244, 223, 66))
                block4 = Block(self.grid.gridLength, xOffset + 2, yOffset, (244, 223, 66))
            elif (shapeType == ShapeType.CORNER):
                block1 = Block(self.grid.gridLength, xOffset + 0, yOffset - 1, (0, 33, 255))
                block2 = Block(self.grid.gridLength, xOffset + 0, yOffset, (0, 33, 255))
                block3 = Block(self.grid.gridLength, xOffset + 1, yOffset, (0, 33, 255))
                block4 = Block(self.grid.gridLength, xOffset + 2, yOffset, (0, 33, 255))
            elif (shapeType == ShapeType.CORNER_MIRROR):
                block1 = Block(self.grid.gridLength, xOffset + 2, yOffset - 1, (255, 114, 0))
                block2 = Block(self.grid.gridLength, xOffset + 0, yOffset, (255, 114, 0))
                block3 = Block(self.grid.gridLength, xOffset + 1, yOffset, (255, 114, 0))
                block4 = Block(self.grid.gridLength, xOffset + 2, yOffset, (255, 114, 0))
            elif (shapeType == ShapeType.STEP):
                block1 = Block(self.grid.gridLength, xOffset + 1, yOffset - 1, (9, 198, 25))
                block2 = Block(self.grid.gridLength, xOffset + 2, yOffset - 1, (9, 198, 25))
                block3 = Block(self.grid.gridLength, xOffset + 0, yOffset, (9, 198, 25))
                block4 = Block(self.grid.gridLength, xOffset + 1, yOffset, (9, 198, 25))
            elif (shapeType == ShapeType.STEP_MIRROR):
                block1 = Block(self.grid.gridLength, xOffset + 0, yOffset - 1, (255, 0, 25))
                block2 = Block(self.grid.gridLength, xOffset + 1, yOffset - 1, (255, 0, 25))
                block3 = Block(self.grid.gridLength, xOffset + 1, yOffset, (255, 0, 25))
                block4 = Block(self.grid.gridLength, xOffset + 2, yOffset, (255, 0, 25))
            elif (shapeType == ShapeType.TRIANGLE):
                block1 = Block(self.grid.gridLength, xOffset + 1, yOffset - 1, (114, 0, 255))
                block2 = Block(self.grid.gridLength, xOffset + 0, yOffset, (114, 0, 255))
                block3 = Block(self.grid.gridLength, xOffset + 1, yOffset, (114, 0, 255))
                block4 = Block(self.grid.gridLength, xOffset + 2, yOffset, (114, 0, 255))
            self.blocks = [block1, block2, block3, block4]

    def rotate(self):
        # TODO - check to see if I CAN rotate

        if(self.shapeType == ShapeType.LINE):
            if(self.rotation == Rotation.NORTH):
                self.rotation = Rotation.EAST
                self.blocks[0].xCoord = self.blocks[0].xCoord + 2
                self.blocks[0].yCoord = self.blocks[0].yCoord - 1
                self.blocks[1].xCoord = self.blocks[1].xCoord + 1
                self.blocks[1].yCoord = self.blocks[1].yCoord
                self.blocks[2].xCoord = self.blocks[2].xCoord
                self.blocks[2].yCoord = self.blocks[2].yCoord + 1
                self.blocks[3].xCoord = self.blocks[3].xCoord - 1
                self.blocks[3].yCoord = self.blocks[3].yCoord + 2
            elif(self.rotation == Rotation.EAST):
                self.rotation = Rotation.SOUTH
                self.blocks[0].xCoord = self.blocks[0].xCoord + 1
                self.blocks[0].yCoord = self.blocks[0].yCoord + 2
                self.blocks[1].xCoord = self.blocks[1].xCoord
                self.blocks[1].yCoord = self.blocks[1].yCoord + 1
                self.blocks[2].xCoord = self.blocks[2].xCoord - 1
                self.blocks[2].yCoord = self.blocks[2].yCoord
                self.blocks[3].xCoord = self.blocks[3].xCoord - 2
                self.blocks[3].yCoord = self.blocks[3].yCoord - 1
            elif(self.rotation == Rotation.SOUTH):
                self.rotation = Rotation.WEST
                self.blocks[0].xCoord = self.blocks[0].xCoord - 2
                self.blocks[0].yCoord = self.blocks[0].yCoord + 1
                self.blocks[1].xCoord = self.blocks[1].xCoord - 1
                self.blocks[1].yCoord = self.blocks[1].yCoord + 0
                self.blocks[2].xCoord = self.blocks[2].xCoord + 0
                self.blocks[2].yCoord = self.blocks[2].yCoord - 1
                self.blocks[3].xCoord = self.blocks[3].xCoord + 1
                self.blocks[3].yCoord = self.blocks[3].yCoord - 2
            elif(self.rotation == Rotation.WEST):
                self.rotation = Rotation.NORTH
                self.blocks[0].xCoord = self.blocks[0].xCoord - 1
                self.blocks[0].yCoord = self.blocks[0].yCoord - 2
                self.blocks[1].xCoord = self.blocks[1].xCoord
                self.blocks[1].yCoord = self.blocks[1].yCoord - 1
                self.blocks[2].xCoord = self.blocks[2].xCoord + 1
                self.blocks[2].yCoord = self.blocks[2].yCoord
                self.blocks[3].xCoord = self.blocks[3].xCoord + 2
                self.blocks[3].yCoord = self.blocks[3].yCoord + 1
        # elif(self.shapeType == ShapeType.SQUARE):
        #     block1 = Block(self.grid.gridLength, xOffset + 1, yOffset - 1, (244, 223, 66))
        #     block2 = Block(self.grid.gridLength, xOffset + 2, yOffset - 1, (244, 223, 66))
        #     block3 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (244, 223, 66))
        #     block4 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (244, 223, 66))
        # elif(self.shapeType == ShapeType.CORNER):
        #     block1 = Block(self.grid.gridLength, xOffset + 0, yOffset - 1, (0, 33, 255))
        #     block2 = Block(self.grid.gridLength, xOffset + 0, yOffset + 0, (0, 33, 255))
        #     block3 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (0, 33, 255))
        #     block4 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (0, 33, 255))
        # elif(self.shapeType == ShapeType.CORNER_MIRROR):
        #     block1 = Block(self.grid.gridLength, xOffset + 3, yOffset - 1, (255, 114, 0))
        #     block2 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (255, 114, 0))
        #     block3 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (255, 114, 0))
        #     block4 = Block(self.grid.gridLength, xOffset + 3, yOffset + 0, (255, 114, 0))
        # elif(self.shapeType == ShapeType.STEP):
        #     block1 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (9, 198, 25))
        #     block2 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (9, 198, 25))
        #     block3 = Block(self.grid.gridLength, xOffset + 0, yOffset + 1, (9, 198, 25))
        #     block4 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (9, 198, 25))
        # elif(self.shapeType == ShapeType.STEP_MIRROR):
        #     block1 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (255, 0, 25))
        #     block2 = Block(self.grid.gridLength, xOffset + 2, yOffset + 0, (255, 0, 25))
        #     block3 = Block(self.grid.gridLength, xOffset + 2, yOffset + 1, (255, 0, 25))
        #     block4 = Block(self.grid.gridLength, xOffset + 3, yOffset + 1, (255, 0, 25))
        # elif(self.shapeType == ShapeType.TRIANGLE):
        #     block1 = Block(self.grid.gridLength, xOffset + 1, yOffset + 0, (114, 0, 255))
        #     block2 = Block(self.grid.gridLength, xOffset + 0, yOffset + 1, (114, 0, 255))
        #     block3 = Block(self.grid.gridLength, xOffset + 1, yOffset + 1, (114, 0, 255))
        #     block4 = Block(self.grid.gridLength, xOffset + 2, yOffset + 1, (114, 0, 255))

    def move(self, direction):
        # TODO - handle holding button down!!

        if (direction == Direction.DOWN):
            if not self.grid.shapeReachedBottom(self):
                for block in self.blocks:
                    block.yCoord += 1
        elif (direction == Direction.LEFT):
            if (self.grid.shapeCanMoveSideways(self, Direction.LEFT)):
                for block in self.blocks:
                    block.xCoord -= 1
        elif (direction == Direction.RIGHT):
            if (self.grid.shapeCanMoveSideways(self, Direction.RIGHT)):
                for block in self.blocks:
                    block.xCoord += 1

    def draw(self, window):
        for block in self.blocks:
            block.draw(window, self.grid)