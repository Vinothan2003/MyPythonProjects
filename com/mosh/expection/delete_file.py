import os

if os.path.exists("test.txt"):
    os.remove("test.txt")  # delete the file from the folder
    print("File deleted successfully")
    # os.rmdir() to remove the folder
else:
    print("File Not Found")
