def converting_dollar(dollar, rupees=82.89):
    dollar_inr = dollar * rupees
    return f"${dollar_currency} Dollar to INR(Indian rupees) : ₹{dollar_inr:.2f}"


def converting_inr(inr, dollar=0.012):
    inr_dollar = inr * dollar
    return f"₹{indian_currency} INR(Indian rupees to Dollar) : ${inr_dollar:.2f}"


dollar_currency = 0
indian_currency = 0
while True:
    user_input = input("which currency you what covert Dollar or INR(Rupees) : ").lower()
    if user_input == "dollar":
        dollar_currency = int(input("Enter Dollar (Dollar to INR) Amount : $"))
        print(converting_dollar(dollar_currency))
        break
    elif user_input == "inr":
        indian_currency = int(input("Enter INR (INR to Dollar Amount) : ₹"))
        print(converting_inr(indian_currency))
        break
    else:
        print("I can't understand, please enter the currency properly")




