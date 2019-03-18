import requests
import json

from coincheck import order, market, account

def coincheck(api_key, api_key_secret):
    
    output_dict = {}
    fiat_values = {}

    try:
        coin_list = ['jpy', 'btc', 'eth', 'etc', 'lsk', 'fct', 'xrp', 'xem', 'ltc', 'bch']

        balances = account.Account(secret_key=api_key_secret, access_key=api_key).get_balance()

        output_dict = {key.upper():value for key, value in balances.items() if float(value) > 0.0 and coin_list.count(key) != 0}

        url = "https://coincheck.com/api/rate/"

        for key, value in output_dict.items():
            if key == "JPY":
                fiat_values[key] = value
            elif key == "BTC":
                fiat_values[key] = float(requests.get(url + 'btc_jpy').json()['rate']) * float(value)
            elif key == "ETH":
                fiat_values[key] = float(requests.get(url + 'eth_jpy').json()['rate']) * float(value)
            elif key == "ETC":
                fiat_values[key] = float(requests.get(url + 'etc_jpy').json()['rate']) * float(value)
            elif key == "LSK":
                fiat_values[key] = float(requests.get(url + 'lsk_jpy').json()['rate']) * float(value)
            elif key == "FCT":
                fiat_values[key] = float(requests.get(url + 'fct_jpy').json()['rate']) * float(value)
            elif key == "XRP":
                fiat_values[key] = float(requests.get(url + 'xrp_jpy').json()['rate']) * float(value)
            elif key == "XEM":
                fiat_values[key] = float(requests.get(url + 'xem_jpy').json()['rate']) * float(value)
            elif key == "LTC":
                fiat_values[key] = float(requests.get(url + 'ltc_jpy').json()['rate']) * float(value)
            elif key == "BCH":
                fiat_values[key] = float(requests.get(url + 'bch_jpy').json()['rate']) * float(value)

        return [output_dict,fiat_values]

    except:
        return [output_dict,fiat_values]