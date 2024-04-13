n = int(input("Enter an integer: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and n in range(2, 6):  # 2 <= n <= 5
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 21):  # 6 <= n <= 20
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
