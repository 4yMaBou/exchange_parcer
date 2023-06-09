import requests as r

def get_ticker_data():
    response = r.get("https://api.latoken.com/v2/ticker")

    """with open("latoken.txt", "w") as file:
        for item in response.json():
            symbol = str(item["symbol"])
            price = str(item["lastPrice"])
            file.write(symbol + "-" + price + "\n") """
        

    return response.json()


def main():
    response = get_ticker_data()
    symbols = []
    prices = []
    symbol_price_dict = {}
    for item in response:
        symbol = str(item["symbol"]).lower()
        symbols.append(symbol[:symbol.find("/")] + symbol[symbol.find("/") + 1:])
        prices.append(float(item["lastPrice"]))
        symbol_price_dict = dict(zip(symbols, prices))
    return symbol_price_dict




if __name__ == "__main__":
    main()