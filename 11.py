# Create a class Account with private attributes balance. Provide public methods to deposit and withdraw money.
class Account:
    def __del__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance is {self.__balance}."

        else:
            return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdraw {amount}. New balance is  {self.__balance}"
        elif amount > self.__balance:
            return "Withdraw amount must be positive."

    def get_balance(self):
        return self.__balance