# OBJECT Class --> is the base class for all classes
#              --> every class default  inherit the object class
class Animal:
    def __init__(self):
        self.name = None

    def eat(self):
        print("eating..")


class Mammal:
    def walk(self):
        print("walking..")


m = Mammal()
m.walk()
print(issubclass(Animal, object))
o = object  # OBJECT Class --> is the base class for classes

print(isinstance(Mammal, object))