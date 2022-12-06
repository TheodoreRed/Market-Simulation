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
                if type(asset) == type_asset:
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
            if type(asset) == type_asset:
                if asset.name == name:
                    if quantity >= asset.quantity:
                        self.close_position(asset)
                        break
                    else:
                        self.uninvested += asset.current_price * quantity
                        self.invested -= asset.current_price * quantity
                        asset.quantity -= quantity

    def display(self):
        print("{}'s Current Portfolio".format(self.name))
        for asset in self.all_assets:

            print(
                "{} {} : {} of this asset at a price of ${} dollars each".format(
                    asset.the_type, asset.name, asset.quantity, asset.current_price
                )
            )
        print(
            "In cash still: ${} Total invested: ${} Buyer name: {}\n".format(
                self.uninvested, self.invested, self.name
            )
        )


class Asset:
    def __init__(self, name, current_price):
        self.name = name
        self.current_price = current_price
        self.quantity = 0.0

        def val_of_asset(self):
            return self.current_price * self.quantity


class Stock(Asset):
    def __init__(self, name, current_price, is_large_company):
        Asset.__init__(self, name, current_price)
        self.the_type = "Stock"
        self.is_large_company = is_large_company


class Bond(Asset):
    def __init__(self, name, current_price):
        RECENT_AVG_RATE = 0.0689
        Asset.__init__(self, name, current_price)
        self.the_type = "Bond"
        self.rate = RECENT_AVG_RATE


class Crypto(Asset):
    def __init__(self, name, current_price):
        Asset.__init__(self, name, current_price)
        self.the_type = "Crypto"


ted = Buyer(100000, "Ted")
ted.new_position(Stock("MSFT", 255, True), 3)
ted.new_position(Stock("AAPL", 149, True), 15)
ted.new_position(Bond("USA", 50), 12)
ted.new_position(Stock("USA", 6, False), 100)

ted.add_to_position(Bond, "USA", 11)
ted.add_to_position(Stock, "USA", 191)

ted.subtract_from_position(Stock, "AAPL", 1)
ted.subtract_from_position(Stock, "USA", 222)


ted.display()
ted.add_to_position(Stock, "MSFT", 4)
ted.new_position(Crypto("BTC", 17019), 4)

ted.display()
