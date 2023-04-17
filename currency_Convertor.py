import requests

def convert_currency(amount, from_currency, to_currency):
    # API endpoint URL with real-time exchange rates
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount

# Example usage
amount = 100
from_currency = "USD"
to_currency = "EUR"
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
