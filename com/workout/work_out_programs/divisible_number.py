number_list = [10, 12, 20, 35, 64, 60, 70]

number = int(input("Enter a number : "))

"""result_comprehension = [x for x in number_list if (x % number) == 0]
print(f"The number {number} divisible {result_comprehension}")"""

# map function it will return the new iterative items
# filter function : it will return the new iterative items if conditions satisfy
result = list(filter(lambda x: (x % number == 0), number_list))
print(f"{number} : {result}")
