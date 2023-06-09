import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

api_key= os.getenv("API_KEY")
url = 'https://api.cryptorank.io/v1/currencies'


def get_allpairs():
    response = requests.get(url, params= {'api_key': api_key})
    
    if response.status_code == 200:
        with open("test.json", "w") as file:
            json.dump(response.json(), file)
        print('done')
    else:
        print(response.text)
    

def main():
    get_allpairs()

if __name__ == "__main__":
    main()