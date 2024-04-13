word = input("").strip()
print(len(word))
print(f"Start - to start the car")
print(f"Stop - to stop the car")
print(f"quit - quit from the car")

response = 0
owner_conformation = 5
while response < owner_conformation:
    car = input("")
    response += 1
    if car.lower() == "start":
        print(f"car started....")
        break
    elif car.lower() == "stop":
        print(f"car is stopped....")
        break
    elif car.lower() == "quit":
        print(f"quit from the car")
        break
    else:
        print(f"I DON'T UNDERSTAND")
else:
    print("Your are not the owner")