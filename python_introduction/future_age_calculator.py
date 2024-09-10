# User Input Age Calculator

#Prompts the user for their current age and calculate the future age in 2025
current_age = int(input("How old are you? "))
current_year = 2023
years_to_add = 2050 - current_year
age = current_age + years_to_add

print(f"In 2050, you will {age} years old.")