import os
import random
import names

# os.system("cls")


class Buyer:
    def __init__(self, starting_amount, name, is_risky):
        self.starting_amount = starting_amount
        self.uninvested = starting_amount
        self.invested = 0
        self.name = name
        self.all_assets = set()
        self.is_risky = is_risky

    def account_total(self):
        for asset in self.all_assets:
            pass  # total += asset

    def new_position(self, new_asset, quantity):
        isNew = True
        # for asset in self.all_assets:
        # if new_asset.name == asset.name and type(new_asset) == type(asset):
        # isNew = False

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
        print("Started with: ${} ".format(self.starting_amount))
        print("Currently have {}".format(self.account_total()))
        print(
            "In cash : ${} Invested: ${} Buyer: {} Risky: {}\n".format(
                self.uninvested, self.invested, self.name, self.is_risky
            )
        )

    def one_day(self, all_asset_in_market):
        new_asset = random.choice(list(all_asset_in_market))
        if self.is_risky:
            while new_asset.is_volatile == False:
                new_asset = random.choice(list(all_asset_in_market))
            if new_asset not in self.all_assets:
                self.new_position(new_asset, 1)
            else:
                self.new_position(new_asset, 1)


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

    def get_true_false(self):
        T_or_F = random.randint(0, 1)
        if T_or_F == 0:
            return False
        else:
            return True


class Stock(Asset):
    def __init__(self, name, current_price, is_volatile):
        Asset.__init__(self, name, current_price, is_volatile)
        self.the_type = "Stock"

    def one_day(self):
        avg_change = 0.0073
        if self.is_volatile:
            change = avg_change * random.randint(0, 5)
            change *= self.current_price
            if self.get_true_false():
                self.current_price += change
            else:
                self.current_price -= change
        else:
            change = avg_change * self.current_price
            if self.get_true_false():
                self.current_price += change
            else:
                self.current_price -= change


class Bond(Asset):
    def __init__(self, name, current_price, is_volatile, rate):
        Asset.__init__(self, name, current_price, is_volatile)
        self.the_type = "Bond"
        self.rate = rate

    def one_day(self):
        self.current_price += self.rate


class Crypto(Asset):
    def __init__(self, name, current_price, is_volatile):
        Asset.__init__(self, name, current_price, is_volatile)
        self.the_type = "Crypto"

    def one_day(self):
        change = (0.01 * random.randint(0, 5)) * self.current_price
        if self.get_true_false():
            self.current_price += change
        else:
            self.current_price -= change


