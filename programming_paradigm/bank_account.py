# Class of bank acount

class BankAccount:
    def __init__(self, initial_balance = 0):
         self.account_balance = initial_balance

    def deposit(self, amount):
         self.account_balance += amount
         return self.account_balance

    def withdraw(self, amount):
         if amount <= self.account_balance:
              self.account_balance -= amount

    def display_balance(self):
         return self.account_balance