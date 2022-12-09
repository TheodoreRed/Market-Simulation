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


market = Market(10, 100)
for x in market.all_assets:
    x.display()

for x in market.all_buyers:
    x.one_day(market.all_assets)

for x in market.all_buyers:
    x.display_stats()
