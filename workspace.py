import os
import random
import names

# os.system("cls")


class Buyer:
    def __init__(self, starting_amount, name, is_risky):
        self.uninvested = starting_amount
        self.invested = 0
        self.name = name
        self.all_assets = set()
        self.is_risky = is_risky

    def new_position(self, new_asset, quantity):
        isNew = True
        for asset in self.all_assets:
            if new_asset.name == asset.name and type(new_asset) == type(asset):
                isNew = False

        if isNew:
            total_equity = new_asset.current_price * quantity

            # If you have the money
            if self.uninvested >= total_equity:
                self.uninvested -= total_equity
                self.invested += total_equity
                self.all_assets.add(new_asset)
                new_asset.quantity += quantity

            else:
                print("not enough money")
        else:
            print("Not a new position")

    def add_to_position(self, type_asset, name, quantity):
        for asset in self.all_assets:
            if self.uninvested >= asset.current_price * quantity:
                if asset.the_type == type_asset:
                    if asset.name == name:
                        self.uninvested -= asset.current_price * quantity
                        self.invested += asset.current_price * quantity
                        asset.quantity += quantity
            else:
                print("not enough money")

    def close_position(self, asset):
        val_of_asset = asset.current_price * asset.quantity
        self.uninvested += val_of_asset
        self.invested -= val_of_asset
        self.all_assets.remove(asset)

    def subtract_from_position(self, type_asset, name, quantity):
        copy_all_assets = self.all_assets
        for asset in self.all_assets:

            # type and name create a unique key
            if asset.the_type == type_asset:
                if asset.name == name:
                    if quantity >= asset.quantity:
                        self.close_position(asset)
                        break
                    else:
                        self.uninvested += asset.current_price * quantity
                        self.invested -= asset.current_price * quantity
                        asset.quantity -= quantity
                        break

    def display(self):
        print("{}'s Current Portfolio".format(self.name))
        for asset in self.all_assets:

            print(
                "{} {} : {} of this asset at a price of ${} dollars each".format(
                    asset.the_type, asset.name, asset.quantity, asset.current_price
                )
            )
        print(
            "In cash : ${} Invested: ${} Buyer: {} Risky: {}\n".format(
                self.uninvested, self.invested, self.name, self.is_risky
            )
        )


class Retail(Buyer):
    def __init__(self, starting_amount, name, is_risky):
        Buyer.__init__(self, starting_amount, name, is_risky)


class HedgeFund(Buyer):
    def __init__(self, starting_amount, name, is_risky):
        Buyer.__init__(self, starting_amount, name, is_risky)


class Asset:
    def __init__(self, name, current_price, is_volatile):
        self.name = name
        self.current_price = current_price
        self.quantity = 0.0
        self.is_volatile = is_volatile

        def val_of_asset(self):
            return self.current_price * self.quantity


class Stock(Asset):
    def __init__(self, name, current_price, is_volatile):
        Asset.__init__(self, name, current_price, is_volatile)
        self.the_type = "Stock"


class Bond(Asset):
    def __init__(self, name, current_price, is_volatile, rate):
        Asset.__init__(self, name, current_price, is_volatile)
        self.the_type = "Bond"
        self.rate = rate


class Crypto(Asset):
    def __init__(self, name, current_price, is_volatile):
        Asset.__init__(self, name, current_price, is_volatile)
        self.the_type = "Crypto"


class Market:
    def __init__(self, num_buyers, num_assets):

        self.all_buyers = set()
        self.all_assets = set()

        def get_unique_bond_name():
            bond_name = names.get_last_name()[0:3].upper()
            if len(self.all_assets) == 0:
                return bond_name
            for asset in self.all_assets:
                if asset.name == bond_name and asset.the_type == "Bond":
                    get_unique_bond_name()
            return bond_name

        def get_random_Bond():
            bond_price = 50
            rate = random.uniform(0, 1)
            name = get_unique_bond_name()
            return Bond(name, bond_price, False, rate)

        def get_unique_stock_name():
            stock_name = names.get_last_name()[0:4].upper()
            if len(self.all_assets) == 0:
                return stock_name
            for asset in self.all_assets:
                if asset.name == stock_name and asset.the_type == "Stock":
                    get_unique_stock_name()
            return stock_name

        def get_true_false():
            T_or_F = random.randint(0, 1)
            if T_or_F == 0:
                return False
            else:
                return True

        def get_random_Stock():
            name = get_unique_stock_name()
            price = random.randint(1, 500)
            T_or_F = get_true_false()
            return Stock(name, price, T_or_F)

        while len(self.all_assets) < num_assets:
            if len(self.all_assets) % 2 == 0:
                self.all_assets.add(get_random_Bond())
            else:
                self.all_assets.add(get_random_Stock())
            # self.all_assets.add(names.get_first_name())

        def get_random_name():
            name = names.get_last_name()
            for buyer in self.all_buyers:
                if buyer.name == name:
                    get_random_name()
            return name

        while len(self.all_buyers) < num_buyers:
            temp = get_random_name()

            T_or_F = random.randint(0, 1)
            if T_or_F == 0:
                T_or_F = False
            else:
                T_or_F = True

            if len(self.all_buyers) % 3 == 0:
                temp += "_Capital"
                starting_amount = random.randint(1000000, 1000000000)
                self.all_buyers.add(HedgeFund(starting_amount, temp, T_or_F))
            else:
                starting_amount = random.randint(1000, 250000)
                self.all_buyers.add(Retail(starting_amount, temp, T_or_F))


market = Market(12, 10)
for x in market.all_buyers:
    pass  # print(x.display())

for x in market.all_assets:
    if hasattr(x, "rate"):
        print(x.name, x.the_type, x.rate)
    else:
        print(x.name, x.the_type, x.current_price)


def main():
    ted = Retail(100000, "Ted", False)

    ted.new_position(Stock("MSFT", 255, True), 3)
    ted.new_position(Stock("AAPL", 149, True), 15)
    ted.new_position(Bond("USA", 50), 12)
    ted.new_position(Stock("USA", 6, False), 100)

    ted.add_to_position("Bond", "USA", 11)
    ted.add_to_position("Stock", "USA", 191)

    ted.subtract_from_position("Stock", "AAPL", 1)
    ted.subtract_from_position("Stock", "USA", 224)

    ted.display()
    ted.add_to_position("Stock", "MSFT", 4)
    ted.new_position(Crypto("BTC", 17019), 4)

    ted.display()
    ted.subtract_from_position("Crypto", "BTC", 2)
    ted.display()
