def fibonacci(number):
    list_num = [0, 1]
    if number == 0:
        return f"{number} : {list_num[0]}"
    elif number == 1:
        return f"{number} : {list_num[0], list_num[1]}"
    elif number >= 2:
        for i in range(1, number + 1):
            num = list_num[-2] + list_num[-1]
            list_num.append(num)
        return f"{number} : {list_num}"


number = int(input("Enter a number :"))
result = fibonacci(number)
print(result)
