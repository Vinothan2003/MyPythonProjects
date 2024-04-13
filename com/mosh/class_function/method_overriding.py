# Method overloading --> to achieve method overloading
#                    --> Base and Derived both class should have same method.

class Animal:
    def __init__(self, name):
        print("Animal constructor is called!")
        self.name = name


class Mammal(Animal):
    def __init__(self, age, name):
        print("Mammal constructor is called!")
        self.age = age
        super().__init__(name)


m = Mammal(name="cheetah", age=20)
print(m.name)
print(m.age)
