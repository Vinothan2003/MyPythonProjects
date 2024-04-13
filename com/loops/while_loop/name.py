name = input("Enter your name :")

while name == "":
    print("Name cannot be empty")
    name = input("Enter your name (Don't leave it blank):")
else:
    print(f"Hello {name}!!!")
