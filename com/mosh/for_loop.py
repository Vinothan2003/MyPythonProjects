prices = [10, 20, 30]  # FOR LOOP --> is a control statement that repeatedly execute a block of code
                                                    # until the condition is satisfied
total_price = 0
for price in prices:  # For loop --> iterative over item of a condition
    total_price += price  # total_price = total_price + price
print(f"total : {total_price}")

names = ['mosh', 'vinothan', 'naruto']

for loop_var in names:
    print(loop_var)

for numbers in range(0, 11, 2):
    print(numbers)

name = "Vinothan"

for number1 in name[3:]:
    print(number1)
