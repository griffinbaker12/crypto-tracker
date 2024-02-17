import requests
from bs4 import BeautifulSoup
from enums import Coin

code_to_price = {}


def get_crytpo_price(code: Coin):
    url = "https://binance.com"
    print(url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    price_div = soup.find_all("div", {"class": "coinRow-coinPrice css-1ld3mhe"})
    for div in price_div:
        print(div.text)
        parent = div.find_parent(id=lambda x: x and "top_crypto_table" in x)
        coin_code = parent.find("div", {"class": "coinRow-coinCode"}).text
        coin_price = div.text
        code_to_price[coin_code] = coin_price

    coin_name = code.name
    if coin_name in code_to_price:
        return code_to_price[coin_name]
    else:
        return "No price found"


print(get_crytpo_price(Coin.BTC))
