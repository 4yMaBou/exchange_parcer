import requests

def get_ticker_data():
    response = requests.get("https://poloniex.com/public?command=returnTicker")

    
    """with open("poloniex.txt", "w") as file:
        data = response.json()
        for key, value in data.items():
            symbol = str(key).lower()
            price = str(value["last"])
            file.write(symbol + " - " + price + "\n")"""
       
        

    return response.json()


def main():
    response = get_ticker_data()
    symbols = []
    prices = []
    symbol_price_dict = {}
    for key, value in response.items():
        symbol = str(key).lower()
        price = float(value["last"])
        symbols.append(symbol[:symbol.find("_")] + symbol[symbol.find("_") + 1:])
        prices.append(price)
        symbol_price_dict = dict(zip(symbols, prices))
    return symbol_price_dict




if __name__ == "__main__":
    main()