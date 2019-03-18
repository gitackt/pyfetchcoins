import requests
import json
from quoine.client import Quoinex
import pybitflyer

def quoine(api_key, api_key_secret):

  output_dict = {}
  btc_base_values = {}

  try:

    api = pybitflyer.API()
    rate = api.ticker(product_code="btc_jpy")
    rate = rate['best_bid']

    client = Quoinex(api_key, api_key_secret)
    
    balances = client.get_crypto_accounts()

    # output_dict = {i['currency']:i['balance'] for i in balances if float(value) > 0.0}
    output_dict = {i['currency']:i['balance'] for i in balances}

    products = [i for i in client.get_products() if i['quoted_currency'] == "JPY"]

    for key, value in output_dict.items():
      for i in products:
        print(i['base_currency'])
        if i['base_currency'] == key:
          btc_base_values[key] = float(rate) * float(value) * float(i['last_traded_price'])
          break

    return [output_dict,btc_base_values]

  except:
      return [output_dict,btc_base_values]