# Get the current Bitcoin price from coincap API and calculate the taotal amount for a given number of input bitcoins though cli using argv

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
