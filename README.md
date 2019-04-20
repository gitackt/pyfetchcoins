# pyfetchcoins
Fetch crypto currency amount from exchange accounts. You need `api_key` and `api_key_secret` for your exchanges.

## Install
Install package from this github repository.
```
pip install git+https://github.com/gitackt/pyfetchcoins.git
```

## Setting
Install package dependencies from pip.

```
pip install git+https://github.com/bitbankinc/python-bitbankcc.git
pip install https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.7.zip
```

## Usage
Use for below exchanges.
* Binance
* Bitflyer
* Quoine
* Kucoin
* Bitbank
* Poloniex
* Coincheck
* Zaif


```python
from pyfetchcoins.fetching import fetch

name = "Bitflyer"
api_key = "xxxxxxxxxxxxxxxxx"
api_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxx"

fetch(name, api_key, api_key_secret)
```

### Response
Return coin volume and JPY values.
```json
[
  {
    "BTC": 0.0001,
    "ETH": 0.02,
    "XRP": 50,
  },
  {
    "BTC": 44,
    "ETH": 300,
    "XRP": 1750,
  }
]
```