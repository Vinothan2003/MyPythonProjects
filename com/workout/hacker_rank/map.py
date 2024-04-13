# Define a function
def square(x):
    return x ** 2


# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Apply the function to each item in the list using map()
squared_numbers = map(square, numbers)
# for num in squared_numbers:
#     print(num)

# Convert the iterator to a list to see the results
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
