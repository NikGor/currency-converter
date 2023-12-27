from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")


def create_database_if_not_exists():
    engine = create_engine(DATABASE_URL)
    if not database_exists(engine.url):
        create_database(engine.url)
    engine.dispose()


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Импорт моделей для автоматического создания таблиц через Alembic
from .models import Currency  # noqa: F401 E402


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
