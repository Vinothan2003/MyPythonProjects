try:
    """ with open("welcome.txt", "w") as file:  # Overriding the file using write
         file.write("Hello welcome to the world")"""

    with open("welcome.txt", "a") as file:
        file.write("i am Vinothan NC")
    with open("welcome.txt", "r") as file:
        for line in file:
            print(line)

except FileNotFoundError:
    print("File Not Found")
