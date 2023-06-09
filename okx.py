import requests as r

def get_ticker_data():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }
    response = r.get("https://www.okex.com/api/spot/v3/instruments/ticker", headers = headers)

    with open("okx.txt", "w") as file:
        file.write(response.text) 
    
    
    return response.text


def main():
    print(get_ticker_data())

if __name__ == "__main__":
    main()