try:
    with open("welcome.txt", "r") as file:
        """ print(file.readline())  # it will read the file line by line
         print(file.readline(6)) # it will read the file line by give integer"""

        # print(file.readlines())  # it will read the lines and give as a list

        for line in file:    # reading the file using loop
            print(line)

except FileNotFoundError:
    print("File Not Found")
