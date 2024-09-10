#Personal Finance Calculator

#Input data by prompting user and declearing variables for monthly income and monthly expenses
monthly_income = int(input("Enter your monthly income: ")) #Monthly income
monthly_expenses = int(input("Enter your monthly expenses: ")) #monthly expenses

#calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

#Project Annual savings
rate = 0.05 #5% annualy
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Printing monthly savings and projected savings 
print(f"Your monthly savings are {monthly_savings}.")
print(f"Projected savings after one year, with interest, is: {int(projected_savings)}.")