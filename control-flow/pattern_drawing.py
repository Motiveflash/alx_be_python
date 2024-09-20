#Prompt User for a positve integer as Pattern Size
size = int(input("Enter the size of the pattern: "))

#Draw the Pattern
i = 0
while i < size:
    for j in range(size):
        print("*", end="")
    print("\n")
    i += 1