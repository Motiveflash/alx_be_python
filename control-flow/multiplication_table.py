#Prompt User for a Number to be multiply
number = int(input("Enter a number to see its multiplication table: "))

#Generate and Print the Multiplication Table
result = 0
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")