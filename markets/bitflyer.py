import requests
import json

import pybitflyer

def bitflyer(api_key, api_key_secret):
    coin_data = {}
    fiat_values = {}
    try:
        api = pybitflyer.API(api_key=api_key, api_secret=api_key_secret)

        rate = api.ticker(product_code="btc_jpy")
        rate = rate['best_bid']

        #資産情報の取得
        balance = api.getbalance()
        for currency in balance:
            coin_data[currency['currency_code']] = currency['amount']

        query = requests.get('https://api.coinmarketcap.com/v1/ticker/')
        coin_rate = query.json()
        rate_list = {x['symbol']:float(x['price_btc'])  for x in coin_rate if x['symbol'] in coin_data.keys()}

        for x_key, x_value in coin_data.items():
            if x_key == "JPY":
                fiat_values[x_key] = x_value
            elif x_key == "BTC":
                fiat_values[x_key] = x_value * rate
            else:
                for y_key, y_value in rate_list.items():
                    if y_key.count(x_key):
                        new_value = x_value * y_value
                        fiat_values[x_key] = new_value * rate

        return [coin_data,fiat_values]
    except:
        return [coin_data,fiat_values]
