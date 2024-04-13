string1 = input("Enter a password : ")
password = "jesus is the god"

string1_case_fold = string1.casefold()

if string1_case_fold == password:
    print("password is matched")
else:
    print(f"{string1_case_fold} does not match!!")