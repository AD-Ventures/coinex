import hashlib
import hmac
import json


import requests

from time import time

class CoinExResponse:
    def __init__(self, success, message, result):
        self.success = success
        self.message = message
        self.result = result

    def __str__(self):
        d = {
            'success': self.success,\
            'message': self.message,\
            'result': self.result
        }
        return str(json.dumps(d, indent = 4))

class CoinEx:
    """A class to interact with the CoinEx API

    Attributes
    ----------
    endpoint : str
        the base url for API calls
    APIKey : str
        key for working with the Market and Account methods
    Secret : str
        secret for working with the Market and Account methods

    Methods
    -------
    expandPathToUrl(path, params={}):
       adds onto the base url for specific methods
    request(path, params={}):
        uses `expandPathToUrl()` to make the API call

    Notes
    -----
    For more information, see: https://github.com/coinexcom/coinex_exchange_api/wiki
    """
    endpoint = 'https://api.coinex.com/v1/'

    def __init__(self, APIKey, Secret):
        self.APIKey = APIKey
        self.Secret = Secret

    def expandPathToUrl(path, params={}):
        """adds onto the base url for specific methods"""
        url = CoinEx.endpoint + path
        url += '?' if params else ''

        for key in params:
            url += key + '=' + params[key] + '&'

        return url

    def request(path, params={}):
        """uses `expandPathToUrl()` to make the API call"""
        url = CoinEx.expandPathToUrl(path, params)
        return requests.get(url)

## COMMON FUNCTIONS ---------------

    def getCurrencyRates():
        res = CoinEx.request('common/currency/rate')
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getAssetConfig(coin_type = ''):
        params = {'coin_type': coin_type}
        res = CoinEx.request('common/asset/config', params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

## MARKET FUNCTIONS ---------------

    def getMarketList():
        res = CoinEx.request('market/list')
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketStatistics(market):
        params = {'market': market}
        res = CoinEx.request('market/ticker', params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketDepth(market, merge, limit = 20):
        params = {'market': market, 'merge': merge, 'limit': str(limit)}
        res = CoinEx.request('market/depth', params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketTransactions(market, last_id = 0, limit = 100):
        params = {'market': market, 'last_id': str(last_id), 'limit': str(limit)}
        res = CoinEx.request('market/deals', params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketKLineData(market, ttype, limit = 100):
        params = {'market': market, 'type': ttype, 'limit': str(limit)}
        res = CoinEx.request('market/deals', params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketInfo():
        res = CoinEx.request('market/info')
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketInfoSingle(market):
        params = {'market': market}
        res = CoinEx.request('market/detail', params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

    def getMarketAMM():
        res = CoinEx.request('amm/market')
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])

if __name__ == '__main__':
    print(CoinEx.getMarketAMM())
