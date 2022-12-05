import os

os.system("cls")


class Asset:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity


class Stock(Asset):
    def __init__(self, price, quantity, ticker):
        Asset.__init__(self, price, quantity)
        self.ticker = ticker


class Bond(Asset):
    def __init__(self, price, quantity, issuer, rate, time):
        Asset.__init__(self, price, quantity)
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
