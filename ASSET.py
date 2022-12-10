import random
import names
import os

os.system("cls")


class Asset:
    def __init__(self, current_price, is_volatile, uniqueID):
        self.uniqueID = uniqueID
        self.current_price = current_price
        self.is_volatile = is_volatile

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

        def get_name():
            char1 = random.choice(names.get_last_name()).upper()
            char2 = random.choice(names.get_first_name()).upper()
            char3 = random.choice(names.get_last_name()).upper()
            char4 = random.choice(names.get_first_name()).upper()
            return char1 + char2 + char3 + char4

        self.name = get_name()

    def display(self):
        print("--------------------------")
        print("UniqueID {}  Name : {}".format(self.uniqueID, self.name))
        print("Current price : {}".format(self.current_price))
        print("Is Volatile :   {}".format(self.is_volatile))

    def get_name(self):
        return self.name

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
