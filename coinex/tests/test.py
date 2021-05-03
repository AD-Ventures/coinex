from coinex import CoinEx, CoinExResponse
import unittest

class TestCoinEx(unittest.TestCase):
    endpoint = 'https://api.coinex.com/v1/'

    def test_endpoint(self):
        self.assertEqual(self.endpoint, CoinEx.endpoint)

if __name__ == '__main__':
    unittest.main()
