class Temperature:
    def __init__(self, celsius=None, fahrenheit=None):
        self.__celsius = celsius
        self.__fahrenheit = fahrenheit

    @property
    def temp_celsius(self):
        self.__fahrenheit = (self.__celsius * 9 / 5) + 32
        return f"Temperature fahrenheit : {self.__fahrenheit}"

    @property
    def temp_fahrenheit(self):
        self.__celsius = (self.__fahrenheit - 32) * 5 / 9
        return f"Temperature in celsius : {self.__celsius}"

    @temp_celsius.setter
    def temp_celsius(self, value) -> None:
        print(f"Updated Temperature {self.__celsius} : {value}  ")
        self.__celsius = value
        self.__fahrenheit = (self.__celsius * 9 / 5) + 32

    @temp_fahrenheit.setter
    def temp_fahrenheit(self, value) -> None:
        print(f"Updated Temperature {self.__fahrenheit} : {value}  ")
        self.__fahrenheit = value
        self.__celsius = (self.__fahrenheit - 32) * 5 / 9


def temp(temp_input):
    temperature = 0
    if temp_input == "c":
        temperature = float(input("Temperature in Celsius : "))
    elif temp_input == "f":
        temperature = float(input("Temperature in Fahrenheit : "))
    return temperature


user_response = "yes"
while user_response != "no":
    if user_response == "yes":
        user_input = input("Enter temperature C | F : ").lower()
        if user_input == "c":
            celsius_temp = temp(user_input)
            object_1 = Temperature(celsius=celsius_temp)
            print(object_1.temp_celsius)
        elif user_input == "f":
            fahrenheit_temp = temp(user_input)
            object_1 = Temperature(fahrenheit=fahrenheit_temp)
            print(object_1.temp_fahrenheit)
        else:
            print("Invalid input!!")
            continue
    user_response = input("You want to continue Yes | No :").lower()
else:
    print("bye...")
