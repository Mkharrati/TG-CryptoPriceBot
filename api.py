import requests

usdtirt_url = "https://api.nobitex.ir/v2/orderbook/USDTIRT"

def USDTIRT_price():
    """
    get USDTIRT price
    """
    usdtirt_response = requests.get(usdtirt_url)
    usdtirt_price = usdtirt_response.json()["lastTradePrice"]
    return usdtirt_price

def get_currency_by_symbol():
    pass
