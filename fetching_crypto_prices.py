import requests

API_KEY = "API_KEY"
def get_current_price(SYMBOL):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency="+SYMBOL+"&to_currency=USD&apikey=" + API_KEY
    response = requests.get(url)
    data = response.json()
    return float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

symbol = "BTC"
print("The current price of ", symbol, " is ", get_current_price("BTC"))