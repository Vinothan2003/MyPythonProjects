password = input("Enter your password: ").lower()
chance = 1

while chance <= 3:
    if password == "password123":
        print("Password matched")
        break
    else:
        print("Password does not match. Please try again.")
        password = input("Enter your password correctly: ").lower()
    chance += 1

else:
    print("You have exceeded the number of attempts. Please try again later.")

"""while password != "password123":
    print("Password does not match TRY again !!")
    password = input("Enter your password correctly :").lower()
print("Password matched")"""
