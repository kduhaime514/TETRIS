import constant
from Shape import Shape
from ShapeType import ShapeType
from Block import Block
from Rotation import Rotation
from ShapeRotationIndices import ShapeRotationIndices

# TODO - create shape objects for other shapes as well
class Line(Shape):
    def __init__(self, grid, xOffset = constant.SPAWN_X, yOffset = -1):
        super().__init__(grid, ShapeType.LINE, xOffset, yOffset)

        self.color = (66, 134, 244)


        # TODO - finish this thought and plug it in...
        rotationIndexList = [
            (Rotation.NORTH, 0, 2, -1),
            (Rotation.NORTH, 1, 1, 0),
            (Rotation.NORTH, 2, 0, 1),
            (Rotation.NORTH, 3, -1, 2),

            (Rotation.EAST, 0, 1, 2),
            (Rotation.EAST, 1, 0, 1),
            (Rotation.EAST, 2, -1, 0),
            (Rotation.EAST, 3, -2, -1),

            (Rotation.SOUTH, 0, -2, 1),
            (Rotation.SOUTH, 1, -1, 0),
            (Rotation.SOUTH, 2, 0, -1),
            (Rotation.SOUTH, 3, 1, -2),

            (Rotation.WEST, 0, -1, -2),
            (Rotation.WEST, 1, 0, -1),
            (Rotation.WEST, 2, 1, 0),
            (Rotation.WEST, 3, 2, 1)
        ]

        self.rotationIndices = ShapeRotationIndices(rotationIndexList)

        block1 = Block(self.grid.gridLength, xOffset + 0, yOffset, self.color)
        block2 = Block(self.grid.gridLength, xOffset + 1, yOffset, self.color)
        block3 = Block(self.grid.gridLength, xOffset + 2, yOffset, self.color)
        block4 = Block(self.grid.gridLength, xOffset + 3, yOffset, self.color)
        self.blocks = [block1, block2, block3, block4]

    # TODO - should be able to move this up into Shape in the end
    def rotate(self):



        if (self.rotation == Rotation.NORTH):
            self.rotation = Rotation.EAST
            self.blocks[0].xCoord = self.blocks[0].xCoord + 2
            self.blocks[0].yCoord = self.blocks[0].yCoord - 1

            self.blocks[1].xCoord = self.blocks[1].xCoord + 1
            self.blocks[1].yCoord = self.blocks[1].yCoord

            self.blocks[2].xCoord = self.blocks[2].xCoord
            self.blocks[2].yCoord = self.blocks[2].yCoord + 1

            self.blocks[3].xCoord = self.blocks[3].xCoord - 1
            self.blocks[3].yCoord = self.blocks[3].yCoord + 2
        elif (self.rotation == Rotation.EAST):
            self.rotation = Rotation.SOUTH
            self.blocks[0].xCoord = self.blocks[0].xCoord + 1
            self.blocks[0].yCoord = self.blocks[0].yCoord + 2

            self.blocks[1].xCoord = self.blocks[1].xCoord
            self.blocks[1].yCoord = self.blocks[1].yCoord + 1

            self.blocks[2].xCoord = self.blocks[2].xCoord - 1
            self.blocks[2].yCoord = self.blocks[2].yCoord

            self.blocks[3].xCoord = self.blocks[3].xCoord - 2
            self.blocks[3].yCoord = self.blocks[3].yCoord - 1
        elif (self.rotation == Rotation.SOUTH):
            self.rotation = Rotation.WEST
            self.blocks[0].xCoord = self.blocks[0].xCoord - 2
            self.blocks[0].yCoord = self.blocks[0].yCoord + 1

            self.blocks[1].xCoord = self.blocks[1].xCoord - 1
            self.blocks[1].yCoord = self.blocks[1].yCoord + 0

            self.blocks[2].xCoord = self.blocks[2].xCoord + 0
            self.blocks[2].yCoord = self.blocks[2].yCoord - 1

            self.blocks[3].xCoord = self.blocks[3].xCoord + 1
            self.blocks[3].yCoord = self.blocks[3].yCoord - 2
        elif (self.rotation == Rotation.WEST):
            self.rotation = Rotation.NORTH
            self.blocks[0].xCoord = self.blocks[0].xCoord - 1
            self.blocks[0].yCoord = self.blocks[0].yCoord - 2

            self.blocks[1].xCoord = self.blocks[1].xCoord
            self.blocks[1].yCoord = self.blocks[1].yCoord - 1

            self.blocks[2].xCoord = self.blocks[2].xCoord + 1
            self.blocks[2].yCoord = self.blocks[2].yCoord

            self.blocks[3].xCoord = self.blocks[3].xCoord + 2
            self.blocks[3].yCoord = self.blocks[3].yCoord + 1
