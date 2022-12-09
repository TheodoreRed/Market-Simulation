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


asset = Asset(0, 10, True)
asset2 = Asset(1, 25, True)
asset3 = Asset(2, 37, True)
list1 = []
list1.append(asset)
list1.append(asset2)
list1.append(asset3)
choice = random.choice(list1)
print(choice.is_volatile)
