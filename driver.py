# Elizabeth Fuller
# 11/20/19
# main code to test textbook class

from textbook import Textbook

# enter info for first book
print("Enter data for text book:")
title = input("Title:\n>")
first = input("Author's first name:\n>")
last = input("Author's last name:\n>")
age = input("Author's age:\n>")
edition = input("Edition:\n>")
isbn_number = input("ISBN Number:\n>")
publisher = input("Publisher:\n>")
year = input("Year published:\n>")
inventory = input("Quantity in inventory:\n>")
price = input("Price:\n>")
# create book object
book1 = Textbook(title, first, last, age, edition, isbn_number, publisher, year, inventory, price)

# enter info for second book
print("Enter data for next text book:")
title2 = input("Title:\n>")
first2 = input("Author's first name:\n>")
last2 = input("Author's last name:\n>")
age2 = input("Author's age:\n>")
edition2 = input("Edition:\n>")
isbn_number2 = input("ISBN Number:\n>")
publisher2 = input("Publisher:\n>")
year2 = input("Year published:\n>")
inventory2 = input("Quantity in inventory:\n>")
price2 = input("Price:\n>")
# create book object
book2 = Textbook(title2, first2, last2, age2, edition2, isbn_number2, publisher2, year2, inventory2, price2)

# menu with data modification options
print("Menu:")
print("Modify Textbook Description [1]\nPrint Textbook Description [2]\nUpdate Textbook Inventory [3]")
choose = input("> ")
# Modify textbook info. ask for textbook to modify. will ask if they want to modify each part.
if choose == "1":
    print(f"Modify {title} [1]\nModify {title2} [2]")
    choice = input("> ")
    # modify first book
    if choice == "1":
        print("Each part of the textbook that can be changed will be prompted.\nTo change it type y, otherwise type n.\n")
        print("Change Title:")
        change = input("> ")
        if change == "y":
            title = input("Enter new title:\n> ")
        print("Change Author:")
        change = input("> ")
        if change == "y":
            first = input("Enter Author's first name:\n> ")
            last = input("Enter Author's last name:\n> ")
            age = input("Enter Author's age:\n> ")
        print("Change Edition:")
        change = input("> ")
        if change == "y":
            edition = input("Enter new edition:\n> ")
        print("Change ISBN:")
        change = input("> ")
        if change == "y":
            isbn_number = input("Enter new ISBN:\n> ")
        print("Change Publisher")
        change = input("> ")
        if change == "y":
            publisher = input("Enter new publisher:\n> ")
        print("Change year published:")
        change = input("> ")
        if change == "y":
            year = input("Enter new year published:\n> ")
        print("Change total stock:")
        change = input("> ")
        if change == "y":
            inventory = input("Enter new stock total:\n> ")
        print("Change Price:")
        change = input("> ")
        if change == "y":
            price = input("Enter new price:\n> ")
        book1 = Textbook(title, first, last, age, edition, isbn_number, publisher, year, inventory, price)
    # modify 2nd book
    elif choice == "2":
        print("Each part of the textbook that can be changed will be prompted.\nTo change it type y, otherwise type n.\n")
        print("Change Title:")
        change = input("> ")
        if change == "y":
            title2 = input("Enter new title:\n> ")
        print("Change Author:")
        change = input("> ")
        if change == "y":
            first2 = input("Enter Author's first name:\n> ")
            last2 = input("Enter Author's last name:\n> ")
            age2 = input("Enter Author's age:\n> ")
        print("Change Edition:")
        change = input("> ")
        if change == "y":
            edition2 = input("Enter new edition:\n> ")
        print("Change ISBN:")
        change = input("> ")
        if change == "y":
            isbn_number2 = input("Enter new ISBN:\n> ")
        print("Change Publisher")
        change = input("> ")
        if change == "y":
            publisher2 = input("Enter new publisher:\n> ")
        print("Change year published:")
        change = input("> ")
        if change == "y":
            year2 = input("Enter new year published:\n> ")
        print("Change total stock:")
        change = input("> ")
        if change == "y":
            inventory2 = input("Enter new stock total:\n> ")
        print("Change Price:")
        change = input("> ")
        if change == "y":
            price2 = input("Enter new price:\n> ")
        book2 = Textbook(title2, first2, last2, age2, edition2, isbn_number2, publisher2, year2, inventory2, price2)
    else:
        print("Bye")
# print descriptions of book
elif choose == "2":
    print(f"Print {title} [1]\n Print {title2} [2]")
    choice = input("> ")
    if choice == "1":
        print(book1.description())
    elif choice == "2":
        print(book2.description())
    else:
        print("Bye")
# add or remove stock. adds or removes from current stock
elif choose == "3":
    print()
    choice = input("> ")
    if choice == "1":
        print(f"For {title}:\nAdd inventory [1]\nDeduct inventory [2]")
        choice1 = input("> ")
        if choice1 == "1":
            new_stock = input("New incoming stock\n> ")
            new_stock = int(new_stock)
            inven = book1.add_inventory(new_stock)
            print(inven)
        elif choice1 == "2":
            lost =  input("Out going stock\n> ")
            lost = int(lost)
            inven = book1.deduct_inventory(lost)
            print(inven)
        else:
            print("Bye")
    if choice == "2":
        print(f"For {title2}:\nAdd inventory [1]\nDeduct inventory [2]")
        choice1 = input("> ")
        if choice1 == "1":
            new_stock = input("New incoming stock\n> ")
            new_stock = int(new_stock)
            inven = book2.add_inventory(new_stock)
            print(inven)
        elif choice1 == "2":
            lost =  input("Out going stock\n> ")
            lost = int(lost)
            inven = book2.deduct_inventory(lost)
            print(inven)
        else:
            print("Bye")
else:
    print("Bye")





