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
        self.all_assets = {"id": [], "shares": [], "total": []}
        self.value_all_assets = 0
        self.is_risky = is_risky

    def add_asset(self, asset, quantity):
        total_to_add = asset.current_price * quantity
        changed = False
        for i in self.all_assets["id"]:
            if i == asset.uniqueID:
                self.all_assets["shares"][i] += quantity
                self.all_assets["total"][i] += total_to_add
                changed = True
                break
        if not changed:
            self.all_assets["id"].append(asset.uniqueID)
            self.all_assets["shares"].append(quantity)
            self.all_assets["total"].append(total_to_add)

    def get_value_of_all_assets(self):
        total = 0
        for x in range(len(self.all_assets["id"])):
            total += self.all_assets["total"][x]
        return total

    def get_total_shares(self):
        total = 0
        for x in range(len(self.all_assets["shares"])):
            total += self.all_assets["shares"][x]
        return total

    def display_stats(self):
        print("Buyer {}".format(self.uniqueID))
        print("-----------------------------------")
        print("Starting amount:     {}".format(self.starting_amount))
        print("Cash:                {}".format(self.cash))
        print("Value of all assets: {}".format(self.get_value_of_all_assets()))
        print("Number of Assets: {}".format(len(self.all_assets["id"])))
        print("Total number of shares: {}".format(self.get_total_shares()))
        print("Are they risky:      {}".format(self.is_risky))


asset = ASSET.Asset(0, 117, True)
buyer = Buyer(1000, True, 0)
buyer.display_stats()
buyer.add_asset(asset, 1)
buyer.display_stats()
buyer.add_asset(asset, 1)
buyer.display_stats()
