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
                else:
                    self.cash += quantity * asset.current_price
                    self.all_assets["total"][idx] -= quantity * asset.current_price
                    self.all_assets["shares"][idx] -= quantity
                    self.num_transactions += 1

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
        return self.get_account_total() - self.starting_amount

    def get_percent_change(self):
        percent_change = (self.get_account_total() / self.starting_amount) - 1
        return percent_change

    def print_total_profit_loss(self):
        account_total = self.get_account_total()
        if self.starting_amount > account_total:
            print("P/L : -${}".format(self.starting_amount - account_total))
        else:
            print("P/L : +${}".format(account_total - self.starting_amount))

    def profit_loss(self, invested, current_equity):
        return current_equity - invested

    def print_portfolio(self):
        print("/\/\/\/\/\/\ Assets /\/\/\/\/\/\/")
        for x in range(len(self.all_assets["asset"])):
            print(
                "Name : {} Invested: {}".format(
                    self.all_assets["asset"][x].name,
                    self.all_assets["total"][x],
                )
            )
            invested = self.all_assets["total"][x]
            try:
                per_share = invested / self.all_assets["shares"][x]
            except:
                per_share = 0
            print(
                "Assets: {} Cost Per Asset: {}".format(
                    self.all_assets["shares"][x],
                    per_share,
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
        self.print_total_profit_loss()
        print("Number of Assets:    {}".format(len(self.all_assets["asset"])))
        print("Total quantity of assets: {}".format(self.get_total_shares()))
        print("Total Transactions: {}".format(self.num_transactions))
        print("Are they risky:      {}".format(self.is_risky))
        print("-----------------------------------")


class Retail(Buyer):
    def __init__(self, starting_amount, is_risky, uniqueID):
        Buyer.__init__(self, starting_amount, is_risky, uniqueID)

    def get_risky_asset(self, assets_in_market):
        risky_asset = random.choice(assets_in_market)

        while risky_asset.is_volatile == False:
            risky_asset = random.choice(assets_in_market)

        return risky_asset

    def one_day(self, assets_in_market):
        if len(self.all_assets["asset"]) > 0:
            if self.is_risky:

                # 75% chance it happens
                if random.randint(1, 100) < 75:

                    # If true we buy
                    if self.get_T_F():
                        risky_asset = self.get_risky_asset(assets_in_market)
                        self.add_asset(risky_asset, random.randint(1, 10))
                    # Or else we sell
                    else:
                        my_asset = random.choice(self.all_assets["asset"])
                        self.subtract_asset(my_asset, random.randint(1, 10))
            # If not risky
            else:

                # 25% chance it happens
                if random.randint(1, 100) < 25:
                    if self.get_T_F():
                        asset = random.choice(assets_in_market)
                        self.add_asset(asset, random.randint(1, 5))
                    else:
                        my_asset = random.choice(self.all_assets["asset"])
                        self.subtract_asset(my_asset, random.randint(1, 5))
        else:
            asset = random.choice(assets_in_market)
            self.add_asset(asset, random.randint(1, 10))


class HedgeFund(Buyer):
    def __init__(self, starting_amount, is_risky, uniqueID):
        Buyer.__init__(self, starting_amount, is_risky, uniqueID)
