price = int(input("Enter the price :"))
credit = input("You have good credits ? ")

if credit.lower() == "true":
    credit = True
else:
    credit = False

if credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(credit)
print(f"Down payment : {down_payment}")