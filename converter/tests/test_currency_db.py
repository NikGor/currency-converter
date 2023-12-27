import unittest
from unittest.mock import patch, Mock
from converter.currency_db import update_currency_rates


class TestUpdateCurrencyRates(unittest.TestCase):
    @patch('converter.currency_db.requests.get')
    def test_update_currency_rates(self, mock_get):
        # Настройка мокированного ответа
        mock_response = Mock()
        mock_response.json.return_value = {
            "success": True,
            "timestamp": 1703712544,
            "base": "EUR",
            "date": "2023-12-27",
            "rates": {
                "USD": 1.110377,
                "GBP": 0.867693,
                # Другие курсы валют по вашему мокированному ответу
            }
        }
        mock_get.return_value = mock_response

        # Вызов функции обновления курсов валют
        update_currency_rates()

        # Проверка, что мокированный запрос был вызван
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
