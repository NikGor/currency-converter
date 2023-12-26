import requests

api_key = 'b9764f61f1ae156a0c82a847ed67bac3'


def convert_currency_logic(amount, currency1, currency2):
    exchange_rate = get_exchange_rate(api_key, currency1, currency2)

    if exchange_rate is None:
        # Вместо возврата None выбрасываем исключение
        raise ValueError('Conversion for the selected '
                         'currency is not supported.')

    # Если дошли до сюда, значит ошибки нет и можно возвращать результат
    result = round(amount * exchange_rate, 2)
    return result


def get_currencies():
    url = f"http://api.exchangeratesapi.io/v1/symbols?access_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        return data['symbols']
    else:
        return None


def get_exchange_rate(api_key, currency1, currency2):
    url = (f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"
           f"&symbols={currency2}&base={currency1}")
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        return data['rates'][currency2]
    else:
        return None
