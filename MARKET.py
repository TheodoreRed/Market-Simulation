import os
import ASSET as A
import BUYER as B
import random


class Market:
    def __init__(self, num_buyers, num_assets):
        self.all_assets = []
        self.all_buyers = []

        def get_true_false():
            T_or_F = random.randint(0, 1)
            if T_or_F == 0:
                return False
            else:
                return True

        for x in range(num_assets):
            price = random.randint(1, 100)
            self.all_assets.append(A.Stock(price, get_true_false(), x))

        for x in range(num_buyers):
            cash = random.randint(100, 100000)
            self.all_buyers.append(B.Retail(cash, get_true_false(), x))

    def one_day(self):
        for buyer in self.all_buyers:
            buyer.one_day(self.all_assets)
        for asset in self.all_assets:
            asset.one_day()

    def simulate(self, num_days):
        for x in range(num_days):
            self.one_day()


def main():
    while True:
        num_buyers = int(input("Input number of buyers : "))
        num_assets = int(input("Input number of Assets : "))
        market = Market(num_buyers, num_assets)
        days = int(input("Number of days to simulate : "))
        market.simulate(days)
        break
    for buyer in market.all_buyers:
        buyer.display_stats()


if __name__ == "__main__":
    main()
