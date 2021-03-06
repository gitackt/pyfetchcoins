import requests
import json

import python_bitbankcc


def bitbank(api_key, api_key_secret):

    output_dict = {}
    fiat_values = {}

    try:
        pair = ["btc_jpy", "xrp_jpy", "ltc_btc", "eth_btc", "mona_jpy", "bcc_jpy"]

        prv = python_bitbankcc.private(api_key, api_key_secret)
        pub = python_bitbankcc.public()

        output_dict = {i['asset'].upper():i['onhand_amount'] for i in prv.get_asset()['assets'] if float(i['onhand_amount']) > 0.0}

        for key, value in output_dict.items():
            if key == "JPY":
                fiat_values[key] = value
            elif key == "BTC":
                fiat_values[key] = float(pub.get_ticker('btc_jpy')['sell']) * float(value)
            elif key == "XRP":
                fiat_values[key] = float(pub.get_ticker('xrp_jpy')['sell']) * float(value)
            elif key == "BCC":
                fiat_values[key] = float(pub.get_ticker('bcc_jpy')['sell']) * float(value)
            elif key == "MONA":
                fiat_values[key] = float(pub.get_ticker('mona_jpy')['sell']) * float(value)
            elif key == "LTC":
                fiat_values[key] = float(pub.get_ticker('ltc_btc')['sell']) * float(pub.get_ticker('btc_jpy')['sell']) * float(value)
            elif key == "ETH":
                fiat_values[key] = float(pub.get_ticker('eth_btc')['sell']) * float(pub.get_ticker('btc_jpy')['sell']) * float(value)

        return [output_dict,fiat_values]

    except:
        return [output_dict,fiat_values]
