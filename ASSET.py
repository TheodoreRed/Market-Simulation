import random
import names
import os

os.system("cls")


class Asset:
    def __init__(self, uniqueID, current_price, is_volatile):
        self.uniqueID = uniqueID
        self.current_price = current_price
        self.is_volatile = is_volatile
