while True:
    number = input("Enter ASCII Number : ")
    if number.isdigit():
        int_number = int(number)
        if int(int_number) <= 127:
            print(f"ASCII value for {number} : {chr(int_number)}")
            print(f"exit from the loop type : 'quit'")
        else:
            print(f"{number} is out of range...Enter a valid range ascii number")
    elif number.lower().strip() == "quit":
        break
    else:
        print(f"{number} is not allowed")
