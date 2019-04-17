# pyfetchcoins
You can fetch crypto currency amount from exchange accounts. 
`pyfetchcoins` is a wrapper libraly for some fetching crypto currency libralies.

## Install
Install package from this github repository.
```
pip install git+https://github.com/gitackt/pyfetchcoins.git
```
<!-- 
## Setting
Install package dependencies from pip.

```
requests
pybitflyer
python-binance
python-kucoin
zaifapi
coincheck
python-quoine
git+https://github.com/bitbankinc/python-bitbankcc.git
https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.7.zip
``` -->

You can use for below exchanges.
* Binance
* Bitflyer
* Quoine
* Kucoin
* Bitbank
* Poloniex
* Coincheck
* Zaif

## Usage
```python
from pyfetchcoins import fetching

name = "Bitflyer"
api_key = "xxxxxxxxxxxxxxxxx"
api_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxx"

fetching.fetch(name, api_key, api_key_secret)
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