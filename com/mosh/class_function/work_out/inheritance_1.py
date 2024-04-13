class Pet:
    def __init__(self, name, age, breed):
        self.__name = name
        self.__age = age
        self.__breed = breed

    def info(self):
        print(f"Pet Name : {self.__name}")
        print(f"Pet Age : {self.__age}")
        print(f"Pet Breed : {self.__breed}")

    def walk(self):
        print("walking..")

    def talk(self):
        print("Hello Human!!")


class Dog(Pet):

    def bark(self):
        print(f"'{dog_name}'Barking..")


class Cat(Pet):
    def hissing(self):
        print(f"'{cat_name}'Hissing..")


class Bird(Pet):
    def fly(self):
        print(f"'{bird_name}' Flying..")


def print_line():
    print('-' * 30)


user_response = "yes"
print("Welcome to Pet Adoption Center")
while True:
    if user_response == "yes":
        user_input = input("> Dog | Cat | Bird : ").lower()
        try:
            if user_input == "dog":
                print("Please fill the Adoption Form.")
                dog_name = input("Enter Dog Name : ")
                dog_age = int(input("Enter Dog Age : "))
                if dog_age < 0:
                    raise ValueError
                dog_Breed = input("Enter Dog Breed : ")
                dog = Dog(dog_name, dog_age, dog_Breed)
                print_line()
                dog.info()
                dog.bark()
                dog.talk()
            elif user_input == "cat":
                print("Please fill the Adoption Form.")
                cat_name = input("Enter cat Name : ")
                cat_age = int(input("Enter cat Age : "))
                if cat_age < 0:
                    raise ValueError
                cat_Breed = input("Enter cat Breed : ")
                cat = Cat(cat_name, cat_age, cat_Breed)
                print_line()
                cat.info()
                cat.hissing()
                cat.talk()
            elif user_input == "bird":
                print("Please fill the Adoption Form.")
                bird_name = input("Enter Bird Name : ")
                bird_age = int(input("Enter Bird Age : "))
                if bird_age < 0:
                    raise ValueError
                bird_breed = input("Enter Bird Breed : ")
                print_line()
                bird = Bird(bird_name, bird_age, bird_breed)
                bird.info()
                bird.fly()
                bird.talk()
            else:
                print("There is no such pets are there!!")
                continue
        except ValueError:
            print("Invalid Value Please Enter Proper Values")
            continue
    elif user_response == "no":
        break
    else:
        print("I dont understand!")
    user_response = input("You Want Adopt Another pet Yes | No : ").lower()
    print_line()

print("Thank you for the Adoption")
