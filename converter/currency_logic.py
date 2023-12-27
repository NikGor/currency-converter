from converter.currency_api import get_exchange_rate
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')


# Функция для конвертации валют
def convert_currency_logic(amount, currency1, currency2):
    exchange_rate = get_exchange_rate(api_key, currency1, currency2)

    if exchange_rate is None:
        # Вместо возврата None выбрасываем исключение
        raise ValueError('Conversion for the selected '
                         'currency is not supported.')

    # Если дошли до сюда, значит ошибки нет и можно возвращать результат
    result = round(amount * exchange_rate, 2)
    return result
