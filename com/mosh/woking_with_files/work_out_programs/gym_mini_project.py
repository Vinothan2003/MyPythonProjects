from gym.utils.validation import error_msg, greetings, Verification
from gym.members_data.member_details import GymMembers


def package_selection(response):
    try:
        if response == "M":
            print("""
            -- GYM MONTHLY CHARGE --
            1 Month --> ₹ 1000 (MIN)
            3 Months --> ₹ 3000
            6 Months --> ₹ 6000
            9 Months --> ₹ 9000 (MAX)
            -------------------------
            """)
            user_payment_month = int(input("How Many Months : "))
            result = Verification.package_validation(package=response, value=user_payment_month)
            if result:
                amount = user_payment_month * 1000
                print(f"Need to Pay : ₹{user_payment_month * 1000: ,}")
                user_paid_amount = int(input("--> Amount : ₹"))
                if Verification.payment_validation(required_amount=amount, user_amount=user_paid_amount):
                    return user_paid_amount

        elif response == "Y":
            print("""
            -- GYM YEARLY CHARGE --
            1 Year --> ₹ 1000 (MIN)
            2 Years --> ₹ 3000
            3 Years --> ₹ 9000 (MAX)
            -------------------------
            """)
            user_payment_yearly = int(input("How Many Years : "))
            result = Verification.package_validation(package=response, value=user_payment_yearly)
            if result:
                amount = user_payment_yearly * 10000
                print(f"Need to Pay : ₹{user_payment_yearly * 10000: ,}")
                user_paid_amount = int(input("--> Amount : ₹"))
                if Verification.payment_validation(required_amount=amount, user_amount=user_paid_amount):
                    return user_paid_amount

    except ValueError:
        print("-- Enter proper value ( Amount | Months )--")


class Members:

    def member_ship(self):
        pass

    def new_member_ship(self):
        try:
            user_name = input("--> Your Name : ").lower().strip().replace(" ", "")
            user_age = int(input("--> Your Age : "))
            user_gender = input("--> Your Gender ( Male | Female ) : ")
            user_contact_no = int(input("--> Your Contact Number : "))
            user_aadhar_no = int(input("--> Your Aadhar Number : "))
            result = Verification.details_validation(name=user_name, age=user_age, gender=user_gender,
                                                     contact_no=user_contact_no,
                                                     aadhar_no=user_aadhar_no)
            if result:
                user_package_selection = input("Payment Selection ( Month(M) | Year(Y) ) : ").upper().strip()
                user_amount = package_selection(user_package_selection)
                GymMembers.new_member_data(name=user_name, age=user_age, gender=user_gender, contact_no=user_contact_no,
                                           aadhar_no=user_aadhar_no, package=user_package_selection, amount=user_amount)

        except ValueError:
            print("-- Provide proper value for required fields --")


def main() -> None:
    user_response = 'no'
    member = Members()

    while True:
        if user_response == 'no':
            user_input = input("Do Have Member-ship ( Yes | No ) : ").lower().strip()
            if user_input == 'yes':
                member.member_ship()
            elif user_input == "no":
                member.new_member_ship()
            else:
                error_msg("Invalid Input")
        elif user_response == 'yes':
            greetings("Thank You")
            quit()
        else:
            error_msg("Invalid Action")

        user_response = input("Want to Exit ( Yes | No ) : ").lower().strip()


if __name__ == '__main__':
    main()
