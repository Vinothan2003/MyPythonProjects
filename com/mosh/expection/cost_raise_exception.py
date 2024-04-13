from timeit import timeit

code1 = """def function(age):
    if age <= 0:
        return None
    return 10 / age


try:
    result = function(-1)
except ValueError as error:
    pass     
"""

code2 = """def function_2(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = function_2(-1)
if xfactor == None:
    pass
"""

print("first program", timeit(code1, number=10000))
print("second program", timeit(code2, number=10000))
