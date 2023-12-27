import unittest
from unittest.mock import patch
from converter.api import app
from fastapi.testclient import TestClient


class TestUpdateRatesEndpoint(unittest.TestCase):
    @patch('converter.currency_db.update_currency_rates')
    def test_update_rates_endpoint(self, mock_update=None):
        mock_update.return_value = None

        # Создание тестового клиента для вашего FastAPI приложения
        client = TestClient(app)

        # Отправка запроса к эндпойнту
        response = client.post('/update-rates')

        # Проверка успешного ответа
        assert response.status_code == 200
        assert (response.json() ==
                {"message": "Currency rates updated successfully"})


if __name__ == '__main__':
    unittest.main()
