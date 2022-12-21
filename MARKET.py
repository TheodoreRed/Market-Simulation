import os
import ASSET as A
import BUYER as B
import random


class Market:
    def __init__(self, num_buyers, num_assets):
        self.all_assets = []
        self.all_buyers = []
        self.total_days = 0

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

        def get_all_assets_value():
            total = 0
            for asset in self.all_assets:
                total += asset.current_price
            return total

        self.market_start_value = get_all_assets_value()

    def get_all_assets_value(self):
        total = 0
        for asset in self.all_assets:
            total += asset.current_price
        return total

    def get_total_market_change(self):
        return self.get_all_assets_value() - self.market_start_value

    def get_total_invested(self):
        total = 0
        for buyer in self.all_buyers:
            total += buyer.get_total_invested()
        return total

    def get_total_cash(self):
        total = 0
        for buyer in self.all_buyers:
            total += buyer.cash
        return total

    def get_market_percent_change(self):
        return (self.get_total_market_change() / self.market_start_value) * 100.0

    def get_best_buyer(self):
        highest = 0
        for idx, buyer in enumerate(self.all_buyers):
            # best = buyer
            if buyer.get_total_profit_loss() > highest:
                highest = buyer.get_total_profit_loss()
                best = buyer
        print("===================================")
        print("||              BEST             ||")
        print("===================================")
        # try:
        best.display_stats()
        # except:
        #   pass

    def get_worst_buyer(self):
        lowest = 99999999
        for idx, buyer in enumerate(self.all_buyers):
            if buyer.get_total_profit_loss() < lowest:
                lowest = buyer.get_total_profit_loss()
                worst = buyer
        print("===================================")
        print("||              WORST             ||")
        print("===================================")
        worst.display_stats()

    def display_buyer_info(self):
        print("===================================")
        print("||        BUYER INFO           ||")
        print("===================================")
        for buyer in self.all_buyers:
            buyer.display_stats()

    def display_asset_info(self):
        print("===================================")
        print("||        ASSET INFO           ||")
        print("===================================")
        for asset in self.all_assets:
            asset.display()

    def display(self):
        self.display_buyer_info()
        self.display_asset_info()
        print("===================================")
        print("||        MARKET INFO           ||")
        print("===================================")
        print("Buyers : {}".format(len(self.all_buyers)))
        print("Assets : {}".format(len(self.all_assets)))
        print("Days Passed : {}".format(self.total_days))
        print("In the market : {}".format(self.get_total_invested()))
        print("Uninvested : {}".format(self.get_total_cash()))
        print("Value of All assets : {}".format(self.market_start_value))
        print("Total Market Change : ${}".format(self.get_total_market_change()))
        print(
            "Market Percent Change : %{}".format(
                round(self.get_market_percent_change(), 2)
            )
        )
        self.get_best_buyer()
        self.get_worst_buyer()
        print("==================================")

    def one_day(self):
        self.total_days += 1
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
    market.display()


if __name__ == "__main__":
    main()
