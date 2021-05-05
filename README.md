# CoinEx [![Build Status](https://travis-ci.com/AD-Ventures/coinex.svg?branch=main)](https://travis-ci.com/AD-Ventures/coinex) ![Last Commit](https://img.shields.io/github/last-commit/AD-Ventures/coinex) ![Python Version](https://img.shields.io/badge/python-3.4%2B-green)  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/AD-Ventures/coinex/blob/main/LICENSE)


A Python3 wrapper for the CoinEx API

## Installation

```bash
pip3 install coinex
```

## Usage

```python
from coinex import CoinEx

# public functions (no APIKEY/Secret needed)
coinex = CoinEx()

markets = coinex.getMarketList().result
marketInfo = coinex.getMarketInfoSingle('BANBTC').result

## Support

For any help or questions, please open an issue on GitHub.

## License

[MIT](https://github.com/AD-Ventures/coinex/blob/master/LICENSE)
