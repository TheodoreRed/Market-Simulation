import random
import names
import os

os.system("cls")


class Asset:
    def __init__(self, current_price, is_volatile, uniqueID):
        self.uniqueID = uniqueID
        self.current_price = current_price
        self.is_volatile = is_volatile
        self.name = names.get_last_name()[0:4].upper()

    def display(self):
        print("--------------------------")
        print("UniqueID :      {}".format(self.uniqueID))
        print("Current price : {}".format(self.current_price))
        print("Is Volatile :   {}".format(self.is_volatile))
        print("Name :          {}".format(self.name))

        # print(self.uniqueID, self.current_price, self.is_volatile, self.name)

    def get_true_false(self):
        T_or_F = random.randint(0, 1)
        if T_or_F == 0:
            return False
        else:
            return True


class Stock(Asset):
    def __init__(self, current_price, is_volatile, uniqueID):
        Asset.__init__(self, current_price, is_volatile, uniqueID)

    def is_black_swan_event(self):
        if random.randint(1, 10) == 10:
            return True
        else:
            return False

    def one_day(self):
        rate_change_up = 0.0073
        rate_change_down = 0.00735368188
        if self.is_volatile:
            if self.get_true_false():
                if self.is_black_swan_event():
                    rate_change_up *= random.randint(1, 10)
                rate_change_up *= random.randint(0, 2)
                change = rate_change_up * self.current_price
                self.current_price += change
            else:
                if self.is_black_swan_event():
                    rate_change_down *= random.randint(1, 9)
                rate_change_down *= random.randint(0, 2)
                change = rate_change_down * self.current_price
                self.current_price -= change
        else:
            if self.get_true_false():
                change = rate_change_up * self.current_price
                self.current_price += change
            else:
                change = rate_change_down * self.current_price
                self.current_price -= change


stock = Stock(100, False, 0)
stock.display()

stock.one_day()
stock.display()
for x in range(1000):
    stock.one_day()
print("-  -   -   -")
stock.display()
