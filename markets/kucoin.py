import requests
import json
from kucoin.client import Client
import pybitflyer

def kucoin(api_key, api_key_secret):

  output_dict = {}
  btc_base_values = {}

  api = pybitflyer.API()
  rate = api.ticker(product_code="btc_jpy")
  rate = rate['best_bid']

  client = Client(api_key, api_secret)
  balances = client.get_all_balances()
  output_dict = {i['coinType']:i['balance'] for i in balances if i['balance'] > 0.0}
  for key, value in output_dict.items():
        if key == "JPY":
          btc_base_values[key] = value
        elif key == "BTC":
          btc_base_values[key] = float(rate) * float(value)
        else:
          try:
            coin_rate = client.get_buy_orders(key + '-BTC', limit=1)[0][0]
            btc_base_values[key] = float(rate) * float(value) * float(coin_rate)
          except:
            pass


  return [output_dict,btc_base_values]
