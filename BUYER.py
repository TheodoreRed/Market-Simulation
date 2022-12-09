import random
import names
import os
import ASSET

os.system("cls")


class Buyer:
    def __init__(self, starting_amount, is_risky, uniqueID):
        self.starting_amount = starting_amount
        self.cash = starting_amount
        self.uniqueID = uniqueID
        self.all_assets = {"asset": [], "shares": [], "total": []}
        # self.value_all_assets = 0
        self.is_risky = is_risky
        self.num_transactions = 0

    def get_T_F(self):
        T_or_F = random.randint(0, 1)
        if T_or_F == 0:
            return False
        else:
            return True

    def add_asset(self, asset, quantity):
        total_to_add = asset.current_price * quantity
        if self.cash >= total_to_add:
            changed = False
            for i, my_asset in enumerate(self.all_assets["asset"]):
                if asset == my_asset:
                    self.all_assets["shares"][i] += quantity
                    self.all_assets["total"][i] += total_to_add
                    self.num_transactions += 1
                    self.cash -= total_to_add
                    changed = True
                    break
            if not changed:
                self.all_assets["asset"].append(asset)
                self.all_assets["shares"].append(quantity)
                self.all_assets["total"].append(total_to_add)
                self.num_transactions += 1
                self.cash -= total_to_add

    def subtract_asset(self, asset, quantity):
        for idx, my_asset in enumerate(self.all_assets["asset"]):
            if my_asset == asset:
                num_shares = self.all_assets["shares"][idx]
                if quantity >= num_shares:
                    self.cash += num_shares * asset.current_price
                    self.all_assets["shares"][idx] = 0
                    self.all_assets["total"][idx] = 0
                    self.num_transactions += 1
                    print("Inside")

                else:
                    print("Outside")

    def get_total_invested(self):
        total = 0
        for x in range(len(self.all_assets["asset"])):
            total += self.all_assets["total"][x]
        return total

    def get_account_total(self):
        total = 0
        for x in range(len(self.all_assets["asset"])):
            asset = self.all_assets["asset"][x]
            shares = self.all_assets["shares"][x]
            total += asset.current_price * shares
        return total + self.cash

    def get_total_profit_loss(self):
        account_total = self.get_account_total()
        if self.starting_amount > account_total:
            print("P/L : -${}".format(self.starting_amount - account_total))
        else:
            print("P/L : +${}".format(account_total - self.starting_amount))

    def profit_loss(self, invested, current_equity):
        return current_equity - invested

    def print_portfolio(self):
        for x in range(len(self.all_assets["asset"])):
            print(
                "Name : {} Invested: {}".format(
                    self.all_assets["asset"][x].name,
                    self.all_assets["total"][x],
                )
            )

            invested = self.all_assets["total"][x]
            print(
                "Assets: {} Cost Per Asset: {}".format(
                    self.all_assets["shares"][x],
                    invested / self.all_assets["shares"][x],
                )
            )
            current_equity = (
                self.all_assets["asset"][x].current_price * self.all_assets["shares"][x]
            )
            print(
                "Equity : ${}  P/L : ${}".format(
                    self.all_assets["asset"][x].current_price
                    * self.all_assets["shares"][x],
                    self.profit_loss(invested, current_equity),
                )
            )

    def get_total_shares(self):
        total = 0
        for x in range(len(self.all_assets["shares"])):
            total += self.all_assets["shares"][x]
        return total

    def display_stats(self):
        print("-----------------------------------")
        print("Buyer {}".format(self.uniqueID))
        print("Starting amount:     {}".format(self.starting_amount))
        print("Account Total:       {}".format(self.get_account_total()))
        print("Cash:                {}".format(self.cash))
        print("Total Invested:      {}".format(self.get_total_invested()))
        self.get_total_profit_loss()
        print("Number of Assets:    {}".format(len(self.all_assets["asset"])))
        print("Total quantity of assets: {}".format(self.get_total_shares()))
        print("Total Transactions: {}".format(self.num_transactions))
        print("Are they risky:      {}".format(self.is_risky))
        self.print_portfolio()
        print("-----------------------------------")


class Retail(Buyer):
    def __init__(self, starting_amount, is_risky, uniqueID):
        Buyer.__init__(self, starting_amount, is_risky, uniqueID)


asset = ASSET.Asset(0, 100, True)
asset_2 = ASSET.Asset(1, 125, False)
buyer = Retail(1000, True, 0)

buyer.add_asset(asset, 1)
buyer.display_stats()

asset.current_price = 99

buyer.add_asset(asset, 1)
buyer.display_stats()


buyer.add_asset(asset_2, 1)
buyer.display_stats()
asset_2.current_price = 126
buyer.add_asset(asset_2, 1)
buyer.display_stats()
