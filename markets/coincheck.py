import requests
import json

from coincheck import order, market, account

def coincheck(api_key, api_key_secret):
    
    output_dict = {}
    btc_base_values = {}

    try:
        coin_list = ['jpy', 'btc', 'eth', 'etc', 'lsk', 'fct', 'xrp', 'xem', 'ltc', 'bch']

        balances = account.Account(secret_key=api_key_secret, access_key=api_key).get_balance()

        output_dict = {key.upper():value for key, value in balances.items() if float(value) > 0.0 and coin_list.count(key) != 0}

        url = "https://coincheck.com/api/rate/"

        for key, value in output_dict.items():
            if key == "JPY":
                btc_base_values[key] = value
            elif key == "BTC":
                btc_base_values[key] = float(requests.get(url + 'btc_jpy').json()['rate']) * float(value)
            elif key == "ETH":
                btc_base_values[key] = float(requests.get(url + 'eth_jpy').json()['rate']) * float(value)
            elif key == "ETC":
                btc_base_values[key] = float(requests.get(url + 'etc_jpy').json()['rate']) * float(value)
            elif key == "LSK":
                btc_base_values[key] = float(requests.get(url + 'lsk_jpy').json()['rate']) * float(value)
            elif key == "FCT":
                btc_base_values[key] = float(requests.get(url + 'fct_jpy').json()['rate']) * float(value)
            elif key == "XRP":
                btc_base_values[key] = float(requests.get(url + 'xrp_jpy').json()['rate']) * float(value)
            elif key == "XEM":
                btc_base_values[key] = float(requests.get(url + 'xem_jpy').json()['rate']) * float(value)
            elif key == "LTC":
                btc_base_values[key] = float(requests.get(url + 'ltc_jpy').json()['rate']) * float(value)
            elif key == "BCH":
                btc_base_values[key] = float(requests.get(url + 'bch_jpy').json()['rate']) * float(value)

        return [output_dict,btc_base_values]

    except:
        return [output_dict,btc_base_values]