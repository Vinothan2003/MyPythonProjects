# Polymorphism --> Doing the same task in different ways
# Polymorphism types --> overloading and overriding

# overloading --> operator overloading and
#                 method overloading (method overloading can be achieved in python using default argument)
from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def with_draw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SavingAccount(Account):
    def with_draw(self):
        print("Withdraw amount using 'saving account'")

    def deposit(self):
        print("Deposit amount using 'saving account'")


class CheckingAccount(Account):
    def with_draw(self):
        print("Withdraw amount using 'checking account'")

    def deposit(self):
        print("Deposit amount using 'checking account'")


class CreditCardAccount(Account):
    def with_draw(self):
        print("Withdraw amount using 'credit card account'")

    def deposit(self):
        print("deposit amount using 'credit card account'")


def amount(account_type):  # account_type = None (default argument)
    for account in account_type:
        account.with_draw()
        account.deposit()


saving_account = SavingAccount()
checking_count = CheckingAccount()
credit_card_account = CreditCardAccount()
amount([saving_account, checking_count, credit_card_account])
