class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


vector_1 = Vector(x=3, y=7)
vector_2 = Vector(x=10, y=3)
result = vector_1 + vector_2
print(result.x, result.y)
