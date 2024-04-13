# keyword Argument - used to specific the value
# have to use keyword Argument after the positional arguments otherwise it will show errors
# keyword argument improve the readability of the code

def shopping(item, product, quantity, price):
    print(f"item no : {item}")
    print(f"Product name : {product}")
    print(f"Quantity : {quantity}")
    print(f"Price : {price}")
    print("Total :", quantity * price)


print("Hello welcome to the Mart")
shopping(1, product="Tooth brush", quantity=5, price=20)  # used to specific the value is called keyword argument
shopping(2, product="Book", quantity=1, price=250)  # used to specific the value is called keyword argument
print("Thank you!")