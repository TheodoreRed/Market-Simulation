import random
import names
import os

os.system("cls")


class Asset:
    def __init__(self, uniqueID, current_price, is_volatile):
        self.uniqueID = uniqueID
        self.current_price = current_price
        self.is_volatile = is_volatile
        self.name = names.get_last_name()[0:4].upper()

    def display(self):
        print(self.uniqueID, self.current_price, self.is_volatile)
