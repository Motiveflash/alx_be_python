# Class Methods and Static Methods

class Calculator:
    calculation_type = "Arithmetic Operations"

    #Add static method that returns the sum of two numbers
    @staticmethod
    def add(a, b):
        return a + b
    
    #Add class method that return the product of two numbers
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b