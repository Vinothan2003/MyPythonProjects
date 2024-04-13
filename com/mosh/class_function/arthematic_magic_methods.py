class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)


point_1 = Point(10, 20)
point_2 = Point(5, 5)

result_add = point_1 + point_2
print((result_add.x, result_add.y))

result_sub = point_1 - point_2
print((result_sub.x, result_sub.y))

result_mul = point_1 * point_2
print((result_mul.x, result_mul.y))