class Market:
    def __init__(self, num_buyers, num_assets):

        self.all_buyers = set()
        self.all_assets = set()

        def get_true_false():
            T_or_F = random.randint(0, 1)
            if T_or_F == 0:
                return False
            else:
                return True

        def get_unique_bond_name():
            bond_name = names.get_last_name()[0:3].upper()
            if len(self.all_assets) == 0:
                return bond_name
            for asset in self.all_assets:
                if asset.name == bond_name and asset.the_type == "Bond":
                    get_unique_bond_name()
            return bond_name

        # returns a random Bond
        def get_random_Bond():
            bond_price = 50
            rate = random.uniform(0, 1)
            name = get_unique_bond_name()
            return Bond(name, bond_price, False, rate)

        def get_unique_crypto_name():
            first2 = names.get_first_name()[0:2].upper()
            last2 = names.get_last_name()[0:2].upper()
            crypto_name = first2 + last2
            for asset in self.all_assets:
                if asset.name == crypto_name and asset.the_type == "Crypto":
                    get_unique_bond_name()
            return crypto_name

        # returns a random crypto
        def get_random_Crypto():
            name = get_unique_crypto_name()
            price = random.randint(1, 18000)
            return Crypto(name, price, True)

        def get_unique_stock_name():
            stock_name = names.get_last_name()[0:4].upper()
            if len(self.all_assets) == 0:
                return stock_name
            for asset in self.all_assets:
                if asset.name == stock_name and asset.the_type == "Stock":
                    get_unique_stock_name()
            return stock_name

        # returns a random stock
        def get_random_Stock():
            name = get_unique_stock_name()
            price = random.randint(1, 500)
            T_or_F = get_true_false()
            return Stock(name, price, T_or_F)

        # initializes all the assets
        while len(self.all_assets) < num_assets:
            the_length = len(self.all_assets)
            if the_length % 5 == 0:
                self.all_assets.add(get_random_Bond())
            elif the_length % 4 == 0:
                self.all_assets.add(get_random_Crypto())
            else:
                self.all_assets.add(get_random_Stock())

        def get_random_name():
            name = names.get_last_name()
            for buyer in self.all_buyers:
                if buyer.name == name:
                    get_random_name()
            return name

        # initializes all the buyers
        while len(self.all_buyers) < num_buyers:
            temp = get_random_name()

            T_or_F = get_true_false()

            if len(self.all_buyers) % 10 == 0:
                temp += "_Capital"
                starting_amount = random.randint(1000000, 1000000000)
                self.all_buyers.add(HedgeFund(starting_amount, temp, T_or_F))
            else:
                starting_amount = random.randint(1000, 250000)
                self.all_buyers.add(Retail(starting_amount, temp, T_or_F))

    def get_total_value_of_market(self):
        total = 0
        for buyer in self.all_buyers:
            total += buyer.uninvested + buyer.invested
        return total

    def get_true_false(self):
        T_or_F = random.randint(0, 1)
        if T_or_F == 0:
            return False
        else:
            return True

    def change(self, asset, change):
        if self.get_true_false():
            asset.current_price += change
        else:
            asset.current_price -= change

    def one_day_for_assets(self):
        # https://www.financialsamurai.com/how-much-does-the-stock-market-move-on-average-a-day/
        avg_stock_change_daily = 0.0073
        for asset in self.all_assets:
            asset.one_day()

    def get_risky_asset(self):
        new_asset = random.choice(list(self.all_assets))
        while new_asset.is_volatile == False:
            new_asset = random.choice(list(self.all_assets))
        return new_asset

    def one_day(self):
        # What do buyers do in a day
        for buyer in self.all_buyers:
            # buyer.display()
            if buyer.is_risky:
                print("This person's risky")
                if type(buyer) == Retail:
                    print("This person's a retail investor")
                    risky_asset = self.get_risky_asset()
                    print("----------------------------------")
                    print(
                        risky_asset.the_type, risky_asset.name, risky_asset.is_volatile
                    )
                    if risky_asset not in buyer.all_assets:
                        buyer.new_position(risky_asset, 12)
                        # TODO: Find a way to get the risky position that was added and and increment quantity by one
                        # buyer.all_assets
                        buyer.display()
        self.one_day_for_assets()

    def show_market(self):
        print("-----Buyers-----")
        for x in self.all_buyers:
            print(x.name, x.uninvested, x.is_risky)
            # print(x.display())

        print("-----Assets-----")
        for x in self.all_assets:
            if hasattr(x, "rate"):
                print(x.name, x.the_type, x.is_volatile, x.current_price, x.rate)
            else:
                print(x.name, x.the_type, x.is_volatile, x.current_price)
        print("Total Buyer Amount: " + str(self.get_total_value_of_market()))


# market = Market(10, 9)

# market.one_day()
# market.show_market()


def main():
    stock = Stock("MSFT", 245, True)
    buyer = Retail(25000, "Bill", True)
    print(stock.current_price)
    stock.one_day()
    print(stock.current_price)
    tempset = set()
    tempset.add(stock)
    buyer.one_day(tempset)
    buyer.display()
    buyer.one_day(tempset)
    buyer.display()
    for x in buyer.all_assets:
        print(x.current_price)
    print(buyer.account_total())
    for num in range(50):
        stock.one_day()
    buyer.display()


if __name__ == "__main__":
    main()
