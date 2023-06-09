import requests 

def get_ticker_data():
    response = requests.get("https://api.bybit.com/v2/public/tickers")

    """with open("bybit.txt", "w") as file:
        for item in response.json()["result"]:
            symbol = str(item["symbol"])
            price = str(item["last_price"])
            file.write(symbol + "-" + price + "\n")"""
    
    return response.json()


def main():
    response = get_ticker_data()
    symbols = []
    prices = []
    symbol_price_dict = {}
    count = 0
    for item in response["result"]:
        symbol = str(item['symbol']) 
        count += 1
        if symbol[0:5] == "10000":
            symbol = symbol[6:]
        elif symbol[0:4] == "1000":
            symbol = symbol[5:]
        symbols.append(symbol.lower())
        prices.append(float(item["last_price"]))
    symbol_price_dict = dict(zip(symbols, prices))
    return symbol_price_dict
    

    
    
if __name__ == "__main__":
    main()