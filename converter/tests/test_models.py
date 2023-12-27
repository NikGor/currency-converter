import unittest
import datetime
from converter.models import Currency, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class TestCurrencyModel(unittest.TestCase):
    def setUp(self):
        # Создание движка памяти для тестирования
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def test_currency_creation(self):
        # Создание сессии и добавление нового объекта Currency
        session = self.Session()
        new_currency = Currency(code="EUR", name="Euro", rate=1.0)
        session.add(new_currency)
        session.commit()

        # Получение и проверка созданного объекта
        retrieved_currency = (session.query(Currency).
                              filter_by(code="EUR").first())
        self.assertIsNotNone(retrieved_currency)
        self.assertEqual(retrieved_currency.name, "Euro")
        self.assertEqual(retrieved_currency.rate, 1.0)
        self.assertIsInstance(retrieved_currency.updated_at, datetime.datetime)

        session.close()


if __name__ == '__main__':
    unittest.main()
