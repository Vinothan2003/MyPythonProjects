while True:
    char = input("Enter a char value : ")
    if len(char) == 1:
        ascii_char = ord(char)
        print(f"ascii value for {char} : {ascii_char}")
        print("if you want to exit from the loop type : 'quit'")
    elif char.lower().strip() == "quit":
        break
    else:
        print(f"cannot find ascii value for {char}")


