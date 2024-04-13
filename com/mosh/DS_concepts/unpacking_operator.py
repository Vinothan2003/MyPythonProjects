# unpacking operator --> used unpack items in the iterable
# *args --> for list, tuple and set
# **kwargs --> for dictionary

names = ["Vinothan", "Tmail Kadavul", "Jesus God"]
print(*names)  # sending arbitrary arguments to the print function

words = ("hello", "world")
print(*words)

details = dict(name="Vinothan", age=20, phone=8778786481)
# print(**details) cannot print unpack dictionary
another_details = dict(name="Tamil", age=10, phone=1, address="unknown")
combine = {**details, **another_details}
print(combine)

unpack = [(key, value) for key, value in details.items()]
print(unpack)
