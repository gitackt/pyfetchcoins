from markets.bitflyer import bitflyer
from markets.bitbank import bitbank
from markets.binance import binance
from markets.poloniex import poloniex
from markets.coincheck import coincheck
from markets.zaif import zaif
from markets.kucoin import kucoin
from markets.quoine import quoine
 
def fetch(name, api_key, api_key_secret):
    if name = "Bitflyer":
        return bitflyer(api_key, api_key_secret)

    elif name = "Binance":
        return binance(api_key, api_key_secret)

    elif name = "Poloniex":
        return poloniex(api_key, api_key_secret)

    elif name = "Bitbank":
        return bitbank(api_key, api_key_secret)

    elif name = "Coincheck":
        return coincheck(api_key, api_key_secret)

    elif name = "Zaif":
        return zaif(api_key, api_key_secret)

    elif name = "Kucoin":
        return zaif(api_key, api_key_secret)

    elif name = "Quoine":
        return quoine(api_key, api_key_secret)
    else:
      return None