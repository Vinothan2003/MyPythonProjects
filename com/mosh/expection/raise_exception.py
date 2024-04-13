# raise --> raising exception. raising exception is costly

def function(age):
    if age <= 0:
        raise ValueError("age cannot be less than or equal to 0")
    return 10 / age


try:
    age = int(input("Enter age : "))
    result = function(age)
    print(result)
except ValueError as error:
    print(error)
