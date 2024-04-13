class Person:
    def __init__(self, name, age):
        self.name = name
        self.age    = age

    def __str__(self):
        print(type(self.age))
        return f"Your Name : {self.name}, Age : {self.age}"


person_1 = Person(name="Vinothan NC", age=20)
print(person_1)
print(type(person_1.age))
