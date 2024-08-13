# Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw, and check the balance.
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Withdraw {amount}. New balance is {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdraw {amount}. New balance is {self.__balance}."
        elif amount > self.__balance:
            return "Insufficient balance."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return self.__balance
