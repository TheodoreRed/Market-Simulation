import os

os.system("cls")


class Asset:
    def __init__(self, owner, price):
        self.owner = owner
        self.price = price


class Stock(Asset):
    def __init__(self, owner, price, ticker):
        Asset.__init__(self, owner, price)
        self.ticker = ticker


class Bond(Asset):
    def __init__(self, owner, price, issuer, rate, time):
        Asset.__init__(self, owner, price)
        self.issuer = issuer
        self.rate = rate
        self.time = time


class Buyer:
    def __init__(self):
        pass


class Retail(Buyer):
    def __init__(self):
        pass


class HedgeFund(Buyer):
    def __init__(self):
        pass
