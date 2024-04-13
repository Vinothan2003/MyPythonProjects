number = []
# sum_numbers = 0

for i in range(1, 6):  # GETTING USER INPUT AND STORING IN THE LIST
    num = int(input("Enter a number :"))
    number.append(num)
print(number)

"""for j in number:
    sum_numbers = sum_numbers + j"""
sum_numbers = sum(number)

avg = sum_numbers / len(number)

print(f"Sum of number : {sum_numbers}")
print(f"Average of numbers : {avg}")
