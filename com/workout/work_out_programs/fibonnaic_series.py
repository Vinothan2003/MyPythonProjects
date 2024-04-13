number = int(input("Enter a number :"))
list_num = [0, 1]
if number == 0:
    print(f"the fibonacci  number {number} : 0")
elif number == 1:
    print(f"the fibonacci number {number} : 0 1")
elif number >= 2:
    for i in range(1, number + 1):
        num = list_num[-2] + list_num[-1]
        list_num.append(num)
    print(f"the fibonacci number {number} : {list_num}")
else:
    print("Hello mother fucker!")