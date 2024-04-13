values = [0, 1, 2, 3, 4, 5]

number_map = list(map(lambda num: num * 2, values))
number_com = [num * 2 for num in values]

print(f"map function : {number_map}")
print(f"map comprehension : {number_com}")


def function(n):
    return lambda a: a * n


fun = function(10)  # n = 10
print(fun(2))  # a =2
