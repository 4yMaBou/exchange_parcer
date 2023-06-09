import requests 

def get_ticker_data():
    response = requests.get("https://api.huobi.pro/market/tickers")

    """with open("huobi.txt", "w") as file:
        for item in response.json()["data"]:
            symbol = str(item["symbol"])
            price = str(item["ask"])
            file.write(symbol + "-" + price + "\n") """
        

    return response.json()


def main():
    response = get_ticker_data()
    symbols = []
    prices = []
    symbol_price_dict = {}
    for item in response["data"]:
        symbols.append(str(item["symbol"]).lower())
        prices.append(float(item["ask"]))
        symbol_price_dict = dict(zip(symbols, prices))
    return symbol_price_dict

if __name__ == "__main__":
    main()