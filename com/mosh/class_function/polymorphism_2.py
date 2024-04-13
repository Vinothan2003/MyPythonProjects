# Polymorphism --> doing the same task in different ways

# Method overloading can be achieved in python using default arguments
def method_overloading(a=None, b=None):
    print(f"result : {a + b}")


method_overloading(10, 20)
method_overloading("Hello", "World")
method_overloading("Vinothan", "NC")
