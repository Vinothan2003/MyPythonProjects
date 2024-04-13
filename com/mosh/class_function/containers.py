class ClassRoom:
    def __init__(self):
        self.__names = {}  # __name --> __ used to make to the variable or dataset to private member

    #                               --> it can only access inside class

    def add(self, name):  # add value to dict container
        self.__names[name.lower()] = self.__names.get(name.lower(), 0) + 1

    def __getitem__(self, name):  # get value
        return self.__names.get(name.lower(), "Not found!")

    def __set__(self, name, value):  # set value
        self.__names[name.lower()] = value

    def __len__(self):  # length of the container
        return len(self.__names)

    def __iter__(self):  # iteration for container
        return iter(self.__names)


class_A = ClassRoom()
class_A.add("Vinothan")
class_A.add("Jesus")
print(class_A.__len__())
print(class_A.__getitem__("Vinothan"))
class_A.__set__("kadavul", 10)

print(class_A._ClassRoom__names)  # way to access the private variable in class

cls = class_A.__iter__()
for i in cls:
    print(i)
