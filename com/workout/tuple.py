"""
TUPLE () --> ordered , unchangeable , duplicates are allowed , faster than list
"""
fruits = ("apple", "mango", "watermelon", "banana", "watermelon")

# print(dir(gods)) --> using this function we can see different methods that can perform
# print(help(gods)) --> using this function we can see description of attributes and methods
# print(len(gods))
# print("watermelon" in gods)

# print(gods.index("mango")) --> methods in tuple
# print(gods.count("watermelon"))

print(fruits)

for fruit in fruits:
    print(fruit)