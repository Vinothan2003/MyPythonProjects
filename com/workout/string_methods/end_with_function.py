while True:
    file_name = input("Enter a file name with extension : ")
    if file_name.endswith(".py"):
        print("file is opened")
        break
    else:
        print("this not a correct file")