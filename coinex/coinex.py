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

    def __expandPathToUrl__(path, params={}):
        """adds onto the base url for specific methods"""
        url = CoinEx.endpoint + path
        url += '?' if params else ''

        for key in params:
            url += key + '=' + params[key] + '&'

        return url

    def __request__(path, params={}):
        """uses `expandPathToUrl()` to make the API call"""
        url = CoinEx.__expandPathToUrl__(path, params)
        return requests.get(url)

    def publicRequest(path, params={}):
        res = CoinEx.__request__(path, params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])


## COMMON FUNCTIONS ---------------

    def getCurrencyRates():
        return CoinEx.publicRequest('common/currency/rate')

    def getAssetConfig(coin_type=''):
        params = {'coin_type': coin_type}
        return CoinEx.publicRequest('common/asset/config', params)


## MARKET FUNCTIONS ---------------

    def getMarketList():
        return CoinEx.publicRequest('market/list')

    def getMarketStatistics(market):
        params = {'market': market}
        return CoinEx.publicRequest('market/ticker', params)

    def getMarketDepth(market, merge, limit=20):
        params = {'market': market, 'merge': merge, 'limit': str(limit)}
        return CoinEx.publicRequest('market/depth', params)

    def getMarketTransactions(market, last_id=0, limit=100):
        params = {'market': market, 'last_id': str(last_id), 'limit': str(limit)}
        return CoinEx.publicRequest('market/deals', params)

    def getMarketKLineData(market, ttype, limit=100):
        params = {'market': market, 'type': ttype, 'limit': str(limit)}
        return CoinEx.publicRequest('market/deals', params)

    def getMarketInfo():
        return CoinEx.publicRequest('market/info')

    def getMarketInfoSingle(market):
        params = {'market': market}
        return CoinEx.publicRequest('market/detail', params)

    def getMarketAMM():
        return CoinEx.publicRequest('amm/market')

if __name__ == '__main__':
    print(CoinEx.getMarketAMM())
