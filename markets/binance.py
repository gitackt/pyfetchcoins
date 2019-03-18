import requests
import json
import pybitflyer
from binance.client import Client


def binance(api_key, api_key_secret):
    output_dict = {}
    btc_base_values = {}
    try:
        api = pybitflyer.API()
        rate = api.ticker(product_code="btc_jpy")
        rate = rate['best_bid']

        client = Client(api_key, api_key_secret)
        prices = client.get_all_tickers()
        prices = {x['symbol']:float(x['price']) for x in prices if x['symbol'].count("BTC")}

        order_account = client.get_account()
        input_dict = order_account.get("balances")
        output_dict = {x['asset']:float(x['free']) for x in input_dict if round(float(x['free']), 8) != 0.00000000}

        for x_key, x_value in output_dict.items():
            if x_key == "JPY":
                btc_base_values[x_key] = x_value
            elif x_key == "BTC":
                btc_base_values[x_key] = x_value * rate
            else:
                for y_key, y_value in prices.items():
                    if y_key.count(x_key):
                        new_value = x_value * y_value
                        btc_base_values[x_key] = new_value * rate

        return [output_dict,btc_base_values]

    except:
        return [output_dict,btc_base_values]
