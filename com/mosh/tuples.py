number = (10, 20, 25, 30)  # TUPLES () --> tuples are immutable (can't able to change) , similar to list
print(number[0])
print(number.count(20))
print(number.index(25))

another_number = 1, 2, 3, 4  # adding to tuples
print(type(another_number))
add = number + another_number
print(add)

alphabetic = tuple("Vinothan NC")  # casting to tuple
print(alphabetic)

letter = ('a', 'b', 'c') * 3  # multiplying tuple with the numbers
print(letter)
