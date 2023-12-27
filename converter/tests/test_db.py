import unittest
from unittest.mock import patch
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
from converter.db import create_database_if_not_exists


class TestDatabaseFunctions(unittest.TestCase):
    @patch.dict('os.environ', {'DATABASE_URL': 'sqlite:///:memory:'})
    def test_create_database_if_not_exists(self):
        # Вызов функции для создания базы данных
        create_database_if_not_exists()

        # Проверка, что база данных была создана
        engine = create_engine('sqlite:///:memory:')
        self.assertTrue(database_exists(engine.url))

        engine.dispose()


if __name__ == '__main__':
    unittest.main()
