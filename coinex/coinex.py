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
