# Class of bank acount
class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount <= 0: # Check if deposit amount is less than or equal to zero(0)
            print("Invalid amount, should be greater that zero(0)")
        else:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")