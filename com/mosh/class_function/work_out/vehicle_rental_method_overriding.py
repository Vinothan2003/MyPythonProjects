class Vehicle:
    def __init__(self):
        self.user_details = {}  # Initialize an empty dictionary to store user details

    @property
    def information(self):
        return f"Details : {self.user_details}"

    def rent(self, days):
        return 100 * days  # Calculate rent for days


class Car(Vehicle):
    def rent(self, days):
        return 1000 * days  # Calculate rent for a car


class Motorcycle(Vehicle):
    def rent(self, days):
        return days * 300  # Calculate rent for motorcycle


class Van(Vehicle):
    def rent(self, days):
        return 2000 * days  # Calculate rent for van


def print_line() -> None:
    print("-" * 30)


def details():
    user_details_information = {}  # Create an empty dictionary to store user details
    while True:
        try:
            user_name = input("Enter Your Name : ")
            user_age = int(input("Enter your Age : "))
            if user_age < 0:
                raise ValueError

            user_phone_no = input("Enter your Phone_no : ")
            if not user_phone_no.isdigit():
                raise ValueError

            user_aadhar_no = input("Enter Your Aadhar_no : ")
            if not user_aadhar_no.isdigit():
                raise ValueError

            # Store user details in the dictionary
            user_details_information["Name"] = user_name
            user_details_information["Age"] = user_age
            user_details_information["Phone_no"] = user_phone_no
            user_details_information["Aadhar_No"] = user_aadhar_no

            print_line()
            print("Rent user Details")
            for key, values in user_details_information.items():
                print(f"{key} : {values}")
            return user_details_information  # Return the user details dictionary
        except ValueError:
            print("Assign Valid Value for Age, Phone Number, Aadhar Number")


print_line()
user_response = "yes"
print("__Vehicle Rental Store__")
print("""
         __Note__
Car Rent   --> 1 Day - ₹ 1000
Motorcycle --> 1 Day - ₹ 300
Van        --> 1 Day - ₹ 2000
 """)
while True:
    try:
        if user_response == "yes":

            user_input = input("Rent > Car | Motorcycle | Van : ").lower().strip()

            if user_input.isalpha():
                # Inside the loop where the user selects to rent a car
                if user_input == "car":

                    rent_car_days = int(input("How many days : "))

                    if rent_car_days <= 0:
                        raise ValueError("Enter Proper Days!")
                    user_details_car = details()  # details() gathering user details
                    car = Car()
                    car.user_details = user_details_car  # Update user details in Car instance
                    print(car.information)
                    print("Total cost :", car.rent(rent_car_days))

                # Inside the loop where the user selects to rent a Motorcycle
                elif user_input == "motorcycle":
                    rent_motor_days = int(input("How many days : "))
                    if rent_motor_days <= 0:
                        raise ValueError("Enter Proper Days!")
                    user_details_motor = details()  # details() gathering user details
                    motor = Motorcycle()
                    motor.user_details = user_details_motor
                    print(motor.information)
                    print("Total Cost : ", motor.rent(rent_motor_days))

                # Inside the loop where the user selects to rent a Motorcycle
                elif user_input == "van":
                    user_rent_van = int(input("How many days : "))
                    if user_rent_van <= 0:
                        raise ValueError("Enter Proper Days!")
                    user_details_van = details()  # details() gathering user details
                    van = Van()
                    van.user_details = user_details_van
                    print(van.information)
                    print("Total Cost : ", van.rent(user_rent_van))

                else:
                    print("There is no such Vehicle are there")
                    continue

            else:
                print("Invalid Value!")
                continue

        elif user_response == "no":
            break

        else:
            print("Invalid input")
        user_response = input("You want rent another Vehicle Yes | No : ").lower()
        print_line()

    except ValueError:
        print("Enter Proper Values for Required Fields")

print("Thank you, Welcome Again...")
