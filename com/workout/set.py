"""
SETS { } --> unordered , unchangeable , we can add / remove item , no duplicate
"""

brands = {"puma", "nike", "titan", "sonata", "titan"}

# print(len(brands))
# print("audi" in brands)

# print(dir(brands)) dir () --> using this function we can see different methods that ca perform
# print((help(brands))) help () --> using this function we can see description of attributes and methods

# brands.add("vega")
# brands.remove("nike")
# brands.pop()  --> it will pop the first items
# brands.clear()

print(brands)

for brand in brands:
    print(brand)