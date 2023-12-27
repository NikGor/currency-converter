import datetime
import requests
import os
from dotenv import load_dotenv
from converter.db import SessionLocal
from converter.models import Currency

load_dotenv()

api_key = os.environ.get('API_KEY')


def update_currency_rates():
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get('success'):
        db = SessionLocal()  # Создание сессии
        try:
            for code, rate in data['rates'].items():
                currency = db.get(Currency, code) or Currency(code=code)
                currency.rate = rate
                currency.updated_at = datetime.datetime.utcnow()
                db.add(currency)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    else:
        raise ValueError("Failed to fetch currency rates")
