# generator comprehension --> use when dealing with large number
# it takes less memory
# it has no length
# it will give one item at the time
from sys import getsizeof

values = [number * 2 for number in range(100000)]
print(type(values))
print(f"Byte list : {getsizeof(values)}")
"""for x in values:
    print(x, end=" ")
print()"""

values_2 = (i * 2 for i in range(100000))
print(type(values_2))
print(f"Byte generator :{getsizeof(values_2)}")
"""for x in values_2:y
    print(x, end=" ")"""
