# class attributes --> two ways to get the class attributes
#                  --> getattr() method, dot method
class Student:
    name = "Vinothan NC"
    age = 20


# getattr() method --> used to get the attribute value
print(getattr(Student, "name"))
print(getattr(Student, 'phone_no', 8778786481))

# . dot notation --> used to get the attribute value
print(Student.age)
Student.city = "Madurai"

# setattr method --> used to set new attribute or change the attribute value
setattr(Student, "gender", 'Male')
print(Student.gender)

# delattr method and dot notation --> deleting the attribute
delattr(Student, "city")
del Student.gender

print(Student.__dict__)