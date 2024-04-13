# Exception handling --> to catch or handle the error
try:
    age = int(input("Enter your age : "))
    print(age)
except ValueError as exception:
    print("Invalid value")
    print(exception)
    print(type(exception))
else:
    print("No Exception arises!")  # the else will execute when try block is executed when no exception arise
print("try again execution continues")