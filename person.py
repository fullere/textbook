# Elizabeth Fuller
# 11/20/19
# Person Class


class Person:
    def __init__(self, first, last, age):
        # init person object
        self.first = first
        self.last = last
        self.age = age

    def description(self):
        # returns a str that list person values
        return self.first + " " + self.last + " is " + str(self.age) + "."
