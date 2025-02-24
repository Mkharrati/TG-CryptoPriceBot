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
    Return a dictionary of all available currencies (key: symbol of corresponding currency like 'BTC', value: id of corresponding currency like 'btc-bitcoin')
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

def get_currency_price_by_symbol(symbol = str(), rounding = True):
    """
    Return currency price by symbol
    api server required to currency id to send information.
    """
    symbol = symbol.upper()
    currency_id = list_of_available_currencies()[symbol]
    response = request_to(f"https://api.coinpaprika.com/v1/tickers/{currency_id}")
    response = response.json()
    price = response["quotes"]["USD"]["price"]
    if rounding:
        return round_currency_price(price)
    else:
        return price

def USDTIRT_price():
    """
    USDTIRT price amount.
    """
    USDTIRT = request_to(USDTIRT_url).json()
    USDTIRT = USDTIRT["lastTradePrice"]
    USDTIRT = int(USDTIRT)
    USDTIRT = USDTIRT / 10 # IRR to IRT
    return USDTIRT

def convert_USDTD_to_IRT(usdt):
    """
    change USDT/Dollar to IRT
    """
    USDTIRT = USDTIRT_price()
    return int(usdt * USDTIRT) # separate integer part

def round_currency_price(price):
    """
    Rounding prices according to their value.
    
    Rounding rules:
    - For prices greater than 50, no decimal precision is needed (using int conversion).
    - For prices between 1 and 50, round to 2 decimal places.
    - For prices between 0.00001 and 1, round to 4 decimal places.
    - For prices between 0.000001 and 0.00001, round to 8 decimal places.
    - For prices at or below 0.000001, round to 7 decimal places.
    """
    if price > 50:
        return int(price)
    elif 1 < price < 50:
        return round(price, 2)
    elif 0.00001 < price < 1:
        return round(price, 4)
    elif 0.000001 < price < 0.00001:
        return round(price, 8)
    else:
        return price
