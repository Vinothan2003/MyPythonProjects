number = int(input("enter an number :"))
for i in range(1, number + 1):
    if number % i == 0:
        print(f"the factors are {i} : {number}")
