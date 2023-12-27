import unittest
from unittest.mock import patch

import os

from converter.currency_api import get_currencies, get_exchange_rate

print("Current working directory:", os.getcwd())


# Предположим, что это ваш фиксированный ответ от mock-сервера
mock_currencies_response = {
    "success": True,
    "symbols": {
        "USD": "United States Dollar",
        "EUR": "Euro"
    }
}

mock_exchange_rate_response = {
    "success": True,
    "rates": {
        "EUR": 0.85
    }
}


class TestCurrencyFunctions(unittest.TestCase):
    @patch('converter.currency_api.requests.get')
    def test_get_currencies(self, mock_get):
        # Настройка мокирования ответа для функции get_currencies
        mock_get.return_value.json.return_value = mock_currencies_response

        # Вызов функции get_currencies и проверка результатов
        response = get_currencies()
        self.assertEqual(response, mock_currencies_response['symbols'])

    @patch('converter.currency_api.requests.get')
    def test_get_exchange_rate(self, mock_get):
        # Настройка мокирования ответа для функции get_exchange_rate
        mock_get.return_value.json.return_value = mock_exchange_rate_response

        # Вызов функции get_exchange_rate и проверка результатов
        response = get_exchange_rate('test_api_key', 'USD', 'EUR')
        self.assertEqual(response, mock_exchange_rate_response['rates']['EUR'])


if __name__ == '__main__':
    unittest.main()
