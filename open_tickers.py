import yfinance as yf

with open("tickers.txt", "r") as f:
    data = f.read()
    data = data.split("\n")
# print(data)

for ticker in data:
    x = yf.Ticker(ticker).info
    price = x["regularMarketPrice"]
    print(ticker, price)
