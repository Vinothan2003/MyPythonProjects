password  = "password123"
user_input = input("Enter your password : ")
while user_input != password:
    print("Password does not match!! try again")
    user_input = input("Enter your password correctly : ")
else :
    print("matched")
