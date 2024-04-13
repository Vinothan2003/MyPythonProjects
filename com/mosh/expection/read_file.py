try:
    # while reading the file, give the exact name of the file; otherwise it will throw exception
    with open("welcome.txt", "r") as file:  # it will automatically close the file
        print(file.read())
except FileNotFoundError:
    print("File Not Found")

