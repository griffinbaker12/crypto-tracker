import requests


def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    bitcoin_price = data["bitcoin"]["usd"]
    return bitcoin_price


price = get_btc_price()
print(price)
