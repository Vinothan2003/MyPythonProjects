# use array when dealing with performance problem otherwise use list and tuple

# array --> take less memory and faster than list (when dealing with large numbers (i.e) 10,000)

from array import array

number = array("I", [1, 2, 3, 4, 5])
number.append(6)
number.insert(0, 7)
print(number)

number.pop()
number.remove(7)
print(number)

print(number.count(1))



