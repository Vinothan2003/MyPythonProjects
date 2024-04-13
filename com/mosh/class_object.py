# CLASS --> is a blueprint that object follows
# OBJECT --> instance of class
class Point:  # we use class to define new types
    def move(self):  # these types have methods that contain in the body of class
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10  # it also has attributes that can be defined anywhere in the program
point1.y = 20
print(point1.x)
point1.move()
point1.draw()

point2 = Point()
point2.x = 100
point2.y = 200
point2.z = point2.x + point2.y
print(point2.z)
point2.move()
point2.draw()
