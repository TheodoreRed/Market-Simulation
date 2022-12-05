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

        if isNew:
            total_equity = new_asset.current_price * quantity
            new_asset.quantity += quantity

            # If you have the money
            if self.uninvested >= total_equity:
                self.uninvested -= total_equity
                self.invested += total_equity
                self.all_assets.add(new_asset)
            else:
                print("not enough money")
        else:
            print("Not a new position")

    def add_to_position(self, name, quantity):
        for asset in self.all_assets:
            if asset.name == name:
                asset.quantity += quantity
                self.uninvested -= asset.current_price * quantity
                self.invested += asset.current_price * quantity


class Stock:
    def __init__(self, name, current_price):
        self.name = name
        self.current_price = current_price
        self.quantity = 0


class GovtBond:
    def __init__(self, name, face_value, rate):
        self.name = name
        self.current_price = 0.5 * face_value
        self.rate = rate
        self.quantity = 0


RECENT_AVG_RATE = 0.0689
ted = Buyer(10000, "Ted")
ted.new_position(Stock("MSFT", 255), 3)
ted.new_position(Stock("AAPL", 149), 1)
ted.new_position(GovtBond("USA", 100, RECENT_AVG_RATE), 10)

ted.add_to_position("MSFT", 1)
ted.add_to_position("AAPL", 30)


for asset in ted.all_assets:
    print(asset.current_price, asset.quantity, asset.name)
    if type(asset) == Stock:
        print("Yes")

print(ted.uninvested, ted.invested, ted.name)
