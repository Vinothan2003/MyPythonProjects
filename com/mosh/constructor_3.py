class Student:
    def __init__(self, name, register_no):
        self.name = name
        self.register_no = register_no

    def display(self):
        print(f"Name : {self.name}")
        print(f"Register No : {self.register_no}")
        print("--------------")


student_1 = Student("Vinothan NC", 2002141)
student_1.display()

student_2 = Student("Allah ", 2002142)
student_2.display()

student_3 = Student("Jesus",2002143)
student_3.display()

student_4 = Student("Kadavul", 2002144)
student_4.display()