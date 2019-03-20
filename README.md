# pyfetchcoins
You can fetch curypto currency amount from exchange accounts. 
`pyfetchcoins` is a wrapper libraly for some fetching crypto currency libralies.

## Install
Install package from this github repository.
```
pip install git+https://github.com/gitackt/pyfetchcoins.git
```

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
```

## Usage
```python
import fetching from pyfetchcoins

name = "Exchange Name"
api_key = "Your api Key"
api_key_secret = "Your api Key Secret"

fetching.fetch(name, api_key, api_key_secret)



// ex)
name = "Bitflyer"
api_key = "xxxxxxxxxxxxxxxxx"
api_key_secret = "xxxxxxxxxxxxxxxxxxxxxxxx"

fetching.fetch(name, api_key, api_key_secret)
```

## Refernce
You can use for below exchanges.
* Binance
* Bitflyer
* Quoine
* Kucoin
* Bitbank
* Poloniex
* Coincheck
* Zaif

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