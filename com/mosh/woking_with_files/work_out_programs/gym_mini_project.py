from gym.utils.validation import error_msg, greetings, Verification
from gym.members_data.member_details import GymMembers
from gym.data_base.gym_details import GymDataBase
from datetime import *
import time


def package_selection():
    user_package_selection = input("Payment Selection ( Month(M) | Year(Y) ) : ").upper().strip()
    try:
        if user_package_selection == "M":
            print("""
            -- GYM MONTHLY CHARGE --
            1 Month  --> ₹ 1,000 (MIN)
            3 Months --> ₹ 3,000
            6 Months --> ₹ 6,000
            9 Months --> ₹ 9,000 (MAX)
            -------------------------
            """)
            user_payment_month = int(input("How Many Months : "))
            result = Verification.package_validation(package=user_package_selection, value=user_payment_month)
            if result:
                amount = user_payment_month * 1000
                print(f"Need to Pay : ₹{user_payment_month * 1000: ,}")
                user_paid_amount = int(input("--> Amount : ₹"))
                if Verification.payment_validation(required_amount=amount, user_amount=user_paid_amount):
                    today = date.today()
                    new_month = (today.month + user_payment_month) % 12
                    new_year = today.year + ((today.month + user_payment_month) // 12)
                    validity_date = date(year=new_year, month=new_month, day=today.day).isoformat()
                    return user_paid_amount, validity_date, user_package_selection

        elif user_package_selection == "Y":
            print("""
            -- GYM YEARLY CHARGE --
            1 Year  --> ₹ 10,000 (MIN)
            2 Years --> ₹ 20,000
            3 Years --> ₹ 30,000 (MAX)
            -------------------------
            """)
            user_payment_yearly = int(input("How Many Years : "))
            result = Verification.package_validation(package=user_package_selection, value=user_payment_yearly)
            if result:
                amount = user_payment_yearly * 10000
                print(f"Need to Pay : ₹{user_payment_yearly * 10000: ,}")
                user_paid_amount = int(input("--> Amount : ₹"))
                if Verification.payment_validation(required_amount=amount, user_amount=user_paid_amount):
                    today = date.today()
                    validity_year = today.year + user_payment_yearly
                    validity_date = date(year=validity_year, month=today.month, day=today.day).isoformat()
                    return user_paid_amount, validity_date, user_package_selection
        else:
            error_msg("Invalid Action")
    except ValueError:
        print("-- Enter proper value ( Amount | Months )--")


class Members:

    def member_ship(self):

        try:
            gym_id = int(input("> Gym-ID : "))
            access = GymMembers.existing_member(gym_id)
            if access:
                gym_database = GymDataBase()
                today = date.today()
                validity = datetime.strptime(access[1], '%Y-%m-%d').date()
                t = time.localtime()
                formatted_time = time.strftime('%I:%M:%S', t)
                session = time.strftime('%p', t)
                if today < validity:
                    gym_database.login_info(gym_id=gym_id, log_date=today.isoformat(), log_time=formatted_time,
                                            log_session=session)
                else:
                    error_msg("Gym Package expired")
                    user_recharge = input("Recharge the Gym Package Yes | No : ").lower().strip()
                    if user_recharge == "yes":
                        result = package_selection()
                        gym_member = GymMembers()
                        gym_member.update_package(gym_id=gym_id, amount=result[0], validity=result[1],
                                                  package=result[2])

        except ValueError:
            print("-- Provide Proper Gym ID --")

    def new_member_ship(self):

        try:
            user_name = input("--> Your Name : ").lower().strip()
            user_age = int(input("--> Your Age : "))
            user_gender = input("--> Your Gender ( Male | Female ) : ").lower().strip()
            user_contact_no = int(input("--> Your Contact Number : "))
            user_aadhar_no = int(input("--> Your Aadhar Number : "))
            result = Verification.details_validation(name=user_name, age=user_age, gender=user_gender,
                                                     contact_no=user_contact_no,
                                                     aadhar_no=user_aadhar_no)
            if result:
                user_amount = package_selection()
                GymMembers.new_member_data(name=user_name, age=user_age, gender=user_gender, contact_no=user_contact_no,
                                           aadhar_no=user_aadhar_no, package=user_amount[2],
                                           amount=user_amount[0], valid_date=user_amount[1])

        except ValueError:
            print("-- Provide proper value for required fields --")


def main() -> None:
    user_response = 'no'
    member = Members()

    while True:
        if user_response == 'no':
            greetings("NCV GYM")
            print("--- Welcome Champ ---".center(31))
            user_input = input("Do Have Member-ship ( Yes | No ) : ").lower().strip()
            if user_input == 'yes':
                member.member_ship()
            elif user_input == "no":
                member.new_member_ship()
            else:
                error_msg("Invalid Input")
        elif user_response == 'yes':
            greetings("Leaving NCV GYM")
            quit()
        else:
            error_msg("Invalid Action")

        user_response = input("Want to Exit ( Yes | No ) : ").lower().strip()


if __name__ == '__main__':
    main()
