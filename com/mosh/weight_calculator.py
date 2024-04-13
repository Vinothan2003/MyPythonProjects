weight = input("Enter your weight :")

weights = input("Weight in KG or LBS :")

if weights.lower() == "k":
    pounds = int(weight) * 2.20
    print(f"your weight in pound {pounds }")
else:
    kilogram = int(weight) * 0.45
    print(f"your weight in kilogram : {kilogram}")