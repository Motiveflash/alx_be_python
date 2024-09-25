def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item: ")
            if item in shopping_list:
                print(f"{item} already exist")
                add = input("Would you like to keep it? Enter y for [y]es and n for [n]o ").lower()
                if add == "y":
                    shopping_list.append(item)
                else:
                    exit
            else:
                shopping_list.append(item)
        elif choice == '2':
            item = input("Enter item: ")
            if item not in shopping_list:
                print("Item dose not exist")
            else:
                shopping_list.remove(item)
                print(f"{item} has been removed")
        elif choice == '3':
            if not shopping_list:
                print("The list is empty")
            else:
                print("\nShopping list")
                for index, item in enumerate(shopping_list, start=1):
                    index = "--->"
                    print(f"{index}. {item.capitalize()}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()