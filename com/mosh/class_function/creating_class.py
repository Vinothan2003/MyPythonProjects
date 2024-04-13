class Human:
    # name = "Vinothan"   --> using setarr() method
    # age = 20            --> using ( . ) operator
    def walk(self):
        print("Walking..")

    def jog(self):
        print("Jogging..")


person = Human()
person.walk()
print(type(person))
print(isinstance(person, float))  # checking person is instance of class

person.jog()

print(setattr(Human, "name", "Vinothan"))
print(Human.__dict__)

Human.age = 20
print(getattr(Human, 'age'))
print(Human.__dict__)
