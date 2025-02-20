import requests

# assign const variables
USDTIRT_url = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
currency_api_url = "https://api.coinpaprika.com/v1/tickers"

def USDTIRT_price():
    """
    get USDTIRT price
    """
    response = requests.get(USDTIRT_url)
    USDTIRT_price = response.json()["lastTradePrice"]
    return USDTIRT_price

def get_currency_list():
    """
    request to currency_api_url
    """
    response = requests.get(currency_api_url)
    return response.json()

def list_of_available_currencies():
    """
    Return a dictionary of all available currencies (key: symbol of corresponding currency, value: id of corresponding currency)
    """
    currency_list = get_currency_list()
    currency_dict = {}
    for currency in currency_list:
        currency_symbol = currency["symbol"]
        currency_id = currency["id"]
        currency_dict[currency_symbol] = currency_id
    return currency_dict

def request_to(url):
    """
    do request and Return response
    """
    return requests.get(url)

def get_currency_price_by_symbol(symbol = str()):
    """
    Return currency price by symbol
    """
    symbol = symbol.upper()
    currency_id = list_of_available_currencies()[symbol]
    response = request_to(f"https://api.coinpaprika.com/v1/tickers/{currency_id}")
    response = response.json()
    price = response["quotes"]["USD"]["price"]
    # price = int(price)
    return price
    pass