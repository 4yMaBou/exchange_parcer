import requests 

def get_ticker_data():
    response = requests.get("https://api.binance.com/api/v3/ticker/price")

    """with open("binance.txt", "w") as file:
        for item in response.json():
            symbol = str(item["symbol"])
            price = str(item["price"])
            file.write(symbol + "-" + price + "\n")"""
            
    return response.json()



def main():
    response = get_ticker_data()
    symbols = []
    prices = []
    symbol_price_dict = {}
    for item in response:
        symbols.append(str(item["symbol"]).lower())
        prices.append(float(item["price"]))
        symbol_price_dict = dict(zip(symbols, prices))
    return symbol_price_dict

if __name__ == "__main__":
    main()