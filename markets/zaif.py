import requests
import json

from zaifapi import *

def zaif(api_key, api_key_secret):

    output_dict = {}
    btc_base_values = {}

    try:
      pub = ZaifPublicApi()
      
      balances = ZaifTradeApi(api_key, api_key_secret).get_info()['funds']

      output_dict = {key.upper():value for key, value in balances.items() if float(value) > 0.0}
      for key, value in output_dict.items():
              if key == "JPY":
                  btc_base_values[key] = value
              elif key == "BTC":
                  btc_base_values[key] = float(pub.last_price('btc_jpy')['last_price']) * float(value)
              elif key == "XEM":
                  btc_base_values[key] = float(pub.last_price('xem_jpy')['last_price']) * float(value)
              elif key == "MONA":
                  btc_base_values[key] = float(pub.last_price('mona_jpy')['last_price']) * float(value)

      return [output_dict,btc_base_values]

    except:
        return [output_dict,btc_base_values]