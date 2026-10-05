"""
Problem:
Take the number of bitcoins as a command-line argument and print what it costs in USD using the current bitcoin price. 
If the argument is missing, or there is more than one, or it is not a number, exit with an error message.

Approach:
I used sys.argv to get the argument and checked that there is exactly one. I converted it to a float and used try/except to catch the case where it is not a number. 
Then I used requests.get() to call the CoinCap API and took priceUsd from the JSON data. If the request fails the program exits with an error. 
At the end I multiply the bitcoins by the price and print it with a $ sign, commas and 4 decimal places.
"""

import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=86d711e6c658f11750a30f4391d259eea9cc97f227afd4c63f638adb326b341e"
    )
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Error")

amount = bitcoins * price

print(f"${amount:,.4f}")
