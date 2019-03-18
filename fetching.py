from markets.bitflyer import bitflyer
from markets.bitbank import bitbank
from markets.binance import binance
from markets.poloniex import poloniex
from markets.coincheck import coincheck
from markets.zaif import zaif
from markets.kucoin import kucoin
from markets.quoine import quoine
 
def fetch(name, api_key, api_key_secret):
    if name="Bitflyer":
        bitflyer_param,bitflyer_yen = bitflyer(api_key, api_key_secret)
        bitflyer_param_count = Counter(bitflyer_param)
        bitflyer_yen_count = Counter(bitflyer_yen)

    elif name="Binance":
        binance_param,binance_yen = binance(api_key, api_key_secret)
        binance_param_count = Counter(binance_param)
        binance_yen_count = Counter(binance_yen)

    elif name="Poloniex":
        poloniex_param,poloniex_yen = poloniex(api_key, api_key_secret)
        poloniex_param_count = Counter(poloniex_param)
        poloniex_yen_count = Counter(poloniex_yen)

    elif name="Bitbank":
        bitbank_param,bitbank_yen = bitbank(api_key, api_key_secret)
        bitbank_param_count = Counter(bitbank_param)
        bitbank_yen_count = Counter(bitbank_yen)

    elif name="Coincheck":
        coincheck_param,coincheck_yen = coincheck(api_key, api_key_secret)
        coincheck_param_count = Counter(coincheck_param)
        coincheck_yen_count = Counter(coincheck_yen)

    elif name="Zaif":
        zaif_param,zaif_yen = zaif(api_key, api_key_secret)
        zaif_param_count = Counter(zaif_param)
        zaif_yen_count = Counter(zaif_yen)

    elif name="Kucoin":
        kucoin_param,kucoin_yen = zaif(api_key, api_key_secret)
        kucoin_param_count = Counter(kucoin_param)
        kucoin_yen_count = Counter(kucoin_yen)

    elif name="Quoine":
        quoine_param,quoine_yen = quoine(api_key, api_key_secret)
        quoine_param_count = Counter(quoine_param)
        quoine_yen_count = Counter(quoine_yen)
