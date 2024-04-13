class Human:
    def __init__(self, name, age, gender, weight, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

    def bmi(self):
        try:
            print(f"Name : {self.name}")
            print(f"Age: {self.age}")
            print(f"Gender : {self.gender}")
            height_meter = self.height / 100
            bmi_result = self.weight / (height_meter ** 2)
            if bmi_result < 18.5:
                print(f"BMI 'under Weight' : {bmi_result:.2f}")
                print("""    You must put on weight.    """)
                return '-' * 40
            elif 18.5 <= bmi_result <= 24.9:
                print(f"BMI 'Normal Weight' : {bmi_result:.2f}")
                print("""    You are in right weight; keep going.    """)
                return '-' * 40
            elif 25.0 <= bmi_result <= 29.9:
                print(f"BMI 'Over Weight' : {bmi_result:.2f}")
                print("""    You have to reduce some weight     """)
                return '-' * 40
            else:
                print(f"Your Obese {bmi_result:.2f}")
                print("""      You must sincerely lose weight. Otherwise your health in danger     """)
                return '-' * 40
        except ZeroDivisionError:
            print("Height (or) Weight cannot be zero!!".center(40))
            return '-' * 40


while True:
    try:
        while True:
            user_name = input("Enter your Name : ").upper()
            if len(user_name) == 0:
                print("Name field cannot be Empty".center(30))
            else:
                break
        user_age = int(input("Enter your Age : "))
        while True:
            user_gender = input("Enter your Gender : ").upper()
            if len(user_gender) == 0:
                print("Gender field cannot be empty".center(30))
            else:
                break
        user_weight = float(input("Enter your wight in KG : "))
        user_height = float(input("Enter your height in centimeters : "))
        print()
        bmi_calculate = Human(user_name, user_age, user_gender, user_weight, user_height)
        print(bmi_calculate.bmi())
        print()
        user_answer = input("Continue Yes or No : ").lower()
        if user_answer == "no":
            break
    except ValueError:
        print("Invalid Value!!".center(50))
        print("please enter proper values for AGE, WEIGHT and HEIGHT fields".center(70))
        print('-' * 50)
