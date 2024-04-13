from abc import ABC, abstractmethod


# Custom exception for invalid operations
class InvalidOperationError(Exception):
    pass


# Abstract base class for bank accounts
class BankAccount(ABC):
    def __init__(self, account_number, account_balance=5000):
        self.account_no: int = account_number
        self.account_balance: float = account_balance

    @property
    def balance(self):
        return f"Your account balance : {self.account_balance}"

    @abstractmethod
    def deposit_amount(self, deposit_amount):
        pass

    @abstractmethod
    def with_draw_amount(self, with_amount):
        pass


# Concrete class for a savings account
class SavingAccount(BankAccount):

    # Property to get balance for savings account
    @property
    def balance(self):
        return f"Your account balance in Savings Account : {self.account_balance}"

    # Method to deposit amount into savings account
    def deposit_amount(self, deposit_amount):
        print(f"₹{deposit_amount} amount deposited successfully to 'Saving Account'..")
        self.account_balance += deposit_amount

    # Method to withdraw amount from savings account
    def with_draw_amount(self, with_amount):
        if with_amount > self.account_balance:
            raise InvalidOperationError("Insufficient balance.")
        print(f"₹{with_amount} withdraw successfully using 'Saving Account'..")
        self.account_balance -= with_amount


# Concrete class for a credit card account
class CreditCardAccount(BankAccount):

    # Property to get balance for a credit card account
    @property
    def balance(self):
        return f"Your account balance in Credit Card Account : {self.account_balance}"

    # Method to deposit amount into credit card account
    def deposit_amount(self, deposit_amount):
        print(f"₹{deposit_amount} amount deposited successfully to 'Credit Card Account'..")
        self.account_balance += deposit_amount

    # Method to withdraw amount from credit card account
    def with_draw_amount(self, with_amount):
        if with_amount > self.account_balance:
            raise InvalidOperationError("Insufficient balance.")
        print(f"₹{with_amount} withdraw successfully using 'Credit Card Account'..")
        self.account_balance -= with_amount


# Function to perform deposit or withdrawal based on user input
def amount(account_type):
    try:
        user_input: str = input("Amount --> DEPOSIT | WITHDRAW : ").lower().strip()

        if account_type == "savings account" or user_input == "saving account":

            if user_input == "deposit":
                user_account: int = int(input(f"Enter Your Account Number ({account_type}): "))
                user_amount: float = float(input(f"Enter Amount to Deposit ({account_type}) :  "))

                if user_amount < 0:
                    raise InvalidOperationError("Enter Proper Deposit Amount.")

                savings = SavingAccount(user_account)
                savings.deposit_amount(user_amount)
                print(savings.balance)
                print_line()

            elif user_input == "withdraw":

                user_account: int = int(input("Enter Your Account Number : "))
                user_amount: float = float(input(f"Enter Amount to Withdraw ({account_type}) :  "))
                savings = SavingAccount(user_account)

                savings.with_draw_amount(user_amount)
                print(savings.balance)
                print_line()

            else:
                print("Invalid Operation")

        elif account_type == "credit card":

            if user_input == "deposit":

                user_account: int = int(input(f"Enter Your Account Number ({account_type}) : "))
                user_amount: float = float(input(f"Enter Amount to Deposit ({account_type}) : "))
                if user_amount < 0:
                    raise InvalidOperationError("Enter Proper Deposit Amount.")
                credit = CreditCardAccount(user_account)
                credit.deposit_amount(user_amount)
                print(credit.balance)
                print_line()

            elif user_input == "withdraw" or user_input == "with draw":

                user_account: int = int(input("Enter Your Account Number : "))
                user_amount: float = float(input(f"Enter Amount to Withdraw ({account_type}) :  "))
                credit = CreditCardAccount(user_account)

                credit.with_draw_amount(user_amount)
                print(credit.balance)
                print_line()

            else:
                print("Invalid Operation")

    except ValueError:
        print_line()
        print("Enter Proper Value for Account number | Deposit Amount | Withdraw Amount")
        print_line()
    except InvalidOperationError as e:
        print(f"Error: {e}")


# Function to handle user interaction and initiate transactions
def information():
    print_line()
    print("Welcome to NCV Bank")
    print_line()
    while True:
        user_response = "yes"
        try:
            if user_response == "yes":
                account_type: str = input("Account Type > ( Savings Account | Credit Card ) : ").lower().strip()
                if account_type == "savings account":
                    amount(account_type)
                elif account_type == "credit card":
                    amount(account_type)
                else:
                    print("Only Two Account types are Available.")

                user_response = input("You want make another transaction Yes | No : ").lower().strip()

                if user_response == "no":
                    print_line()
                    print("Thanks appreciate your transaction with our NCV bank.")
                    print_line()
                    quit()

        except InvalidOperationError as e:
            print(f"Error: {e}")


# Function to print a line separator
def print_line():
    print('-' * 40)


# Call the main function to start the program
information()
