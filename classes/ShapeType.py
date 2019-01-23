import enum
import random

class ShapeType(enum.Enum):
    LINE = 1
    SQUARE = 2
    CORNER = 3
    CORNER_MIRROR = 4
    STEP = 5
    STEP_MIRROR = 6
    TRIANGLE = 7

    def get(index):
        return ShapeType(index)

    @staticmethod
    def getRandom():
        return ShapeType(1)
        # return ShapeType(random.randint(1, 7))
