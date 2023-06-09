import requests 

def get_markets(slug = "slug=bitcoin", start = "start=1", limit = "limit=1000", category = "category=spot", centerType = "centerType=all", sort = "sort=cmc_rank_advanced"):
    response = requests.get(url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?{slug}&{start}&{limit}&{category}&{centerType}&{sort}")
    
    #with open("coin.txt", "w") as file:
    #    file.write(response.text)
    
    with open("t.txt", "w") as file:
        for item in response.json()["data"]["marketPairs"]:
            exchangeName = str(item["exchangeName"]) 
            marketPair = str(item["marketPair"])
            price = str(item["price"])
            file.write(exchangeName + " ")
            file.write(marketPair + " ")
            file.write(price + ";" + "\n")
    #return response.text

def main():
    print(get_markets())

if __name__ == '__main__':
    main()