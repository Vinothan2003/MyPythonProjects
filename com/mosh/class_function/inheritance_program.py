# inheritance --> class that inherit the method and properties from another class
#             --> prevents code duplication and reusability of code
#             --> too much inheritance between the class improve the complexity of the code
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal --> parent, Base
# Mammal --> child , sub
class Mammal(Animal):
    def walk(self):
        print("walk")


# Animal --> parent, Base
# Fish --> child , sub
class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)

f = Fish()
f.eat()
f.swim()
print(m.age)
