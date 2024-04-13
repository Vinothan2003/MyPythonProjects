# namedtuple --> use when the class only have data(attributes)
#            --> they are immutable (cannot assign or change the date(attributes) value

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])  # class only contain attributes..
point1 = Point(x=1, y=2)
# point1.x = 10 cannot assign or change value because its immutable
point2 = Point(x=1, y=2)
print(point1 - point2)

"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point1 = Point(1, 2)
point2 = Point(1, 2)
print(point1 == point2)
"""
