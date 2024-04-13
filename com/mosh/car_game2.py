conformation = ""
car_is_started = False
while True:  # conformation != "quit":
    conformation = input("--> ").lower()
    if conformation == "start":
        if car_is_started:
            print("the car is already started!!")
        else:
            car_is_started = True
            print("the car is started...")
    elif conformation == "stop":
        if not car_is_started:
            print("the car is alredy stopped!!")
        else:
            car_is_started = False
            print("the car is stopped...")
    elif conformation == "help need":
        print("""
Start - to start the car 
Stop - to stop the car
 Quit - to quit 
        """)
    elif conformation == "quit":
        break
    else:
        print("i don' understand")
