class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


vector_1 = Vector(1, 2)
vector_2 = Vector(10, 20)
vector_3 = Vector(2, 3)
print(vector_1 < vector_3 < vector_2)
