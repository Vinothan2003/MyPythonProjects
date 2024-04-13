class Person:
    def __init__(self, name):
        self.name = name
        print(name)

    def talk(self):
        print(f"talk")

    def myself(self):
        print(f"Hi i am {self.name}")


human = Person("Vinothan NC")
human.talk()
human.myself()
