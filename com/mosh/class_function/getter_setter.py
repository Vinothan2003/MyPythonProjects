class Fruits:
    def __init__(self, name):
        self.__name = name
        self.set_name(name)

    def get_name(self):
        print(f"{self.__name} was accessed!")
        return self.__name

    def set_name(self, value):
        if value.isdigit():
            print("Provide a proper fruit name")
        else:
            print(f"{self.__name} is set to {value}")
            self.__name = value

    def del_name(self):
        print(f"{self.__name} is deleted!")
        del self.__name


banana = Fruits("Banana")
banana.get_name()

banana.set_name("Orange")

banana.del_name()

banana.get_name()




