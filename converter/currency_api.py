import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')


# Функция для получения списка валют
def get_currencies():
    url = f"http://api.exchangeratesapi.io/v1/symbols?access_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        return data['symbols']
    else:
        return None


# Функция для получения курса валюты
def get_exchange_rate(api_key, currency1, currency2):
    url = (f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"
           f"&symbols={currency2}&base={currency1}")
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        return data['rates'][currency2]
    else:
        return None
