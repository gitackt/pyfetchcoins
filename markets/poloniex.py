import requests
import json
import pybitflyer
from poloniex import Poloniex

def poloniex(api_key, api_key_secret):
    output_dict = {}
    btc_base_values = {}
    try:
        api = pybitflyer.API()
        rate = api.ticker(product_code="btc_jpy")
        rate = rate['best_bid']
        
        polo = Poloniex()
        polo.key = api_key
        polo.secret = api_key_secret
        balance = polo.returnBalances()

        prices = polo.returnTicker()

        output_dict = {key:float(value) for key, value in balance.items() if float(value) > 0.0}

        for x_key, x_value in output_dict.items():
            if x_key == "JPY":
                btc_base_values[x_key] = x_value
            elif x_key == "BTC":
                btc_base_values[x_key] = x_value * rate
            else:
                for y_key, y_value in prices.items():
                    if y_key == "BTC_" + str(x_key):
                        new_value = x_value * float(y_value['last'])
                        btc_base_values[x_key] = new_value * rate


        return [output_dict,btc_base_values]

    except:
        return [output_dict,btc_base_values]
