import os

os.system("cls")


class Buyer:
    def __init__(self, startingAmount, name):
        self.uninvested = startingAmount
        self.invested = 0
        self.name = name
        self.all_assets = set()

    def new_position(self, new_asset, quantity):
        isNew = True
        for asset in self.all_assets:
            if new_asset.name == asset.name:
                isNew = False
                if type(new_asset) != type(asset):
                    isNew = True

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
            if type(asset) == type_asset:
                if asset.name == name:
                    self.uninvested -= asset.current_price * quantity
                    self.invested += asset.current_price * quantity
                    asset.quantity += quantity

    def subtract_from_position():
        pass

    def close_position():
        pass


class Stock:
    def __init__(self, name, current_price):
        self.name = name
        self.current_price = current_price
        self.quantity = 0


class Bond:
    def __init__(self, name, face_value, rate):
        self.name = name
        self.current_price = int(0.5 * face_value)
        self.rate = rate
        self.quantity = 0


RECENT_AVG_RATE = 0.0689
ted = Buyer(10000, "Ted")
ted.new_position(Stock("MSFT", 255), 3)
ted.new_position(Stock("AAPL", 149), 1)
ted.new_position(Bond("USA", 100, RECENT_AVG_RATE), 10)
ted.new_position(Stock("USA", 6), 10)

ted.add_to_position(Bond, "USA", 10)
ted.add_to_position(Stock, "USA", 190)


for asset in ted.all_assets:
    if type(asset) == Stock:
        the_type = "Stock"
    elif type(asset) == Bond:
        the_type = "Bond"
    print(
        "{} {} : There are {} at a price of ${} dollars each".format(
            the_type, asset.name, asset.quantity, asset.current_price
        )
    )
print(
    "In cash still: ${} Total invested: ${} Buyer name: {}".format(
        ted.uninvested, ted.invested, ted.name
    )
)
