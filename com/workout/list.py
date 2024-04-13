""""
LIST [] --> used to store multiple values in a single variable
        --> ordered , changeable , duplicate are allowed
        --> list items are indexed
"""

car = ["BMW", "Honda", "Tata", "Toyota", "Mercedes"]

cars = car.copy()

# car[0] = "Benz"


# car.insert(0,"Audi") ---> These are list methods
car.append("Skoda")
car.sort()
car.remove("Tata")
car.pop()
print(car.count("Honda"))
# car.clear()
# print(car[0])


print(dir(car))  # dir() --> using this function we can see different methods that can perform
print(help(car))  # help() --> using this function we can see description of the methods and attributes

print(len(cars))
print(car)
print("Ferrari" in car)
