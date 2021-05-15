# CoinEx [![Build Status](https://travis-ci.com/AD-Ventures/coinex.svg?branch=main)](https://travis-ci.com/AD-Ventures/coinex) ![Last Commit](https://img.shields.io/github/last-commit/AD-Ventures/coinex) ![Python Version](https://img.shields.io/badge/python-3.4%2B-green)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/AD-Ventures/coinex/blob/main/LICENSE)


A Python3 wrapper for the [CoinEx API](https://github.com/coinexcom/coinex_exchange_api/wiki)

This is an unofficial wrapper with no affiliation with CoinEx, use at your own risk.

*Note: no limit on Market calls; generally 200 requests per 10 seconds for other operations. Specific rates can be found in thier respective documentation pages*

## Installation

```bash
pip3 install coinex
```

## Usage

Methods in the coinex package return a `CoinExResponse` object containing three attributes (success, message, and result) aligning with the coinex API response (code, message, and data). For more information on the success/code, see [here](https://github.com/coinexcom/coinex_exchange_api/wiki/013error_code)

```python
import coinex

coinex = coinex.CoinEx()  #initalize the object

request = coinex.getMarketList()  # use one of the object's methods to make an API call
request.success  # returns 0
request.message  # returns OK
request.result  # returns a list of markets
```
## Common and Market API

The methods in this section do not require additional signature/authentication. An exception will be raised if trying to use the other methods without supplying a AccessID and Secret.

```python
coinex = coinex.CoinEx()  # no AccessID and Secret needed for common and market methods
```

### Common API

* `getCurrencyRates()` - https://github.com/coinexcom/coinex_exchange_api/wiki/070currency_rate
* `getAssetConfig(coin_type='')` - https://github.com/coinexcom/coinex_exchange_api/wiki/071asset_config

### Market API

* `getMarketList()` - https://github.com/coinexcom/coinex_exchange_api/wiki/020market
* `getMarketStatistics(market)` - https://github.com/coinexcom/coinex_exchange_api/wiki/021ticker
* `getMarketDepth(market, merge, limit=20)` - https://github.com/coinexcom/coinex_exchange_api/wiki/022depth
* `getMarketTransactions(market, last_id=0, limit=100)` - https://github.com/coinexcom/coinex_exchange_api/wiki/023deals
* `getMarketKLineData(market, ttype, limit=100)` - https://github.com/coinexcom/coinex_exchange_api/wiki/024kline
* `getMarketInfo()` - https://github.com/coinexcom/coinex_exchange_api/wiki/025marketinfo
* `getMarketInfoSingle(market)` - https://github.com/coinexcom/coinex_exchange_api/wiki/026market_single_info
* `getMarketAMM()` - https://github.com/coinexcom/coinex_exchange_api/wiki/092amm_market_list

## Account and Trading API

The Account and Trading APIs require additional signature/authentication in order to use.

This wrapper handles most of the authentication process, so the only thing that needs to be supplied is an AccessID and Secret with proper permissions. We recommend saving your key and secret as variables (`ACCESSID = XXX` and `SECRET=XXX`) in a separate python file named `secrets.py` and importing it such as the example below.

For more information about acquiring an AccessID and Secret, refer to the CoinEx API [documentation](https://github.com/coinexcom/coinex_exchange_api/wiki/012security_authorization#acquire-access_id-and-secret_key)

```python
from secrets import ACCESSID, SECRET  # import api id and secret

coinex = coinex.CoinEx(ACCESSID, SECRET)
```

### Account API

* `getAccountInfo()` - https://github.com/coinexcom/coinex_exchange_api/wiki/060balance
* `getAccountDepositAddress()` - https://github.com/coinexcom/coinex_exchange_api/wiki/072get_deposit_address

### Trading API


## Websocket API

Using the Websocket API is currently not supported. Supported is planned in future updates.

## Support

For any help or questions, please open an issue on GitHub.

## License

[MIT](https://github.com/AD-Ventures/coinex/blob/master/LICENSE)
