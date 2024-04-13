# word = ""
car_status = False
while True:          # word != "quit":
    word = input().lower()
    if word == "start":
        if car_status:
            print("Car is already started")
        else:
            car_status = True
            print("As you wish car is started!")
    elif word == "stop":
        if not car_status:
            print("Car is already stopped")
        else:
            car_status = False
            print("As you wish car is stopped!")
    elif word == "help":
        print("""
        1.start - to start the car
        2.stop - to stop the car
        3.quit - exit from the car 
        """)
    elif word == "quit":
        break
    else:
        print("I don't understand!!")
