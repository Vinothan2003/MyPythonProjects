class Fruit:
    def __init__(self, name: str):
        self.__name = name

    @property
    def fruit_name(self):
        print(f"{self.__name} is obtained!")
        return self.__name

    @fruit_name.setter
    def fruit_name(self, value):
        print(f"{self.__name} is set to {value}")
        self.__name = value

    @fruit_name.deleter
    def fruit_name(self):
        print(f"{self.__name} is removed")
        del self.__name


fruit = Fruit("Watermelon")
print(fruit.fruit_name)

fruit.fruit_name = "mango"
print(fruit.fruit_name)

del fruit.fruit_name
