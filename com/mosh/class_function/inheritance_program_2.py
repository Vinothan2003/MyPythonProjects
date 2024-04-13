# INHERITANCE --> class that inherit the method and properties from another
#             --> prevents code duplication and reusability of code
#             --> too much inheritance between the class increase the complexity of the code

# METHOD OVERRIDING --> if the method name of the child class as same as parent class. the instance of parent method is overridden
class Person:
    def __init__(self, f_name, s_name):
        self.f_name = f_name
        self.s_name = s_name

    def print_details(self):
        print(f"Full Name : {self.f_name} {self.s_name} ")


class Student(Person):
    def __init__(self, f_name, s_name):  # Method Overriding --> override the constructor in the base class
        super().__init__(f_name, s_name)
        # super() --> child class inherit the method and properties from its base class


student = Student("Vinothan", "NC")
student.print_details()
