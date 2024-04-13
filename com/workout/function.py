# type function --> 1.return function and 2.function that execute block of code
def function(name):
    print(f"Hi {name}")
    return '-' * 10


print(function("Vinothan"))


# keyword and default argument

def increment(number, by=1):  # default argument
    return number + by


result = increment(number=2, by=5)  # keyword argument
print(result)
print("-" * 10)


# arbitrary arguments
# if we don't know the no of arguments then use * in parameter
def multiply(*numbers):  # package the numbers in 'TUPLES'
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))
print("-" * 10)


# arbitrary keyword arguments
# if we don't know the no of keyword arguments then use ** in parameter
def person(**details):  # package the details in 'DICTIONARY'
    return details


print(person(name="Vinothan", age=18, phone_no=8778786481))
