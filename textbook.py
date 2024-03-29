# Elizabeth Fuller
# 11/20/19
# Textbook class

from person import Person


class Textbook(Person):
    def __init__(self, title, first, last, age, edition, isbn_number, publisher, year, inventory, price):
        # init textbook object. send parameters to person class to create author
        super().__init__(first, last, age)
        self.title = title
        self.edition = edition
        self.isbn_number = isbn_number
        self.publisher = publisher
        self.year = year
        self.inventory = inventory
        self.price = price

    def add_inventory(self, new_stock):
        # add more stock to inventory. return statement to say how much inventory is available
        self.inventory = int(self.inventory)
        self.inventory = self.inventory + new_stock
        return "Inventory is now " + str(self.inventory)

    def deduct_inventory(self, lost_stock):
        # add more stock to inventory.
        self.inventory = int(self.inventory)
        self.inventory = self.inventory - lost_stock
        warning = " "
        if self.inventory < 5:
            warning = "Warning inventory is low!"
        # return statement to say how much inventory is available and a warning if it is lower than 5
        return "Inventory is now " + str(self.inventory) + "\n" + warning

    def description(self):
        # method to overwrite description method of person class
        description = self.title + " " + self.edition + " edition, by " + self.first + " " + self.last + ". ISBN: " + self.isbn_number + ". Published by " + self.publisher + " in the year " + self.year+". Price: $" + self.price + " Inventory: " + self.inventory

        return description
