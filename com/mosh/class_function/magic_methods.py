class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Points(x=10, y=20)
print(type(point.x))
print(point)
# point.draw()
