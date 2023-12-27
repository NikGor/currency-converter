import unittest
from unittest.mock import patch
from converter.currency_logic import convert_currency_logic


class TestCurrencyConversionLogic(unittest.TestCase):
    @patch('converter.currency_logic.get_exchange_rate')
    def test_convert_currency_success(self, mock_get_exchange_rate):
        # Настройка мокированного ответа
        mock_get_exchange_rate.return_value = 0.85  # Пример курса обмена

        amount = 100  # 100 USD
        currency_from = "USD"
        currency_to = "EUR"

        # Вызов функции конвертации валют
        result = convert_currency_logic(amount, currency_from, currency_to)

        # Проверка результата
        self.assertEqual(result, 85.00)  # 100 USD * 0.85 = 85 EUR

    @patch('converter.currency_api.get_exchange_rate')
    def test_convert_currency_unsupported(self, mock_get_exchange_rate):
        # Настройка мокированного ответа для неподдерживаемой валюты
        mock_get_exchange_rate.return_value = None

        amount = 100
        currency_from = "USD"
        currency_to = "XYZ"  # Неподдерживаемая валюта

        # Проверка вызова исключения при неподдерживаемой валюте
        with self.assertRaises(ValueError):
            convert_currency_logic(amount, currency_from, currency_to)


if __name__ == '__main__':
    unittest.main()
