#!/usr/bin/python3

shopping_list = {
        "Onion rings": 20,
        "Leffe": 40,
        "Pizza rolls": 20,
        "Chicken wings": 16
}

def add_item():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    shopping_list[item] = quantity

def remove_item():
    item = input("Enter item remove: ")
    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} removed from shopping list.")
    else:
        print(f"{item} is not in shopping list.")

def view_list():
    if not shopping_list:
        print("Shopping list is empty!")
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity}")

def clear_list():
    shopping_list.clear()
    print("Shopping list has been cleared!")

def check_item():
    item = input("Enter item to check: ")
    if item in shopping_list:
        print(f"{item} is in shopping list.")
    else:
        print(f"{item} is not in shopping list.")

def total_items():
    total = sum(shopping_list.values())
    print(f"Total number of items is {total}")

def largest_quantity_item():
    if shopping_list:
        max_item = max(shopping_list, key=shopping_list.get)
        print(f"{max_item} has the largest quantity with {shopping_list[max_item]}.")
    else:
        print("Shopping list is empty!")

def sort_list():
    if not shopping_list:
        print("Shopping list is empty!")
    sorted_list = dict(sorted(shopping_list.items()))
    for item, quantity in sorted_list.items():
        print(f"{item}: {quantity}")

def main():
    while True:
        print("")
        print("Shopping List Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Clear list")
        print("5. Check item")
        print("6. Total items")
        print("7. Item with largest quantity")
        print("8. Sort list")
        print("9. Exit")
        choice = input("*** Choose one of the options: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            clear_list()
        elif choice == "5":
            check_item()
        elif choice == "6":
            total_items()
        elif choice == "7":
            largest_quantity_item()
        elif choice == "8":
            sort_list()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please enter a valid one.")

main()

