class Human:
    company = "amazon"  # class attributes --> these attributes belong to both class and object property
    # changing value to class attribute visible to the all instance or object

    def __init__(self, name, age):
        self.name = name  # instance attributes --> these attributes belong to object
        self.age = age  # instance attributes

    def employee(self):
        print(f"Employee Name : {self.name}, Age : {self.age}, Company : {self.company}")


user_name = input("Enter Name : ")
user_age = int(input("Enter Age : "))
person_1 = Human(name=user_name, age=user_age)
person_1.employee()


print(person_1.__dict__)
person_1.company = "TCS"  # Creating the instance attribute value in instance namespace using instance or object
print(person_1.__dict__)

Human.company = "Facebook"  # changing the class attribute value --> it will be visible to all instance
print(Human.__dict__)

person_1.employee()

person_2 = Human(name="Jesus", age=100000000)
person_2.employee()
