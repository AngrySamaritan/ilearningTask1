"""Module for class Person"""


class Person:
    """
    Class for person record
    """
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address

    def __str__(self):
        return self.name + " | " + self.address + " | " + self.number + "\n"