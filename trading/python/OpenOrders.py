import requests
import json

# set the url
url = "https://api.deversifi.dev/v1/trading/r/openOrders"

"""
set payload

symbol
    string, optional, trading pair, separated by ":"

nonce
    number, seconds since epoche. Gives the time until this nonce is valid

signature
    hex-string, the signature obtained by signing the nonce with Your private Ethereum key
"""
payload = {
    "symbol": "ETH:USDT",
    "nonce": 1577836800000,
    "signature": "0x1234abcd"
}

# standard headers
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# execute the request and load into dictionary
response = json.loads(requests.request(
    "POST", url, headers=headers, json=payload).text)

# print the response from dictionary
print(json.dumps(response, indent=2))
