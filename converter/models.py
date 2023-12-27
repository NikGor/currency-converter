from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()


class Currency(Base):
    __tablename__ = 'currencies'
    code = Column(String, primary_key=True)  # Код валюты, например, "USD"
    name = Column(String)  # Название валюты, например, "US Dollar"
    rate = Column(Float)  # Курс валюты
    updated_at = Column(DateTime,
                        default=datetime.datetime.utcnow)
