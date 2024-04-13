addition = lambda x, y, z: x + y + z
print(f"addition : {addition(x=10, y=20, z=5)}")
print("-" * 10)

multiple = lambda x, y: x * y
print(f"multiplication : {multiple(10, 10)}")
print("-" * 10)

numbers = [1, 2, 3, 4, 5]
square_num = tuple(map(lambda x: pow(x, 2), numbers))
print(square_num)
