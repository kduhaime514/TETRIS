import constant
import sys

sys.path.append('./classes')
from ShapeType import ShapeType
from Shape import Shape
from Line import Line


def spawnNewShape(grid):
    if constant.TEST_ROTATE_MODE:
        return Line(grid)
    else:
        shapeType = ShapeType.getRandom()
        if (shapeType == ShapeType.LINE):
            return Line(grid)
        else:
            return Shape(grid, shapeType)