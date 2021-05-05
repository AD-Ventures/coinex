import hashlib
import json
import time


import requests

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
    AccessID : str
        key for working with the Market and Account methods
    Secret : str
        secret for working with the Market and Account methods

    Methods
    -------
    _expandPathToUrl(path, params={}):
       adds onto the base url for specific methods
    _request(path, params={}):
        uses `_expandPathToUrl()` to make the API call

    Notes
    -----
    For more information, see: https://github.com/coinexcom/coinex_exchange_api/wiki
    """
    endpoint = 'https://api.coinex.com/v1/'

    def __init__(self, AccessID=None, Secret=None):
        self.AccessID = AccessID
        self.Secret = Secret

    def _expandParams(params={}):
        url = ''

        for key in params:
            url += key + '=' + str(params[key]) + '&'

        return url

    def _expandPathToUrl(path, params={}):
        """adds onto the base url for specific methods"""
        url = CoinEx.endpoint + path
        url += '?' if params else ''

        for key in params:
            url += key + '=' + str(params[key]) + '&'

        return url

    def _request(path, params={}):
        """uses `expandPathToUrl()` to make the API call"""
        url = CoinEx._expandPathToUrl(path, params)
        return requests.get(url)

    def publicRequest(self, path, params={}):
        res = CoinEx._request(path, params)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])


## COMMON FUNCTIONS ---------------

    def getCurrencyRates(self):
        return self.publicRequest('common/currency/rate')

    def getAssetConfig(self, coin_type=''):
        params = {'coin_type': coin_type}
        return self.publicRequest('common/asset/config', params)


## MARKET FUNCTIONS ---------------

    def getMarketList(self):
        return self.publicRequest('market/list')

    def getMarketStatistics(self, market):
        params = {'market': market}
        return self.publicRequest('market/ticker', params)

    def getMarketDepth(self, market, merge, limit=20):
        params = {'market': market, 'merge': merge, 'limit': limit}
        return self.publicRequest('market/depth', params)

    def getMarketTransactions(self, market, last_id=0, limit=100):
        params = {'market': market, 'last_id': last_id, 'limit': limit}
        return self.publicRequest('market/deals', params)

    def getMarketKLineData(self, market, ttype, limit=100):
        params = {'market': market, 'type': ttype, 'limit': limit}
        return self.publicRequest('market/deals', params)

    def getMarketInfo(self):
        return self.publicRequest('market/info')

    def getMarketInfoSingle(self, market):
        params = {'market': market}
        return self.publicRequest('market/detail', params)

    def getMarketAMM(self):
        return self.publicRequest('amm/market')


## ACCOUNT FUNCTIONS ---------------

    def getAccountInfo(self):
        tonce = time.time() * 1000
        params = {'access_id': self.AccessID, 'tonce': tonce, 'secret_key': self.Secret}
        signature = hashlib.md5(CoinEx._expandParams(params).encode()).hexdigest().upper()
        headers = {'authorization': signature}
        url = CoinEx._expandPathToUrl('balance/info', params)
        res = requests.get(url, headers=headers)
        rjson = res.json()
        return CoinExResponse(res.ok and rjson['code'] == 0, rjson['message'], rjson['data'])


if __name__ == '__main__':
    coinex = CoinEx()
    print(coinex.getMarketAMM())

    from secret import AccessID, Secret
    coinex = CoinEx(AccessID, Secret)
    print(coinex.getAccountInfo())

    s = 'access_id=4DA36FFC61334695A66F8D29020EB589&amount=1.0&market=BTCBCH&price=680&tonce=1513746038205&type=buy&secret_key=B51068CF10B34E7789C374AB932696A05E0A629BE7BFC62F'
    signature = hashlib.md5(s.encode()).hexdigest().upper()
    print(signature)
