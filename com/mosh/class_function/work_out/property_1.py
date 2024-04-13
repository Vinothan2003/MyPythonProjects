"""class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def bank_balance(self):
        return f"Your account Balance : {self.__balance}"

    def deposit(self, value):
        if value > 0:
            self.__balance += value
            print(f"Bank balance : {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, value):
        if value <= 0 and value >= self.__balance:
            print("Insufficient account balance or Invalid amount")
        else:
            self.__balance -= value
            print(f"Amount withdraw : {value} \nBank balance : {self.__balance}")


person = BankAccount(1000)
print(person.bank_balance)

person.deposit(1000)

person.withdraw(200)
"""