def myfunc(n):
    return lambda a: a * n


double = myfunc(2)
print(double(11))

triple = myfunc(3)
print(triple(11))
