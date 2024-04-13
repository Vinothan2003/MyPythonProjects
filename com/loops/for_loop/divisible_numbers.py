three_count = 0
five_count = 0
three_and_five = 0
for i in range(1,100):
    if (i % 3) == 0 and (i % 5) == 0:
        three_and_five = three_and_five + 1
        print(f"Divided by 3 and 5: {i}")
    elif (i % 3) == 0:
        three_count = three_count + 1
        print(f"Divided by 3 : {i}")
    elif (i % 5) == 0:
        five_count = five_count + 1
        print(f"Divided by 5 : {i}")
print(three_and_five)
print(three_count)
print(five_count)