name = input("Enter your name :")

if len(name) < 8:
    print(f"Name must be at least '8 characters' : {name}")
elif len(name) > 20:
    print(f"Name must be maximum '20 characters' : {name} ")
else:
    print(f"Nice name! : {name} ")